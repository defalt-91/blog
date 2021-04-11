const path = require("path");

module.exports = {
  publicPath: process.env.VUE_APP_STATIC_URL,
  outputDir: path.resolve(__dirname, "../../static/", "blog"),
  indexPath: path.resolve(__dirname, "../templates/", "blog", "index.html"),
};