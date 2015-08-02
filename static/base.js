window.onload = function(){
  create_event();
}

var location_options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

var getLocation = function(succ_cbk, fail_cbk, options) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(succ_cbk, fail_cbk, options);
    } else {
       console.log("Geolocation is not supported by this browser.");
    }
};

var setLocationInForm = function(position) {
  document.getElementById('position_lat').value = position.coords.latitude;
  document.getElementById('position_long').value = position.coords.longitude;
  console.log("dskjnfs "+document.getElementById('position_lat').value+" "+document.getElementById('position_long').value);
};

var getLocationFailureHandle = function(err) {
  document.getElementById('error_box').value = "Your browser is too old to be cool! Please upgrade"
};

var create_event = function() {
  getLocation(setLocationInForm, getLocationFailureHandle, location_options);
};