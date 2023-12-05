#include "lists.h"

/**
 * palindrome - useage for is_palindrome
 * @top: a pointer to a pointer to a singly linked list
 * @next: a pointer to a singly linked list
 * Return: 1 if palindrome otherwise 0
 */

int palindrome(listint_t **top, listint_t *next)
{
	int result = 0;

	if (next == NULL)
		return (1);

	if (palindrome(top, next->next) && ((*top)->n == next->n))
		result = 1;

	*top = (*top)->next;

	return (result);
}

/**
 * is_palindrome - a function that check if a singly linked list is a palindrome
 * @head: the linked list double pointer.
 * Return: 1 if list is a palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	return (palindrome(head, *head));
}
