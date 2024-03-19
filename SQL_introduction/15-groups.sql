-- Retrieve the 'score' column and count the occurrences of each score from the 'second_table' table in the 'hbtn_0c_0' database
-- Group the results by the 'score' column
-- Order the results by 'score' in descending order
SELECT score, COUNT(score) AS number FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY score DESC;
