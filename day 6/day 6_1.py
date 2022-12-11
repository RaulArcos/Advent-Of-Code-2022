def stream_marker_finder(input):
    input = open(input, 'r')
    datastream = input.readline()
    buffer = []
    for pos,char in enumerate(datastream):
        if(len(buffer) == 4):
            if len(set(buffer)) == len(buffer):
                return pos
            buffer.pop(0)
            buffer.append(char)
        else:
            buffer.append(char)
if '__main__' == __name__:
    print("Primer caracter en la pos = ", stream_marker_finder("input.txt"))