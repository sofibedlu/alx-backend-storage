-- SQL script that creates an index idx_name_first_score on the table names and
-- the first letter of name and the score

CREATE INDEX idx_name_first_score ON names ((SUBSTRING(name FROM 1 FOR 1)), score);
