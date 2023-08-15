#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to the pointer of the first node of a listint_t list
 *
 * Return: 1 if list is a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	int i = 0, k = 0, arr[1024], is_p = 0;
	listint_t *new_list, *temp = *head;

	if (*head != NULL)
	{
		while (*head != NULL)
		{
			arr[i] = (*head)->n;
			*head = (*head)->next;
			i++;
		}
		new_list = malloc(sizeof(listint_t));
		k = i--;
		*head = temp;
		while(k >= 0)
		{
			add_nodeint_end(&new_list, arr[k]);
			k--;
		}
		printf("Newlist \n");
		print_listint(new_list);
		while (*head != NULL)
		{
			printf("l1 %d l2 %d\n", (*head)->n, new_list->n);
			if ((*head)->n == new_list->n)
				is_p = 1;
			else
				return (0);
			printf("l1 %d l2 %d\n", (*head)->n, new_list->n);
			*head = (*head)->next;
			new_list = new_list->next;
		}
	}
	return (is_p);
}
