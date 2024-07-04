import { spawn } from 'child_process';

export async function getJobDetails(req, res, next) {
    const { url } = req.body;

    if (!url) {
        return res.status(400).json({ error: 'URL is required' });
    }

    const pythonProcess = spawn('python', ['src/services/4개모음.py', url]);

    let scriptOutput = '';

    pythonProcess.stdout.on('data', (data) => {
        scriptOutput += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            try {
                const jobDetails = JSON.parse(scriptOutput);
                console.log(jobDetails)
                res.json(jobDetails);
            } catch (parseError) {
                res.status(500).json({ error: 'Error parsing JSON data from Python script' });
            }
        } else {
            res.status(500).json({ error: `Python script exited with code ${code}` });
        }
    });
}