document.addEventListener('DOMContentLoaded', function() {
    var table = $('#maestrosTable').DataTable();

    function bindButtons() {
        // Cargar datos del maestro en el modal de edición
        document.querySelectorAll('.edit-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                var maestroId = button.getAttribute('data-id');
                fetch('/maestro/editar/' + maestroId + '/')
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            document.getElementById('maestro_id').value = maestroId;
                            document.getElementById('id_nombre').value = data.maestro.Nombre;
                            document.getElementById('id_apellido_paterno').value = data.maestro.Apellido_Paterno;
                            document.getElementById('id_apellido_materno').value = data.maestro.Apellido_Materno;
                            $('#exampleModal').modal('show');
                        }
                    });
            });
        });

        // Eliminar maestro
        document.querySelectorAll('.delete-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                var maestroId = button.getAttribute('data-id');
                var row = button.closest('tr');
                var nombreCompleto = row.querySelector('td:nth-child(2)').textContent;
                
                Swal.fire({
                    title: '¿Estás seguro?',
                    text: `¡No podrás revertir esto! Eliminarás al maestro "${nombreCompleto}" con ID: ${maestroId}`,
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Sí, eliminarlo!'
                }).then((result) => {
                    if (result.isConfirmed) {
                        fetch('/maestro/eliminar/' + maestroId + '/', {
                            method: 'DELETE',
                            headers: {
                                'X-CSRFToken': getCookie('csrftoken')
                            }
                        })
                        .then(response => {
                            if (response.ok) {
                                Swal.fire(
                                    'Eliminado!',
                                    `El maestro "${nombreCompleto}" ha sido eliminado.`,
                                    'success'
                                ).then(() => {
                                    location.reload();
                                });
                            } else {
                                Swal.fire(
                                    'Error!',
                                    'Hubo un problema al eliminar el maestro.',
                                    'error'
                                );
                            }
                        });
                    }
                });
            });
        });
    }

    // Limpiar formulario cuando se abre el modal para añadir un nuevo maestro
    document.getElementById('open-modal-btn').addEventListener('click', function() {
        document.getElementById('maestro_id').value = '';
        document.getElementById('id_nombre').value = '';
        document.getElementById('id_apellido_paterno').value = '';
        document.getElementById('id_apellido_materno').value = '';
        $('#exampleModal').modal('show');
    });

    // Llama a la función bindButtons inicialmente
    bindButtons();

    // Vuelve a enlazar los eventos cada vez que la tabla se redibuja (cuando se cambia de página, etc.)
    table.on('draw', function() {
        bindButtons();
    });

    // Enviar formulario de edición
    document.getElementById('modal-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var form = event.target;
        var maestroId = form.querySelector('#maestro_id').value;
        var actionUrl = maestroId ? '/maestro/editar/' + maestroId + '/' : form.action;
        fetch(actionUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: new URLSearchParams(new FormData(form)).toString()
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                Swal.fire(
                    'Guardado!',
                    'El maestro ha sido guardado correctamente.',
                    'success'
                ).then(() => {
                    $('#exampleModal').modal('hide');
                    location.reload();
                });
            } else {
                Swal.fire(
                    'Error!',
                    'Hubo un problema al guardar el maestro: ' + JSON.stringify(data.errors),
                    'error'
                );
            }
        })
        .catch(error => {
            Swal.fire(
                'Error!',
                'Hubo un problema en el servidor.',
                'error'
            );
        });
    });

    // Obtener el token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
