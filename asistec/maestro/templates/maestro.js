
var tblClient;
 var modal_title;
$(function(){

$('#myModalClient').modal('show');

});
 







const _modeloMaestro = {
    idAccion: "",
    intIdMaestro: 0,
    strNombre: "",
    strApellido_Paterno: "",
    strApellido_Materno: ""



}
document.addEventListener("DOMContentLoaded", function () {
   console.log("ddf");
    //fetch("/Categoria/Mostrar")
    //    .then(response => {
    //        return response.ok ? response.json() : Promise.reject(response)
    //    })
    //    .then(responseJson => {

    //        if (responseJson.length > 0) {
    //            responseJson.forEach((item) => {
    //                $("#cboCategoria").append(
    //                    $("<option>").val(item.intIdCategoria).text(item.strTitulo)
    //                )
    //            })
    //        }

    //    })

   //   $('.btnTest').on('click', function () {
      //       $.ajax({
      //           url: '{% url 'erp:category_list' %}',
      //           type: 'POST',
      //           data: {id: 1},
      //           dataType: 'json'
      //       }).done(function (data) {
      //           console.log(data);
      //       }).fail(function (jqXHR, textStatus, errorThrown) {
      //           alert(textStatus + ': ' + errorThrown);
      //       }).always(function (data) {

      //       });
      //   });


}, false)
function MostrarModal() {

    $("#Nombre").val(_modeloMaestro.strNombre);
    $("#Apellido_Paterno").val(_modeloMaestro.strApellido_Paterno);
    $("#Apellido_Materno").val(_modeloMaestro.strApellido_Materno); 
    // $("#cboDepartamento").val(_modeloEmpleado.idDepartamento == 0 ? $("#cboDepartamento option:first").val() : _modeloEmpleado.idDepartamento)

    $("#modalMaestro").modal("show");

}


$(document).on("click", "#agregarMaestro", function (event) {
    event.preventDefault(); // Evita que se siga el enlace
console.log("patas");
    _modeloMaestro.idAccion = "Nuevo";
    _modeloMaestro.intIdMaestro = 0;
    _modeloMaestro.strNombre = "";
    _modeloMaestro.strApellido_Paterno = "";
    _modeloMaestro.strApellido_Materno = "";
    MostrarModal();
});

$(document).on("click", ".boton-nuevo-maestro", function () {
    console.log("patas");
    _modeloMaestro.idAccion = "Nuevo";
    _modeloMaestro.intIdMaestro = 0;
    _modeloMaestro.strNombre = "";
    _modeloMaestro.strApellido_Paterno = "";
    _modeloMaestro.strApellido_Materno = "";
    MostrarModal();

})

$(document).on("click", ".boton-editar-maestro", function () {


    _modeloMaestro.idAccion = "Editar";
    var idMaestro = $(this).data("idMaestro");
    var nombre = $(this).data("nombre");
    var apellido_paterno = $(this).data("apellido_paterno");
    var apellido_materno = $(this).data("apellido_materno");
    _modeloMaestro.intidMaestro = idMaestro;
    _modeloMaestro.strNombre = nombre;
    _modeloMaestro.strApellido_Paterno = apellido_paterno;
    _modeloMaestro.strApellido_Materno = apellido_materno;

    MostrarModal();

})

$(document).on("click", ".boton-eliminar-maestro", function () {


    var idMaestro = $(this).data("idMaestro");
    var nombre = $(this).data("nombre");
    Swal.fire({
        title: "Esta seguro?",
        text: `Eliminar Nota "${nombre}"`,
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminar",
        cancelButtonText: "No, volver"
    }).then((result) => {

        if (result.isConfirmed) {

            fetch(`/Categoria/Eliminar?idMaestro=${idMaestro}`, {
                method: "DELETE"
            })
                .then(response => {
                    return response.ok ? response.json() : Promise.reject(response)
                })
                .then(responseJson => {

                    if (responseJson.valor) {
                        Swal.fire("Listo!", "Categoria Eliminada", "success");
                        MostrarCategoria();
                    }
                    else
                        Swal.fire("Lo sentimos", "No se puedo eliminar", "error");
                })

        }



    })

    _modeloMaestro.idAccion = "";

})



$(document).on("click", ".boton-guardar-cambios-maestro", function () {
console.log("hola diavlo");
    _modeloMaestro.strNombre = $("#txtNombre").val();
    _modeloMaestro.strApellido_Paterno = $("#txtApellido_Paterno").val();

    if (_modeloMaestro.idAccion == "Nuevo") {

        fetch("/Maestro/Insertar", {
            method: "POST",
            headers: { "Content-Type": "application/json; charset=utf-8" },
            body: JSON.stringify(_modeloMaestro)
        })
            .then(response => {
                return response.ok ? response.json() : Promise.reject(response)
            })
            .then(responseJson => {//ff

                if (responseJson.valor) {
                    $("#modalMaestro").modal("hide");
                    Swal.fire("Listo!", "Maestro Creado con Exito", "success");
                    MostrarCategoria();
                }
                else
                    Swal.fire("Lo sentimos", "No se puedo crear", "error");
            })

    } else {

        fetch("/Maestro/Editar", {
            method: "PUT",
            headers: { "Content-Type": "application/json; charset=utf-8" },
            body: JSON.stringify(_modeloMaestro)
        })
            .then(response => {
                return response.ok ? response.json() : Promise.reject(response)
            })
            .then(responseJson => {

                if (responseJson.valor) {
                    $("#modalMaestro").modal("hide");
                    Swal.fire("Listo!", "El Maestro fue Actualizado", "success");
                    MostrarCategoria();
                }
                else
                    Swal.fire("Lo sentimos", "No se puedo actualizar", "error");
            })

    }

    _modeloMaestro.idAccion = "";

})