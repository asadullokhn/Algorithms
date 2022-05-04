static bool IsPalindrome(int x)
{
    string sx = x.ToString();

    for (int i = 0; i < sx.Length / 2; i++)
        if (sx[i] != sx[sx.Length - i - 1])
            return false;

    return true;
}

Console.WriteLine(IsPalindrome(121));