int[] inputs = Console.ReadLine().Split().Select(int.Parse).ToArray();

var date = new DateTime(inputs[2], inputs[1], inputs[0]);
Console.WriteLine(date.DayOfWeek.ToString().ToUpper());
