function updateGreeting() {
    let date = new Date();
    let hh = date.getHours();
    let greeting;

    if (hh >= 0 && hh < 12) {
        greeting = '¡Buenos días!';
    } else if (hh >= 12 && hh < 18) {
        greeting = '¡Buenas tardes!';
    } else {
        greeting = '¡Buenas noches!';
    }

    let saludo = document.querySelector('#greeting'); // Selecciona el elemento por su ID
    saludo.textContent = greeting;
}

function currentTime() {
    let date = new Date();
    let hh = date.getHours();
    let ampm = (hh >= 12) ? 'PM' : 'AM';

    hh = (hh % 12) || 12; // Convierte la hora a formato de 12 horas
    hh = (hh < 10) ? String(hh) : hh; // Añade cero si la hora es menor que 10
    
    let mm = date.getMinutes();
    let ss = date.getSeconds();

    hh = (hh < 10) ? "0" + hh : hh;
    mm = (mm < 10) ? "0" + mm : mm;
    ss = (ss < 10) ? "0" + ss : ss;

    let time = hh + ":" + mm + ":" + ss + " " + ampm;
    let watch = document.querySelector('#watch');
    watch.innerHTML = time;

    // Llama a la función para actualizar el saludo
    updateGreeting();
}

setInterval(currentTime, 1000);
