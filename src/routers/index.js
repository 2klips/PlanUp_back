import express from 'express';
import userRouter from './user';
import mainRouter from './main';
import todolistRouter from './todolist';

const router = express.Router();

router.use('/', mainRouter);
router.use('/main', mainRouter);
router.use('/user', userRouter);
router.use('/list', todolistRouter)



export default router