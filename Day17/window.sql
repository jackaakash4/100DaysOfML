--Window functions are  one of the SQL's superpowers
SELECT
    experiment_id,
    loss,
    LAG(loss) OVER (
        ORDER BY experiment_id
    )  AS previous_loss
FROM experiments;

SELECT
    experiment_id,
    loss,
    LAG(loss) OVER (
        ORDER BY experiment_id
    ) AS previous_loss,
    loss - 
    LAG(loss) OVER (
        ORDER BY experiment_id
    ) AS loss_change
FROM experiments;
