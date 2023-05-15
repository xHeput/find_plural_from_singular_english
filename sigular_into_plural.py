  # program will take singular form of word and find it's plural form
  # install package on yr IDE / paste this command line into cmd "py -m pip install pattern.en"
import numpy
from pattern.en import pluralize

  # imports file where your singular words are
file_name = 'English_words_singular.txt'
import_file = numpy.loadtxt(file_name, delimiter=",", dtype=str)
  # prints importer words
print("Twoje słowa w l. pojedynczej",import_file)


  # loop which uses pluralize() to find plural form for all words
plural_file = []
for i in range(len(import_file)):
    plural_file.append(pluralize(import_file[i]))
  # prints table with prulal words
print("Twoje słowa w l. mnogiej",plural_file)

numpy.savetxt('English_words_plural.txt', plural_file, delimiter=',', fmt='%s')

