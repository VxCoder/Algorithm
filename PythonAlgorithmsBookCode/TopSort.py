def topsort(G):
	#计算各个节点的入边
	count = {u:0 for u in G}
	for u in G:
		for v in G[u]:
			count[v] += 1

	Q = [u for u in G if count[u] == 0]
	S = []

	while Q:
		u = Q.pop()
		S.append(u)
		for v in G[u]:
			count[v] -= 1
			if count[v] == 0:
				Q.append(v)
	return S


def naive_topsort(G, S=None):
	S = S if S is not None else set(G)

	if len(S) == 1: return list(S)
	
	v = S.pop()
	seq = naive_topsort(G, S)

	insert_index = 0
	for i, u in enumerate(seq):
		if v in G[u]: insert_index = i+1
	seq.insert(insert_index, v)
	return seq

if __name__ == '__main__':
	a, b, c, d, e, f = range(6)
	DAG = {
		a:(b, f),		
		b:(c, d, f),
		c:(d,),		
		d:(e, f),		
		e:(f,),		
		f:(),			
	} 

	print(naive_topsort(DAG))
	print(topsort(DAG))