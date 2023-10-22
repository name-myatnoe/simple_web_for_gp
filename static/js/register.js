document.getElementById("nextButton").addEventListener("click", function () {
    const userType = document.querySelector('input[name="userType"]:checked').value;

    if (userType === "student") {
        document.querySelector('.student-fields').style.display = "block";
        document.querySelector('.teacher-fields').style.display = "none";
        // Hide the "Next" button and show the "Sign Up" button
        document.getElementById("nextButton").style.display = "none";
        document.getElementById("signUpButton").style.display = "block";
    } else if (userType === "teacher") {
        document.querySelector('.student-fields').style.display = "none";
        document.querySelector('.teacher-fields').style.display = "block";
        // Hide the "Next" button and show the "Sign Up" button
        document.getElementById("nextButton").style.display = "none";
        document.getElementById("signUpButton").style.display = "block";
    }
});
