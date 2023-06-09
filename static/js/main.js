
function abrir_modal_edicion(url) {
	$('#edicion').load(url, function () {
		$(this).modal('show');
	});
}
function abrir_modal_creacion(url) {
	$('#creacion').load(url, function () {
		$(this).modal('show');
	});
}
function abrir_modal_eliminacion(url) {
	$('#eliminacion').load(url, function () {
		$(this).modal('show');
	});
}
function cerrar_modal_creacion(){
	$('#creacion').modal('hide');
}

function cerrar_modal_edicion() {
	$('#edicion').modal('hide');
}
function cerrar_modal_eliminacion() {
	$('#eliminacion').modal('hide');
}
function activarBoton(){
	if($('#boton_all').prop('disabled')){
		$('#boton_all').prop('disabled',false);
	}else{
		$('#boton_all').prop('disabled', true);
	}
}

function notificacionError(mensaje) {
	swal.fire({
		title: 'Error!',
		text: mensaje,
		icon: 'error'
	})
}
function notificacionSuccess(mensaje) {
	swal.fire({
		title: 'Buen Trabajo!',
		text: mensaje,
		icon: 'success'
	})
}