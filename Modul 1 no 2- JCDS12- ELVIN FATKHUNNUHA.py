# list2 = list(zip(*List_Awal))
# print(list2)
# print(list2[::-1])

# Function Initialization
#  def counterClockwise(...):
#      .....
     
# # Use the Function
# print(counterClockwise(List_awal))
# List Output

# [[4, 8, 12, 16]
# [3, 7, 11, 15],
# [2, 6, 10, 14],
# [1, 5, 9, 13]]

# no 2 Elvin Fatkhunnuha

def counterClockwise(List_Awal):
    list2 = list(zip(*List_Awal))
    tuple_convert = []
    for x in list2:
        tuple_convert.append(list(x))
    
    for i in range(len(tuple_convert)):
        for j in range(i+1, len(tuple_convert)):
            if tuple_convert[i] < tuple_convert[j]:
                tuple_convert[i], tuple_convert[j] = tuple_convert[j], tuple_convert[i]
    return tuple_convert

   

List_Awal= [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

print(counterClockwise(List_Awal))


