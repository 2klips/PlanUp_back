import express from 'express';
import userRouter from './user.js';
import recruitmentRouter from './recruitment.js';
import todolistRouter from './todolist.js';
import checklistRouter from './checklist.js';
import certificateRouter from './certificate.js';
import scraperRouters from './scraper.js';
import jobPostingRouter from './jobPostings.js'; // 새로 추가된 라우터

const router = express.Router();

router.use('/user', userRouter);
router.use('/recruitment', recruitmentRouter);
router.use('/list', todolistRouter);
router.use('/checklist', checklistRouter);
router.use('/certifi', certificateRouter);
router.use('/scrape', scraperRouters);
router.use('/jobPostings', jobPostingRouter); // 새로 추가된 라우터 경로

export default router;
