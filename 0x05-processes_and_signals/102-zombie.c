#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int infinite_while(void);
void createZombie(int n);

/**
 * main - C program that creates 5 zombie processes
 * Return: int
 */
int main(void)
{
	createZombie(5);
	return (0);
}

/**
 * createZombie - creates zombie process
 * @n: number of zombies to create
 * Return: void
 */
void createZombie(int n)
{
	pid_t pid;

	if (n == 0)
	{
		return;
	}

	pid = fork();

	if (pid == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	else if (pid > 0)
	{
		createZombie(n - 1);
		infinite_while();
	}
	else
	{
		perror("fork");
		exit(EXIT_FAILURE);
	}
}

/**
 * infinite_while - runs infinite while loop
 * to keep the child process from terminating
 * Return: int
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
