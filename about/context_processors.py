from .forms import QuestionForm

def get_question_form(request):
    form = QuestionForm()

    context = {
        'question_form': form
    }

    return context