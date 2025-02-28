import sys   #https://docs.python.org/3/library/sys.html#sys.argv

from stats import word_count

from stats import character_dictionary

from stats import dictionary_sort

from stats import dictionary_sort_print

if len(sys.argv) < 2:
   print ("Usage: python 3 main.py <path to book>")
   sys.exit(1)
else:
   pass
  
    
def main():
   
   print ("============ BOOKBOT ============")
   print (f"Analyzing: {sys.argv[1]}")
   print ("----------- Word Count ----------")
   word_count()
   print ("--------- Character Count -------")
   dictionary_sort_print()
   print ("============= END ===============")
   
#print ("Usage: python 3 main.py <path to book>")

main()
