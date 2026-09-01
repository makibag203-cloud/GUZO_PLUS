/* =========================================
GUZO PLUS — ENGLISH / AMHARIC LANGUAGE
========================================= */

const translations = {

en: {
    "Smart Dashboard": "Smart Dashboard",
    "AI Traffic Prediction": "AI Traffic Prediction",
    "Smart ETA": "Smart ETA",
    "Driver Management": "Driver Management",
    "Smart Scheduling": "Smart Scheduling",
    "Accident Detection": "Accident Detection",
    "Passenger Demand": "Passenger Demand",
    "Smart Routes": "Smart Routes",
    "Open Traffic": "Open Traffic",
    "Check ETA": "Check ETA",
    "Manage Drivers": "Manage Drivers",
    "Smart Schedule": "Smart Schedule",
    "Monitor Accidents": "Monitor Accidents",
    "View Demand": "View Demand",
    "Find Routes": "Find Routes"
},

am: {
    "Smart Dashboard": "ዘመናዊ ዳሽቦርድ",
    "AI Traffic Prediction": "የAI የትራፊክ ትንበያ",
    "Smart ETA": "ዘመናዊ ETA",
    "Driver Management": "የአሽከርካሪ አስተዳደር",
    "Smart Scheduling": "ዘመናዊ የጊዜ ሰሌዳ",
    "Accident Detection": "የአደጋ ማወቂያ",
    "Passenger Demand": "የተሳፋሪ ፍላጎት",
    "Smart Routes": "ዘመናዊ መንገዶች",
    "Open Traffic": "ትራፊክን ክፈት",
    "Check ETA": "ETA ይመልከቱ",
    "Manage Drivers": "አሽከርካሪዎችን ያስተዳድሩ",
    "Smart Schedule": "ዘመናዊ የጊዜ ሰሌዳ",
    "Monitor Accidents": "አደጋዎችን ይከታተሉ",
    "View Demand": "ፍላጎትን ይመልከቱ",
    "Find Routes": "መንገዶችን ያግኙ"
}


};

const languageBtn = document.getElementById("languageBtn");
const languageText = document.getElementById("languageText");

let currentLanguage =
localStorage.getItem("guzoLanguage") || "en";

function translatePage() {


document.querySelectorAll(
    "h1, h2, h3, p, span, a, button, .page-label"
).forEach(element => {

    const original =
        element.getAttribute("data-original-text") ||
        element.textContent.trim();

    if (!element.getAttribute("data-original-text")) {
        element.setAttribute(
            "data-original-text",
            original
        );
    }

    const translated =
        translations[currentLanguage][original];

    if (translated) {
        element.textContent = translated;
    }

});


if (languageText) {

    languageText.textContent =
        currentLanguage === "am" ? "EN" : "አማ";

}


document.documentElement.lang =
    currentLanguage === "am" ? "am" : "en";


}

if (languageBtn) {


languageBtn.addEventListener("click", function () {

    currentLanguage =
        currentLanguage === "en" ? "am" : "en";

    localStorage.setItem(
        "guzoLanguage",
        currentLanguage
    );

    translatePage();

});


}

translatePage();
