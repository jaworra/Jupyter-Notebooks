def speedFineZone(speed = 50, zone= 60):
    """calculate speeding fine"""
    if speed > zone:
        if zone == 40:
            fine = 100 *(speed - zone)
        elif zone == 60:
            fine = 40 *(speed - zone)
        elif zone == 100:
            fine = 20 *(speed - zone)
    else:
        fine = 0

    return fine
            
