#Ex1 part 2
#Noa Koahan 315243501
#Chani Mark 318781671
import itertools as iter
import math as mt

Output_file = open("Part2_output.txt", "w")

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

def get_num_of_instances(sub_graph, sub_g, n):
    num = 0
    if len(sub_g) > len(sub_graph):
        for possible_sub_graph in iter.product(sub_g, repeat=len(sub_graph)):
            if is_exist(n,sub_graph, possible_sub_graph):
                num += 1
        num = int(num/mt.factorial(len(sub_graph)))
    else:
        if is_exist(n, sub_graph, sub_g):
            num += 1
    return num

def get_sub_graphs(n, sub_g):
    Output_file.write("n=" + str(n) + "\n")
    vertices_list = list(range(1, n + 1))
    all_edges = [edge for edge in list(iter.product(vertices_list, repeat=2)) if edge[0] != edge[1]]
    all_sub_graphs = []
    for number_of_edges in range(1, n*(n-1) + 1):
        Output_file.write("#" + str(number_of_edges) + "\n")
        sub_graphs_of_number_of_edges = list(iter.combinations(all_edges, number_of_edges))
        for sub_graph in sub_graphs_of_number_of_edges:
            sub_graph = list(sub_graph)
            if not is_exist(n, sub_graph, all_sub_graphs)  and is_cc(list(sub_graph)):
                all_sub_graphs.append(sub_graph)
                num_of_instances = get_num_of_instances(sub_graph, sub_g, n)
                Output_file.write(str(sub_graph) + " - counter: " + str(num_of_instances) + "\n")


# if __name__ == '__main__':
n = int(input("please insert n"))
sub_graph = []
while True:
        edge = input("please insert new edge (x and y), to end enter 0 0:")
        edge = list(int(x) for x in edge.split())
        if edge == [0, 0]:
            break
        if edge[0] == edge[1] or edge[0] < 1 or edge[1] < 1:
            print("invalid, please reenter")
            continue
        sub_graph.append(edge)
get_sub_graphs(n, sub_graph)


