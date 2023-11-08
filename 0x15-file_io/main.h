#ifndef MAIN_H
#define MAIN_H

#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>

int _putchar(char c);
ssize_t read_textfile(const char *filename, size_t letters);
int create_file(const char *filename, char *text_content);
int append_text_to_file(const char *filename, char *text_content);
size_t _strlen(char *text)
{
	size_t i = 0;

	if (text == NULL)
		return (0);
	while (text[i] != '\0')
	{
		i++;
	}
	return (i);
}
#endif /*MAIN_H*/