const axios = require('axios');
const fs = require('fs');
const { checkTorRunning, checkOnionSite } = require('../utils/torCheck');

async function findDirectories(url, dirFile, saveFile, saveDirectory) {
  await checkTorRunning();

  const { siteExists, message } = await checkOnionSite(url);
  if (!siteExists) {
    console.error(message);
    return;
  }

  const directories = fs.readFileSync(dirFile, 'utf-8').split('\n');
  const foundDirectories = [];

  for (const directory of directories) {
    const testUrl = `${url}/${directory}`;
    try {
      const response = await axios.get(testUrl, { proxy: { host: '127.0.0.1', port: 9050, protocol: 'socks5h' } });
      if (response.status === 200 && (
        response.data.includes('index.html') || response.data.includes('index.php') ||
        response.data.includes('login.html') || response.data.includes('login.php') ||
        response.data.includes('home.html') || response.data.includes('home.php') ||
        response.data.includes('main.html') || response.data.includes('main.php') ||
        response.data.includes('about.html') || response.data.includes('contact.html') ||
        response.data.includes('contact.php') || response.data.includes('form.html') ||
        response.data.includes('form.php') || response.data.includes('register.html') ||
        response.data.includes('register.php') || response.data.includes('signup.html') ||
        response.data.includes('signup.php') || response.data.includes('dashboard.html') ||
        response.data.includes('dashboard.php') || response.data.includes('admin.html') ||
        response.data.includes('admin.php') || response.data.includes('logout.html') ||
        response.data.includes('404.html') || response.data.includes('style.css') ||
        response.data.includes('styles.css') || response.data.includes('script.js') ||
        response.data.includes('database.db') || response.data.includes('app.db') ||
        response.data.includes('main.db') || response.data.includes('web.db') ||
        response.data.includes('users.db') || response.data.includes('customer.db') ||
        response.data.includes('inventory.db')
      )) {
        foundDirectories.push(testUrl);
        console.log(`Found: ${testUrl}`);
      }
    } catch (error) {
      continue;
    }
  }

  if (foundDirectories.length > 0) {
    const savePath = saveDirectory ? `${saveDirectory}/${saveFile}` : saveFile;
    fs.writeFileSync(savePath, foundDirectories.join('\n'), 'utf-8');
    console.log(`Found directories saved to ${savePath}`);
  } else {
    console.log('No directories found.');
  }
}

module.exports = { findDirectories };
                                                          
