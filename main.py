# Write your function here
def middle_element(lst):
    if len(lst) % 2 == 0:
        sum_of = lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]
        return sum_of / 2
    else:
        return lst[int(len(lst) / 2)]


print(middle_element([5, 2, -10, -4, 4, 5]))
