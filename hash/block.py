import hashlib

class Block:
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculate()

    def calculate(self):
        text = self.data + self.previousHash
        self.hash = hashlib.sha256(text.encode()).hexdigest()
        return self.hash

block1 = Block("developer", "000")
block2 = Block("engineer", block1.hash)
block3 = Block("software developer", block2.hash)

print("========== Block 1 ==========")
print("Block Data   :", block1.data)
print("Previous Hash:", block1.previousHash)
print("Current Hash :", block1.hash)
print("Hash Length  :", len(block1.hash))

print("\n========== Block 2 ==========")
print("Block Data   :", block2.data)
print("Previous Hash:", block2.previousHash)
print("Current Hash :", block2.hash)
print("Hash Length  :", len(block2.hash))

print("\n========== Block 3 ==========")
print("Block Data   :", block3.data)
print("Previous Hash:", block3.previousHash)
print("Current Hash :", block3.hash)
print("Hash Length  :", len(block3.hash))