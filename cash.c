#include <cs50.h>
#include <stdio.h>
int main(void)
{
    int coins;
    int multiple;
    int x;
    int y;
    int z;
    int a;
    int change = get_int("Change owed: ");
    while (change <= 0)
    {
        change = get_int("change owed: ");
    }
    if (change < 5)
    {
        coins = change;
    }
    else if (change < 10)
    {
        multiple = change / 5;
        coins = change - multiple * 5 + multiple;
    }
    else if (change < 25)
    {
        multiple = change / 10;
        x = change - multiple * 10;
        y = x / 5;
        coins = x - y * 5 + y + multiple;
    }
    else
    {
        multiple = change / 25;
        x = change - multiple * 25;
        y = x / 10;
        z = x - y * 10;
        a = z / 5;
        coins = z - a * 5 + multiple + y + a;
    }
    printf("%i\n", coins);
}
