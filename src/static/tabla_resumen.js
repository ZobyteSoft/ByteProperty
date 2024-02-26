

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
    var tabla = $('#tabla_potreros_completa').DataTable({
        select: true,
        stateSave: true,
        keys: true,
        dom: 'Blfrtip',
        "pageLength": 10,
        lengthMenu: [
            [5, 10, 20, 30],
            [5, 10, 20, 30]
        ],
        "language": {
            "url": 'https://cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        },
        buttons: [
            {
                extend: 'copy',
                text: '<i class="fa-solid fa-copy"></i> Copiar' // Icono de copiar
            },
            {
                extend: 'csv',
                text: '<i class="fa-solid fa-file-csv"></i> CSV' // Icono de CSV
            },
            {
                extend: 'excel',
                text: '<i class="fa-solid fa-file-excel"></i> Excel' // Icono de Excel
            },
            {
                extend: 'pdf',
                text: '<i class="fa-solid fa-file-pdf"></i> PDF' // Icono de PDF
            },
            {
                extend: 'print',
                text: '<i class="fa-solid fa-print"></i> Imprimir' // Icono de imprimir
            }
        ]
    });

    tabla.on('init.dt', function () {
        $('#tabla_potreros_completa').removeAttr('style');
    });
});

