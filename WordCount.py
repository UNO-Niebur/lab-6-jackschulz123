#WordCount.py
#Name: Jack Schulz
#Date: 2-25-2026
#Assignment:Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0 
  wordCount = 0
  letterCount = 0
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      
      for letter in w:
        letterCount = letterCount + 1

   
    #print(line)
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", letterCount)
  

if __name__ == '__main__':
  main()
