

print("=== Sentiment Analysis Project ===")

text = input("Enter your sentence: ").lower()

positive_words = [
    "good", "great", "excellent", "amazing", "happy",
    "love", "best", "nice", "awesome", "wonderful"
]

negative_words = [
    "bad", "worst", "hate", "sad", "poor",
    "angry", "terrible", "awful", "boring", "disappointing"
]

positive_score = 0
negative_score = 0

words = text.split()

for word in words:
    if word in positive_words:
        positive_score += 1
    elif word in negative_words:
        negative_score += 1

print("\nPositive Score:", positive_score)
print("Negative Score:", negative_score)

if positive_score > negative_score:
    print("Sentiment: Positive")
elif negative_score > positive_score:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")