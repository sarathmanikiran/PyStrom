"""
    Determine ticket price based on age and student status.

    Args:
        age: Integer representing the person's age.
        is_student: Boolean indicating if the person is a student.

    Returns:
        The ticket price as an integer.
"""
def get_ticket_price(age: int, is_student: bool) -> int:

    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:  # age between 12 and 64
        if is_student:
            return 12
        else:
            return 15

