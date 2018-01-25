$( document ).ready(function() {
    $('#submit').click(function() {
        $('table').append('<tr><td>' + $('input[name="first_name"]').val() + '</td><td>'
            + $('input[name="last_name"]').val() + '</td><td>'
            + $('input[name="email"]').val() + '</td><td>'
            + $('input[name="phone_number"]').val() + '</td></tr>');
        return false;
    });
});