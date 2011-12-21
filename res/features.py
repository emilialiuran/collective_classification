fin = open("wdcl.model")
result = []
def sort_inner(inner):
    """
    inner is each inner list in the list of lists to be sorted
    (here item at index 1 of each inner list is to be sorted)
    """
    return inner[2]

for line in fin:
	line = line.strip()
	line = line.split()
	result.append(line)
result.pop(0)
result.sort(key=sort_inner)
print result 