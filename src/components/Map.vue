<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <l-map
                    ref="map"
                    id="map"
                    style="height: 600px; width: 100%"
                    :zoom="zoom"
                    :extraOptions="extraOptions"
                    :center="center">
                    <l-tile-layer :url="url" :attribution="attribution"/>
                </l-map>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import { LMap, LTileLayer, L } from "vue2-leaflet";

    export default {
        name: "Map",
        data() {
            return {
                url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors\'',
                extraOptions: { zoomControl: false },
                zoom:
            }
        }
    }
</script>

<style scoped>

</style>
