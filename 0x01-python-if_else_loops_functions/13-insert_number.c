#include "lists.h"

/**
 * insert_node - this will Insert a number into a sorted singly-linked list.
 * @head: pointer the head of the linked list.
 * @number: number to be  inserted.
 *
 * Return: NULL If the function fails
 * else - a pointer to the new_node.
 */

#include "lists.h"

listint_t *insert_node(listint_t **head, int number)

{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)

		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)

	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	listint_t *current = *head;

	while (current->next != NULL && current->next->n < number)

	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}

