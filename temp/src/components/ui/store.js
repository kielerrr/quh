
const store = {}

/**
 * A Global Store for component instances
 * Note that id should be unique
 */
export default {
    setInstance(id,proxy){
        store[id] = proxy;
    },
    getInstance(id){
        return store[id];
    }
}