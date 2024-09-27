def calculateCredits(selected):
    total_credits = 0
    seen_courses = set()

    for course_code, slot in selected:
        if course_code in seen_courses:
            continue

        seen_courses.add(course_code)
        slot_credits = 0
        sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
        sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

        # Calculate credits for sections
        for section in sections:
            if section.startswith("T"):  # TA1, TA2, etc. are 1 credit
                slot_credits += 1
            else:  # A1, A2, B1, etc. are 2 credits
                slot_credits += 2

        # Calculate credits for sub-slots (L1, L2, etc.)
        for sub_slot in sub_slots:
            if sub_slot.startswith("L"):  # Each L slot (L1, L2, etc.) is 0.5 credit
                slot_credits += 0.5

        # Special case: STS courses
        if course_code.startswith("STS"):
            slot_credits = 1

        total_credits += slot_credits

    return total_credits

