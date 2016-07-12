$(document).ready(function() {
    $('.field-status').each(function(index, element) {
        var element = $(element);
        switch (element.text()) {
            case "Zgłoszona":
                element.addClass('add');
            break;
            case "Usunięta":
                element.addClass('done');
            break;
        }
    });
});
