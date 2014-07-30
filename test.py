fin = open('/Users/ashleysdoane/Desktop/words.txt')
def wrds_list(fin):
    wrds = []
    for line in fin:
        word = line.strip()
        wrds.append(word)
    return wrds
    
wrds_list(fin)
