import state from "./module-example/state"

const { P } = require("vue-eva-icons")

const variables = {

}

const mutations = {

}

const actions = {

}

const getters = {
    tasks: (variables) => {
        return state.tasks
    }

}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters
}