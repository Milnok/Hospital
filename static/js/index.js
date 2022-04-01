function get_node_list() {
    $.ajax({
        type: "GET",
        url: '/api/v1/get_notes',
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            update_table(response);
        },
    });
}

function delete_note(id) {
    $.ajax({
        type: "DELETE",
        url: '/api/v1/delete_note/' + id.toString(),
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            get_node_list(response);
        },
    });
}

function update(id) {
    $.ajax({
        type: "GET",
        url: 'api/v1/get_note_by_id',
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            'id': id.toString(),
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            console.log(response)
            detail_redirect(response);
        },
    });
}

function detail_redirect(data) {
    data = data[0]
    localStorage.doctor = data['doctor']['first_name'] + ' ' + data['doctor']['last_name']
    localStorage.patient = data['patient']['first_name'] + ' ' + data['patient']['last_name']
    localStorage.description = data['description']
    localStorage.note_id = data['id']
    document.location.href = '/detail/'
}

function update_table(response) {
    var c = [];
    c.push("<tr><th>Имя доктора</th><th>Фамилия доктора</th><th>Имя пациента</th><th>Фамилия пациента</th><th>Комментарии</th></tr>")
    $.each(response, function (i, item) {
        c.push("<tr class='t__td'><td>" + item.doctor.first_name + "</td><td>" + item.doctor.last_name + "</td>");
        c.push("<td>" + item.patient.first_name + "</td><td>" + item.patient.last_name + "</td>");
        c.push("<td>" + item.description + "</td>");
        if (localStorage.logintype === 'Doctor') {
            c.push("<td> <button onclick='" + "update(" + item.id + ")" + "' class='update'>Изменить</button></td>")
            c.push("<td> <button onclick='" + "delete_note(" + item.id + ")" + "' class='delete'>Удалить</button> </td></tr>")
        }
        else{
            c.push("</tr>")
        }

    });
    $('#myTable tbody').html(c.join(""));
}

window.onload = function () {
    check_login();
    get_node_list()
}