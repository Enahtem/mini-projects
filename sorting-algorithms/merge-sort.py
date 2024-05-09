def merge(list1, list2):
    i1 = 0
    i2 = 0
    merged_list = []
    while(i1<len(list1) or i2<len(list2)):
        if (i1==len(list1)):
            merged_list.append(list2[i2])
            i2+=1            
        elif (i2 == len(list2)):
            merged_list.append(list1[i1])
            i1+=1
        else:
            if (list1[i1]>list2[i2]):
                merged_list.append(list2[i2])
                i2+=1
            else:
                merged_list.append(list1[i1])
                i1+=1
    return merged_list

def merge_sort(list):
    if (len(list)<=1):
        return list
    else:
        middle = len(list)//2
        return merge(merge_sort(list[:middle]), merge_sort(list[middle:]))

if __name__ == "__main__":
    print(merge_sort([4,3,1,2]))