#54


class Node:
    def __init__(self, subject, unit):
        self.subject = subject # row, col
        self.unit = unit # +1, -1
        self.next = None

    @staticmethod
    def switch_status(next_node, curr_i, curr_j, bound_map, visited, matrix):
        if next_node.subject == "i":
            curr_i+=next_node.unit
            # change bound
            if next_node.unit == 1:
                bound_map['upper_i'] = curr_i
            else:
                bound_map['lower_i'] = curr_i
        elif next_node.subject == "j":
            curr_j+=next_node.unit
            if next_node.unit == 1:
                bound_map['left_j'] = curr_j
            else:
                bound_map['right_j'] = curr_j
        if (curr_i, curr_j) in visited or not 0<=curr_i<=len(matrix)-1 or not 0<=curr_j<=len(matrix[0])-1:
            return False, None, None
        return True, curr_i, curr_j


class Solution:
    def spiralOrder(self, matrix):
        node_right = Node('j', 1)
        node_down = Node('i', 1)
        node_left = Node('j', -1)
        node_up = Node('i', -1)
        node_right.next = node_down
        node_down.next = node_left
        node_left.next = node_up
        node_up.next = node_right

        curr_node = node_right
        bound_map = {
            'left_j': 0,
            'right_j': len(matrix[0])-1,
            'upper_i': 0,
            'lower_i': len(matrix)-1
        }
        curr_i, curr_j = 0, 0
        visited = set()

        result = []
        while True:
            if bound_map['upper_i'] <= curr_i <= bound_map['lower_i'] and bound_map['left_j'] <= curr_j <= bound_map['right_j']:
                result.append(matrix[curr_i][curr_j])
                visited.add((curr_i, curr_j))
                if curr_node.subject == "j":
                    curr_j+=curr_node.unit
                elif curr_node.subject == "i":
                    curr_i+=curr_node.unit
            else:
                if curr_j > bound_map['right_j']:
                    curr_j -= 1
                elif curr_j < bound_map['left_j']:
                    curr_j += 1
                elif curr_i > bound_map['lower_i']:
                    curr_i -= 1
                elif curr_i < bound_map['upper_i']:
                    curr_i += 1
                is_valid, curr_i, curr_j = curr_node.switch_status(curr_node.next, curr_i, curr_j, bound_map, visited, matrix)
                if not is_valid:
                    break
                curr_node = curr_node.next
        return result
