$("document").ready(function(){
    $(".send").click(function(){
        var sentence = $(".text1").val();
        var sentence2 = $(".text2").val();
        $.ajax({
            url: "http://localhost:5000/api/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"message": sentence, 'message2' : sentence2})
        }).done(function(data) {
            console.log(data);
            $('.output').text(data.output).show()

        });
    });
});