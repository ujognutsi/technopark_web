from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
QUESTIONS = []
for i in range(1,40):
    tags_arr = []
    for j in range (1, i+1):
        tags_arr.append('tag' + str(j))          # массив строк!!
    QUESTIONS.append({
        'title': 'title' + str(i), 
        'id': i, 
        'text': 'text' + str(i),
        'tags': tags_arr
    })

def paginate(objects_list, request, per_page=10):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)
    page_obj = paginator.page(page_num)
    return page_obj

def index(request):
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, request, 10) })

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def ask(request):
    return render(request, 'ask.html')

def hot(request):
    hot = QUESTIONS[5:20]
    return render(request, 'hot.html', {'questions': paginate(hot, request, 10) })

def question(request, question_id):
    item = QUESTIONS[question_id - 1]
    return render(request, 'question_detail.html', {'question': item })

def settings(request):
    return render(request, 'settings.html')

def tag(request, tag_name = str()):
    tag_questions = []
    for question in QUESTIONS:
        if tag_name in question.get('tags'):
            tag_questions.append(question)
    return render(request, 'tag.html', {'questions': paginate(tag_questions, request, 10) })
    

# QUESTIONS - это массив словарей, каждый словарь - это вопрос, у каждого вопроса есть айди, титул, текст и тэги (массив)
# задача в том, чтобы в карточке с вопросом выводился список тэгов (ссылок), принадлежащих этому вопросу
# при нажатии на тэг должна происходить адресация на tag.html - альтернативу hot.html, но на этой странице
# должны отображаться только те вопросы, в которых содержится данный тэг
# tag_questions - список вопросов, содержащих передаваемый в функцию