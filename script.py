last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
# Checkpoint 1 :
subjects = ["physics", "calculus", "poetry", "history"]

# Checkpoint 2 :
grades = [98, 97, 85, 88]

# Checkpoint 3 :
gradebook = [["physics",98],["calculus",97],["poetry",85],["history",88]]

# Checkpoint 4 :
print(gradebook)

# Checkpoint 5 :
gradebook.append(["computer science", 100])

# Checkpoint 6 :
gradebook.append(["visual arts", 93])
print(gradebook)

# Checkpoint 7 :
gradebook[-1][-1] = 98
print(gradebook)

# Checkpoint 8 :
gradebook[2].remove(85)
print(gradebook)

# Checkpoint 9 :
gradebook[2].append("Pass")
print(gradebook)

# Checkpoint 10 :
full_gradebook = last_semester_gradebook +gradebook
print("########################################")
print(full_gradebook)
