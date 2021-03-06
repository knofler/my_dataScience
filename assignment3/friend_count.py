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
    mr.emit_intermediate(key,1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # print list_of_values[1][6]
    # print "key is : ", key
    total = 0
    for l in list_of_values:
      total+= 1
    mr.emit((key,total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)