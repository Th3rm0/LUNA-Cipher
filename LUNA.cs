
/*
#### Caleb Ha, 23/03/2023
# LUNA Cipher

This is the LUNA Cipher. LUNA is an acryonym for Layered Unbreakable Numerical Algorithm. This cipher will be based upon a previous cipher I created named the TESS Cipher.
The TESS Cipher (Transformational Enhanced Shift System) used a modified version of the Ceaser Cipher which increases
the shift used as it encrypts the message. The LUNA Cipher is based on the same principle, however, at the very end of the
encryption, the whole message is put through the Polybius Cipher.

No value greater than 1 billion may be entered for the shift value due to limitations in the code
*/

using System;

namespace LUNA
{
    class Program
    {
        static void Main(string[] args)
        {
            char[] characterSet = 
            {
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z', '1', '2', '3', '4',
                '5', '6', '7', '8', '9', '0', '!', ' '
            };

            char[,] polybiusSquare = {
                {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'},
                {'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'},
                {'q', 'r', 's', 't', 'u', 'v', 'w', 'x'},
                {'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F'},
                {'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'},
                {'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'},
                {'W', 'X', 'Y', 'Z', '1', '2', '3', '4'},
                {'5', '6', '7', '8', '9', '0', '!', ' '}
            };

            const string polybiusRowKey = "ABCDEFGH";
            const string polybiusColumnKey = "ABCDEFGH";

            string[] inputs = getInput();

            string phrase = inputs[0];
            int shift = Convert.ToInt32(inputs[1]);
       
            string encryptedTess = encryptionTess(characterSet, phrase, shift);
            Console.WriteLine(encryptedTess);

            string encryptedPolybius = encryptionPolybius(polybiusSquare, polybiusRowKey, polybiusColumnKey, encryptedTess);
            Console.WriteLine($"Encrypted: {encryptedPolybius}");

            string decryptedPolybius = decryptionPolybius(polybiusSquare, polybiusRowKey, polybiusColumnKey, encryptedPolybius);
            Console.WriteLine($"Decrypted: {decryptedPolybius}");

            string decryptedTess = decryptionTess(characterSet, decryptedPolybius, shift);
            Console.WriteLine(decryptedTess);
        }
        static string encryptionTess(char[] characterSet, string phrase, int shift)
        {
            string encryptedPhrase = "";
            int totalShift = 0;

            foreach (char c in phrase)
            {
                int i = 0;

                while (c != characterSet[i])
                {
                    i++;
                }

                totalShift += shift;
                i += totalShift;

                while (i >= characterSet.Count())
                {
                    i -= characterSet.Count();
                }

                encryptedPhrase += characterSet[i];

                Console.WriteLine($"[ENCRYPTION:     TESS] Char {c}, Shift {totalShift}, Enc {characterSet[i]}");
                
            }

            return encryptedPhrase;
        }

        static string decryptionTess(char[] characterSet, string phrase, int shift)
        {
            string decryptedPhrase = "";
            int totalShift = 0;

            foreach (char c in phrase)
            {
                int i = 0;

                while (c != characterSet[i])
                {
                    i++;
                }

                totalShift += shift;
                i -= totalShift;

                while (i < 0)
                {
                    i += characterSet.Count();
                }

                decryptedPhrase += characterSet[i];

                Console.WriteLine($"[DECRYPTION:     TESS] Char {c}, Shift {totalShift}, Dec {characterSet[i]}");
            }

            return decryptedPhrase;
        }

        static string encryptionPolybius(char[,] polybiusSquare, string polybiusRowKey, string polybiusColumnKey, string phrase)
        {
            List<string> encryptedBlocks = new List<string>();
            int width = polybiusSquare.GetLength(0);
            int height = polybiusSquare.GetLength(1);

            foreach (char c in phrase)
            {
                for (int i = 0; i < width; i++)
                {
                    for (int j = 0; j < height; j++)
                    {
                        if (polybiusSquare[i, j].Equals(c))
                        {
                            encryptedBlocks.Add(polybiusRowKey[i].ToString() + polybiusColumnKey[j].ToString());

                            Console.WriteLine($"[ENCRYPTION: POLYBIUS] Char {c}, Row {i}, Column {j}, Encrypted Block {polybiusRowKey[i].ToString() + polybiusColumnKey[j].ToString()}");
                        }
                    }
                }
            }

            string encryptedPhrase = string.Concat(encryptedBlocks);

            return encryptedPhrase;
        }

        static string decryptionPolybius(char[,] polybiusSquare, string polybiusRowKey, string polybiusColumnKey, string phrase)
        {
            List<char> decryptedChars = new List<char>();

            int width = polybiusSquare.GetLength(0);
            int height = polybiusSquare.GetLength(1);

            for (int i = 0; i < phrase.Length; i += 2)
            {
                int rowIndex = 0;
                int columnIndex = 0;

                for (int j = 0; polybiusRowKey[j] != phrase[i]; j++)
                {
                    rowIndex++;
                }

                for (int j = 0; polybiusColumnKey[j] != phrase[i + 1]; j++)
                {
                    columnIndex++;
                }

                decryptedChars.Add(polybiusSquare[rowIndex, columnIndex]);

                Console.WriteLine($"[DECRYPTION: POLYBIUS] Encrypted Block {phrase[i].ToString() + phrase[i + 1].ToString()}, Row {rowIndex}, Column {columnIndex}, Decrypted {polybiusSquare[rowIndex, columnIndex]}");
            }

            string decryptedPhrase = string.Concat(decryptedChars);

            return decryptedPhrase;
        }
        static string[] getInput()
        {
            string[] inputs = new string[2];

            Console.Write("Input text: ");
            inputs[0] = Console.ReadLine();

            Console.Write("Input shift: ");
            inputs[1] = Console.ReadLine();

            return inputs;
        }
    }
}