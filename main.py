def parseFile(file):
    cells_num = int(file.readline())
    if cells_num < 2 or cells_num > 200000:
        print("Number of cells is too big, try again. Goodbye!")
        exit(1)
    cells = []
    for line in file:
        if line[0] == "d":
            coins = int(line[1:])
            if coins < 1 or coins > 10000:
                print("Number of coins the dragon keeps is too big, try again. Goodbye!")
                exit(1)
            cells.append(("d", coins))
        elif line[0] == "p":
            beauty = int(line[1:])
            if beauty < 2 or beauty > 200000:
                print("Beauty of the princess is too big, try again. Goodbye!")
                exit(1)
            cells.append(("p", beauty))
    return cells_num, cells


def indexOfCells(list, res_matrix, res_val, idx, k):
    idx_list = []
    res_val_tmp = res_val
    k_tmp = k
    for i in range(idx - 1, -1, -1):
        if res_val_tmp <= 0:
            break
        if i != -1 and res_val_tmp == res_matrix[i - 1][k_tmp]:
            continue
        else:
            if list[i][0] == 'd':
                idx_list.append(i + 2)
                k_tmp = k_tmp - 1
                res_val_tmp = res_val_tmp - list[i][1]
    return idx_list


def dragonsAndPrincesses(t):
    cells_Num = t[0]
    cells = t[1]
    coins_Collected = 0
    first_idx = cells_Num - 3
    idx_Killed_dragons = []
    """
    The Knight can collect all coins between 
    [last-1] princess and [last] princess.
    Add indexes to the index list.
    first_idx = [last-1] princess index. 
    """
    for i in range(cells_Num - 3, 0, -1):
        if cells[i][0] == 'p':
            first_idx = i
            break
        elif cells[i][0] == 'd':
            coins_Collected = coins_Collected + cells[i][1]
            idx_Killed_dragons.append(i + 2)
    """
    End sum 
    """
    first_k = cells[first_idx][1] - 1
    res_matrix = F(cells, first_idx - 1, first_k)  # Dynamic programing
    res_val = res_matrix[first_idx - 1][first_k]  # result value is in the last cells of the matrix
    idx_list2 = indexOfCells(cells, res_matrix, res_val, first_idx, first_k)  # Calculate indexes from the result matrix
    for element in idx_list2:  # Union of the indexes lists
        idx_Killed_dragons.append(element)
    dragon_killed = len(idx_Killed_dragons)  # Number of dragon killed = length of the idx list
    if dragon_killed < cells[cells_Num - 2][1]:  # The Knight need to kill at least [last] princess beauty
        return -1
    coins_Collected = coins_Collected + res_matrix[first_idx - 1][first_k]  # Sum all coins
    idx_Killed_dragons.reverse()  # Ordering
    return coins_Collected, dragon_killed, idx_Killed_dragons


def F(A, n, k):
    """
    :param A: Cells list
    :param n: the [last-1] princess - 1
    :param k: kills left (the beauty of the ([last-1] princess - 1) - 1)
    :return: matrix with values of gold coins that the Knight can collect while he is in the cell i and left j kills
    """
    matrix = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(k + 1):
            if j == 0:
                matrix[i][j] = 0
                continue
            if A[i][0] == 'p':
                if A[i][1] <= j:
                    matrix[i][j] = matrix[i - 1][A[i][1] - 1] # Don't update kills left
                else:
                    matrix[i][j] = matrix[i - 1][j] # update kills left
            if A[i][0] == 'd':
                if i == 0 and j > 0:
                    matrix[i][j] = A[i][1] # First dragon and more than 0 kills left. Kill the dragon.
                else:
                    # Take the maximum between kill the i-th dragon (and take his gold coins) or not
                    matrix[i][j] = max(matrix[i - 1][j - 1] + A[i][1], matrix[i - 1][j])
    return matrix


def main():
    with open('Tests/input8.yaml', 'r') as txtfile:
        input = parseFile(txtfile)
    res = dragonsAndPrincesses(input)
    if res != -1:
        print(res[0])
        print(res[1])
        for i in res[2]:
            print(i, end=" ")
    else:
        print(-1)


if __name__ == "__main__":
    main()
