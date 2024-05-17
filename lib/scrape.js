const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const { checkTorRunning, checkOnionSite } = require('../utils/torCheck');

async function scrapeOnionSite(url, searchQuery, saveFile, saveDirectory) {
  await checkTorRunning();

  const { siteExists, message } = await checkOnionSite(url);
  if (!siteExists) {
    console.error(message);
    return;
  }

  try {
    const response = await axios.get(url, { proxy: { host: '127.0.0.1', port: 9050, protocol: 'socks5h' } });
    const $ = cheerio.load(response.data);

    let content = searchQuery ? $(`*:contains(${searchQuery})`).html() : $.html();

    if (saveFile) {
      const savePath = saveDirectory ? `${saveDirectory}/${saveFile}` : saveFile;
      fs.writeFileSync(savePath, content, 'utf-8');
      console.log(`Content saved to ${savePath}`);
    } else {
      console.log(content);
    }
  } catch (error) {
    console.error(`Error fetching the page: ${error.message}`);
  }
}

module.exports = { scrapeOnionSite };
        
