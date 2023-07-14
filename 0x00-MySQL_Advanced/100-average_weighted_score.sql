-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
	IN user_id INT
)
BEGIN
	DECLARE total_weighted_score FLOAT;
	DECLARE total_weighted FLOAT;
	DECLARE average_weighted_score FLOAT;

	SELECT SUM(score * weight) INTO total_weighted_score
	FROM corrections
	JOIN projects ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	SELECT SUM(weight) INTO total_weighted
	FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

	IF total_weighted IS NOT NULL AND total_weighted > 0 THEN
		SET average_weighted_score = total_weighted_score / total_weighted;
	ELSE
		SET average_weighted_score = 0;
	END IF;

	UPDATE users
	SET average_score = average_weighted_score
	WHERE id = user_id;
END //

DELIMITER ;
