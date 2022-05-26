import Api from '@/api/Api'

export default {
  async getBillingPeriods () {
    return await Api().get('/billing_periods/')
  }
}