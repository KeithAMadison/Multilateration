from dataclasses import dataclass
import numpy as np
​
M = np.diag([1, 1, 1, -1]) 
​
@dataclass
class Vertexer:
​
	nodes: np.ndarray
	c: float

	def reconstruct(self, times):
		# Normalize times
		times -= times.min()
​
		A = np.append(self.nodes, np.reshape(times, (-1, 1)) * self.c, axis=1)
​
		def ssr_error(point):
			# Return SSR error
			return np.sum(((np.linalg.norm(self.nodes - point, axis=1) / self.c)  
				   - times)**2)
​
		def lorentz(a, b):
			# Return Lorentzian Inner-Product
			return np.sum(a * (b @ M), axis=-1)
​
		b = lorentz(A, A) * 0.5
		C = np.linalg.solve(A, np.ones(4))
		D = np.linalg.solve(A, b)
​
		roots = np.roots([lorentz(C, C),
				(lorentz(C, D) - 1) * 2, 
				 lorentz(D, D)])
​
		solutions = []
		for root in roots:
			X, Y, Z, T = M @ np.linalg.solve(A, root + b)
			solutions.append(np.array([X,Y,Z]))
​
		return max(solutions, key = ssr_error)
