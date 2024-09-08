import { configureStore } from '@reduxjs/toolkit';

const initialState = {
  urls: [],
};

function urlReducer(state = initialState, action) {
  switch (action.type) {
    case 'ADD_URL':
      return { ...state, urls: [...state.urls, action.payload] };
    default:
      return state;
  }
}

const store = configureStore({
  reducer: urlReducer,
});

export default store;
