<template>
  <div>
    <b-form-group label="Tagged input using dropdown" label-for="tags-with-dropdown">
      <b-form-tags id="tags-with-dropdown" v-model="value" no-outer-focus class="mb-2">
        <template v-slot="{tagVariant}">
          <ul v-if="value.length > 0" class="list-inline d-inline-block mb-2">
            <li v-for="tag in value" :key="tag" class="list-inline-item">
              <b-form-tag
                @remove="removeTag(tag)"
                :title="tag"
                :variant="tagVariant"
                class=""
              >
                <strong> {{ tag }} </strong>
              </b-form-tag>
            </li>
          </ul>

          <b-dropdown size="sm" variant="outline-secondary" block menu-class="w-100">
            <template #button-content>
              <b-icon icon="tag-fill"></b-icon> Choose tags
            </template>
            <b-dropdown-form @submit.stop.prevent="() => {}">
              <b-form-group
                label="Search tags"
                label-for="tag-search-input"
                label-cols-md="auto"
                class="mb-0"
                label-size="sm"
                :description="searchDesc"
              >
                <b-form-input
                  v-model="search"
                  id="tag-search-input"
                  type="search"
                  size="sm"
                  autocomplete="off"
                 ></b-form-input>
              </b-form-group>
            </b-dropdown-form>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item-button
              v-for="option in availableOptions"
              :key="option"
              @click="onOptionClick(option)"
            >
              {{ option }}
            </b-dropdown-item-button>
            <b-dropdown-text v-if="availableOptions.length === 0">
              There are no tags available to select
            </b-dropdown-text>
          </b-dropdown>
        </template>
      </b-form-tags>
    </b-form-group>
  </div>
</template>

<script>
export default {
  name: "TagMultiSelect",
  props: {
    options: Array,
    value: Array
  },
  data() {
    return {
      search: ''
    }
  },
  computed: {
    criteria() {
      // Compute the search criteria
      return this.search.toLowerCase()
    },
    availableOptions() {
      const criteria = this.criteria
      if (criteria) {
        // Show only options that match criteria
        return this.options.filter(opt => opt.toLowerCase().indexOf(criteria) > -1);
      }
      // Show all options available
      return this.options.slice(0,4)
    },
    searchDesc() {
      if (this.criteria && this.availableOptions.length === 0) {
        return 'There are no tags matching your search criteria'
      }
      return ''
    }
  },
  methods: {
    onOptionClick(option) {
      this.addTag(option)
      this.search = ''
    },
    addTag (tag) {
      this.value.push(tag)
    },
    removeTag (tag) {
      const ind = this.value.findIndex(item => item === tag)
      this.value.splice(ind, 1)
    }
  }
}
</script>

<style scoped>

</style>