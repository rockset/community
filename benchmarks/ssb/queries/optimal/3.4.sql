select c_city, s_city, d_year, sum(lo_revenue) as revenue
from denormalized HINT(access_path=column_scan)
where (c_city='UNITED KI1' or c_city='UNITED KI5')
  and (s_city='UNITED KI1' or s_city='UNITED KI5')
  and c_region = 'EUROPE'
  and s_region = 'EUROPE'
  and d_year = 1997
  and d_monthnuminyear = 12
group by c_city, s_city, d_year
order by d_year asc, revenue desc;
