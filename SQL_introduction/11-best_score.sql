-- Retrieve the 'score' and 'name' columns from the 'second_table' table in the 'hbtn_0c_0' database
-- Filter the results to include only records where the 'score' is greater than or equal to 10
-- Order the filtered results by 'score' in descending order
SELECT score, name FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
