import axios from 'axios';

export const scrapeJobDetails = async (url) => {
    try {
        const response = await axios.post('http://localhost:8000/scrape', { url });
        return response.data;
    } catch (error) {
        throw new Error('Failed to scrape job details');
    }
};
