var path = require('path');

var root = path.resolve(__dirname, '..');
var files = [`${root}/app/**/*.py`, `${root}/app/**/*.html`, `${root}/app/**/*.js`];
var watch = `${root}/app/static/**/*.css`;

// require the module as normal
var bs = require("browser-sync").create();

// .init starts the server
bs.init({
    proxy: "0.0.0.0:8000",
    files: files,
    notify: false,
    port: 3000,
});

// stream changes to all browsers
bs.watch(watch).on("change", bs.reload);
