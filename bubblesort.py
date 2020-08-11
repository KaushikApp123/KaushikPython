def bubbleSort(list):
    for passnumber in range(len(list)-1,0,-1):

        for condi in range(passnumber):

            if list[condi]>list[condi+1]:

                temp = list[condi]
                list[condi] = list[ condi+1]
                list[condi+1] = temp

list = list(map(int, input("What numbers do you want sorted?: ").split(" ")))



bubbleSort(list)
print(list)