# Pulsar Classifier
A machine learning model based on k-Nearest-Neighbor for classifying pulsars based on pulsar radio wave emission patterns. 

## Abstract
HTRU2 is a data set which describes a sample of pulsar candidates collected during the High Time Resolution Universe Survey.

Pulsars are a rare type of Neutron star that produce radio emission detectable here on Earth. They are of considerable scientific interest as probes of space-time, the inter-stellar medium, and states of matter.

As pulsars rotate, their emission beam sweeps across the sky, and when this crosses our line of sight, produces a detectable pattern of broadband radio emission. As pulsars
rotate rapidly, this pattern repeats periodically. Thus pulsar search involves looking for periodic radio signals with large radio telescopes.

Each pulsar produces a slightly different emission pattern, which varies slightly with each rotation. Thus a potential signal detection known as a 'candidate', is averaged over many rotations of the pulsar, as determined by the length of an observation. In the absence of additional info, each candidate could potentially describe a real pulsar. However in practice almost all detections are caused by radio frequency interference (RFI) and noise, making legitimate signals hard to find.

## Attributes
Each candidate is described by 8 continuous variables, and a single class variable. The first four are simple statistics obtained from the integrated pulse profile. This is an array of continuous variables that describe a longitude-resolved version of the signal that has been averaged in both time and frequency. The remaining four variables are obtained from the DM-SNR curve. These are summarised below:

  1. Mean of the integrated profile.
  2. Standard deviation of the integrated profile.
  3. Excess kurtosis of the integrated profile.
  4. Skewness of the integrated profile.
  5. Mean of the DM-SNR curve.
  6. Standard deviation of the DM-SNR curve.
  7. Excess kurtosis of the DM-SNR curve.
  8. Skewness of the DM-SNR curve.
  9. Class

HTRU 2 Summary:

  1. 17,898 total examples.
  2. 1,639 positive examples.
  3. 16,259 negative examples.

## Machine Learning Model 
For the data analysis, a classification method was used in order to predict the classes. Specifically, a k-Nearest-Neighbor test was utilized for the model. Specific parameters implemented are the following:

  1. n_neighbors = n (n is a dynamic number and can be changed by the user)
  2. weights = 'uniform'
  3. algorithm = 'ball_tree'
  4. p = 1
  5. n_jobs = -1

For the n_neighbors parameter, the maximum accuracy was reached when either the number of neighbors was 3, 6, or 9. The highest accuracy obtained with this model was 98.043921%. After over 300 runs, I found the other parameters listed for weights, algorithm, p, and n_jobs to be most efficient for the pulsar data set.

Additional information regarding the effects of each parameter can be found on the scikit-learn documentation.

## Packages Used
  
  1. sklearn (neighbors, KNeighborsClassifier)
  2. pandas
  3. NumPy
  4. matplotlib.pyplot
  5. seaborn
  6. mlxtend.plotting

## Further Development
In terms of the machine learning model, I believe that other machine learning models can be implemented such as SVM or k-Means-Clustering for classification, but the current model is sufficient for this dataset. 
In regards to visualization, I was unable to find an effective method through matplotlib or seaborn to visualize this dataset. Since the dataset consists of 9 dimensions, it would be very difficult to develop a scatter plot or other visualization for the dataset. If you have any ideas on how a visualization for the dataset can be developed, please use my contact information below and let me know about your ideas. The packages I tried to use for developing plots are already included in the Python script. Additionally, I am planning to utilize more classification models on the dataset, so please let me know if you have any ideas for maximizing model accuracy.

## Contact
If you have any inquiries regarding my code or you have any ideas that can better the code, please let me know by emailing me at zeeshanp@berkeley.edu.
