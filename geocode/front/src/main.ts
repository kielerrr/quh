import { createApp } from 'vue'
import App from './App.vue'
import Zone from "./components/Zone.vue"


var app = createApp(App)

app.component("Zone", Zone)
app.mount('#app')
