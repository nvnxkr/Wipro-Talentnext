'''
Your friend has sent you a text file containing n lines. He sent a secret message
with it, which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has
given hints to find it. Let's surprise him by breaking the challenge with our
python code.

Hints to find the secret message:

1. The number of lines in the file tells you the meeting time.
Note: 1 <= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12 hour
format. For example,
. If the number of lines is 15, then the meeting time is 3 PM.

. If the number of lines is 10, then the meeting time is 10 AM.
2. The word appearing for the maximum number of times tells you the

meeting place.
Note: Meeting place will be a street name.
For example,
. If the word Oxford appears for the maximum number of times,
then meeting place is Oxford Street.

. If the word Park appears for the maximum number of times, then

meeting place is Park Street.
'''

import re
from collections import Counter

def find_secret_message():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        num_lines = len(lines)
        if num_lines == 0:
            print("File is empty.")
            return
            
        # Calculate meeting time based on number of lines
        time = num_lines
        period = "AM"
        if time == 12:
            period = "PM"
        elif time > 12 and time < 24:
            time -= 12
            period = "PM"
        elif time == 24:
            time = 12
            period = "AM"
            
        meeting_time = f"{time} {period}"
        
        # Calculate meeting place based on most frequent word
        content = " ".join(lines)
        # Extract words using regex
        words = re.findall(r'\b\w+\b', content)
        if not words:
            print("No words found.")
            return
            
        word_counts = Counter(w.lower() for w in words)
        most_common_word = word_counts.most_common(1)[0][0].title()
        
        meeting_place = f"{most_common_word} Street"
        
        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}")
        
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    find_secret_message()
