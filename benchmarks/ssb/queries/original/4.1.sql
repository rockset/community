select dwdate.d_year, customer.c_nation, sum(lineorder.lo_revenue - lineorder.lo_supplycost) as profit
from lineorder
  join customer on lineorder.lo_custkey = customer.c_custkey
  join supplier on lineorder.lo_suppkey = supplier.s_suppkey
  join part on lineorder.lo_partkey = part.p_partkey
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where customer.c_region = 'AMERICA'
  and supplier.s_region = 'AMERICA'
  and (part.p_mfgr = 'MFGR#1' or part.p_mfgr = 'MFGR#2')
group by d_year, c_nation
order by d_year, c_nation;
