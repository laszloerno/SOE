#!/usr/bin/env python3
# audit_padding_oracle_no_requests.py
# Audit script using only the Python standard library (no requests).
# Usage: python3 audit_padding_oracle_no_requests.py http://localhost:3000/decrypt

import sys, time, statistics, json
from urllib import request, error

TEST_CIPHERTEXTS = [
    'good',
    'bad-1', 'bad-2', 'bad-3', 'random-xxxxx', ''
]

def probe(url, payload):
    body = json.dumps({'ciphertext': payload}).encode('utf-8')
    req = request.Request(url, data=body, headers={'Content-Type':'application/json'}, method='POST')
    t0 = time.time()
    try:
        with request.urlopen(req, timeout=5) as r:
            elapsed = time.time() - t0
            status = r.getcode()
            resp = r.read().decode('utf-8', errors='replace').strip()
            return (status, resp, elapsed)
    except error.HTTPError as e:
        # HTTP error has .code and .read()
        try:
            resp = e.read().decode('utf-8', errors='replace').strip()
        except Exception:
            resp = f'HTTPError {e.code}'
        elapsed = time.time() - t0
        return (e.code, resp, elapsed)
    except Exception as e:
        return (None, f'ERROR:{e}', None)

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 audit_padding.py <url>')
        sys.exit(1)
    url = sys.argv[1].rstrip('/')
    results = []
    print('Probing server:', url)
    for ct in TEST_CIPHERTEXTS:
        print(f' -> testing ciphertext: {repr(ct)}')
        trials = []
        for i in range(5):
            code, body, elapsed = probe(url, ct)
            print(f'    try {i+1}: status={code}, body={body[:80]!r}, time={elapsed}')
            trials.append((code, body, elapsed))
            time.sleep(0.15)
        results.append((ct, trials))
        print('')
    print('\\n=== Analysis ===')
    for ct, trials in results:
        codes = [t[0] for t in trials]
        bodies = [t[1] for t in trials]
        times = [t[2] for t in trials if t[2] is not None]
        same_code = all(c == codes[0] for c in codes)
        same_body = all(b == bodies[0] for b in bodies)
        avg_time = statistics.mean(times) if times else None
        stdev = statistics.pstdev(times) if times else None
        print(f"Ciphertext={ct!r}: same_status={same_code}, same_body={same_body}, avg_time={avg_time}, stdev={stdev}")
    print('\\nIf you see different bodies or status codes for invalid inputs -> server may be vulnerable to padding-oracle leaks.')
    print('If timings differ significantly between good vs bad -> consider blinding/normalizing timing.')

if __name__ == '__main__':
    main()


# python3 audit_padding.py http://localhost:3000/decrypt
