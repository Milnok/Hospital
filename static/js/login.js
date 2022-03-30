function auth_request() {
    $.ajax({
        type: "POST",
        url: '/auth/token/login/',
        data: {
            'username': document.getElementById("username").value,
            'password': document.getElementById("password").value,
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            localStorage.webtoken = response['auth_token']
            document.location.href = '/'
            console.log(response)
        },
        error: function (response) {
            console.log(response)
        },
    });
}


