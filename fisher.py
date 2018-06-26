from scipy.stats import chi2_contingency
import numpy as np

# only takes positive numbers

obs = np.array([[0.001348492, 0.146205004], [0.084789681, 0.211746132]])

print(chi2_contingency(obs))

# returns [chi2, p, dof, expected]
