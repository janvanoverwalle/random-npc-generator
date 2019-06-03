function roll_npc() {
    console.log("Rolling NPC...")
    __collect_checked_items()

}

function roll_pc() {
    console.log("Rolling PC...")
    __collect_checked_items()
}

function __collect_checked_items() {
    selected = {
        gender: __collect_checked_items_for("gender"),
        race: __collect_checked_items_for("race"),
        class: __collect_checked_items_for("class"),
        profession: __collect_checked_items_for("profession")
    }
    console.log(selected)
}

function __collect_checked_items_for(table_id) {
    $table = $("#" + table_id)
    $inputs = $table.find("input")
    items = []

    if ($inputs.length <= 0) {
        return items
    }

    for (i = 0; i < $inputs.length; i++) {
        if (!$inputs[i].checked) {
            continue
        }

        items.push($inputs[i].value)

        if ($inputs[i].value.trim().toLowerCase() == 'all') {
            break
        }
    }

    return items
}