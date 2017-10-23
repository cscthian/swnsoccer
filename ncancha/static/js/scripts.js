jQuery(document).ready(function($) {
  // selecion del toogle dle menu
	var toggleMenu = $('#toggle-menu');
	var mainNav = $('#main-nav');
  toggleMenu.on('click', function() {
    toggleMenu.add(mainNav).toggleClass('show');
  });

});
