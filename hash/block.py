import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate()

    def calculate(self):
        text = self.data + self.previous_hash
        self.hash = hashlib.sha256(text.encode()).hexdigest()
        return self.hash

block1 = Block("developer", "000")
block2 = Block("engineer", block1.hash)
block3 = Block("software developer", block2.hash)

print("Block Data: ", block1.data)
print("Block hash: ", block1.hash)
print("Block hash: ", block2.hash)
print("Block hash: ", block3.hash)