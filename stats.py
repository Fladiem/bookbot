import sys

#WAI: Working as Intended
#IMP: Implemented, not final
#NFP: Null For Purpose, remains for study

def get_book_text(path_to_file):
        with open(path_to_file) as f:   #accepts path to the file written as string
            file_contents = f.read()
        return file_contents       #returns contents of file targeted by path_to_file

def word_count():
     text = get_book_text(sys.argv[1]) # removed hardcoded path for lesson
     words = text.split()
     count = 0
     for i in range(0, len(words)):
          count += 1
     print(f"Found {count} total words")

def character_dictionary():
     char_dict = {}
     text = get_book_text(sys.argv[1]) # removed hardcoded path for lesson
     cd_text = str.lower(text)
     
     #characters = []   A: Not needed, use cd_text[i] for character strings
    #for i in range(0, len(cd_text)): no list needed, use cd_text[i]
          #characters.append(cd_text[i])  #split words into individual characters, WAI, NFP

     for i in range (0,len(cd_text)):

          for char in cd_text[i]:            #add and count new characters to char_dict
               if char not in char_dict:
                    char_dict[cd_text[i]] = 1 
               else:
                    char_dict[cd_text[i]] += 1 #A: This operation does not work on a list
     return char_dict

def dictionary_sort():
     ds_dict = character_dictionary()
     dict_sortie = []
     
     for char in ds_dict:
          if char.isalpha():
               ds_single= {char: ds_dict[char]} #single dictionary for use in helper
               dict_sortie.append({char: ds_dict[char]}) #creating list of dictionaries
           
     def dictionary_sort_helper(ds_single): # must return count value for purpose of sorting
          keyh = list(ds_single.keys())[0]
          return ds_single[keyh]
     dict_sortie.sort(reverse=True, key= dictionary_sort_helper)
     return dict_sortie


def dictionary_sort_print():  #prints the sorted list from dictionary_sort
     dsv = dictionary_sort()
     """for i in range(0, len(dsv)): 
          for char, count in dsv[i]:
               print (f"{char}: {count}")"""  #This doesn't work for unpacking a dictionary list
     for pridi in dsv:
          for char, count in pridi.items(): #new information from boots, look into .items 
               print (f"{char}: {count}")

    

     
     

