
$(document).ready(function () {
    $("#annotationbutton").click(function () {
        var newannotation = $("#annotationtext").val().trim()
        submitannotation(newannotation)
    })
})

var submitannotation = function (annotation) {
    /* ajax call */
}