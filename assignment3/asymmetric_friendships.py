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
    person = record[0]
    friend = record[1]

    mr.emit_intermediate(person,[person,friend])
    mr.emit_intermediate(friend,[friend,person])

def reducer(key, list_of_values):

    # key: word
    # value: list of occurrence counts
    # print list_of_values[1][6]
    # for l in list_of_values:
      # print "each l is : ", l
    pairs = [tuple(l) for l in list_of_values]
    all_set = set(pairs)

    # print pairs.count(pair)

    dups_set = set([pair for pair in pairs if pairs.count(pair) > 1]) 
    # print "dups_set : ", dups_set
    # print "pair is : " , pair
    asymmetric_friends = all_set^dups_set
    # print "pair is : " , pair
    map(lambda x: mr.emit(pair),asymmetric_friends)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)