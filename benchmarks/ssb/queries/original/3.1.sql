select customer.c_nation, supplier.s_nation, dwdate.d_year, sum(lineorder.lo_revenue) as revenue
from lineorder
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
  join customer on lineorder.lo_custkey = customer.c_custkey
  join supplier on lineorder.lo_suppkey = supplier.s_suppkey
where  customer.c_region = 'ASIA'
  and supplier.s_region = 'ASIA'
  and dwdate.d_year >= 1992
  and dwdate.d_year <= 1997
group by c_nation, s_nation, d_year
order by d_year asc, revenue desc;
