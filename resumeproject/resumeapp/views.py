from django.shortcuts import render

# Create your views here.


def resume(request):

    resume_data = {
        'name': 'Vebeeta Lancy',
        'age': 33,
        'gender': 'Female',
        'email': 'vebeetalancy@gmail.com',

        'skills': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript'
        ],

        'education': {
            'SSLC': 'Sacred heart girls high school - 2009',
            'Plus Two': 'st. Joseph hss - 2011',
            'BCA': 'Mahe co-operative College - 2014',
            'MCA': 'FISAT - 2016'
        }
    }

    return render(request, 'resume.html',
                  {'resume': resume_data})