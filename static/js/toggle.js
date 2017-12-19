$(document).ready(function () {
  $('#menu-toggle').click(function (e) {
      e.preventDefault();
    $('#wrapper').toggleClass('menuDisplayed');
    $("#image-holder").toggleClass("col-lg-3 col-lg-4");
  });
});