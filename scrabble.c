#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string player1 = get_string("player 1, enter your word: ");
    string player2 = get_string("player 2, enter your word: ");
    int player1score = 0;
    int player2score = 0;
    int num = 0;

    int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    //this creates the arry for the points
    int n;

    for (n = 0; n < strlen(player1); n++)
    {
        player1[n] = toupper(player1[n]);
    }
    for (n = 0; n < strlen(player2); n++)
    {
        player2[n] = toupper(player2[n]);
    }
    for (n = 0; n < strlen(player1); n++)
    {
        num = player1[n] - 'A';
        player1score += points[num];
    }
    for (n = 0; n < strlen(player2); n++)
    {
        num = player2[n] - 'A';
        player2score += points[num];
    }
    if (player1score > player2score)
    {
        printf("Player 1 wins!\n");
    }
    else if (player2score > player1score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!");
    }
}
