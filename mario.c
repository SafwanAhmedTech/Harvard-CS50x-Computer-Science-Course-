#include <cs50.h>
#include <stdio.h>
int main(void)
{
    int height = get_int("what is the height of the pyramid");
    // That was to get the height of the pyramid
    while (height <= 0)
    {
        height = get_int("what is the height of the pyramid: ");
    }
    for (int row = 1; row <= height; row++)
    {
        // print spaces
        for (int space = 0; space < height - row; space++)
        {
            printf(" ");
        }
        // print hashes
        for (int hash = 0; hash < row; hash++)
        {
            printf("#");
        }
        printf("\n");
    }
}
