s = "SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF"

#values of different residues

p_alpha = {'A': 1.45, 'R': 0.79, 'N': 0.73, 'D': 0.98, 'C': 0.77, 'E': 1.53, 'Q': 1.17, 'G': 0.53, 'H': 1.24, 'I': 1.00, 'L': 1.34, 'K': 1.07, 'M': 1.20, 'F': 1.12, 'P': 0.59, 'S': 0.79, 'T': 0.82, 'W': 1.14, 'Y': 0.61, 'V': 1.14}
p_beta = {'A': 0.97, 'R': 0.90, 'N': 0.65, 'D': 0.80, 'C': 1.30, 'E': 0.26, 'Q': 1.23, 'G': 0.81, 'H': 0.71, 'I': 1.60, 'L': 1.22, 'K': 0.74, 'M': 1.67, 'F': 1.28, 'P': 0.62, 'S': 0.72, 'T': 1.20, 'W': 1.19, 'Y': 1.29, 'V': 1.65}

helix = {'E': 1, 'A': 1, 'L': 1, 'H': 1, 'M': 1, 'Q': 1, 'W': 1, 'V': 1, 'F': 1, 'K': 0.5, 'I': 0.5, 'D': 0, 'T': 0, 'S': 0, 'R': 0, 'C': 0, 'N': -1, 'Y': -1, 'P': -1, 'G': -1}
sheet = {'M': 1, 'V': 1, 'I': 1, 'C': 1, 'Y': 1, 'F': 1, 'Q': 1, 'L': 1, 'T': 1, 'W': 1, 'A': 0.5, 'R': 0, 'G': 0, 'D': 0, 'K': -1, 'S': -1, 'H': -1, 'N': -1,'P': -1, 'E': -1}

listHelix = []
listSheet = []

#identifying alpha helix
for i in range(len(s)-5):
	window = s[i:i+6]
	counter = 0
	for x in window:
		if p_alpha.get(x)>1:
			counter = counter+1
	if counter>=4:
		for j in range(6):
			if (not(i+j in listHelix)):
				listHelix.append(i+j)
		extensionScore = 1000000
		ex = i+6
		while extensionScore>=4:
			if ex<len(s):
				extensionWindow = s[ex-3:ex+1]
				extensionScore = 0
				for y in extensionWindow:
					extensionScore = extensionScore + p_alpha.get(y)
				if extensionScore>=4:
					if (not(ex in listHelix)):
						listHelix.append(ex)
			else:
				break
			ex = ex+1
		extensionScore = 10000000
		ex = i-1
		while extensionScore>=4:
			if ex>=0:
				extensionWindow = s[ex:ex+4]
				extensionScore = 0
				for y in extensionWindow:
					extensionScore = extensionScore +p_alpha.get(y)
				if extensionScore>=4:
					if (not(ex in listHelix)):
						listHelix.append(ex)
			else:
				break
			ex = ex-1


print(s)
for i in range(len(s)):
	if i in listHelix:
		print("H", end = "")
	else:
		print(" ", end = "")

#identifying alpha helix
for i in range(len(s)-4):
	window = s[i:i+5]
	counter = 0
	for x in window:
		if p_beta.get(x)>1:
			counter = counter+1
	if counter>=3:
		for j in range(5):
			if (not(i+j in listSheet)):
				listSheet.append(i+j)
		extensionScore = 1000000
		ex = i+5
		while extensionScore>4:
			if ex<len(s):
				extensionWindow = s[ex-3:ex+1]
				extensionScore = 0
				for y in extensionWindow:
					extensionScore = extensionScore + p_beta.get(y)
				if extensionScore>4:
					if (not(ex in listSheet)):
						listSheet.append(ex)
			else:
				break
			ex = ex+1
		extensionScore = 10000000
		ex = i-1
		while extensionScore>4:
			if ex>=0:
				extensionWindow = s[ex:ex+4]
				extensionScore = 0
				for y in extensionWindow:
					extensionScore = extensionScore +p_beta.get(y)
				if extensionScore>4:
					if (not(ex in listSheet)):
						listSheet.append(ex)
			else:
				break
			ex = ex-1

print()
print(s)
for i in range(len(s)):
	if i in listSheet:
		print("S", end = "")
	else:
		print(" ", end = "")


		