function create_note() {
    console.log(document.getElementById('doctor_name').value)
    console.log(document.getElementById('description').value)
    $.ajax({
        type: "POST",
        url: '/api/v1/create_note',
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            'doctor.first_name': document.getElementById('doctor_name').value,
            'doctor.last_name': document.getElementById('doctor_fam').value,
            'patient.first_name': document.getElementById('patient_name').value,
            'patient.last_name': document.getElementById('patient_fam').value,
            'description': document.getElementById('description').value,
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function () {
            document.location.href = '/';
        },
    });
}

window.onload = function () {
    check_login();
    document.getElementById('doctor_name').value = localStorage.login_first
    document.getElementById('doctor_fam').value = localStorage.login_last
}