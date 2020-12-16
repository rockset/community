select customer.c_city, supplier.s_city, dwdate.d_year, sum(lineorder.lo_revenue) as revenue
from lineorder
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
  join supplier on lineorder.lo_suppkey = supplier.s_suppkey
  join customer on lineorder.lo_custkey = customer.c_custkey
where (customer.c_city='UNITED KI1' or customer.c_city='UNITED KI5')
  and (supplier.s_city='UNITED KI1' or supplier.s_city='UNITED KI5')
  and dwdate.d_yearmonth = 'Dec1997'
group by c_city, s_city, d_year
order by d_year asc, revenue desc;
