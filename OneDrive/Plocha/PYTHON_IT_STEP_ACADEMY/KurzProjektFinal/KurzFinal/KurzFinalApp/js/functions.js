
document.querySelector('.js-whatHide').addEventListener( 'keyup', function() {
	let hodnota = this.value;

	let ctverecky = document.querySelectorAll('.js-searchIn p');
	for (let i = 0; i < ctverecky.length; i++) {
		if( ctverecky[i].innerText.includes( hodnota ) && hodnota.length != 0 ) {
			ctverecky[i].classList.add('nalezeno');
		}		
		else {
			ctverecky[i].classList.remove('nalezeno');
		}
	}
}) 

