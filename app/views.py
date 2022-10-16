from django.shortcuts import render


# Create your views here.

def counting_range(count):
    str = ''
    for i in range(count):
        str += ' '
    return str


QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question #{i}",
        "number": i,
        "answers": i,
        "counting_tags": counting_range(i),
        "tag_name": f"{i}",
        "text_answers": f"This is answer is text for question #{i}",
        "counting_answers": counting_range(i),
    } for i in range(5)
]


def index(request):
    return render(request, "index.html", {"questions": QUESTIONS})
def new_ask(request):
    return render(request, "new_ask.html", {"questions": QUESTIONS})
def question(request, i: int):
    return render(request, "page_question.html", {"question": QUESTIONS[i]})
def tag(request, i: int):
    return render(request, "listing_po_tegu.html", {"question": QUESTIONS[i], "questions": QUESTIONS})
def settings(request):
    return render(request, "settings.html", {"questions": QUESTIONS})
def login(request):
    return render(request, "login.html", {"questions": QUESTIONS})
def registration(request):
    return render(request, "registration.html", {"questions": QUESTIONS})


