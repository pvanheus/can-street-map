# can-street-map

A street map to assist the Muizenberg Community Action Network in mapping resources.

The tiles are from OpenStreetMap, the streets are from there too. Buildings are added as additional layer
using QGIS. The QGIS project is in [data/StreetsOfMuizenberg.qgz]. Rep names are in a Google sheet
which is downloaded as CSV [data/MuizenbergStreetReps.csv] and turned into a JSON file using the little
Python script in the data directory. This data is loaded by the code from the Github repository.
 
## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
