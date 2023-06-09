function listadoBanco(){
    $.ajax({
        url: "/banco/listar_banco/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_banco')){
                $('#tabla_banco').DataTable().destroy();
            }
            $('#tabla_banco').DataTable();
            $('#tabla_banco tbody').html("");
            for(let i = 0; i < response.length; i++){
                let fila = '<tr>';
                    fila += '<td>' + response[i]["pk"] + '</td>';
                    fila += '<td>' + response[i]["fields"]['nombre_banco'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['tipo_banco'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['direccion'] + '</td>';
                    fila += '</tr>';
                    $('#tabla_banco tbody').append(fila);
            }

        },
        error: function(error){
            console.log(error);
        }
    });
}

function registrar(){
    activarBoton();
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function(response){
            notificacionSuccess(response.mensaje);
            listadoBanco();
            cerrar_modal_creacion();
        },
        error:function(error){
            notificacionError(error.responseJSON.mensaje);
            activarBoton();
        }
    });
}


$(document).ready(function(){
    listadoBanco();
});
