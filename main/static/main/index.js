function say_hello_frontend() {
    console.log("HELLO")
}

function say_hello_backend() {
    let shopping_item = $("#input_item").val();
    let store = $("#input_store").val();
    let buy_date = $("#input_date").val();
    // I'd like to do a back-end call here
    $.ajax(
        {
            url: "/ajax_say_hello/", // www.domain.com/ajax_say_hello
            type: "POST",
            data: {
                "csrfmiddlewaretoken": $('input[name=csrfmiddlewaretoken]').val(),
                "shopping_item": shopping_item,
                "store": store,
                "buy_date": buy_date
            }
        })
}