document.getElementById('agua-form').onsubmit = function (event) {
	event.preventDefault();
	const idadeGrupo = document.getElementById('idade_grupo').value;
	const peso = parseFloat(document.getElementById('peso').value); // Convertendo para número
	const spinner = document.getElementById('spinner');
	const result = document.getElementById('result');

	// Validações adicionais no frontend
	if (isNaN(peso) || peso <= 0) {
		result.innerText = 'Peso deve ser maior que 0';
		return;
	}

	spinner.classList.add('show'); // Mostra o spinner
	result.innerHTML = ''; // Limpa resultados anteriores
	const startTime = Date.now(); // Registra o tempo de início da requisição

	fetch('http://18.228.236.114:5000/calcular', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({ idade_grupo: idadeGrupo, peso: peso }),
	})
		.then((response) => {
			if (!response.ok) {
				throw new Error('Erro ao calcular ingestão de água');
			}
			return response.json();
		})
		.then((data) => {
			const elapsedTime = Date.now() - startTime; // Calcula o tempo decorrido
			const remainingTime = Math.max(0, 2000 - elapsedTime); // Calcula o tempo restante para completar os 2 segundos

			// Define um atraso para garantir que o spinner fique visível por pelo menos 2 segundos
			setTimeout(() => {
				spinner.classList.remove('show'); // Esconde o spinner
				if (data.error) {
					result.innerText = data.error;
				} else {
					result.innerText = 'Ingestão diária de água: ' + data.total + ' ml';
				}
			}, remainingTime);
		})
		.catch((error) => {
			console.error('Erro:', error);
			const elapsedTime = Date.now() - startTime; // Calcula o tempo decorrido
			const remainingTime = Math.max(0, 4000 - elapsedTime); // Calcula o tempo restante para completar os 4 segundos

			// Define um atraso para garantir que o spinner fique visível por pelo menos 4 segundos
			setTimeout(() => {
				spinner.classList.remove('show'); // Esconde o spinner
				result.innerText = 'Erro ao calcular ingestão de água';
			});
		}, remainingTime);
};
