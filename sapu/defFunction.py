# 関数について
# 関数とは処理をひとつにまとめて定義すること
def print_banana():
    print("banana")
def print_text(text):
    print(text)
def question_text(text):
    text_q = text + '?'
    print(text_q)
def question_exclamation_text(text1, text2):
    return_text1 = text1 + '?'
    return_text2 = text2 + '!'
    return return_text1, return_text2
# main
print_banana()
print_text("apple")
question_text("orange")
r1, r2 = question_exclamation_text("apple", "banana")
print(r1)
print(r2)