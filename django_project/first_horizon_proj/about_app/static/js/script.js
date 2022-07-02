window.onscroll = function() {scrollFunc()};

function scrollFunc() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("button_scroll").style.display = "block";
    } else {
        document.getElementById("button_scroll").style.display = "none";
    };
};