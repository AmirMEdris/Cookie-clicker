from pyautogui import moveTo,click
cpdef int click100():
    cdef int i = 0
    cdef int times = 100
    moveTo(135,513)
    while i < times:
        click()
        i+=1
    return 0
cpdef int clickx(int x):
    cdef int i
    moveTo(135,513)
    for i in range(x):
        click()
    return 0


    