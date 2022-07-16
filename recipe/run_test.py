import numpy as np
from pys2index import S2PointIndex

latlon_points = np.array([[40.0, 15.0], 
                          [-20.0, 53.0], 
                          [81.0, 153.0]])

index = S2PointIndex(latlon_points)

query_points = np.array([[-10.0, 60.0],
                         [45.0, -20.0],
                         [75.0, 122.0]])

index.get_cell_ids()
distances, positions = index.query(query_points)
assert np.all(positions == np.array([1, 0, 2]))
