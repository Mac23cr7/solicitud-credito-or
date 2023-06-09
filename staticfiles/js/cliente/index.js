function listadoCliente(){
    $.ajax({
        url: "/cliente/listar_cliente/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_cliente')){
                $('#tabla_cliente').DataTable().destroy();
            }
            $('#tabla_cliente').DataTable();
            $('#tabla_cliente tbody').html("");
            for(let i = 0; i < response.length; i++){
                let fila = '<tr>';
                    fila += '<td>' + response[i]["pk"] + '</td>';
                    fila += '<td>' + response[i]["fields"]['nom_ape'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['fec_nacimiento'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['edad'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['nacionalidad'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['direccion'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['correo'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['telefono'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['tipo_persona'] + '</td>';
                    fila += '<td>' + response[i]["fields"]['nombre_banco'] + '</td>';
                    fila += '<td> <button type="button" class="btn btn-primary btn-sm"';
                    fila += 'onclick="abrir_modal_edicion(\'/cliente/actualizar_cliente/'+response[i]["pk"]+'\');"><i class="fas fa-edit"></i></button>';
                    fila += '<button type="button" class="btn btn-danger btn-sm"';
                    fila += 'onclick="abrir_modal_eliminacion(\'/cliente/eliminar_cliente/'+response[i]["pk"]+'\');"><i class="fas fa-trash-alt"></i></button></td>';
                    fila += '</tr>';
                    $('#tabla_cliente tbody').append(fila);
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
            listadoCliente();
            cerrar_modal_creacion();
        },
        error:function(error){
            notificacionError(error.responseJSON.mensaje);
            activarBoton();
        }
    });
}

function editar(){
    activarBoton();
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function(response){
            notificacionSuccess(response.mensaje);
            listadoCliente();
            cerrar_modal_edicion();
        },
        error:function(error){
            notificacionError(error.responseJSON.mensaje);
            activarBoton();
        }
    });

}

function eliminar(pk){
    console.log($("[name='csrfmiddlewaretoken']").val());
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/cliente/eliminar_cliente/'+pk+'/',
        type: 'post',
        success: function(response){
            notificacionSuccess(response.mensaje);
            listadoCliente();
            cerrar_modal_eliminacion();
        },
        error:function(error){
            notificacionError(error.responseJSON.mensaje);
        }
    });

}


$(document).ready(function(){
    listadoCliente();
});
