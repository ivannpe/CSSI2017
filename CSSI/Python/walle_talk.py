word = raw_input('Talk to Wall-e: ')
inputs = {'Hello':'HIII','Whats Up': '*looks up* EEEVVVAAA','Whats your name':'WALL-E'}
def WalleSpeaks():
    if word in inputs:
        return inputs[word]
    return 'Dirrrrr-ect-tivvve?'
print WalleSpeaks()
