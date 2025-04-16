
#Team sets
basketball_team = {"Jack", "Jess", "Jane", "Jen", "Juliet", "Jap"}
baseball_team = {"Jack", "Jane", "Juliet", "Jacob", "Jax", "Justice"}

#Operations

# Show students who play both sports with the "&" operator
both_sports = basketball_team & baseball_team
print("Students who play both sports:", both_sports)

# Show students who play either sport with the "|" operator
either_sport = basketball_team | baseball_team
print("Students who play either sport:", either_sport)

# Show only students who play baseball but not basketball with the "-" operator
only_baseball = baseball_team - basketball_team
print("Students who play baseball but not basketball:", only_baseball)

# Display students who play basketball but not baseball using the "-" operator
only_basketball = basketball_team - baseball_team
print("Students who play basketball but not baseball:", only_basketball)

# Students who only play one sport but not both using the "^" operator
symmetric_difference = basketball_team ^ baseball_team
print("Students who play only one sport:", symmetric_difference)
