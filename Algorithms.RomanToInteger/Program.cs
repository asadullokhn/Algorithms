Dictionary<char, int> romanToInt = new Dictionary<char, int>() {
    { 'I', 1 },
    { 'V', 5 },
    { 'X', 10 },
    { 'L', 50 },
    { 'C', 100 },
    { 'D', 500 },
    { 'M', 1000 }
};

string s = "III";

int number = 0;
s = s.Replace("IV", "IIII")
     .Replace("IX", "VIIII")
     .Replace("XL", "XXXX")
     .Replace("XC", "LXXXX")
     .Replace("CD", "CCCC")
     .Replace("CM", "DCCCC");

foreach (char c in s)
    number += romanToInt[c];

Console.WriteLine(number);
