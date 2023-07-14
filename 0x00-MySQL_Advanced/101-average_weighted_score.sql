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

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;
