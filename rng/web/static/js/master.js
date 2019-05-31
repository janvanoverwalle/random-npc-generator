function roll_npc() {
    __roll("npc")
}

function roll_pc() {
    __roll("pc")
}

function __roll(char_type) {
    json_data = {
        roll: char_type
    }

    $.post({
        url: "/",
        data: JSON.stringify(json_data),
        contentType: "application/json"
    }).done(function(response) {
        console.log(response)
        console.log(response["character"])
    }).fail(function(e) {
        console.log("Request failed")
    })
}