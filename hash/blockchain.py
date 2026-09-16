import hashlib

data = input("Enter the value: ")
hash_value = hashlib.sha256(data.encode()).hexdigest()
print(hash_value)
print("sha256 algo: ", len(hash_value))

# hash_value_md5 = hashlib.md5(data.encode()).hexdigest()
# print(hash_value_md5)
# print("md5 algo: ", len(hash_value_md5))

# hash_value_sha1 = hashlib.sha1(data.encode()).hexdigest()
# print(hash_value_sha1)
# print("sha1 algo: ", len(hash_value_sha1))

# hash_value_sha512 = hashlib.sha512(data.encode()).hexdigest()
# print(hash_value_sha512)
# print("sha512 algo: ", len(hash_value_sha512))


# # List Data
# # -------------------------------
# list_data = ['A', 'B', 'C', 'D', 'E']
# print("\n-------------List Data--------------")

# print("\n-------------sha256 also---------------")
# for data in list_data:
#     hash_value = hashlib.sha256(data.encode()).hexdigest()
#     print(hash_value)
#     print("sha256 algo: ", len(hash_value))

# print("\n-------------md5 also---------------")
# for data in list_data:
#     hash_value_md5 = hashlib.md5(data.encode()).hexdigest()
#     print(hash_value_md5)
#     print("md5 algo: ", len(hash_value_md5))

# print("\n-------------sha1 also---------------")
# for data in list_data:
#     hash_value_sha1 = hashlib.sha1(data.encode()).hexdigest()
#     print(hash_value_sha1)
#     print("sha1 algo: ", len(hash_value_sha1))

# print("\n-------------sha512 also---------------")
# for data in list_data:
#     hash_value_sha512 = hashlib.sha512(data.encode()).hexdigest()
#     print(hash_value_sha512)
#     print("sha512 algo: ", len(hash_value_sha512))



'''
Question: Take 5 inputs from user and find out hash value of each with its length(use sha512)
'''
# import hashlib
# user_input = []

# for i in range(5):
#     item = input(f"Enter data {i + 1}: ")
#     user_input.append(item)

# print("\nUsing sha512 algo")
# for data in user_input:
#     hash_value_sha512 = hashlib.sha512(data.encode()).hexdigest()
#     print(hash_value_sha512)
#     print("sha512 algo: ", len(hash_value_sha512))