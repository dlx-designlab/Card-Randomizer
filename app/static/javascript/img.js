/* random generater : character_cards
function randomize_image_character_cards() {
    $.ajax({
        type: 'GET',
        url: "/randomNum_character_cards",
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            var res = result.split(' ')
            var imgName = "character_card-" + res[0] + ".jpg";
            document.getElementById("character_cards_imageid").src= "../../static/image/character_cards" + "/" + imgName;
            document.getElementById("count").innerHTML= res[1];
        },
        error: function(result) {
              document.getElementById("cards").innerHTML = "ERROR!";
        }
    });
};
*/




/* random generater : context_cards */
function randomize_image_context_cards() {
    $.ajax({
        type: 'GET',
        url: "/randomNum_context_cards",
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            var res = result.split(' ')
            var imgName = "context_card-" + res[0] + ".jpg";
            document.getElementById("context_cards_imageid").src= "../../static/image/context_cards" + "/" + imgName;
            document.getElementById("count").innerHTML= res[1];  
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
            var res = result.split(' ')
            var imgName = "parameter_card-" + res[0] + ".jpg";
            document.getElementById("parameter_cards_imageid").src= "../../static/image/parameter_cards" + "/" + imgName;
            document.getElementById("count").innerHTML= res[1];  
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
            var res = result.split(' ')
            var imgName = "rammojammo_card-" + res[0] + ".jpg";
            document.getElementById("rammojammo_cards_imageid").src= "../../static/image/rammojammo_cards" + "/" + imgName;
            document.getElementById("count").innerHTML= res[1];
        },
        error: function(result) {
              document.getElementById("cards").innerHTML = "ERROR!";
        }
    });
};


/* humberger menu */
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');


    burger.addEventListener('click', () => {
        //Toggle Nav
        nav.classList.toggle('nav-active');

        //Animate Links
        navLinks.forEach((link, base_test) => {
            if(link.style.animation) {
                link.style.animation = ``
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${base_test / 5 + 0.3}s`;
            }
        });
        //Burger Animation
        burger.classList.toggle('toggle')


    });
    
    
}

navSlide();