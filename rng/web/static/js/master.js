function roll_npc() {
    console.log("Rolling NPC...")
    __collect_all_checked_items()

}

function roll_pc() {
    console.log("Rolling PC...")
    __collect_all_checked_items()
}

function click_row(obj) {
    $checkboxes = $(obj).find("input")
    if ($checkboxes.length <= 0) {
        return
    }
    $checkboxes[0].checked = !$checkboxes[0].checked
    $(obj).toggleClass("table-primary")

    $val = $checkboxes[0].value

    if ($val == "all") {
        if ($checkboxes[0].checked) {
            $(obj).parent().find("input").each(function() {
                $box = $(this)[0]
                $box.checked = true
                $row = $($box).closest("tr")
                $row.removeClass("table-primary") // To avoid duplicate classes
                $row.addClass("table-primary")
            })
        }
    } else {
        $box = $(obj).parent().find("input")
        $box[0].checked = false
        $($box[0]).closest("tr").removeClass("table-primary")
    }
}

function __collect_all_checked_items() {
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