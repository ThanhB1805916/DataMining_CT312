import re
import string
from pyvi import ViTokenizer

def preprocess(text):
    text = clean_text(text)
    token = ViTokenizer.tokenize(text)

    return token

# xóa các ký tự đặc biệt chỉ chừa lại chữ
def clean_text(text):

    # viết thường
    text = text.lower()

    # xóa dấu ngoặc
    text = re.sub('[\(\[].*?[\)\]]', '', text)

    # dấu nháy
    text = re.sub("[''‘’“”…]", '', text)

    # bỏ dấu câu (, . : ;)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)

    # xóa từ có số
    text = re.sub('\w*\d\w*', '', text)

    # xóa dấu new line
    text = re.sub('\n', ' ', text)

    return text