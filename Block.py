import hashlib

class Block():
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()
        # self.nonce = nonce

    def calculateHash(self):
        param = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousHash)
        return hashlib.sha256(param.encode()).hexdigest()