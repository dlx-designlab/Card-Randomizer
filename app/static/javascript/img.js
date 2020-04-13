function randomize_image() {
    $.ajax({
        type: 'GET',
        url: "/randomcards",
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            var imgName = "img_" + result + ".jpg";
            document.getElementById("imageid").src= "../../static/image" + "/" + imgName ;  
        },
        error: function(result) {
              document.getElementById("cards").innerHTML = "ERROR!";
        }
    });
  };
