import { map,select_interaction } from "{% static 'functions.js' %}";
map.addInteraction(select_interaction);
select_interaction.on('select', function (e) {
  // console.log()
  if (e.selected[0]) {
    Swal.fire({
      width: '900px',
      html:
        "<table style='width: -moz-available'>" +
        "<tr>" +
        "<th>Full Name</th>" +
        "<th>Short Name</th>" +
        "<th>Zone</th>" +
        "<th>Wereda</th>" +
        "<th>Kebele</th>" +
        "<th>Phone Mobile</th>" +
        "<th>Email</th>" +
        "<th>Organization</th>" +
        "<th>Service</th>" +
        "</tr>" +
        "<tr>" +
        "<td>" + e.selected[0].get('full_name') + "</td>" +
        "<td>" + e.selected[0].get('short_name') + "</td>" +
        "<td>" + e.selected[0].get('zone') + "</td>" +
        "<td>" + e.selected[0].get('wereda') + "</td>" +
        "<td>" + e.selected[0].get('kebele') + "</td>" +
        "<td>" + e.selected[0].get('phone_mobi') + "</td>" +
        "<td>" + e.selected[0].get('email') + "</td>" +
        "<td>" + e.selected[0].get('organizati') + "</td>" +
        "<td>" + e.selected[0].get('service') + "</td>" +
        "</tr>" +

        "</table>",
      imageUrl: '{% static "a1.jpg" %}',
      imageHeight: 150,
      title: e.selected[0].get('service'),
      showClass: {
        popup: 'animate__animated animate__fadeInDown'
      },
      hideClass: {
        popup: 'animate__animated animate__fadeOutUp'
      }
    })
  }
  else {
    // console.log(false)
  }

});
var layerSwitcher = new ol.control.LayerSwitcher({
  tipLabel: 'Légende' // Optional label for button
});
map.addControl(layerSwitcher);