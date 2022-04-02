export var view = new ol.View({
    center: [37.121327027069874, 5.722531225442945],
    zoom: 8,
    projection: 'EPSG:4326'
  })
export var select_interaction = new ol.interaction.Select({});
export var service_vector = new ol.source.Vector({
      });
export var destination_vector = new ol.source.Vector({
      });
export var service_layer = new ol.layer.Vector({
        source: service_vector,
      });
export var destination_layer = new ol.layer.Vector({
        source: destination_vector,
      });
export var map = new ol.Map({
    layers: [
      new ol.layer.Tile({
        source: new ol.source.Stamen({
          layer: 'watercolor'
        })
      }),
      new ol.layer.Tile({
        source: new ol.source.Stamen({
          layer: 'terrain-labels'
        })
      }),
      new ol.layer.Tile({
        title: 'Water color',
        type: 'base',
        visible: false,
        source: new ol.source.Stamen({
          layer: 'watercolor'
        })
      }),
      new ol.layer.Tile({
        title: 'OSM',
        type: 'base',
        visible: true,
        source: new ol.source.OSM()
      }),

      service_layer,destination_layer
    ],
    target: 'map',
    controls: ol.control.defaults({
      attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
        collapsible: false
      })
    }),
    view: view
  });