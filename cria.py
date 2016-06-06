import os, errno
with open("pastas.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip("\n")
        directoryPath = linha
        try:
            os.mkdir (directoryPath)
        except OSError:
           if not os.path.isdir(directoryPath):
               raise
