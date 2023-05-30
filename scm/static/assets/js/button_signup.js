$(document).on('submit', '.button-submittion-form', function (event) {
    event.preventDefault();
    const eventFormId = event.target.id
    const id = eventFormId.split('-')[2];
    console.log(eventFormId)
    const btnId = event.originalEvent.submitter.id;
    $.ajax({
        type: 'POST',
        url: $(event.target).attr('action'),
        data: {
            target_pk: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            console.log(json)
            $(`#${btnId}`).html(json.btn_text)
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});