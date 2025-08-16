from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


ANSWER_KEY = {
	"Q1": "A",
	"Q2": "B",
	"Q3": "C",
	"Q4": "D",
	"Q5": "A",
}


def home(request):
	return render(request, 'evaluator/home.html', {"questions": list(ANSWER_KEY.keys())})


@require_http_methods(["POST"])
def evaluate_answers(request):
	# Expect form inputs like answers[Q1]=A, answers[Q2]=B, ...
	answers = {}
	for key, value in request.POST.items():
		if key.startswith('answers[') and key.endswith(']'):
			q = key[len('answers['):-1]
			answers[q] = value.strip()

	score = 0
	results = []
	for question_id, correct in ANSWER_KEY.items():
		given = answers.get(question_id, '')
		is_correct = given.upper() == correct.upper()
		score += 1 if is_correct else 0
		results.append({
			"question": question_id,
			"given": given,
			"correct": correct,
			"is_correct": is_correct,
		})

	percent = (score / max(len(ANSWER_KEY), 1)) * 100.0
	context = {
		"score": score,
		"total": len(ANSWER_KEY),
		"percent": round(percent, 2),
		"results": results,
	}
	return render(request, 'evaluator/result.html', context)
