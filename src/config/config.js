const dotenv = require('dotenv');

dotenv.config();

function required(key, defaultValue=undefined){
    const value = process.env[key] || defaultValue; 
    if(value == null){
        throw new Error(`키 ${key}는 undefined입니다.`);
    }
    return value;
};

const config = {
    host: {
        port: parseInt(required('HOST_PORT', 8080))
    },
};

module.exports = config;