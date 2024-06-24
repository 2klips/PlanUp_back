const express = require('express');
// const mainRouter = require('./main');
const userRouter = require('./user');
const mainRouter = require('./main');
const todolistRouter = require('./todolist');

const router = express.Router();

router.use('/', mainRouter);
router.use('/main', mainRouter);
router.use('/user', userRouter);
router.use('/list', todolistRouter)


module.exports = router;