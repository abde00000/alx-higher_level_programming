#include "main"
/**
 * _puts_recursion - prints the text
 *
 * @s: the text should be printed
 *
 */
void _puts_recursion(char *s)
{
	if (*s == '\0')
	{
		_putchar('\n');
		return;
	}
	_putchar(*s);
	_puts_recursion(s + 1);
}
