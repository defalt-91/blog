const path = require("path");

module.exports = {
    outputDir: path.resolve(__dirname, "../static", "survey"),
    publicPath: process.env.VUE_APP_STATIC_URL,
    indexPath: path.resolve(__dirname, "../templates/", "survey", "index.html"),
    productionSourceMap: false,
};