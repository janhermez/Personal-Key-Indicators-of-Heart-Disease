import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

file_path = r"C:\Users\janhe\Downloads\heart_2020_cleaned.csv"
data = pd.read_csv(file_path)

data_with_text = data.copy()


# Define the numerical columns
numerical_columns = ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']

# Function to create and save plots
def create_and_save_plots(df, columns, dataset_type):
    sns.set(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i//2, i%2], color="skyblue")
        axes[i//2, i%2].set_title(f'Distribution of {col} ({dataset_type} Data)')
    
    plt.tight_layout()
    plt.savefig(f'{dataset_type.lower()}_data_plots.png')  # Save as PNG
    plt.show()

# Create and save plots for original data
create_and_save_plots(data, numerical_columns, 'Original')

# Function to remove outliers using IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Remove outliers from the specified columns
data_cleaned = data.copy()
for col in numerical_columns:
    data_cleaned = remove_outliers(data_cleaned, col)

# Create and save plots for cleaned data
create_and_save_plots(data_cleaned, numerical_columns, 'Cleaned')

# Calculating and printing descriptive statistics for the cleaned dataset
descriptive_stats_cleaned = data_cleaned[numerical_columns].describe()
modes_cleaned = data_cleaned[numerical_columns].mode().loc[0]
descriptive_stats_cleaned.loc['mode'] = modes_cleaned
print(descriptive_stats_cleaned)

# Convert categorical variables to numerical for correlation analysis
label_encoder = LabelEncoder()
categorical_columns = ['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'Asthma', 'KidneyDisease', 'SkinCancer']
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Convert HeartDisease to a binary numerical variable
data['HeartDisease'] = data['HeartDisease'].map({'Yes': 1, 'No': 0})

# Correlation matrix
corr_matrix = data.corr()

# Plotting the heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

# Logistic Regression Analysis
# Define the feature matrix and target vector
X = data.drop('HeartDisease', axis=1)
y = data['HeartDisease']

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and fit the logistic regression model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

# Extracting and plotting coefficients
coefficients = pd.DataFrame(logreg.coef_[0], X.columns, columns=['Coefficient'])
coefficients.sort_values(by='Coefficient', ascending=False, inplace=True)

plt.figure(figsize=(10, 6))
sns.barplot(x=coefficients['Coefficient'], y=coefficients.index)
plt.title('Logistic Regression Coefficients')
plt.savefig('logreg_coefficients.png')
plt.show()


demographic_columns = ['AgeCategory', 'Race', 'Sex']

# Sort the DataFrame by the demographic column in ascending order
data_with_text.sort_values(by='AgeCategory', ascending=True, inplace=True)

plt.figure(figsize=(15, 5 * len(demographic_columns)))

for i, demographic in enumerate(demographic_columns):
    plt.subplot(len(demographic_columns), 1, i + 1)
    sns.countplot(x=demographic, hue='HeartDisease', data=data_with_text, order=data_with_text[demographic].unique())
    plt.title(f'Distribution of Heart Disease across {demographic}')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('heart_disease_distribution_across_demographics.png')
plt.show()



























