import React from "react";
import { Provider } from "react-redux";
import store from "./store";
import Currency from "./components/containers/Currency.jsx";

const App = () => (
  <Provider store={store}>
    <Currency />
  </Provider>
);

export default App;
