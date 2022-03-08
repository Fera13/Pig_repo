
class File_handling:
    def readNameFiles(self, filename:str):
        names = []

        with open(filename, 'r') as chatReader:
            for line in chatReader:
                name = line.rstrip("\n")
                names.append((name))
        return names
    
    def writeNameFiles(self, filename:str, names:list[str]):
        writing = open(filename, "w")
        for name in names:
            writing.write(name + "\n")
        writing.close()
    
    def readDicFiles(self, filename:str):
        highScoreDic = {}
        name = ""
        score = 0
        with open(filename, 'r') as chatReader:
            for line in chatReader:
                name = line.rstrip("\n")
                score = chatReader.readline().rstrip("\n")
                intValue = int(score)
                highScoreDic[name] = intValue
        return highScoreDic
    
    def writeDicFiles(self, filename:str, highScoreDic: dict[str: int]):
        writing = open(filename, "w")
        for key, value in highScoreDic.items():
            stringvalue = str(value)
            writing.write(key + "\n" + stringvalue + "\n")
        writing.close()