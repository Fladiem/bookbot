"""
def get_book_text(path_to_file):
        f=""
        with open(path_to_file) as f:   #accepts path to the file written as string
            file_contents = f.read()
        return file_contents       #returns contents of file targeted by path_to_file
"""
from stats import word_count

from stats import character_dictionary

from stats import dictionary_sort

from stats import dictionary_sort_print
    
def main():
   print ("============ BOOKBOT ============")
   print ("Analyzing book found at location this program knows about trust me it knows")
   print ("----------- Word Count ----------")
   #print(get_book_text("books/frankenstein.txt"))
   word_count()
   print ("--------- Character Count -------")
   dictionary_sort_print()
   print ("============= END ===============")
   
   


    
main()
