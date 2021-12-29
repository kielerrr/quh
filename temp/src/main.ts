import {createApp} from 'vue'
import {createStore} from 'vuex'
import App from './App.vue'
import Zone from "./components/Zone.vue"

const store = createStore({
	state() {
		return {
			count: 504,
			shapes: [],
			nads: []
		}
	},
	
	actions: {
		addShape: ({commit, state}, shape) => {
			commit('addShape', shape)
		},
		deleteShape: ({commit, state}, selectedShape) => {
			let newShapes = []
			for (let shape in state.shapes) {
				if (store.getters.shapes[shape].getBounds().getNorthEast().lat() == selectedShape.getBounds().getNorthEast().lat()) {
					true
				}
				else {
					newShapes.push(store.getters.shapes[shape])
				
				}
			}
			commit('deleteShape', newShapes)
		},
		
		increment: (store) => {commit('increment')}
		
	},
	mutations: {
		addShape(state, shape) {
			state.shapes.push(shape);
		},
		deleteShape(state, shape) {
			state.shapes = []
			state.shapes =  shape
		},
		increment(state) {state.count++}
	},
	computed: {
		count() {return store.getters.count},
		shapes() {return store.getters.shapes},
	},
	getters: {
		count: state => state.count,
		shapes: state => state.shapes,
		shape: (state) => (shapeID) => {
			console.log('fuck')
		}
	}
})

var app = createApp(App)
app.component("Zone", Zone)
app.use(store)
app.mount('#app')
