// Binary compression.

string input = Console.ReadLine()!;

int count = 0;

foreach (var c in input)
{
    if (c == '1')
    {
        if (97 + count <= 122)
        {
            Console.Write((char)(97 + count));
        }
        else
        {
            for (int i = 0; i < (97 + count - 121); i++)
                Console.Write('0');

            Console.Write('z');
        }

        count = 0;
    }
    else
        count++;
}
