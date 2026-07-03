#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int only_digits(string word);
char rotate(char c, int y);

int main(int argc, string argv[])
{
    int r;
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (only_digits(argv[1]) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        string plaintext = get_string("plaintext: ");
        int plainlength = strlen(plaintext);
        printf("ciphertext: ");
        for (r = 0; r < plainlength; r++)
        {
            printf("%c", rotate(plaintext[r], atoi(argv[1])));
        }
        printf("\n");
        return 0;
    }
}

int only_digits(string word)
{
    int length = strlen(word);
    int n;
    int count = 0;
    for (n = 0; n < length; n++)
    {
        int x = (int) word[n];
        if (isdigit(word[n]))
        {
            count += 1;
        }
    }
    if (count == length)
    {
        return true;
    }
    else
    {
        return false;
    }
}

char rotate(char c, int y)
{
    if (isupper(c))
    {
        return ((c - 'A' + y) % 26) + 'A';
    }
    if (islower(c))
    {
        return ((c - 'a' + y) % 26) + 'a';
    }
    else
    {
        return c;
    }
}
