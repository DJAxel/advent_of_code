with open(r"input.txt", "r") as input:

    max_calories = 0
    subtotal_calories = 0

    def end_of_elve():
        global max_calories, subtotal_calories
        max_calories = max(max_calories, subtotal_calories)
        subtotal_calories = 0


    for line in input.readlines():
        line = line.strip()
        try:
            subtotal_calories += int(line)
        except:
            end_of_elve()

end_of_elve()

print("max_calories => " + str(max_calories))