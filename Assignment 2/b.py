s = "SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF"

#values of different residues

p_alpha = {'A': 1.45, 'R': 0.79, 'N': 0.73, 'D': 0.98, 'C': 0.77, 'E': 1.53, 'Q': 1.17, 'G': 0.53, 'H': 1.24, 'I': 1.00, 'L': 1.34, 'K': 1.07, 'M': 1.20, 'F': 1.12, 'P': 0.59, 'S': 0.79, 'T': 0.82, 'W': 1.14, 'Y': 0.61, 'V': 1.14}
p_beta = {'A': 0.97, 'R': 0.90, 'N': 0.65, 'D': 0.80, 'C': 1.30, 'E': 0.26, 'Q': 1.23, 'G': 0.81, 'H': 0.71, 'I': 1.60, 'L': 1.22, 'K': 0.74, 'M': 1.67, 'F': 1.28, 'P': 0.62, 'S': 0.72, 'T': 1.20, 'W': 1.19, 'Y': 1.29, 'V': 1.65}

helix = {'E': 1, 'A': 1, 'L': 1, 'H': 1, 'M': 1, 'Q': 1, 'W': 1, 'V': 1, 'F': 1, 'K': 0.5, 'I': 0.5, 'D': 0, 'T': 0, 'S': 0, 'R': 0, 'C': 0, 'N': -1, 'Y': -1, 'P': -1, 'G': -1}
sheet = {'M': 1, 'V': 1, 'I': 1, 'C': 1, 'Y': 1, 'F': 1, 'Q': 1, 'L': 1, 'T': 1, 'W': 1, 'A': 0.5, 'R': 0, 'G': 0, 'D': 0, 'K': -1, 'S': -1, 'H': -1, 'N': -1,'P': -1, 'E': -1}
