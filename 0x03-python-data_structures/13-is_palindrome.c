#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *mid = NULL;
    int is_pal = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1; // Empty list or single node list is palindrome

    // Use slow and fast pointers to find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        // The list has odd number of nodes, skip the middle node
        mid = slow;
        slow = slow->next;
    }

    // Reverse the first half of the list
    listint_t *prev = NULL, *next = NULL, *current = *head;
    while (current != slow)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    // Compare the reversed first half with the second half of the list
    listint_t *first_half = prev;
    listint_t *second_half = slow;
    while (first_half != NULL && second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            is_pal = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the original list by reversing the first half again
    prev = NULL;
    current = *head;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;

    // If the list had an odd number of nodes, re-link the middle node
    if (mid != NULL)
        prev_slow->next = mid;

    return is_pal;
}
