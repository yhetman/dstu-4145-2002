/* ************************************************************************** */
/*                                                                            */
/*                                                                            */
/*   elliptic_curve.h                                                         */
/*                                                                            */
/*   By: yhetman <yhetman@student.unit.ua>                                    */
/*                                                                            */
/*   Created: 2021/11/29 21:53:28 by yhetman                                  */
/*   Updated: 2021/11/29 21:53:29 by yhetman                                  */
/*                                                                            */
/* ************************************************************************** */

#ifndef ELLIPTIC_CURVE_H
# define ELLIPTIC_CURVE_H

# include <stdio.h>
# include <stdlib.h>
# include <stdint.h>
# include <string.h>
# include <unistd.h>
# include <stdbool.h>

typedef struct 	s_elliptic_curve
{
	size_t		A;
	size_t		m;
	char		B[46];
	char   		n[46];
}				t_elliptic_curve;


#endif
