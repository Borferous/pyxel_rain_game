def lerp(a,b,t):
    return a + (b-a) * t

def clamp(v, mi, mx):
    return min(max(v,mi),mx)
