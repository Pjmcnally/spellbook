$(document).ready(main);

function main() {
    loadSpells();
}

function loadSpells (slug=null) {
    $.ajax({
        url: "spell_content",
        success: function(data){
            $("#content-box").html(data);
        }
    });
}
