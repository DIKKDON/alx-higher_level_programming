#include "lists.h"


/**
 * check_cycle - check if a linked list contains cycles
 * @list: head of the linked list
 * Return: 1 if there is acycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_pointer = list;
	listint_t *fast_pointer = list;

	if (list == NULL)
		return (0);
	while (fast_pointer->next && fast_pointer->next->next)
	{
		slow_pointer = slow_pointer->next;
		fast_pointer = fast_pointer->next->next;

		if (fast_pointer == slow_pointer)
			return (1);
	}
	return (0);
}
