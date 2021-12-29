<template>
    <div class="blob">
        <div>
            <div id="color-palette"></div>
        </div>
        <div>
            <div id="map"></div>
        </div>
        <div>
            <div class="shapes">
                <Zones />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">


import Zones from './Zones.vue'
import {ref, computed} from 'vue'
import {useStore} from 'vuex'

const store = useStore()
const count = computed(() => store.getters.count)
const shapes = computed(() => store.getters.shapes)


function initialize() {
	let map = new google.maps.Map(document.getElementById('map'), {
		zoom: 9,
		center: new google.maps.LatLng(43.580, -76.164),
		mapTypeId: google.maps.MapTypeId.HYBRID,
		disableDefaultUI: true,
		zoomControl: true
	});

	let polyOptions = {
		strokeWeight: 0,
		fillOpacity: 0.45,
		editable: true,
		draggable: true
	};

	drawingManager = new google.maps.drawing.DrawingManager({
		drawingMode: google.maps.drawing.OverlayType.RECTANGLE,
		polylineOptions: {
			editable: true,
			draggable: true
		},
		drawingControlOptions: {
			position: google.maps.ControlPosition.TOP_CENTER,
			drawingModes: [
				google.maps.drawing.OverlayType.RECTANGLE,
			],
		},
		rectangleOptions: polyOptions,
		map: map
	});
	window.google.maps.event.addListener(drawingManager, 'overlaycomplete', function (e) {
		let newShape = e.overlay;
		newShape.type = e.type;
		// touchShape(newShape)
		store.dispatch('addShape', newShape)
		touchShape(newShape)
		drawingManager.setDrawingMode(null);
		window.google.maps.event.addListener(newShape, 'click', function (e) {
			setSelection(newShape);
		});
		window.google.maps.event.addListener(newShape, 'bounds_changed', touchShape);
        setSelection(newShape);
	});
    window.google.maps.event.addListener(drawingManager, 'drawingmode_changed', clearSelection);
    window.google.maps.event.addListener(map, 'click', clearSelection);
	window.addEventListener('keydown', event => {
		if (event.key === 'Delete') {
			deleteSelectedShape()
		}
	}, true);


	window.addEventListener('keydown', event => {
		if (event.key === ' ') {
			drawingManager.setDrawingMode(null);
		}
	}, true);
	buildColorPalette();
}

window.google.maps.event.addDomListener(window, 'load', initialize);


const addShape = (shape) => {
	store.dispatch('addShape', shape)
}

function touchShape(shape) {
	let bounds = shape.getBounds()  // google api function to get bounds
    console.log('new bounds set: ', bounds, shape)
}


let drawingManager;
let selectedShape;
let colors = ['#1E90FF', '#FF1493', '#32CD32', '#FF8C00', '#4B0082'];
let selectedColor;
let colorButtons = {};

function clearSelection() {
	if (selectedShape) {
		console.log('clearing')
		selectedShape.setEditable(false);
		selectedShape = null;
	}
}

function pushShape(shape) {
	true
}


function setSelection(shape) {
	clearSelection();
	selectedShape = shape;
	shape.setEditable(true);
	selectColor(shape.get('fillColor') || shape.get('strokeColor'));
}

function deleteSelectedShape() {
	if (selectedShape) {
		store.dispatch('deleteShape', selectedShape)
		selectedShape.setMap(null);

	}
}

function selectColor(color) {
	selectedColor = color;
	for (let i = 0; i < colors.length; ++i) {
		let currColor = colors[i];
		colorButtons[currColor].style.border = currColor === color ? '2px solid #789' : '2px solid #fff';
	}

	let rectangleOptions = drawingManager.get('rectangleOptions');
	rectangleOptions.fillColor = color;
	drawingManager.set('rectangleOptions', rectangleOptions);

}

function setSelectedShapeColor(color) {
	if (selectedShape) {
		selectedShape.set('fillColor', color);
	}
}

function makeColorButton(color) {
	let button = document.createElement('span');
	button.className = 'color-button';
	button.style.backgroundColor = color;
	window.google.maps.event.addDomListener(button, 'click', function () {
		selectColor(color);
		setSelectedShapeColor(color);
	});

	return button;
}

function buildColorPalette() {
	let colorPalette = document.getElementById('color-palette');
	for (let i = 0; i < colors.length; ++i) {
		let currColor = colors[i];
		let colorButton = makeColorButton(currColor);
		colorPalette.appendChild(colorButton);
		colorButtons[currColor] = colorButton;
	}
	selectColor(colors[0]);
}


</script>


<style scoped>
#map {
    height: 500px;
    width: 700px;
    margin: 0 auto;
}

a {
    color: #42b983;
}

label {
    margin: 0 0.5em;
    font-weight: bold;
}

code {
    background-color: #eee;
    padding: 2555px 4555px;
    border-radius: 4px;
    color: #304455;
}

#blob {
    font-family: Arial, sans-serif;
    font-size: 13px;
    margin: 10px;
}

#color-palette {
    clear: both;
    margin: 0 auto;
}
</style>
