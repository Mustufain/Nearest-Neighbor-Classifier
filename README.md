# Nearest-Neighbor-Classifier
Algorithm for simple nearest neighbor classification 
We will use real data about medical conditions related to vertigo (a disorder of the balance system). Each data item corresponds to a single patient and consists of several attributes (sometimes called features). The attributes convey information about what kind of symptoms etc. the patients have experienced. The goal is to be able to deduce the patient's condition (= classify, or actually diagnose, the patient) based on the symptoms.The training data
Your program will receive three command line parameters that specify input file names. The first command line parameter, sys.argv[1], gives the name of a file that contains training data. Each row of the file describes both the correct classification and five attribute values for one data item (= patient). The values are separated from each other by white space (tab values). Therefore each row has a total of six values. The first line of the file is shown below.

1 4 1 1 5 0

The first line describes a data item whose correct class is 1 and whose five attributes (describing symptoms) have values 4, 1, 1, 5 and 0. It is typical that all data is transformed into numeric form (to better enable e.g. statistical analysis of the values). For example in this case the class 1 really means a condition called vestibular schwannoma. Each attribute gives, again in numeric form, information about the level or variation of some symptom.

The second command line parameter, sys.argv[2], specifies a file that contains test data about vertigo patients. This data is otherwise similar to the training data but now the first value, the correct classification, is missing. Therefore each row contains only five values. These five attribute values are given in the same order as they appear in the training set.

The third command line parameter, sys.argv[3], specifies a file that contains the true classifications for each patient in the test set. Each row contains only one value: the classification of the corresponding test patient. Here "correspondence" means the row index. Row i of the answers file corresponds to row i of the test file.
