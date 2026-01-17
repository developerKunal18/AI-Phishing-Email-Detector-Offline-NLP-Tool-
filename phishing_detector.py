from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "Verify your account immediately by clicking this link",
    "Your bank account has been suspended",
    "Meeting scheduled at 3 PM tomorrow",
    "Please review the attached project report",
    "Urgent action required update your password now",
    "Let us discuss the presentation tomorrow"
]

labels = [1, 1, 0, 0, 1, 0]  # 1 = Phishing, 0 = Safe

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

print("🛡️ AI Phishing Email Detector \n")

email = input("Paste email content: ")

vec = vectorizer.transform([email])
prediction = model.predict(vec)[0]

if prediction == 1:
    print("\n🚨 PHISHING email detected")
else:
    print("\n✅ Email looks safe")
