#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int a;
int b;
int c;
int d;

int fd[2];

/*void Child()
{
  a = 3 + 3;
  printf("%d\n",a);
  write(fd[1], &a, sizeof(a));
  close(fd[1]);
}*/

/*void Parent()
{
  c = a + b;
  d = c - 1;
  close(fd[0]);
}*/

int main(int argc, char **argv)
{
  pipe(fd);
  int pid = fork();
  if (pid == 0)
    {
      //child
      close(fd[0]);	
      a = 3 + 3;
      write(fd[1], &a, sizeof(a));
      close(fd[1]);
      return 0;
    }
  else
    {
      //parent
      close(fd[0]);
      b = 2 + 1;
      wait(&a);
      read(fd[0], &a, sizeof(a));
      c = a + b;
      printf("%d\n",a);
      d = c - 1;
      close(fd[0]);
      printf("%d\n",a);
      printf("D = %d\n", d);
      return 0;
    }
}

