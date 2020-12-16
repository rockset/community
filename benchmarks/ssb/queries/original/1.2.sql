select sum(lineorder.lo_extendedprice * lineorder.lo_discount) as revenue
from lineorder
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where dwdate.d_yearmonthnum = 199401
  and lineorder.lo_discount between 4 and 6
  and lineorder.lo_quantity between 26 and 35;
