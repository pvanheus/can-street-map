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
    import axios from 'axios';
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
                center: L.latLng(-34.0956, 18.4840),
                features: null,
            }
        },
        components: {
            LMap,
            LTileLayer
        },
        mounted() {
            let tile_base = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
            this.url = tile_base;

            let data_url = 'https://raw.githubusercontent.com/pvanheus/can-street-map/master/data/StreetsOfMuizenberg.json';
            axios.get(data_url).then(response => {
                this.feature = response.data
            })
        }
    }
</script>

<style scoped>

</style>
