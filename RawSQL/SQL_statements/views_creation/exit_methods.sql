#
CREATE OR REPLACE VIEW fifo AS
SELECT * FROM purchase
WHERE in_stock > 0
ORDER BY created_at;
#
CREATE OR REPLACE VIEW lifo AS
SELECT * FROM purchase
WHERE in_stock > 0
ORDER BY created_at DESC;