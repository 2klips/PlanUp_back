import { Router } from 'express';
import { spawn } from 'child_process';
import { isAuth } from '../middlewares/user.js';

const router = Router();

const scrapeHandler = (scriptPath) => async (req, res, next) => {
    const { url } = req.body;
    if (!url) {
        return res.status(400).send({ error: 'URL is required' });
    }
    console.log(`Scraping URL: ${url}`); // 로그 추가
    const python = spawn('python', [scriptPath, url]);

    let scriptOutput = '';

    python.stdout.on('data', (data) => {
        scriptOutput += data.toString();
    });

    python.stderr.on('data', (data) => {
        console.error('stderr:', data.toString());
    });

    python.on('close', (code) => {
        if (code === 0) {
            try {
                const parsedData = JSON.parse(scriptOutput);
                console.log(`Scraped details: ${JSON.stringify(parsedData)}`); // 로그 추가
                res.json(parsedData);
            } catch (err) {
                console.error('Failed to parse JSON:', scriptOutput);
                res.status(500).json({ error: 'Failed to parse JSON' });
            }
        } else {
            res.status(500).json({ error: `Python script exited with code ${code}` });
        }
    });
};

router.post('/scrape', isAuth, scrapeHandler('C:\\gisan\\kdt3\\backend2\\src\\controllers\\scraper.py'));

export default router;
