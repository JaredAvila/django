$('document').ready(function(){

    $('#creationBtn').on('click', function(){
        $("#createRecipe").show()
    });
    $('#createClose').on('click', function(){
        $("#createRecipe").hide()
    });
    $('#reviewBtn').on('click', function(){
        $("#reviewRecipe").show()
    });
    $('#reviewClose').on('click', function(){
        $("#reviewRecipe").hide()
    });

    $('.commentBtn').on('click', function(){
        $('#hiddenForm').slideToggle()
    });

});