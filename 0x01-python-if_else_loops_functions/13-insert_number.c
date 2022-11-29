#include "lists.h"
#include<stdlib.h>



/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: 1st digit in the multiplication
 * @number: 2nd digit to be multiplied
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL)
	{
		*head = newnode;
		return (newnode);
	}

	temp = *head;
	if (number <= temp->n)
	{
		newnode->next = temp;
		*head = newnode;
		return (newnode);
	}

	while (number > temp->n && temp->next != NULL && number > temp->next->n)
		temp = temp->next;

	newnode->next = temp->next;
	temp->next = newnode;
	return (newnode);
}
