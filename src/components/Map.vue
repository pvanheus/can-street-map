<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <div class="map">
                    <l-map
                            ref="map"
                            id="map"
                            style="height: 600px; width: 100%"
                            :zoom="zoom"
                            :extraOptions="extraOptions"
                            :center="center">
                        <l-tile-layer v-if="url" :url="url" :attribution="attribution"/>
                    </l-map>
                </div>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    const axios = require('axios').default;
    // import axios from 'axios';
    import L from 'leaflet';
    import { LMap, LTileLayer } from "vue2-leaflet"

    export default {
        name: "Map",
        data() {
            return {
                url: null,
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors\'',
                extraOptions: { zoomControl: false },
                zoom: 16,
                center: L.latLng(-34.10340, 18.47027),
                features: null,
                streetNames: null,
            }
        },
        components: {
            LMap,
            LTileLayer
        },
        mounted() {
            this.url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

            let data_url = 'https://raw.githubusercontent.com/pvanheus/can-street-map/master/data/StreetsOfMuizenberg.geojson';
            axios.get(data_url).then(response => {
                this.features = response.data.features;
                let streetNameSet = new Set();
                this.features.forEach( feature => {
                    if (feature.properties.name != null) {
                        streetNameSet.add(feature.properties.name);
                    }

                } );
                this.streetNames = Array.from(streetNameSet);
                this.streetNames.sort();

                let street_rep_data_url = 'https://raw.githubusercontent.com/pvanheus/can-street-map/master/data/MuizenbergStreetReps.json';
                axios.get(street_rep_data_url).then(response => {
                    let streetrep_data = response.data;
                    let repsForStreet = {};
                    streetrep_data.forEach(element => {
                        if (!this.streetNames.includes(element.locationName)) {
                            console.log(element.locationName);
                        } else {
                            repsForStreet[element.locationName] = element.repName;
                        }
                    });
                    console.log(repsForStreet);
                    this.features.forEach(feature => {
                        // console.log(feature.properties.name);
                        if (feature.properties.name in repsForStreet) {
                            let street = L.geoJSON(feature).addTo(this.$refs.map.mapObject);
                            street.bindTooltip(repsForStreet[feature.properties.name]);
                        }
                    });
                }).catch(error => {
                    console.log(error);
                });

                // L.geoJSON(this.features).addTo(this.$refs.map.mapObject);

            }).catch(error => {
                console.log(error)
            });

        }
    }
</script>

<style scoped>

</style>
