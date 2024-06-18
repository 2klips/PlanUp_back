const database = require('../models/userDB.js');
const config = require('../config/config.js');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

function createJwtToken(id){
    return jwt.sign({id}, config.jwt.secretKey, {expiresIn: config.jwt.expiresInSec});
}
