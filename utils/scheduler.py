from datetime import datetime, timedelta

def allocate_slot(existing_bookings):
    start_time = datetime.strptime("08:00", "%H:%M")

    if len(existing_bookings) == 0:
        return start_time.strftime("%H:%M")

    next_slot = start_time + timedelta(minutes=30 * len(existing_bookings))
    return next_slot.strftime("%H:%M")