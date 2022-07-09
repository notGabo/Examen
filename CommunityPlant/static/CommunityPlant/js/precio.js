$(document).ready(function(){
    var precioTotal;
    var descuento;
    var elem = $(this);
    precioTotal = 0;
    descuento = 0;
    $('.calculoPrecioUnitario').each(function(index){
        precioTotal += parseInt($(this).html());  
    });

    $('#precioTotal').html('Precio total: $' + (precioTotal));

    $('#checkDescuento').click(function() {
        setTimeout(function() {
          descuento = parseInt($('#valorDescuento').html());
          $('#precioTotal').html('Precio total: $' + (precioTotal - (precioTotal * (descuento/100))));
        }, 1000);
      }); 
});
