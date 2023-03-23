"""递归算法的不足"""
def uinique3(S,start,stop):
    if stop - start <= 1:
        return True
    elif not uinique3(S,start,stop-1):
        return False
    elif not uinique3(S,start+1,stop):
        return False
    else:
        return S[start] != S[stop-1]