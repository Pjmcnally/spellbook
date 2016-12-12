$(document).ready(main);

function main() {
    switchNavbar();
    closeNavbar();
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
        if ($("#navbar").hasClass("navbar-collapse collapse in")) {
            $("#nav-toggle-main").click();
        }
        if ($("#navbar2").hasClass("navbar-collapse collapse in")) {
            $("#nav-toggle-internal").click();
        }
    });
}
