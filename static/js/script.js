/* =========================================
   GUZO PLUS LANGUAGE SYSTEM
========================================= */

const languageBtn = document.getElementById("languageBtn");
const languageText = document.getElementById("languageText");

let currentLanguage = localStorage.getItem("guzoLanguage") || "en";


function updateLanguage() {

    if (currentLanguage === "am") {

        document.body.classList.add("amharic");

        languageText.textContent = "EN";

        document.documentElement.lang = "am";

    } else {

        document.body.classList.remove("amharic");

        languageText.textContent = "አማ";

        document.documentElement.lang = "en";
    }
}


if (languageBtn) {

    languageBtn.addEventListener("click", function () {

        currentLanguage =
            currentLanguage === "en" ? "am" : "en";

        localStorage.setItem(
            "guzoLanguage",
            currentLanguage
        );

        updateLanguage();

    });

}


updateLanguage();
