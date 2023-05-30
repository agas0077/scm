$(document).on('submit', '.button-submittion-form', function (event) {
    event.preventDefault();
    const eventFormId = event.target.id
    const id = eventFormId.split('-')[2];
    const btnId = event.originalEvent.submitter.id;

    $(`#${event.originalEvent.submitter.id}`).html('Отправка...')

    $.ajax({
        type: 'POST',
        url: $(event.target).attr('action'),
        data: {
            target_pk: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            const idFilter = event.originalEvent.submitter.id.replace(/\d+/, '')
            document.querySelectorAll(`[id^='${idFilter}']`).forEach(element => {
                if (element.id != btnId) {

                    $(element).prop('disabled', (i, v) => !v);
                }
            })
            $(`#${btnId}`).html(json.btn_text)
        },
        error: function (xhr, errmsg, err) {
            $(`#${event.originalEvent.submitter.id}`).html('Ошибка')
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});