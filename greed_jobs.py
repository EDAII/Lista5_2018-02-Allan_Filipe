jobs_list = [[8, 11], [9, 10], [10, 11], [11, 15], [13, 14], [12, 13]]
jobs_list_sorted = [[9, 10], [8, 11], [10, 11], [12, 13], [13, 14], [11, 15]]

jobs_selected = [jobs_list_sorted[0],]
current_position = len(jobs_selected)-1
for i in range(1, len(jobs_list_sorted)):
    if jobs_selected[current_position][1] <= jobs_list_sorted[i][0]:
        jobs_selected.append(jobs_list_sorted[i])
        current_position += 1

print("Os trabalhos selecionados são: ", jobs_selected)
print("A quantidade de trabalhos é: ", len(jobs_selected))
