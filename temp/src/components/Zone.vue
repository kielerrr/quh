<template>
    <div class="coords-box">
        {
        'north': {{ xyzs.north }}, <br />
        'east': {{ xyzs.east }}, <br />
        'south': {{ xyzs.south }}, <br />
        'west': {{ xyzs.west }}, <br />
        }
    </div>
    <div class="nads-box">

    </div>
</template>

<script setup lang="ts">
import {ref, computed} from 'vue'
import {useStore} from 'vuex'

const store = useStore()
const count = computed(() => store.getters.count)
const shapes = computed(() => store.getters.shapes)


const props = defineProps<{
	shape: Object,
	// msg?: string,
}>()


const nads = []

const xyzs =
	{
		north: props.shape.getBounds().getNorthEast().lat(),
		south: props.shape.getBounds().getSouthWest().lat(),
		east: props.shape.getBounds().getNorthEast().lng(),
		west: props.shape.getBounds().getSouthWest().lng(),
	}



async function getNads(xyzs: { north: any; south: any; east: any; west: any }) {
	let config = {
		method: 'POST',
		body: JSON.stringify(xyzs),
		headers: {
			'Content-Type': 'application/json',
			'accept': 'application/json',
		}
	}
	try {
		const response = await fetch("http://localhost:8000/xyzs/", config);
		const data = await response.json();
		console.log("SUCCESS ON POST", data)
        return data

	} catch (error) {
		console.log('shit broke start: ', error, ' :shit broke end')

	}
}



let new_xys = getNads(xyzs)


//
// const emit = defineEmits<{
//   (e: 'change', id: number): void
//   (e: 'update', value: string): void
// }>()
// emit('asdf')


</script>

<style scoped>
.coords-box {
    font-family: "Courier New";
    font-weight: bolder;
    font-size: 32px;
    margin: 25px auto;
    display: block;
    width: 600px;
    height: 175px;
    background-color: #4caf50;
}

</style>
