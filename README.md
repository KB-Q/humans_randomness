# Can humans fake randomness?

Project by: Olga Graf, Anshuman Gupta, Akash Reddy, Karthik Balaji.

The concept of randomness emerges often in our daily lives as well as in many professional fields including ML and AI. Yet humans are known to be struggling with the deep understanding of randomness. This manifests itself in the form of well-known cognitive biases, such as gambler's fallacy and many others. E.g., in response to complaints from customers, iTunes' shuffle feature was made less random in order to make it feel more random.
Our inability to critically assess randomness has gained attention of many researchers and provoked numerous studies including those by the Nobel Prize-winning economist Daniel Kahneman.

In our small project, we'd like to approach this vast and interesting topic in two ways:

- Take a sneak peak at our brain and explore our perception of randomness. For this purpose, we conducted a simple coin toss experiment — as a computer simulation and as a human thought experiment.

- Utilize ML methods to predict whether a random binary sequence was generated by human or not. First, we built a classifier using simple logistic regression, and then moved on towards MLP methods and neural networks.

### Contents:

- Report.ipynb - Jupyter notebook containing all the code.
- human_data.csv - Contains the binary strings generated by the project members.
- machine_data.csv - Contains the machine generated binary strings.
- univ_data.csv - Contains the binary strings generated by the students of the AI-1 course as part of the experiment.
- olga_data.csv - Contains data generated by Olga after our data analysis to see if humans could *learn* to be more random.
- randomness_test.py - Contains "randomness tests", which are functions used to generate predictors for our machine learning model. 
