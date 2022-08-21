# Step1:　Program design and data struct

TEXT = {'agree': '''Yes, I agree. That sounds fine to me.''',
        'busy': '''Sorry, can we do this later this week or next week?''',
        'upsell': '''Would you consider making this a monthly donation?'''}

# Step2: Execution
import sys
if len(sys.argv) < 2:
        print('Usage: python mclip.py [keyphrase] - copy phrase text')
        sys.exit()

keyphrase = sys.argv[1]
# Step 3: Copy right keyphrase
import pyperclip

if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')
else:
        print('There is no text for ' + keyphrase)
