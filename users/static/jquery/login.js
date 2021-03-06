$(document).ready(function () {

    var loginError = $("#loginError").val();
    var regError =  $("#regError").val();


    if ( loginError != '' && loginError != null) {
        //console.log(loginError);
        $('.error-box').slideDown('slow').removeClass('green').addClass('red');
        $(".error-message").text(loginError)
    }
    if ( regError!='' && regError != undefined){
        $('.error-box').slideDown('slow').removeClass('green').addClass('red');
        $(".error-message").text(regError)
    }
    
    $('.forgotten-password-link').click(function () {
        $('.forgotten-password-box').slideToggle('slow');
        $('.error-box').slideUp('slow');
        $('#ipt-fp-email').val('')
    });



    $("#sign-in-form").submit(function () {
        var value_login = $("#ipt-login").val();
        var value_password = $("#ipt-password").val();
        if (value_login != "" && value_password != "") {
            $('#ipt-login').removeClass('ipt-error');
            $('#ipt-password').removeClass('ipt-error');
            $('.error-box').slideUp('slow');
            return true
        } else {
            if (value_login == "") {
                $('#ipt-login').addClass('ipt-error');
                $('.error-box').slideDown('slow').removeClass('green').addClass('red');
                $(".error-message").text("Need both username and password.")
            } else if (value_login != "") {
                $('#ipt-login').removeClass('ipt-error')
            }
            if (value_password == "") {
                $('#ipt-password').addClass('ipt-error');
                $('.error-box').slideDown('slow').removeClass('green').addClass('red');
                $(".error-message").text("Need both username and password.")
            } else if (value_password != "") {
                $('#ipt-password').removeClass('ipt-error')
            }
            event.preventDefault();
        }
    });



    $("#registration-form").submit(function () {
        /*var value_login = $("#ipt-login").val();*/
        var value_charName = $("#ipt-charName").val();
        var value_email = $("#ipt-email").val();
        var value_password = $("#ipt-password").val();
        var value_repassword = $("#ipt-repassword").val();
        var email_values = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;

        if ( $("#regError").val()!='' ){
            $('.error-box').slideDown('slow').removeClass('green').addClass('red');
            $(".error-message").text($("#loginError").val())
        }
        
        if (value_charName != "") {
            $('#ipt-charName').removeClass('ipt-error')
        }
        /*
        if (value_login != "") {
            $('#ipt-login').removeClass('ipt-error')
        }
        */
        if (value_email != "") {
            $('#ipt-email').removeClass('ipt-error')
        }
        if (value_password != "") {
            $('#ipt-password').removeClass('ipt-error')
        }
        if (!email_values.test(value_email)) {
            $('#ipt-email').addClass('ipt-error');
            $('.error-box').slideDown('slow').removeClass('green').addClass('red');
            $(".error-message").text("Please, fill your correct email.");
            event.preventDefault();
        }
        if (value_charName != "" && value_email != "" && value_password != "" && value_repassword == value_password && ($('#tac-checkbox:checked').val() !== undefined)) {
            $('#ipt-charName').removeClass('ipt-error');
            $('#ipt-email').removeClass('ipt-error');
            $('#ipt-password').removeClass('ipt-error');
            $('#ipt-repassword').removeClass('ipt-error');
            $('.error-box').slideUp('slow');
            return true
        } else {
            if (value_charName == "") {
                $('#ipt-charName').addClass('ipt-error');
                $('.error-box').slideDown('slow').removeClass('green').addClass('red');
                $(".error-message").text("Please, fill all information.")
            } else if (value_charName != "") {
                $('#ipt-charName').removeClass('ipt-error')
            }
            if (value_email == "") {
                $('#ipt-email').addClass('ipt-error');
                $('.error-box').slideDown('slow').removeClass('green').addClass('red');
                $(".error-message").text("Please, fill all information.")
            } else if (value_email != "") {
                $('#ipt-email').removeClass('ipt-error')
            }
            if (value_password == "") {
                $('#ipt-password').addClass('ipt-error');
                $('.error-box').slideDown('slow').removeClass('green').addClass('red');
                $(".error-message").text("Please, fill all information.")
            } else if (value_password != "") {
                $('#ipt-password').removeClass('ipt-error')
            }
            if (value_password != value_repassword) {
                $('#ipt-repassword').addClass('ipt-error');
                $('.error-box').slideDown('slow').removeClass('green').addClass('red');
                $(".error-message").text("Retyped password doesn't match.")
            } else if (value_password == value_repassword) {
                $('#ipt-repassword').removeClass('ipt-error')
            }
            if (($('#tac-checkbox:checked').val() == undefined) && value_email != "" && value_password != "" && value_repassword == value_password) {
                $('.error-box').slideDown('slow');
                $(".error-message").text("You have to agree with terms and conditions.")
            }
            event.preventDefault();
            //Console.log("Testing things");
        }
    });


    $("#forgotten-password-form").submit(function () {
        var email_values = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
        var value_email = $("#ipt-fp-email").val();
        if (!email_values.test(value_email)) {
            $('#ipt-fp-email').addClass('ipt-error');
            $('.error-box').slideDown('slow').removeClass('green').addClass('red');
            $(".error-message").text("Please, fill your correct email.");
            event.preventDefault();
        }
        if ((value_email != "") && (email_values.test(value_email))) {
            $('#ipt-fp-email').removeClass('ipt-error');
            $('.forgotten-password-box').slideUp('slow');
            $('.error-box').removeClass('red').addClass('green').slideDown('slow');
            $(".error-message").text("We have successfully sent the password reset email.");
            return true
        } else {
            var value_email = $("#ipt-fp-email").val();
            if (value_email == "") {
                $('#ipt-fp-email').addClass('ipt-error');
                $('.error-box').slideDown('slow').removeClass('green').addClass('red');
                $(".error-message").text("Please, fill your email.")
            } else if (email_values.test(value_email)) {
                $('.forgotten-password-box').slideUp('slow');
                $('.error-box').slideDown('slow');
                $(".error-message").text("We have successfully sent the password reset email.")
            } else if (value_email != "") {
                $('#ipt-fp-email').removeClass('ipt-error');
                $('.error-box').slideUp('slow');
                return true
            }
            event.preventDefault();
        }
    })
});
