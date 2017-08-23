def Walk(G, s, S=set()):
	P, Q = dict(), set()
	P[s] = None
	Q.add(s)

	while Q:
		u = Q.pop()
		for v in G[u].difference(P, S):
			Q.add(v)
			P[v] = u

	return P


def Components(G):
	comp = []
	seen = set()
	for u in G:
		if u in seen: continue
		C = Walk(G, u)
		seen.update(C)
		comp.append(C)

	return comp

if __name__ == "__main__":
	a,b,c,d,e,f,g,h,i=range(9)
	G = {
	a:{b,d,c},
	b:{a,d},
	c:{a,d},
	d:{a,b,c},
	e:{g,f},
	f:{e,g},
	g:{e,f},
	h:{i},
	i:{h},
	}

	print(Components(G))
