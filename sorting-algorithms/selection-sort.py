def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i,len(list)):
            if (list[j]<list[min_index]):
                min_index=j
        list[min_index], list[i] = list[i], list[min_index]
    return list

if __name__ == "__main__":
    print(selection_sort([4,3,1,2]))