#include "lists.h"
/**
 * reversed - reverses a linked list
 * @head: pointer to the head of the linked list
 *
 * Return: pointer to the reversed linked list
 */
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
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    listint_t *rev;
    int i, len = 0;

    if (current == NULL)
        return (0);
    else if (current->next == NULL)
        return (1);
    rev = reversed(current);
    while (current != NULL)
    {
        len++;
        current = current->next;
    }
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