#include "lists.h"

/*
  *check_cycle -check the cycle of a linked list
  *@list: the variable
  *
  *Description - check loops
  *Return: 0 or 1
  */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
