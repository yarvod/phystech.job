<template>
    <div>
    <treeselect
        :options="options"
        v-model="selected"
        :normalizer="normalizer"
      />
    </div>

</template>

<script>
import Treeselect from '@riophae/vue-treeselect';
import '@riophae/vue-treeselect/dist/vue-treeselect.css';
export default {
  name: "CategorySelect",
  components: { Treeselect },
  props: [
    'options',
    'value'
  ],
  data () {
    return {
    }
  },
  computed: {
    selected: {
      set: function (v) {
        let serialized_value = null;
        if (typeof v === "string") {
          serialized_value = v
        }
        else if (typeof v === "object") {
          serialized_value = v.id
        }
        this.$emit('set_category', serialized_value)
      },
      get: function () {
        return this.value
      }
    }
  },
  methods: {
    normalizer(node) {
      let new_node = node
      if (new_node.hasOwnProperty('children')) {
        if (new_node.children.length == 0) {
          delete new_node.children
        }
      }
      return new_node
    }
  }
}

</script>