// Cards 

var input = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();

int p = input[0], k = input[1];

int count = 0;

while (p <= k)
{
    int c = p;

    while (c != 2)
    {
        c = c % 2 == 0 ? c / 2 : c * 3 + 1;
        count++;
    }

    p++;
}

Console.WriteLine(count);
