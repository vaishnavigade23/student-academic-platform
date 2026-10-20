from app.services.academic_service import (
    calculate_gpa,
    validate_credit_limit,
    has_enrollment_conflict,
)


def test_calculate_gpa():
    grades = [
        {"grade_point": 9, "credits": 3},
        {"grade_point": 8, "credits": 3},
    ]
    assert calculate_gpa(grades) == 8.5


def test_gpa_with_no_credits():
    assert calculate_gpa([]) == 0.0


def test_credit_limit_allowed():
    assert validate_credit_limit(15, 3) is True


def test_credit_limit_exceeded():
    assert validate_credit_limit(18, 3) is False


def test_enrollment_conflict():
    existing_slots = [(9, 10), (11, 12)]
    assert has_enrollment_conflict(existing_slots, (9.5, 10.5)) is True


def test_no_enrollment_conflict():
    existing_slots = [(9, 10), (11, 12)]
    assert has_enrollment_conflict(existing_slots, (10, 11)) is False
