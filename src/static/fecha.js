function mostrarFecha() {
    // Obtiene la fecha actual
    const fechaActual = new Date();

    // Obtiene el día, mes y año
    const dia = fechaActual.getDate();
    const mes = fechaActual.toLocaleString('default', { month: 'long' });
    const año = fechaActual.getFullYear();

    // Construye la cadena de fecha en el formato deseado
    const fechaFormateada = `${dia} ${mes} ${año}`;

    // Muestra la fecha en el elemento con el id "fecha"
    document.getElementById('fecha').textContent = fechaFormateada;
}

// Llama a la función al cargar la página
mostrarFecha();