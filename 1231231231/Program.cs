using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace _1231231231
{
    internal class Program
    {
        static int playerX, playerY;

        static void Main(string[] args)
        {
            Console.CursorVisible = false;

            for (int level = 1; level <= 3; level++)
            {
                PlayLevel(level);
            }

            Console.Clear();
            Console.WriteLine("Поздравляем! Вы прошли все уровни!");
            Console.ReadKey();
        }

        static void PlayLevel(int level)
        {
            char[,] maze = GetLevel(level);

            playerX = 1;
            playerY = 1;

            while (true)
            {
                Console.Clear();
                DrawMaze(maze);

                var key = Console.ReadKey(true).Key;

                int newX = playerX;
                int newY = playerY;

                switch (key)
                {
                    case ConsoleKey.UpArrow: newY--; break;
                    case ConsoleKey.DownArrow: newY++; break;
                    case ConsoleKey.LeftArrow: newX--; break;
                    case ConsoleKey.RightArrow: newX++; break;
                }

                if (maze[newY, newX] == ' ' || maze[newY, newX] == 'E')
                {
                    playerX = newX;
                    playerY = newY;
                }

                if (maze[playerY, playerX] == 'E')
                {
                    Console.Clear();
                    Console.WriteLine($"Уровень {level} пройден!");
                    Thread.Sleep(1000);
                    break;
                }
            }
        }

        static void DrawMaze(char[,] maze)
        {
            for (int y = 0; y < maze.GetLength(0); y++)
            {
                for (int x = 0; x < maze.GetLength(1); x++)
                {
                    if (x == playerX && y == playerY)
                        Console.Write('P');
                    else
                        Console.Write(maze[y, x]);
                }
                Console.WriteLine();
            }
        }

        static char[,] GetLevel(int level)
        {
            switch (level)
            {
                case 1:
                    return new char[,]
                    {
                        {'#','#','#','#','#','#','#'},
                        {'#',' ',' ',' ','#','E','#'},
                        {'#',' ','#',' ','#',' ','#'},
                        {'#',' ','#',' ',' ',' ','#'},
                        {'#','#','#','#','#','#','#'},
                    };

                case 2:
                    return new char[,]
                    {
                        {'#','#','#','#','#','#','#','#','#'},
                        {'#',' ',' ',' ','#',' ',' ','E','#'},
                        {'#',' ','#',' ','#',' ','#','#','#'},
                        {'#',' ','#',' ',' ',' ',' ',' ','#'},
                        {'#',' ','#','#','#','#','#',' ','#'},
                        {'#',' ',' ',' ',' ',' ','#',' ','#'},
                        {'#','#','#','#','#','#','#','#','#'},
                    };

                case 3:
                    return new char[,]
                    {
                        {'#','#','#','#','#','#','#','#','#','#','#'},
                        {'#',' ',' ',' ','#',' ',' ',' ',' ','E','#'},
                        {'#',' ','#',' ','#',' ','#','#','#','#','#'},
                        {'#',' ','#',' ',' ',' ',' ',' ',' ',' ','#'},
                        {'#',' ','#','#','#','#','#','#','#',' ','#'},
                        {'#',' ',' ',' ',' ',' ',' ',' ','#',' ','#'},
                        {'#','#','#','#','#','#','#','#','#','#','#'},
                    };

                default:
                    return null;
            }
        }
    }
}