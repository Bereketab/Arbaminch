export var view = new ol.View({
    center: [37.67, 6.22],
    zoom: 10,
    projection: 'EPSG:4326'
  })
export var select_interaction = new ol.interaction.Select({});
export var service_vector = new ol.source.Vector({
      });
      export var nearest_vertex = new ol.source.Vector({
      });
export var destination_vector = new ol.source.Vector({
      });
export var service_layer = new ol.layer.Vector({
        source: service_vector,
      });
      export var vertex_layer = new ol.layer.Vector({
        source: nearest_vertex,
        style:new ol.style.Style({
          image: new ol.style.Circle({
              radius: 7,
              fill: new ol.style.Fill({ color: 'red' }),
              stroke: new ol.style.Stroke({
                  color: [255, 0, 0], width: 2
              })
          })
      })
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

      service_layer,destination_layer,vertex_layer
    ],
    target: 'map',
    controls: ol.control.defaults({
      attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
        collapsible: false
      })
    }),
    view: view
  });