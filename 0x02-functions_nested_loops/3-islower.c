nclude"main.h"

/**
 * _islower - function to check if
 *           character is lowerchar
 *
 * @c: checks input of function
 *
 * Return: returns 1 if `c` is lower
 *         or always 0 (Success)
*/
int _islower(int c)
{
	if (c >= 97 && c <= 122)
		return (1);
	return (0);
}
