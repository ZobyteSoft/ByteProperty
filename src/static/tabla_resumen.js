$(document).ready(function () {
    $('#tabla_resumen').DataTable({
        "pageLength": 3,
        "lengthMenu": [
            [3,5,10,],
            [3,5,10]
        ],
        "language": {
            "url": 'https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        }
    });
});

$(document).ready(function () {
    $('#tabla_potreros_completa').DataTable({
        "pageLength": 5,
        lengthMenu: [
            [3,5,10,],
            [3,5,10]
        ],
        "language": {
            "url": 'https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        }
    });
});
