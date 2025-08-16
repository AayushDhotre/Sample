document.addEventListener('DOMContentLoaded', () => {
	const inputs = document.querySelectorAll('input[name^="answers["]');
	for (const input of inputs) {
		input.addEventListener('input', () => {
			input.value = input.value.toUpperCase().replace(/[^ABCD]/g, '');
		});
	}
});