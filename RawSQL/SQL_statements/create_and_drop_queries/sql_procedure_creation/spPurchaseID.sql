#
CREATE PROCEDURE spPurchaseId (
    IN n_index INT,
    IN product_id INT,
    OUT purchase_id INT
) BEGIN DECLARE m_index INT DEFAULT n_index -1;

SET
    purchase_id = (
        SELECT
            id
        FROM
            purchase
        WHERE
            purchase.product_id = product_id
        ORDER BY
            purchase.created_at
        LIMIT
            m_index, 1
    );

END;