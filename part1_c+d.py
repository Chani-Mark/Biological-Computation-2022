#Ex1 part 1 c+d
#Noa Koahan 315243501
#Chani Mark 318781671
import itertools as iter
import time as time
How_long_file = open("Part1_c.txt", "w")


def is_cc(sub_graph): #to check connectivity
    component = set(sub_graph[0])
    Cc = [component] #all connected components
    for edge in sub_graph[1:]:
        next_component = set(edge) - component
        if len(next_component) == 2: #if they don't have mutaual elements
            component = next_component
            Cc.append(component) #
        else:
            component.update(next_component) #adding the elements from next_component to the current component
    for i in range(len(Cc)-1):
        if len(Cc[i].intersection(Cc[i+1])) == 0: #checking every component and its neighbor, if the intersection is empety so the grafh is disconnected
            return False
    return True


def is_exist(n, sub_graph, all_sub_graphs):
    vertices = range(1, n + 1)
    for permutation in iter.permutations(vertices):
        ver_combinations = {}
        for i, j in enumerate(permutation):
            ver_combinations[i+1]=j
        sub_graph_combinations = sorted(list(tuple((ver_combinations[edge[0]], ver_combinations[edge[1]]) for edge in sub_graph)))
        if sub_graph_combinations in all_sub_graphs:
            return True
    return False


def has_all_vertices(vertices_list, sub_graph):
    vertices=set()
    for edge in sub_graph:
        for ver in edge:
            vertices.add(ver)
    return vertices.issuperset(set(vertices_list)) #returns True if all items in vertices set(which holds all the vertices from sub_graph) exists in vertices_list, otherwise it retuns False.


def get_sub_graphs(n):
    vertices_list = list(range(1, n + 1))
    all_edges = []
    for ver_a in vertices_list:
        for ver_b in vertices_list:
            if ver_a != ver_b:
                all_edges.append((ver_a,ver_b))
    all_sub_graphs = []
    for number_of_edges in range(n-1, n*(n-1) + 1):
        sub_graphs_of_number_of_edges = list(iter.combinations(all_edges, number_of_edges))
        for sub_graph in sub_graphs_of_number_of_edges:
            if not is_exist(n, list(sub_graph), all_sub_graphs) and has_all_vertices(vertices_list, list(sub_graph)) and is_cc(list(sub_graph)):
                all_sub_graphs.append(list(sub_graph))



# Parts c+d:
for n in range(2, 8):
    one_hour,two_hours,four_hours,eight_hours = "","","",""
    start = time.time()
    get_sub_graphs(n)
    end_time = (time.time() - start) / 3600
    if end_time > 1 and end_time < 2:
        one_hour = "The maximal number n for which the program can complete in less then 1 hour is" + n-1 + "\n"
    if end_time > 2 and end_time < 3:
        two_hours = "The maximal number n for which the program can complete in less then 2 hours is" + n - 1 + "\n"
    if end_time > 4 and end_time < 5:
        four_hours = "The maximal number n for which the program can complete in less then 4 hours is" + n - 1 + "\n"
    if end_time > 8 and end_time < 9:
        eight_hours = "The maximal number n for which the program can complete in less then 8 hours is" + n - 1 + "\n"

How_long_file.write(one_hour)
How_long_file.write(two_hours)
How_long_file.write(four_hours)
How_long_file.write(eight_hours)


