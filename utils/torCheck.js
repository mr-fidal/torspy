const axios = require('axios');

async function checkTorRunning() {
  try {
    await axios.get('http://check.torproject.org', { proxy: { host: '127.0.0.1', port: 9050, protocol: 'socks5h' } });
  } catch (error) {
    console.error('Error: Tor is not running or not properly configured. Please start Tor and try again.');
    process.exit(1);
  }
}

async function checkOnionSite(url) {
  if (!url.startsWith('http://') && !url.startsWith('https://')) {
    url = 'http://' + url;
  }

  try {
    const response = await axios.get(url, { proxy: { host: '127.0.0.1', port: 9050, protocol: 'socks5h' } });
    if (response.status === 200) {
      return { siteExists: true, message: 'Site exists and is reachable.' };
    } else {
      return { siteExists: false, message: `Site returned status code: ${response.status}` };
    }
  } catch (error) {
    return { siteExists: false, message: `Error fetching the page: ${error.message}` };
  }
}

module.exports = { checkTorRunning, checkOnionSite };
      
