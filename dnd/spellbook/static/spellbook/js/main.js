$(document).ready(main);

function main() {
    loadSpells();
    setFakeLinkListener();

}

function setFakeLinkListener () {
    $(".fake-link").click(function(event) {
        event.preventDefault();
        window.location = "?class=wizard";
    });
}

function loadSpells () {
    search = GetQueryStringParams('search');
    clss = GetQueryStringParams('class');

    $.ajax({
        method: "post",
        url: "/spellbook/spell_content",
        data: {
            class: clss,
            search: search,
        },
        success: function(data){
            $("#content-box").html(data);
        }
    });
}

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
