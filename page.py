from constants import page_constants
from caption import caption_page
from detect import detect_page
from question import question_page

page_titles = []
for page in page_constants.keys():
    page_titles.append(page_constants[page]["title"])

page_handlers = {
    page_constants["question"]["title"]: question_page,
    page_constants["detect"]["title"]: detect_page,
    page_constants["caption"]["title"]: caption_page
}
