$(document).ready(main);

function main() {
    highlightActive();
    switchNavbar();
    closeNavbar();
    loadSpells();
}

//function to set the active class on navbar
function highlightActive() {
    $.each($('#navbar').find('li'), function() {
        $(this).toggleClass('active', 
            $(this).find('a').attr('href') == window.location.pathname);
    });
}

// fuction to hide internal navbar when main nav is expanded
function switchNavbar () {
    $("#nav-toggle-main").bind("click", function (event) {
        if ($("#navbar").hasClass("in")) {
            $(".internal-navbar").removeClass("hidden");
        }
        else {
            $(".internal-navbar").addClass("hidden");
        }
    });
}

//function to close expanded navbar when clicked away or when used
function closeNavbar () {
    $(document).click(function (event) {
        var clickover = $(event.target);
        if ($("#navbar").hasClass("navbar-collapse collapse in") &&
            clickover[0].nodeName != "A") {
            $("#nav-toggle-main").click();
        }
        if ($("#navbar2").hasClass("navbar-collapse collapse in")) {
            $("#nav-toggle-internal").click();
        }
    });
}

function loadSpells () {
    $.ajax({
        url: "spell_content",
        success: function(data){
            $("#content-box").html(data);
        }
    });
}
