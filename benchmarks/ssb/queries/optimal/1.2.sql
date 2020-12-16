select sum(lo_extendedprice * lo_discount) as revenue
from denormalized HINT(access_path=column_scan)
where d_year = 1994 and d_monthnuminyear = 1
and lo_discount between 4 and 6
and lo_quantity between 26 and 35;
