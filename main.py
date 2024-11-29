from collections import defaultdict

# Дані задачі
variables = ["Math", "Physics", "Chemistry"]
domains = {
    "Math": ["9:00", "10:00", "11:00"],
    "Physics": ["9:00", "10:00"],
    "Chemistry": ["10:00", "11:00"]
}
constraints = [
    (("Math", "Physics"), lambda x, y: x != y),
    (("Math", "Chemistry"), lambda x, y: x != y),
    (("Physics", "Chemistry"), lambda x, y: x != y)
]

# Функція перевірки обмежень
def is_consistent(assignment, variable, value):
    for (var_pair, constraint) in constraints:
        if variable in var_pair:
            other_var = var_pair[0] if var_pair[1] == variable else var_pair[1]
            if other_var in assignment and not constraint(value, assignment[other_var]):
                return False
    return True

# Алгоритм пошуку з поверненням
def backtracking_search(assignment={}):
    if len(assignment) == len(variables):
        return assignment

    # Вибір змінної
    unassigned_vars = [v for v in variables if v not in assignment]
    var = unassigned_vars[0]  # Евристики можна додати сюди

    for value in domains[var]:
        if is_consistent(assignment, var, value):
            assignment[var] = value
            result = backtracking_search(assignment)
            if result:
                return result
            del assignment[var]
    return None

# Виконання
solution = backtracking_search()
if solution:
    print("Розклад знайдено:", solution)
else:
    print("Розклад неможливо знайти")
