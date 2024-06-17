const express = require("express");
const config = require("./config");
const morgan = require("morgan");
const cors = require("cors");
const routers = require("./routers");
const path = require("path");

const app = express();
app.use(cors());

app.use(express.json());

app.use(morgan("dev"));
app.use('/', routers);

app.listen(config.host.port);
