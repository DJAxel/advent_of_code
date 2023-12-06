from functools import reduce


if __name__ == "__main__":
    with open("./2023/day06/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file]

    values = [line.split(":")[1].split() for line in lines]

    p1_races = list(zip(*[[int(num) for num in sublist] for sublist in values]))
    p2_races = [(tuple(int(reduce(lambda x, y: x + y, sublist)) for sublist in values))]

    for pt, races in enumerate((p1_races, p2_races)):
        total_winning_methods = []
        for time, highscore in races:
            race_winning_methods = 0
            for t in range(time):
                speed = t + 1
                travel_time = time - (t + 1)
                score = speed * travel_time
                if score > highscore:
                    race_winning_methods += 1
            total_winning_methods.append(race_winning_methods)

        print(f"Part {pt+1}: {reduce(lambda x, y: x * y, total_winning_methods)}")
