#include "lists.h"

/**
 * insert_node - this will Insert a number into a sorted singly-linked list.
 * @head: pointer the head of the linked list.
 * @number: number to be  inserted.
 *
 * Return: NULL If the function fails
 * else - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)

		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	listint_t *current = *head;

	while (current->next && current->next->n < number)

		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
