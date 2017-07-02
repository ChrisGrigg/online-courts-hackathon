from sklearn import datasets
from random import randint

X = []
y = []

for i in range(10000):
    PREV_ADV = randint(1,3)
    CASE_AGE = randint(0,10)
    APOLOGY_GIVEN = randint(1,2)
    BARRISTER_ADVICE = randint(1,3)
    DOCUMENTED_CONTRACT = randint(1,2)
    BREACH_DUTY = randint(1,2)
    SPECIALIST_CLAIM = randint(1,2)
    CONFLICT_OF_INTEREST = randint(1,2)
    FEE_EXCESS_QUOTE = randint(1,2)
    CLIENT_DELAY = randint(1,2)
    CLIENT_HAS_LOSS = randint(1,3)
    CLIENT_IS_EXPERT = randint(1,2)
    CASE_IS_WON = randint(1,2)
    X.append([
        PREV_ADV,
        CASE_AGE,
        APOLOGY_GIVEN,
        BARRISTER_ADVICE,
        DOCUMENTED_CONTRACT,
        BREACH_DUTY,
        SPECIALIST_CLAIM,
        CONFLICT_OF_INTEREST,
        FEE_EXCESS_QUOTE,
        CLIENT_DELAY,
        CLIENT_HAS_LOSS,
        CLIENT_IS_EXPERT
    ])
    y.append(CASE_IS_WON)

# Split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# Train
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train, y_train)

# Predict
predictions = my_classifier.predict(X_test)

# Score
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))

# Export
from sklearn.externals import joblib
joblib.dump(my_classifier, 'model.pkl')
