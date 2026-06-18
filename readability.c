#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");
    int wordcount = 1;
    int lettercount = 0;
    int length = strlen(text);
    int n;
    for (n = 0; n < length; n++)
    {
        if (isalpha(text[n]))
        {
            lettercount += 1;
        }
        else if (text[n] == ' ')
        {
            wordcount += 1;
        }
    }
    float L = lettercount / ((float) wordcount / 100);
    int fullstopcount = 0;
    for (n = 0; n < length; n++)
    {
        if (text[n] == '.')
        {
            fullstopcount += 1;
        }
        if (text[n] == '?')
        {
            fullstopcount += 1;
        }
        if (text[n] == '!')
        {
            fullstopcount += 1;
        }
    }
    float S = fullstopcount / ((float) wordcount / 100);
    float index = 0.0588 * L - 0.296 * S - 15.8;
    index = round(index);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) index);
    }
}
