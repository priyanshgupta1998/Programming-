 
def lexNext(s, n): 
	for i in range(n - 1, -1, -1): 
		if s[i] != 'z': 
			k = ord(s[i]) 
			s[i] = chr(k + 1) 
			return ''.join(s)  
		s[i] = 'a'


S = "abcdeg"
n = len(S) 
S = list(S) 
res = lexNext(S, n) 

print(s)
