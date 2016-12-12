$(document).ready(main);

function main() {
    loadSpells();
    setFakeLinkListener();

}

$(function() {
    if (Modernizr.history) {

    } else {

    }
});

window.onpopstate = function(event) {
    console.log("navigated");
};

function setFakeLinkListener () {
    $(".class-link").click(function(event) {
        event.preventDefault();
        loadSpells(event.target.id, "");
        switchActive($(this));
        // removeHash();
    });
}

function switchActive (elem) {
    $(".class-link").parent().removeClass("active");
    $(elem).parent().addClass("active");
}

// function found at https://stackoverflow.com/questions/1397329/how-to-remove-the-hash-from-window-location-with-javascript-without-page-refresh/5298684#5298684
function removeHash () {
    history.pushState("", document.title,
                      window.location.pathname + window.location.search);
}

function loadSpells (clss, search) {
    urlPath = clss;
    $.ajax({
        method: "post",
        url: "/spellbook/spell_content",
        data: {
            class: clss,
            // search: search,
        },
        success: function(data){
            $("#content-box").html(data);
            history.pushState({},"", urlPath);
        }
    });
}

function GetQueryStringParams(sParam) {
    var queryString = window.location.search.substring(1);
    var queryVars = queryString.split('&');
    for (var i = 0; i < queryVars.length; i++) {
        var param = queryVars[i].split('=');
        if (param[0] == sParam) {
            return param[1];
        }
    }
}

/* All functions belowed copied from Django documentation.
 * link = https://docs.djangoproject.com/en/1.10/ref/csrf/
 * these functions ensure csrf token passed through with AJAX POST requests
*/
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
