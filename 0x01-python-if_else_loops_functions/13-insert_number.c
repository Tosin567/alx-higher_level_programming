#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: double pointer to the head of the linked list
* @number: number to be inserted in the list
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *current;

if (head == NULL)
return (NULL);

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
if (*head == NULL)
{
new->next = NULL;
*head = new;
return (new);
}

current = *head;
while (current != NULL)
{
if (number < current->n)
{
new->next = current;
*head = new;
return (new);
}
if (current->next == NULL)
{
current->next = new;
new->next = NULL;
return (new);
}
if (number >= current->n && number <= current->next->n)
{
new->next = current->next;
current->next = new;
return (new);
}
current = current->next;
}

return (NULL);
}
