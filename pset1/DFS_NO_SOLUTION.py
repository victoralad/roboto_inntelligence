import copy
import time

graph = {'AL': ['FL', 'GA', 'MS', 'TN'],
		 'FL': ['AL', 'GA'],
		 'GA': ['AL', 'FL', 'NC', 'SC', 'TN'],
		 'MS': ['AL', 'AR', 'LA', 'TN'],
		 'TN': ['AL', 'AR', 'GA', 'KY', 'MO', 'MS', 'NC', 'VA'],
		 'AR': ['LA', 'MO', 'MS', 'OK', 'TN', 'TX'],
		 'LA': ['AR', 'MS', 'TX'],
		 'MO': ['AR', 'IA', 'IL', 'KS', 'KY', 'NE', 'OK', 'TN'],
		 'OK': ['AR', 'CO', 'KS', 'MO', 'NM', 'TX'],
		 'TX': ['AR', 'LA', 'NM', 'OK'],
		 'AZ': ['CA', 'NM', 'NV', 'UT'],
		 'CA': ['AZ', 'NV', 'OR'],
		 'NM': ['AZ', 'CO', 'OK', 'TX'],
		 'NV': ['AZ', 'CA', 'ID', 'OR', 'UT'],
		 'UT': ['AZ', 'CO', 'ID', 'NV', 'WY'],
		 'OR': ['CA', 'ID', 'NV', 'WA'],
		 'CO': ['KS', 'NE', 'NM', 'OK', 'UT', 'WY'],
		 'KS': ['CO', 'MO', 'NE', 'OK'],
		 'NE': ['CO', 'IA', 'KS', 'MO', 'SD', 'WY'],
		 'WY': ['CO', 'ID', 'MT', 'NE', 'SD', 'UT'],
		 'CT': ['MA', 'NY', 'RI'],
		 'MA': ['CT', 'NH', 'NY', 'RI', 'VT'],
		 'NY': ['CT', 'MA', 'NJ', 'PA', 'VT'],
		 'RI': ['CT', 'MA'],
		 'DC': ['MD', 'VA'],
		 'MD': ['DC', 'DE', 'PA', 'VA', 'WV'],
		 'VA': ['DC', 'KY', 'MD', 'NC', 'TN', 'WV'],
		 'DE': ['MD', 'NJ', 'PA'],
		 'NJ': ['DE', 'NY', 'PA'],
		 'PA': ['DE', 'MD', 'NJ', 'NY', 'OH', 'WV'],
		 'NC': ['GA', 'SC', 'TN', 'VA'],
		 'SC': ['GA', 'NC'],
		 'IA': ['IL', 'MN', 'MO', 'NE', 'SD', 'WI'],
		 'IL': ['IA', 'IN', 'KY', 'MO', 'WI'],
		 'MN': ['IA', 'ND', 'SD', 'WI'],
		 'SD': ['IA', 'MN', 'MT', 'ND', 'NE', 'WY'],
		 'WI': ['IA', 'IL', 'MI', 'MN'],
		 'ID': ['MT', 'NV', 'OR', 'UT', 'WA', 'WY'],
		 'MT': ['ID', 'ND', 'SD', 'WY'],
		 'WA': ['ID', 'OR'],
		 'IN': ['IL', 'KY', 'MI', 'OH'],
		 'KY': ['IL', 'IN', 'MO', 'OH', 'TN', 'VA', 'WV'],
		 'MI': ['IN', 'OH', 'WI'],
		 'OH': ['IN', 'KY', 'MI', 'PA', 'WV'],
		 'WV': ['KY', 'MD', 'OH', 'PA', 'VA'],
		 'NH': ['MA', 'ME', 'VT'],
		 'VT': ['MA', 'NH', 'NY'],
		 'ME': ['NH'],
		 'ND': ['MN', 'MT', 'SD']}


def DFS_no_visited_list(start_node, goal_node, graph):
	"""

	:param start_node: start location of search
	:param goal_node: goal location of search
	:param graph: graph searched through (expects a dict)
	:return:
	"""
	queue = []  # initialize q to empty list
	path = [start_node]
	nodes_popped = 0  # bookkeeping for nodes popped
	max_queue_size = 0  # bookkeeping for max queue size
	while path[-1] != goal_node:
		nodes_popped += 1
		children = graph[path[-1]]  # returns a list of neighboring nodes
		for child in reversed(children):
			queue.append(copy.deepcopy(path) + [child])  # add to queue
		if len(queue) > max_queue_size:
			max_queue_size = len(queue)
			if max_queue_size > 5000:
				print('DFS no visited list infeasable')
				return 0,0,0
		print(queue)
		path = queue.pop()  # get the next path
	return path, nodes_popped, max_queue_size


if __name__ == "__main__":
	start = time.time()
	path, nodes_popped, max_queue_size = DFS_no_visited_list("WA", "GA", graph)
	stop = time.time()
	runtime = stop - start
	print("Time (s): ",str(runtime))
	print("Number of paths popped: ", str(nodes_popped))
	print("Max queue size: ", str(max_queue_size))
	print("Returned Path cost: ", str(len(path) - 1))
