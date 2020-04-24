/* random generater : character_cards */
function randomize_image_character_cards() {
    $.ajax({
        type: 'GET',
        url: "/randomNum_character_cards",
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            var imgName = "character_card-" + result + ".jpg";
            document.getElementById("character_cards_imageid").src= "../../static/image/character_cards" + "/" + imgName ;  
        },
        error: function(result) {
              document.getElementById("cards").innerHTML = "ERROR!";
        }
    });
};

/* random generater : context_cards */
function randomize_image_context_cards() {
    $.ajax({
        type: 'GET',
        url: "/randomNum_context_cards",
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            var imgName = "context_card-" + result + ".jpg";
            document.getElementById("context_cards_imageid").src= "../../static/image/context_cards" + "/" + imgName ;  
        },
        error: function(result) {
              document.getElementById("cards").innerHTML = "ERROR!";
        }
    });
};

/* random generater : parameter_cards */
function randomize_image_parameter_cards() {
    $.ajax({
        type: 'GET',
        url: "/randomNum_parameter_cards",
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            var imgName = "parameter_card-" + result + ".jpg";
            document.getElementById("parameter_cards_imageid").src= "../../static/image/parameter_cards" + "/" + imgName ;  
        },
        error: function(result) {
              document.getElementById("cards").innerHTML = "ERROR!";
        }
    });
};

/* random generater : rammojammo_cards */
function randomize_image_rammojammo_cards() {
    $.ajax({
        type: 'GET',
        url: "/randomNum_rammojammo_cards",
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            var imgName = "rammojammo_card-" + result + ".jpg";
            document.getElementById("rammojammo_cards_imageid").src= "../../static/image/rammojammo_cards" + "/" + imgName ;
        },
        error: function(result) {
              document.getElementById("cards").innerHTML = "ERROR!";
        }
    });
};