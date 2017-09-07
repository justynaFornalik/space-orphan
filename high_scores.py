def high_scores(name, time_spent, text_file):
    with open(text_file, "r") as file:
        lines = []
        for line in file:
            line = line.strip()
            line = line.split(",")
            lines.append(line)
    new_score = [name, str(time_spent)]

    for i in range(len(lines)):
        if time_spent < int(lines[i][1]):
            lines.insert(i, new_score)
            lines.pop()
            break

    new_scores = ""
    for line in lines:
        new_scores += ",".join(line)+'\n'
    with open(text_file, "w") as new_file:
        new_file.write(new_scores)
