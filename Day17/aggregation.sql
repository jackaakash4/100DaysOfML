SELECT architecture,
        AVG(accuracy) AS avg_accuracy

FROM model_runs
WHERE accuracy > 0.85
GROUP BY architexture
HAVING AVG(accuracy) > 0.90
ORDER BY avg_accuracy DESC;
