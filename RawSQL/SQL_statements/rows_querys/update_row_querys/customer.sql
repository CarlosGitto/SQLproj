#
UPDATE
    customer
SET
    customer.name = val2,
    customer.surname = val3,
    customer.phone_number = val4,
    customer.email = val5
WHERE
    customer.id = val1;