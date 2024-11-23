# 🌟 Data Science Projects Portfolio

Explore my curated collection of data science projects, showcasing end-to-end workflows in data preprocessing, feature engineering, machine learning, and deployment. 🚀 Each project reflects practical applications of data science principles and tools.

---

## 🏠 **Project 1: House Price Prediction**
**Objective:**  
The goal of this project was to develop a predictive model to estimate house prices based on various features such as size, location, number of rooms, and other amenities. Accurate house price predictions help buyers and sellers make informed decisions, improving efficiency in the real estate market.

**Steps Involved:**  
- 🧹 **Data Preprocessing:**  
  * Cleaned the dataset by handling missing values using mean and mode imputation.  
  * Scaled numerical features to ensure uniformity and encoded categorical variables.  
- 🔧 **Feature Engineering:**  
  * Created new features such as "BsmtHalfBath" and reduced the dimensions of the dataset.  
- 🤖 **Model Selection and Training:**  
  * Trained an XGBoost model, leveraging its ability to handle feature interactions and missing values effectively.  
  * Performed hyperparameter tuning using GridSearchCV to optimize model performance.  
- 📊 **Evaluation:**  
  * Assessed model performance using RMSE and MAE to evaluate prediction accuracy.  

**🔗 [Notebook Link](https://github.com/syedasonianaz/Data_Science_Projects/blob/main/house_price_prediction.ipynb)**

---

## 💬 **Project 2: Sentiment Analysis**
**Objective:**  
This project focused on building a text classification system to categorize user reviews or comments as positive or negative. Sentiment analysis is widely used in business applications to gauge customer feedback and brand perception.

**Steps Involved:**  
- 🧹 **Data Preprocessing:**  
  * Removed noise such as HTML tags, special characters, and stop words.  
  * Tokenized text into meaningful units using NLTK.  
  * Normalized text data using lemmatization for consistency.  
- 📐 **Feature Extraction:**  
  * Extracted numerical representations of text using TF-IDF (Term Frequency-Inverse Document Frequency) and Count Vector.  
- 🤖 **Model Training:**  
  * Implemented Naive Bayes and Logistic Regression models, both of which are well-suited for text classification tasks.  
- 📊 **Evaluation:**  
  * Evaluated models using accuracy, precision, recall, and F1-score on both datasets: TF-IDF and Count Vector.  

**🔗 [Notebook Link](https://github.com/syedasonianaz/Data_Science_Projects/blob/main/sentiment_analysis.ipynb)**

---

## 🚢 **Project 3: Titanic Classification**
**Objective:**  
The objective was to predict the survival of passengers aboard the Titanic using machine learning. This binary classification problem helps in understanding factors that influence survival in catastrophic events.

**Steps Involved:**  
- 🔍 **Data Exploration:**  
  * Performed exploratory data analysis (EDA) to identify trends between survival and features like gender, age, class, and ticket fare.  
  * Visualized data using histograms, box plots, and bar charts.  
- 🔧 **Feature Engineering:**  
  * Handled missing values in the dataset, particularly for "Age" using imputation and "Cabin" features.  
  * Encoded categorical variables like "Sex" and "Embarked."  
- 🤖 **Model Training:**  
  * Trained models including Random Forest, Logistic Regression, and several others.  
- 📊 **Evaluation:**  
  * Measured model performance using accuracy.

**🔗 [Notebook Link](https://github.com/syedasonianaz/Data_Science_Projects/blob/main/titanic.ipynb)**

---

## 👥 **Project 4: Customer Segmentation**
**Objective:**  
This project aimed to segment customers into distinct groups based on purchasing behavior, demographic data, and other attributes. Customer segmentation helps businesses create personalized marketing strategies, boosting customer retention and sales.

**Steps Involved:**  
- 🔍 **Data Exploration:**  
  * Analyzed the dataset to understand relationships between features.  
  * Visualized data using scatter plots, histograms, and box plots to identify patterns.  
- 🔧 **Feature Engineering:**  
  * Created new features such as "Age Group" to uncover latent patterns.  
  * Used K-Means to find the optimal number of clusters by plotting an elbow graph.  
  * Standardized features to improve clustering model performance.  
- 🤖 **Model Training:**  
  * Applied clustering techniques, including K-Means and hierarchical clustering.  
  * Tested models with and without feature scaling for comparison.  
- 📊 **Evaluation:**  
  * Visualized clusters using contour plots.  
  * Analyzed centroids to interpret customer group characteristics.  

**🔗 [Notebook Link](https://github.com/syedasonianaz/Data_Science_Projects/blob/main/customers_segmentation_clustering.ipynb)**

---

## 💳 **Project 5: Credit Card Fraud Detection**
**Objective:**  
This project focused on detecting fraudulent credit card transactions using machine learning. Early fraud detection is critical for minimizing financial losses and safeguarding customers.

**Steps Involved:**  
- 🔍 **Data Exploration:**  
  * Analyzed a highly imbalanced dataset with numerical features.  
  * Visualized class distributions (99:1 ratio) and plotted histograms and box plots for all columns.  
- 🔧 **Feature Engineering:**  
  * Applied scaling techniques to standardize features like "Amount."  
  * Handled class imbalance using oversampling, undersampling, and SMOTE techniques.  
- 🤖 **Model Training:**  
  * Tested various models, including Logistic Regression and Random Forest, to identify the best performer.  
  * Compared results of models under different sampling techniques.  
- 📊 **Evaluation:**  
  * Assessed models using confusion matrices, precision, recall, and F1-scores.  

**🔗 [Notebook Link](https://github.com/syedasonianaz/Data_Science_Projects/blob/main/creditcard.ipynb)**

---

## 📉 **Project 6: Customer Churn Prediction**
**Objective:**  
This project aimed to predict whether customers are likely to churn based on their historical interactions and demographic data. Churn prediction enables proactive measures to retain valuable customers.

**Steps Involved:**  
- 🔍 **Data Exploration:**  
  * Conducted EDA to identify trends and correlations between features and churn.  
  * Visualized data distributions for categorical and numerical features using pie charts, pair plots, and box plots.  
  * Used heatmaps to check correlations between numerical features.  
- 🔧 **Feature Engineering:**  
  * Addressed incorrect data types and scaled numerical features using outlier-robust scalers.  
  * Dealt with class imbalance using techniques like undersampling, oversampling, and SMOTE.  
- 🤖 **Model Training:**  
  * Trained multiple models, including Decision Trees, Random Forest, and XGBoost on different sampling techniques.  
  * Conducted hyperparameter tuning to improve model accuracy.  
- 📊 **Evaluation:**  
  * Evaluated models using confusion matrices and ROC-AUC.  
- 🖥️ **Deployment:**  
  * Developed an interactive dashboard using Streamlit for visualizing predictions and insights.  

**🔗 [Notebook Link](https://github.com/syedasonianaz/Data_Science_Projects/blob/main/customer_churn.ipynb)**  
**🔗 [Dashboard Link](https://customerchurndashboard.streamlit.app/)**

---

💡 **Feel free to explore the projects and provide feedback!**  
✨ Connect with me on [LinkedIn](https://linkedin.com/in/syedasonianaz) for collaborations or discussions!
