import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics 
import seaborn as sns

trials = [1,2,3,4,5,6,7,8,9,10]
methods = ['no interaction', 'grabbing', 'pulling', 'shaking']
data = {
    'no interaction': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'grabbing': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'pulling': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'shaking': [0, 1, 1, 1, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data, index=trials)

fig, axs = plt.subplots(2, 2, figsize=(10, 9))
axs[0, 0].plot(df.index, df['no interaction'], marker='o', label='No Interaction', color='turquoise')
axs[0, 0].set_ylabel('Activation (1) / Neutral (0)')
axs[0, 0].set_title('No Interaction')
axs[0, 0].set_xlabel('Trial Number')
axs[0, 0].set_yticks([0, 1])
axs[0, 0].set_xticks(trials)


axs[0, 1].plot(df.index, df['grabbing'], marker='o', label='Grabbing', color='hotpink')
axs[0, 1].set_ylabel('Activation (1) / Neutral (0)')
axs[0, 1].set_title('Grabbing')
axs[0, 1].set_xlabel('Trial Number')
axs[0, 1].set_yticks([0, 1])
axs[0, 1].set_xticks(trials)

axs[1, 0].plot(df.index, df['pulling'], marker='o', label='Pulling', color='orange'  )
axs[1, 0].set_ylabel('Activation (1) / Neutral (0)')
axs[1, 0].set_title('Pulling')
axs[1, 0].set_xlabel('Trial Number')
axs[1, 0].set_yticks([0, 1])
axs[1, 0].set_xticks(trials)

axs[1, 1].plot(df.index, df['shaking'], marker='o', label='Shaking', color='yellowgreen')
axs[1, 1].set_ylabel('Activation (1) / Neutral (0)')
axs[1, 1].set_title('Shaking')
axs[1, 1].set_xlabel('Trial Number')
axs[1, 1].set_yticks([0, 1])
axs[1, 1].set_xticks(trials)

plt.suptitle('Interaction Activation Results Across Trials')
plt.show()

ground_truth = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
activations = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1])
confusion_matrix = metrics.confusion_matrix(ground_truth, activations)
print(confusion_matrix)



sns.heatmap(confusion_matrix,
            annot=True,
            fmt='g',
            xticklabels=['Neutral','Activation'],
            yticklabels=['Neutral','Activation'])

# display matrix
plt.title('Confusion Matrix')
plt.ylabel('Actual',fontsize=12)
plt.xlabel('Reading',fontsize=12)
plt.show()
