function create_note() {
    console.log(document.getElementById('doctor_name').value)
    console.log(document.getElementById('description').value)
    $.ajax({
        type: "POST",
        url: '/api/v1/create_note',
        // headers: {
        //     "Authorization": "Token " + localStorage.webtoken
        // },
        data: {
            'doctor_name': document.getElementById('doctor_name').value,
            'doctor_fam': document.getElementById('doctor_fam').value,
            'patient_name': document.getElementById('patient_name').value,
            'patient_fam': document.getElementById('patient_fam').value,
            'description': document.getElementById('description').value,
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function () {
            document.location.href = '/';
        },
    });
}
