function listadoCredito(){
    $.ajax({
        url: "/credito/listar_credito/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_credito')){
                $('#tabla_credito').DataTable().destroy();
            }
            $('#tabla_credito').DataTable();
            $('#tabla_credito tbody').html("");
            for(let i = 0; i < response.length; i++){
                let fila = '<tr>';
                    fila += '<td>' + response[i]["pk"] + '</td>';
                    fila += '<td>' + response[i]['id_cliente'] + '</td>';
                    fila += '<td>' + response[i]['desc_credito'] + '</td>';
                    fila += '<td>' + response[i]['pago_minimo'] + '</td>';
                    fila += '<td>' + response[i]['pago_maximo'] + '</td>';
                    fila += '<td>' + response[i]['plazo_credito'] + '</td>';
                    fila += '<td>' + response[i]['id_banco'] + '</td>';
                    fila += '<td>' + response[i]['tipo_credito'] + '</td>';

                    fila += '</tr>';
                    $('#tabla_credito tbody').append(fila);
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
            listadoCredito();
            cerrar_modal_creacion();
        },
        error:function(error){
            notificacionError(error.responseJSON.mensaje);
            activarBoton();
        }
    });
}


$(document).ready(function(){
    listadoCredito();
});
