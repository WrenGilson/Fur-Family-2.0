import { API_URL } from "./api.js";

export function getList() {
    return fetch(API_URL)
      .then(data => data.json())
  }