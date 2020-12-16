select sum(lineorder.lo_revenue), dwdate.d_year, part.p_brand1
from lineorder
  join part on lineorder.lo_partkey = part.p_partkey
  join supplier on lineorder.lo_suppkey = supplier.s_suppkey
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where part.p_brand1 = 'MFGR#2221'
  and supplier.s_region = 'EUROPE'
group by d_year, p_brand1
order by d_year, p_brand1;
