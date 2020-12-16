select sum(lo_extendedprice * lo_discount) as revenue
from denormalized HINT(access_path=column_scan)
where d_weeknuminyear = 6
  and d_year = 1994
  and d_monthnuminyear = 2
  and lo_discount between 5 and 7
  and lo_quantity between 26 and 35;
