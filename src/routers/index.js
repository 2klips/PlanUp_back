import express from 'express';
import userRouter from './user.js';
import recruitmentRouter from './recruitment.js';
import todolistRouter from './todolist.js';
import checklistRouter from  './checklist.js';
import certificateRouter from './certificate.js'
import scraperRouters from './scraper.js';

const router = express.Router();

router.use('/recruitment', recruitmentRouter);
router.use('/user', userRouter);
router.use('/list', todolistRouter);
router.use('/scrape', scraperRouters);
router.use('/checklist', checklistRouter);
router.use('/certifi', certificateRouter);


export default router
