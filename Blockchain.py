import Block as block

class Blockchain():
    def __init__(self):
        # self.block = Block
        self.chain = [self.createGenesisBlock()]
    
    def createGenesisBlock(self):
        return block.Block(0, "01/08/18", "Genesis Block", "0x00")


    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)
    