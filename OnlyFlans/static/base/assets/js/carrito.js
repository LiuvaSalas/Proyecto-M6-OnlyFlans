$(document).ready(function () {
  $(".agregar-al-carrito").click(function (e) {
    e.preventDefault(); // Evitar el comportamiento por defecto del botón
    const flanId = $(this).data("flan-id"); // Obtener el ID del flan

    $.ajax({
      url: "{% url 'agregar_al_carrito' 0 %}".replace("0", flanId), // Reemplaza 0 por el ID del flan
      type: "POST",
      data: {
        csrfmiddlewaretoken: "{{ csrf_token }}", // Incluir el token CSRF
      },
      success: function (response) {
        // Mostrar el popup cuando se agrega el producto
        $("#popupModal").modal("show");
      },
      error: function (xhr, status, error) {
        console.error("Error al agregar el producto al carrito:", error);
        alert("Hubo un problema al agregar el producto al carrito."); // Manejo de errores
      },
    });
  });
});
