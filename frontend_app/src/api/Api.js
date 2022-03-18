import axios from 'axios'
import {backendAPIURL} from '@/config'

export default() => {
  return axios.create({
    baseURL: backendAPIURL,
    withCredentials: false,
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  })
}