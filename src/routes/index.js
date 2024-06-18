const express = require('express');
// const mainRouter = require('./main');
const userRouter = require('./user');

const router = express.Router();


router.use('/main', mainRouter);
router.use('/user', userRouter);



module.exports = router;