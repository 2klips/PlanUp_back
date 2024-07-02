import express from 'express';
import userRouter from './user.js';
import mainRouter from './main.js';
import todolistRouter from './todolist.js';
import checklistRouter from  './checklist.js';

const router = express.Router();

router.use('/', mainRouter);
router.use('/main', mainRouter);
router.use('/user', userRouter);
router.use('/list', todolistRouter);
router.use('/list/check', checklistRouter);


export default router