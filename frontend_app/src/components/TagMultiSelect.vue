<template>
  <div>
    <label class="typo__label">Тэги:</label>
     <multiselect 
     v-model="selected" 
     placeholder="Type to search" 
     label="title" 
     track-by="title" 
     :options="options" 
     :multiple="true"
     :close-on-select="false"
    >
      <span slot="noResult">
        Не удалось найти тэг :(
      </span>
    </multiselect>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
export default {
  name: "TagMultiSelect",
  props: {
    options: Array,
    value: Array
  },
  components: {
    Multiselect
  },
  data () {
    return {
      
    }
  },
  computed: {
    selected: {
      set: function (v) {
        let serialized_value = v.map(x => x.title)
        this.$emit('set_tags', serialized_value)
      },
      get: function () {
        return this.options.filter(x => this.value.indexOf(x.title) !== -1)
      }
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>