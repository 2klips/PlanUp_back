import express from 'express';
import userRouter from './user.js';
import mainRouter from './main.js';
import todolistRouter from './todolist.js';

const router = express.Router();

router.use('/', mainRouter);
router.use('/main', mainRouter);
router.use('/user', userRouter);
router.use('/list', todolistRouter)



export default router