-- 15. Only Comedy
SELECT score, COUNT(*) AS number FROM sceond_table GROUP BY score ORDER BY number DESC;
