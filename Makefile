#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   Makefile                                                                 *#
#*                                                                            *#
#*   By: yhetman <yhetman@student.unit.ua>                                    *#
#*                                                                            *#
#*   Created: 2021/11/29 21:49:25 by yhetman                                  *#
#*   Updated: 2021/11/29 21:49:26 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

SRCS =  

SRCS_DIR = src/

OBJ_DIR = obj/

OBJ = $(addprefix $(OBJ_DIR), $(SRCS:.c=.o))

LIB_NAME = libdsa.a

DSA = dsa

FLAGS = -I includes -Wall -Wextra -Werror #-I ../../SHA256/includes/  -I /usr/include/openssl/
DEBUG_FLAGS = -g3 -fsanitize=address

DSA_MAIN = src/main.c 

all: make_obj_dir $(DSA)

$(OBJ_DIR)%.o: $(SRCS_DIR)%.c 
	gcc $(FLAGS) -c $< -o $@

$(LIB_NAME): $(OBJ)
	ar -rv $(LIB_NAME) $^
	ranlib $(LIB_NAME)

$(DSA): $(LIB_NAME) $(DSA_MAIN)
	gcc $(FLAGS) $(DSA_MAIN) $(LIB_NAME) -o $(DSA) #-lgmp -lssl -lcrypto libSHA256.a

make_obj_dir:
	mkdir -p $(OBJ_DIR)

clean:
	rm -rf $(OBJ_DIR)

fclean: clean
	rm -f $(DSA)
	rm -f $(LIB_NAME)

re: fclean all

.PHONY: all clean flcean re debug