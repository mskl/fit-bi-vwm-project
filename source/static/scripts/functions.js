// this function makes sure that at least one checkbox is checked before sending the form
function validateform() {
    var checkboxes = document.getElementsByName("sort");
    var okay = false;
    for (var i = 0,l = checkboxes.length; i<l; i++) {
        if(checkboxes[i].checked) {
            okay = true;
            break;
        }
    }
    if (okay) {
        return true;
    }
    else {
        alert("Please check a checkbox");
        return false;
    }
}
