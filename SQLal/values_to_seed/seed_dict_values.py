import datetime

expense_item_values = [
    {
        "item_name": "vendedor",
        "family_id": 1,
        "cost": 2200.01
    },
    {
        "item_name": "rrhh",
        "family_id": 1,
        "cost": 1200.01
    },
    {
        "item_name": "anuncio de tv",
        "family_id": 3,
        "cost": 1111.01
    }
]


expense_family_values = [
    {
        "service_name": "personal"
    },
    {
        "service_name": "servicios basicos"
    },
    {
        "service_name": "marketing"
    },
    {
        "service_name": "contabilidad"
    }
]

assigned_expense_values = [
    {
        "item_id": 1,
        "state": "pagado",
        "created_at": datetime.datetime(2021, 12, 19, 22, 23, 30),
        "sale_id": 1
    },
    {
        "item_id": 1,
        "state": "pagado",
        "created_at": datetime.datetime(2021, 12, 19, 22, 23, 30),
        "sale_id": 3
    },
    {
        "item_id": 1,
        "state": "pagado",
        "created_at": datetime.datetime(2021, 12, 19, 22, 23, 30)
    },
    {
        "item_id": 3,
        "state": "pagado",
        "created_at": datetime.datetime(2018, 12, 9, 20, 0, 0)
    }
]

product_values = [
    {
        "price": 22000,
        "cost": 15000,
        "stock": 100
    },
    {
        "price": 20000,
        "cost": 18000,
        "stock": 100
    },
    {
        "price": 25000,
        "cost": 10000,
        "stock": 100
    }
]

sale_values = [
    {
        "product_id": 1,
        "created_at": datetime.datetime(2021, 12, 19, 22, 23, 30)
    },
    {
        "product_id": 2,
        "created_at": datetime.datetime(2021, 12, 19, 22, 23, 30)
    },
    {
        "product_id": 3,
        "created_at": datetime.datetime(2021, 12, 19, 22, 23, 30)
    },
    {
        "product_id": 4,
        "created_at": datetime.datetime(2007, )
    }
]
