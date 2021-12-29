<template>
  <div>
    <h1>Zones are here</h1>

    <DynamicComp v-for="(shape, index) in computedThing"
                 :key="index"
                 :shape="shape">
    </DynamicComp>
  </div>
</template>

<style scoped>
</style>

<script setup lang="ts">
import DcButton from "./DcButton.vue"
import DynamicComp from "./DynamicComp.vue";
import Zone from "./Zone.vue";
import {ref, computed} from 'vue'
import {useStore} from 'vuex'

const store = useStore()
const state = store.state


const computedThing = computed(() => store.getters.shapes)

</script>

