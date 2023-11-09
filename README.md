# 1 Background
During the last lockdown, tough social distancing regulations were put in place. This was particularly difficult for
students at the Tongersestraat 53. With a combination of one-way staircases and hallways, the building became even
harder to navigate than it already was. We hope it won’t be needed, but just in case and to be prepared, you’re asked
to create a program to help confused students safely find their way around the building!
# 2 Problem Statement
Given is an undirected graph G = (V, E) together with a minimum distance D, maximum time T and two players a, b
that have starting points sa, sb and target points ta, tb respectively.
We wish to find two Socially Distant Paths for the two players to walk. The players walk at equal speeds in the
unweighted graph (one edge per unit of time) and both start walking at t = 0. The path are considered Socially
Distant Paths if at no point in time the players come within distance D (or less) of each other. I.e., if the paths are
given as sequences of vertices pa,1, pa,2, . . . , pa,k and pb,1, pb,2, . . . , pb,k the paths are Socially Distant Paths if and only
if the graph distance between pa,i and pb,i is more than D for all i. E.g., D = 1 indicates the players may never be on
adjacent vertices, D = 2 means they cannot be on two vertices that share a common neighbour, etc...
The path for player a must start at sa and end at ta (so pa,1 = sa and pa,k = ta) and similarly, the path for player b
must start at sb and end at tb (so pb,1 = sb and pb,k = tb).
The possible actions for each player at any time step is to move one edge, or remain in place at the current vertex.
The players move simultaneously, so if one player a moves from a1 to a2 and player b moves from b1 to b2, it is only
required that the distance between a1 and b1 and that between a2 and b2 is large enough; a1 and b2 (and a2 and b1)
can possibly be closer to each other.
The goal is to minimize the time at which both players have arrived at their respective target vertices, that is, to
minimize k. Because the players are in a hurry, k must be at most T . If there is no solution with k ≤ T , report that
this is the case.
