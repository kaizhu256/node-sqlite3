(function () {
    "use strict";
    let sqlite3 = require("./sqlite3");
    let db = new sqlite3.Database(":memory:");
    db.all("SELECT sqrt(2);", function (err, data) {
        if (err) {
            throw err;
        }
        console.error(data);
    });
}());
