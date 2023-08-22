import re
def empty_kmap():
	return['0', '45', '3', '2', '4', '5', '7', '6', '12', '13', '15', '14', '8', '9', '11', '10']
def kmap_box(arr):
	print("""
   | 00  |  01 |  11 |  10 |
---|-----|-----|-----|-----|-----
00 |  {0}  |  {1}  |  {2}  |  {3}  |
---|-----|-----|-----|-----|-----
01 |  {4}  |  {5}  |  {6}  |  {7}  |
---|-----|-----|-----|-----|-----
11 |  {8}  |  {9}  |  {10}  |  {11}  |
---|-----|-----|-----|-----|-----
10 |  {12}  |  {13}  |  {14}  |  {15}  |""".format(*arr))


def convert_input(input_str):
	return [re.sub(r'\b1\b', '45', i.strip()) for i in input_str.split(" ")]

def mapping_terms(kmap, terms, char):
	for i in range(len(terms)):
	    for j in range(len(kmap)):
	        if terms[i] == kmap[j]:
	            kmap[j] = char
	return kmap            
def plotting_zero(kmap):
	for k in range(len(kmap)):
		if kmap[k] != 1 and kmap[k] != 'x':
			kmap[k] = 0
	return kmap
if __name__ == '__main__':

	#Get Minterms and Don't care terms mf
	minterms = convert_input(input("Enter minterms: "))
	xterms = convert_input(input("Enter Don't Care: "))

	#create an empty kmap mf
	k_map = empty_kmap()

	#plot minterms and don't cares mf
	k_map = mapping_terms(k_map,minterms,1)
	k_map = mapping_terms(k_map,xterms,'x')

	#plotting zero in empty spaces mf
	k_map = plotting_zero(k_map)

	print("\nValues to be plotted: ", k_map,"\n")

	#print the board
	kmap_box(k_map)