/* ************************************************************************** */
/*                                                                            */
/*                                                                            */
/*   gf.h                                                                     */
/*                                                                            */
/*   By: yhetman <yhetman@student.unit.ua>                                    */
/*                                                                            */
/*   Created: 2021/11/29 22:02:40 by yhetman                                  */
/*   Updated: 2021/11/29 22:02:42 by yhetman                                  */
/*                                                                            */
/* ************************************************************************** */

#ifndef GF_H
# define GF_H

# include <stdio.h>
# include <stdlib.h>
# include <stdint.h>
# include <string.h>
# include <unistd.h>
# include <stdbool.h>


typedef struct  	s_gf
{
	size_t			m;
	size_t			f;
	size_t 			mask;
}					t_gf;


void				init_gf(size_t m, t_gf	*gf);
#endif
