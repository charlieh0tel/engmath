import quantities as pq

_m2 = pq.m * pq.m
_m2K = _m2 * pq.C               # sic

H_PASSIVE_CONVECTION = 5. * pq.W / _m2K
H_PASSIVE_RADIATION = 7. * pq.W / _m2K
H_PASSIVE = H_PASSIVE_CONVECTION + H_PASSIVE_RADIATION

SOLAR_INSOLATION = 800 * pq.W / _m2
