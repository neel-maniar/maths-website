function toggleHint(hintId) {
    var hint = document.getElementById(hintId);
    if (hint.style.display === "none" || hint.style.display === "") {
        hint.style.display = "block";
    } else {
        hint.style.display = "none";
    }
}
