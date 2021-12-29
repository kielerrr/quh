<template>
  <button class="btn">
    {{ label }}
  </button>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: "Default",
    },
  },
  setup() {
    return {};
  },
};
</script>

<style scoped>
.btn {
  background-color: #4999f5;
  border: none;
  color: white;
  padding: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 2px 2px;
  cursor: pointer;
}
.btn:hover {
  background-color: #0417c0;
  color: white;
}
</style>
