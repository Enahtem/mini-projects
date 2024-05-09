def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if (list[j]>list[j+1]):
                list[j],list[j+1]=list[j+1], list[j]

    return list

if __name__ == "__main__":
    print(bubble_sort([4,3,1,2]))