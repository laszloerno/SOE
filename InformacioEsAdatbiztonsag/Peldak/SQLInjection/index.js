// index.js - run demos from vulnerable/ or solutions/
const which = process.env.DEMO || 'v1';
console.log('Starting demo', which);
if (which === 'v1') require('./vulnerable/vulnerable-1.js');
else if (which === 'v2') require('./vulnerable/vulnerable-2.js');
else if (which === 'v3') require('./vulnerable/vulnerable-3.js');
else if (which === 'v4') require('./vulnerable/vulnerable-4.js');
else if (which === 'v5') require('./vulnerable/vulnerable-5.js');
else if (which === 'v6') require('./vulnerable/vulnerable-6.js');
else if (which === 'v7') require('./vulnerable/vulnerable-7.js');
else if (which === 'v8') require('./vulnerable/vulnerable-8.js');
else if (which === 's_all') {
  require('./solutions/solution-1.js');
  require('./solutions/solution-2.js');
  require('./solutions/solution-3.js');
  require('./solutions/solution-4.js');
  require('./solutions/solution-5.js');
  require('./solutions/solution-6.js');
  require('./solutions/solution-7.js');
  require('./solutions/solution-8.js');
} else if (which === 's1') require('./solutions/solution-1.js');
else require('./vulnerable/vulnerable-1.js');
