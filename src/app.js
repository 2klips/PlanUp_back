const express = require("express");
const config = require("./config/config");
const morgan = require("morgan");
const cors = require("cors");
const routers = require("./routers");
const path = require("path");
// const db = require("./models/db");

// db.connectMongoose();

const app = express();
app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

app.use('/', routers);

app.listen(8080, () => {
    console.log('Server listening on port 8080');
});
