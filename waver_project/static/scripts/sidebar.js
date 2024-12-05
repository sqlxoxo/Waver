function navigateTo(section) {
	const sections = document.querySelectorAll('.content-section')
	sections.forEach(sec => sec.classList.add('hidden'))
	document.getElementById(section).classList.remove('hidden')
}
