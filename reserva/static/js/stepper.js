const formBtn1 = document.querySelector('#btn-1');
const formBtnPrev2 = document.querySelector('#btn-2-prev');
const formBtnNext2 = document.querySelector('#btn-2-next');
const formBtn3 = document.querySelector('#btn-3');

// Listener del Boton del formulario 1
formBtn1.addEventListener('click', function(e) {
    gotoNextForm(formBtn1, formBtnNext2, 1, 2);
    e.preventDefault();
});

// Listener del Boton Siguiente del formulario 2
formBtnNext2.addEventListener('click', function(e) {
    gotoNextForm(formBtnNext2, formBtn3, 2, 3);
    e.preventDefault();
});

// Listener del Boton Anterior del formulario 2
formBtnPrev2.addEventListener('click', function(e) {
    gotoNextForm(formBtnNext2, formBtn1, 2, 1);
    e.preventDefault();
});

// Listener del Boton del formulario 3
formBtn3.addEventListener('click', function(e) {
    document.querySelector(`.step--3`).classList.remove('step-active');
    document.querySelector(`.step--4`).classList.add('step-active');
    formBtn3.parentElement.style.display = 'none';
    document.querySelector('.form--message').innerHTML = `
        <div class="form--message-text">
            <h2>¡Registro realizado con éxito!</h2>
            <p >Gracias por registrarte en Pacific Reef Hotel</p>
        </div>
   `;
    e.preventDefault();
});

const gotoNextForm = (prev, next, stepPrev, stepNext) => {
    // Obtener el formulario a través del botón
    const prevForm = prev.parentElement;
    const nextForm = next.parentElement;
    const nextStep = document.querySelector(`.step--${stepNext}`);
    const prevStep = document.querySelector(`.step--${stepPrev}`);
    // Agregar clases activas/inactivas a ambos formularios anterior y siguiente
    nextForm.classList.add('form-active');
    nextForm.classList.add('form-active-animate');
    prevForm.classList.add('form-inactive');
    // Cambiar el elemento de paso activo
    prevStep.classList.remove('step-active');
    nextStep.classList.add('step-active');
    // Eliminar clases activas/inactivas a ambos formularios anterior y siguiente
    setTimeout(() => {
        prevForm.classList.remove('form-active');
        prevForm.classList.remove('form-inactive');
        nextForm.classList.remove('form-active-animate');
    }, 1000);
};