/* ************************************************************************** */
/*                                                                            */
/*                                                                            */
/*   main.c                                                                   */
/*                                                                            */
/*   By: yhetman <yhetman@student.unit.ua>                                    */
/*                                                                            */
/*   Created: 2021/11/29 21:51:58 by yhetman                                  */
/*   Updated: 2021/11/29 21:51:59 by yhetman                                  */
/*                                                                            */
/* ************************************************************************** */

#include "dsa.h"
#include "gf.h"


void
init_ecc(t_elliptic_curve	*ecc)
{
	ecc->m = 167;
	ecc->A = 1;
	ecc->B = "6EE3CEEB230811759F20518A0930F1A4315A827DAC";
	ecc->n = "3FFFFFFFFFFFFFFFFFFFFFB12EBCC7D7F29FF7701F";
}


int 	main(int argc, char const *argv[])
{
	t_gf				gf;
	t_elliptic_curve	ecc;


	init_ecc(&ecc);

	init_gf(ecc.m, &gf);

	return 0;
}