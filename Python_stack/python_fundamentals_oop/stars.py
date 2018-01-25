#part 1
def draw_stars(arr):
    for i in arr:
        print "*"* i
x =[4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

#part 2
def draw_stars2(lst):
    for i in range(0, len(lst)):
        if type(lst[i]) == int:
            print "*"* lst[i]
        elif type(lst[i]) == str:
            print lst[i][0].lower()*len(lst[i])
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
