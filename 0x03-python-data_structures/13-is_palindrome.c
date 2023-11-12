#include "lists.h"

/**
 * palindrom - recursive palind or not
 * @head: head list
 * Return 0 if it is not palindrom
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - func to know if it's palindrom
 * @head: head list
 * @end: end list
 */
int aux_palind(listint_t **head, listint_ t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
