"""
	HTTP Status codes and their occurrences
	Parameter: log: example.log file

"""
import re
# Global Variable: store distinct HTTP statuses


def frequency(log):
	
	try:
		# Find all the statuses in the log file
		status = re.findall(r'(GET\s.+\s\w+/.+"\s)([\d]+)\s', log.read())
	except:
		raise TypeError("The file GET and HTTP status format is different.")
		
	# Store distinct values of statuses
	global LIST_SET
	LIST_SET = list(set([x[1] for x in status]))
	
	# Print the status code and number of their occurrences
	print '\n--------------------HTTP Status codes and their occurrences--------------------'
	dic = dict()
	for a in xrange(len(LIST_SET)):
		dic[int(LIST_SET[a])] = ([x[1] for x in status]).count(LIST_SET[a])
	for k in dic:
		print k, dic[k]
	return dic
