SELECT 
    title,
    url,
    author,
    score,
    posted_date
FROM 
    HackerNews
WHERE 
    score >= 100
ORDER BY 
    score DESC, posted_date DESC;
