import express from 'express';
import mongoose from 'mongoose';

const router = express.Router();

// 채용 공고 스키마 정의
const jobPostingSchema = new mongoose.Schema({
  title: String,
  company: String,
  deadline: String,
  userid: String
});

// 모델 생성
const JobPosting = mongoose.model('JobPosting', jobPostingSchema);

// 채용 공고 저장
router.post('/', async (req, res) => {
  try {
    const { title, company, deadline, userid } = req.body;
    const newJobPosting = new JobPosting({ title, company, deadline, userid });
    await newJobPosting.save();
    res.status(201).send(newJobPosting);
  } catch (error) {
    res.status(500).send(error);
  }
});

// 채용 공고 목록 가져오기
router.get('/:userid', async (req, res) => {
  try {
    const { userid } = req.params;
    const jobPostings = await JobPosting.find({ userid });
    res.status(200).send(jobPostings);
  } catch (error) {
    res.status(500).send(error);
  }
});

// 채용 공고 삭제
router.delete('/:id', async (req, res) => {
    try {
      const { id } = req.params;
      await JobPosting.findByIdAndDelete(id);
      res.status(200).send({ message: '채용 공고가 삭제되었습니다.' });
    } catch (error) {
      res.status(500).send(error);
    }
  });

export default router;
