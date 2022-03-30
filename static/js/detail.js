console.log('abs')
console.log(localStorage.doctor)
document.getElementById('doctor').value = localStorage.doctor
document.getElementById('patient').value = localStorage.patient
document.getElementById('note_id').value = localStorage.note_id
document.getElementById('description').innerHTML = localStorage.description

function update() {
    $.ajax({
        type: "PATCH",
        url: '/api/v1/update_note/' + document.getElementById('note_id').value,
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            'description': document.getElementById('description').value,
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function () {
            document.location.href = '/';
        },
    });
}


// localStorage.removeItem('doctor')
// localStorage.removeItem('patient')
// localStorage.removeItem('id')
// localStorage.removeItem('description')
