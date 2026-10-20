MAX_SEMESTER_CREDITS = 18


def calculate_gpa(grades):
    total_credits = sum(item["credits"] for item in grades)

    if total_credits == 0:
        return 0.0

    weighted_points = sum(
        item["grade_point"] * item["credits"]
        for item in grades
    )

    return round(weighted_points / total_credits, 2)


def validate_credit_limit(current_credits, course_credits):
    return current_credits + course_credits <= MAX_SEMESTER_CREDITS


def has_enrollment_conflict(existing_slots, new_slot):
    for start, end in existing_slots:
        new_start, new_end = new_slot

        if new_start < end and new_end > start:
            return True

    return False
