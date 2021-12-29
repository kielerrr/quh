<template>
  <div v-show="display">
    <button class="btn">
      {{ label }}
    </button>
  </div>
</template>

<script>
import { getCurrentInstance, onMounted, reactive, toRefs } from "vue";
import store from "./store";
export default {
  props: {
    id: String,
    label: {
      type: String,
      default: "Default",
    },
  },
  setup(props) {
    let state = reactive({
      display: true,
    });
    useBase(props);
    const methods = useMethods(state);
    return {
      ...methods,
      ...toRefs(state),
    };
  },
};
// getCurrentInstance accessible on a composable function
// But it should be called inside setup function
const useBase = function (props) {
  onMounted(() => {
    let instance = getCurrentInstance();
    // Component instance stored in a global store.
    store.setInstance(props.id, instance.proxy);
  });
};
const useMethods = function (state) {
  const hide = () => {
    state.display = false;
  };
  const show = () => {
    state.display = true;
  };
  return {
    hide,
    show,
  };
};
</script>

<style scoped>
.btn {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>