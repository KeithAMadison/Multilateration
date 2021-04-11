# Multilateration

Efficient algebraic Time Delay of Arrival (TDoA) algorithms, designed to provide more accurate localizations given fewer datapoints than required for other approaches. Requires just three data points ("nodes") for 2-Dimensional vertexing, and four nodes for 3-Dimensional vertexing. Robust against noisy data.

# Usage

Initialize an object of the `Vertexer` class, passing a `NumPy` array of the form:

```
[[x_1, y_1, z_1],
 [x_2, y_2, z_2],
 ...
 [x_4, y_4, z_4]]
```

...as well as the signal velocity, where `x_i, y_i, z_i` are the coordinates of node `i`. 

To perform localization, pass a `NumPy` array of the form `[t_1, t_2, t_3, t_4]` to the `reconstruct()` method, where `t_i` is the time of arrival at node `i`. Choice of `t0` is arbitrary. A `NumPy` array of the form `[x,y,z]` will be returned, giving the co-ordinates of the solution with least SSR error.

# Practical Usage in Anisotropic Media

An efficient approximation can be made in many anisotropic media by assuming `c`, computing `c_0` using the found solution, then iterating this process until convergence.
