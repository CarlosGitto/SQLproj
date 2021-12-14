
from make_views import create_views
from drop_tables import drop_tables
from make_tables import create_tables
from table_seeder import seed_tables
from selec_views import select_views_month, select_views_year

drop_tables()
create_tables()
create_views()
seed_tables(10,1000,50,200)
select_views_month()
select_views_year()
