<template>
  <component :is=Zone v-bind:shape="props.shape"></component>
</template>
<script setup lang="ts">
import Zone from "./Zone.vue";

const props = defineProps({
  shape: Object,
})

</script>

