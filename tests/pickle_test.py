import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "김정협", "나이" : 20, "취미" : ["잠", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()