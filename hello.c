#include <cs50.h>
#include <stdio.h>
int main(void)
{
    char * name = get_string("what is your name: ");
    // this is to get your name
    printf("hello, %s\n", name);
}
