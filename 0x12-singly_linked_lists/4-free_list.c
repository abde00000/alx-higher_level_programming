#include "lists.h"
/**
 * free_list - frees a list_t list
 * @head: pointer to the list_t
 */
void free_list(list_t *head)
{
	list_t *current;

	while (head != NULL)
	{
		current = head;
		free(current->str);
		free(current);
		head = head->next;
	}
}
