const switchElement = document.querySelector(".switch");
const footerImage = document.querySelector(".footer img");
const headerImage = document.querySelector(".header .h-izquierda img");


console.log("Switch Element:", switchElement);


// Recupera el estado del switch desde localStorage
const isSwitchActive = localStorage.getItem("switchActive") === "true";

// Establece el estado inicial del switch
if (isSwitchActive) {
    switchElement.classList.add("active");
    document.body.classList.add("active");
    updateImages();
}

switchElement.addEventListener("click", e => {
    switchElement.classList.toggle("active");
    document.body.classList.toggle("active");

    // Guarda el estado en localStorage
    localStorage.setItem("switchActive", switchElement.classList.contains("active"));

    // Actualiza las imágenes
    updateImages();
});

function updateImages() {
    // Actualiza la imagen del pie de página directamente basándote en la presencia de la clase 'active' en el body
    footerImage.src = (switchElement.classList.contains("active") ? activeFooterImage : defaultFooterImage);

    // Actualiza la imagen del encabezado directamente basándote en la presencia de la clase 'active' en el body
    headerImage.src = (switchElement.classList.contains("active") ? activeHeaderImage : defaultHeaderImage);
}
