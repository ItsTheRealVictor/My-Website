$('.fart').on('click', function(){
    $('#about').css('background-color', 'white')
})

$('#flexSwitchCheckDefault').change(function(){
    if ($(this).is(':checked')){
        $('h1').css('color', 'red')
    }
    else {
        $('h1').css('color', 'blue')

    }
  })