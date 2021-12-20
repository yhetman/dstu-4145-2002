#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   consts.py       	                                                      *#
#*                                                                            *#
#*   By: yhetman <yhetman@student.unit.ua>                                    *#
#*                                                                            *#
#*   Created: 2021/11/29 21:49:25 by yhetman                                  *#
#*   Updated: 2021/11/29 21:49:26 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#


DEBUG = True

A=1
B=0x4A6E0856526436F2F88DD07A341E32D04184572BEB710
n=0x3FFFFFFFFFFFFFFFFFFFFFFB981960435FE5AB64236EF
m = 179

prim_eleme = (1 << m) - 1 # ptimitive element

polinominal = (1 << m) + (1 << 4) + (1 << 2) + (1 << 1) + 1 # primitive polynomial

O = (0, 0)
