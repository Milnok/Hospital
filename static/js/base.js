function check_login() {
    $.ajax({
        type: "POST",
        url: '/api/v1/check_login',
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            localStorage.login_first = response['login_first']
            localStorage.login_last = response['login_last']
            localStorage.logintype = response['type']
            document.getElementById('a_username').innerHTML = response['login_first'] + ' ' + response['login_last']
            document.getElementById('login_page').style.display = 'none'
            document.getElementById('quit').style.display = ''
            if (response['type'] === 'Doctor') {
                document.getElementById('create_note').style.display = ''
            } else {
                document.getElementById('create_note').style.display = 'none'
            }
        },
        error: function (response) {
            localStorage.webtoken = null
            localStorage.login_first = null
            localStorage.login_last = null
            localStorage.logintype = null
            document.getElementById('login_page').style.display = ''
            document.getElementById('quit').style.display = 'none'
            document.getElementById('create_note').style.display = 'none'
        },
    });
}

function logout() {
    $.ajax({
        type: "POST",
        url: '/auth/token/logout/',
        headers: {
            "Authorization": "Token " + localStorage.webtoken
        },
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (response) {
            localStorage.webtoken = null
            localStorage.login = null
            document.getElementById('login_page').style.display = ''
            document.getElementById('quit').style.display = 'none'
            document.location.href = '/'
        },
        error: function (response) {
            localStorage.login = response['login']
            document.getElementById('login_page').style.display = 'none'
            document.getElementById('quit').style.display = ''
        },
    });
}



