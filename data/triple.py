import  re

file = open('small_data.txt', 'r', encoding='utf-8')
ff = open('small_data.json', 'w', encoding='utf-8')
lines = file.readlines()

maps = []
nodes = []
links = []

for line in lines:
	arr = line.split(' ')
	# source_id = maps.index(arr[0])
	# target_id = maps.index(arr[2])
	if arr[0] not in maps:
		maps.append(arr[0])
		nodes.append({
			'id': maps.index(arr[0]),
			'name': arr[0]
		})
	arr[2] = arr[2].strip('\n')
	if arr[2] not in maps:
		maps.append(arr[2])
		nodes.append({
			'id': maps.index(arr[2]),
			'name': arr[2]}
		)

	source_id = maps.index(arr[0])
	target_id = maps.index(arr[2])
	
	links.append({
		'id': len(links),
		'name': arr[1],
		'source': source_id,
		'target': target_id
		})

print(nodes)
print(links)

ff.write(str({
	'nodes': nodes,
	'links': links
	}))


