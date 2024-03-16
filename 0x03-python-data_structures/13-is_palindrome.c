#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *reversed(listint_t *head)
{
    listint_t *current = head, *prev = NULL, *next;

    if (current == NULL || current->next == NULL)
    {
        return (current);
    }
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
    return (head);
}

void push(listint_t **head, int data)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    new_node->n = data;
    new_node->next = *head;
    *head = new_node;
}

int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    listint_t *tmp = NULL; // Declaration of tmp pointer
    listint_t *rev;
    int i, len = 0;

    if (current == NULL)
        return (0);
    else if (current->next == NULL)
        return (1);
    tmp = NULL;
    while (current != NULL)
    {
        push(&tmp, current->n);
        len++;
        current = current->next;
    }
    rev = reversed(tmp);

    // Reset current to the head of the list for further use
    current = *head;
    for (i = 0; i < len / 2; i++)
    {
        if (current->n != rev->n)
            return (0);
        current = current->next;
        rev = rev->next;
    }
    
    return (1);
}
