## Group A:

## 1) Data Wrangling I

Perform the following operations using Python on any open-source dataset (e.g., `data.csv`):

1. **Import all the required Python Libraries.**
2. **Locate open-source data from the web** (e.g., [Kaggle](https://www.kaggle.com)). Provide a clear description of the data and its source (i.e., URL of the website).
3. **Load the Dataset** into a Pandas DataFrame.
4. **Data Preprocessing**:
   - Check for missing values using `pandas.isnull()`.
   - Use `describe()` function to get initial statistics.
   - Provide variable descriptions and types.
   - Check the dimensions of the DataFrame.
5. **Data Formatting and Normalization**:
   - Summarize variable types (character, numeric, integer, factor, logical).
   - Apply proper type conversions if necessary.
6. **Turn Categorical Variables into Quantitative Variables** in Python.

In addition to the code and outputs, explain every operation that you do in the above steps and explain everything that you do to import/read/scrape the dataset.

---

## 2) Data Wrangling II

Create an **Academic Performance** dataset of students and perform the following operations using Python:

1. **Scan all variables** for missing values and inconsistencies. Use suitable techniques to handle them.
2. **Scan numeric variables** for outliers. Use appropriate techniques to handle them.
3. **Apply data transformation** on at least one variable. The transformation should serve one of the following purposes:
   - Change the scale for better understanding,
   - Convert a non-linear relationship into a linear one,
   - Decrease skewness and normalize the distribution.

Document your reasoning and approach clearly.

---

## 3) Descriptive Statistics - Measures of Central Tendency and Variability

Perform the following operations on any open-source dataset (e.g., `data.csv`):

1. **Provide summary statistics** (mean, median, min, max, std. deviation) for numeric variables grouped by a categorical variable.  
   Example: If the categorical variable is age group and numeric variable is income, then provide summary stats of income grouped by age groups.  
   Create a list that contains a numeric value for each response to the categorical variable.
2. **Display basic statistical details** (percentile, mean, standard deviation, etc.) for each species in the `iris.csv` dataset (`Iris-setosa`, `Iris-versicolor`, `Iris-virginica`).

Provide code, outputs, and explanations for each step.

---

## 4) Data Analytics I

Create a **Linear Regression Model** using Python or R to predict home prices using the **Boston Housing Dataset** ([Kaggle Link](https://www.kaggle.com/c/boston-housing)).

- The dataset has 506 samples and 14 feature variables.
- The objective is to **predict house prices** using the given features.

---

## 5) Data Analytics II

1. **Implement Logistic Regression** using Python or R on the `Social_Network_Ads.csv` dataset.
2. **Compute the Confusion Matrix** to calculate:
   - True Positives (TP)
   - False Positives (FP)
   - True Negatives (TN)
   - False Negatives (FN)
   - Accuracy
   - Error rate
   - Precision
   - Recall

---

## 6) Data Analytics III

1. **Implement Naïve Bayes Classification Algorithm** using Python or R on the `iris.csv` dataset.
2. **Compute the Confusion Matrix** to calculate:
   - True Positives (TP)
   - False Positives (FP)
   - True Negatives (TN)
   - False Negatives (FN)
   - Accuracy
   - Error rate
   - Precision
   - Recall

---

## 7) Text Analytics

1. **Extract a sample document** and apply the following preprocessing methods:
   - Tokenization
   - POS Tagging
   - Stop Words Removal
   - Stemming
   - Lemmatization
2. **Create representation of documents** by calculating:
   - Term Frequency (TF)
   - Inverse Document Frequency (IDF)

---

## 8) Data Visualization I

1. Use the inbuilt dataset `titanic`. This dataset contains 891 rows of information about Titanic passengers.  
   Use **Seaborn** to find patterns in the data.
2. **Plot a histogram** to check how the **fare** (`fare` column) is distributed among passengers.

---

## 9) Data Visualization II

1. Use the inbuilt dataset `titanic` again.
2. **Plot a box plot** for the distribution of **age** (`age`) with respect to **gender** (`sex`), including survival status (`survived`).
3. Write **observations and inferences** from the plot.

---

## 10) Data Visualization III

Download the **Iris flower dataset** or any other dataset (e.g., [Iris Dataset on UCI](https://archive.ics.uci.edu/ml/datasets/Iris)) into a DataFrame and perform the following:

1. **List the features** and their data types (numeric, nominal, etc.).
2. **Create a histogram** for each feature to show distributions.
3. **Create a boxplot** for each feature.
4. **Compare distributions** and **identify outliers**.

---

## Group B

---

## 1) Create databases and tables, insert small amounts of data, and run simple queries using Impala.

---

## 3) Write a simple program in SCALA using Apache Spark framework.

---

## Group C 

---

## 4) COVID-19 Vaccine Data Analytics (India)

**Dataset:** [covid_vaccine_statewise.csv](https://www.kaggle.com/sudalairajkumar/covid19-inindia?select=covid_vaccine_statewise.csv)

### Tasks:

a. **Describe the Dataset**
- Load the `covid_vaccine_statewise.csv` file using Pandas.
- Provide an overview of the dataset including:
  - Number of rows and columns
  - Column names and their data types
  - Use `info()` and `describe()` functions
  - Describe what each column represents (especially vaccination columns)

b. **Number of Persons State-wise Vaccinated for First Dose in India**
- Group the data by `State` and find the **maximum value** of `First Dose Administered` for each state.
- Remove duplicates, if any.
- Visualize using a bar chart (optional).

c. **Number of Persons State-wise Vaccinated for Second Dose in India**
- Group the data by `State` and find the **maximum value** of `Second Dose Administered` for each state.
- Display the results as a table or chart.

d. **Number of Males Vaccinated**
- Sum the values under the column `Male(Individuals Vaccinated)` to find the total number of males vaccinated across India.

e. **Number of Females Vaccinated**
- Sum the values under the column `Female(Individuals Vaccinated)` to find the total number of females vaccinated across India.







