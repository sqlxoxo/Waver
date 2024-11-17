document.addEventListener('DOMContentLoaded', function () {
	// Получаем все ссылки в боковой панели
	const navLinks = document.querySelectorAll('.sidebar nav ul li a')
	const sections = document.querySelectorAll('.content-section')

	// Устанавливаем активный раздел
	function activateSection(targetId) {
		sections.forEach(section => {
			section.classList.remove('active')
		})
		document.getElementById(targetId).classList.add('active')

		// Обновляем активные ссылки
		navLinks.forEach(link => {
			link.classList.remove('active')
		})
		const activeLink = document.querySelector(
			`.sidebar nav ul li a[href="#${targetId}"]`
		)
		if (activeLink) activeLink.classList.add('active')
	}

	// Добавляем обработчик кликов для навигации
	navLinks.forEach(link => {
		link.addEventListener('click', function (e) {
			e.preventDefault()
			const targetId = link.getAttribute('href').substring(1) // Извлекаем ID из href
			activateSection(targetId)
		})
	})

	// Инициализация: активируем первый раздел по умолчанию
	activateSection('groups')
})
