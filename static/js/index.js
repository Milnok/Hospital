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
        } else {
            c.push("</tr>")
        }

    });
    $('#myTable tbody').html(c.join(""));
}

function get_timetable() {
    $.ajax({
        type: "GET",
        url: '/api/v1/get_timetable',
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            update_timetable(response);
        },
    });
}

function update_timetable(response) {
    var c = [];
    c.push("<tr><th>Имя доктора</th><th>Фамилия доктора</th><th>Понедельник</th><th>Вторник</th><th>Среда</th><th>Четверг</th><th>Пятница</th></tr>")
    $.each(response, function (i, item) {
        c.push("<tr class='t__td'><td>" + item.doctor.first_name + "</td><td>" + item.doctor.last_name + "</td>");
        c.push("<td>" + item.monday_start + " - " + item.monday_end + "</td>");
        c.push("<td>" + item.tuesday_start + " - " + item.tuesday_end + "</td>");
        c.push("<td>" + item.wednesday_start + " - " + item.wednesday_end + "</td>");
        c.push("<td>" + item.thursday_start + " - " + item.thursday_end + "</td>");
        c.push("<td>" + item.friday_start + " - " + item.friday_end + "</td></tr>");
    });
    $('#myTimetable tbody').html(c.join(""));
}


window.onload = function () {
    get_timetable()
    check_login();
    get_node_list()
}