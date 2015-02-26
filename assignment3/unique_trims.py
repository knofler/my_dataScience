import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents

    key = record[0]

    mr.emit_intermediate(key,record)

def reducer(key, list_of_values):

    # key: word
    # value: list of occurrence counts

    # pairs = [tuple(l) for l in list_of_values]
    # all_set = set(pairs)

    # dups_set = set([pair for pair in pairs if pairs.count(pair) > 1]) 

    # asymmetric_friends = all_set^dups_set

    # map(lambda x: mr.emit(pair),asymmetric_friends)
    mr.emit(list_of_values)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)