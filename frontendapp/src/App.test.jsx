import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import configureStore from 'redux-mock-store';
import {Input} from "./components/styles";

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});



const mockStore = configureStore([]);
describe('My Connected React-Redux Component', () => {
  
  let store;
  beforeEach(() => {
	store = mockStore({
    	currency: {
		    data: {},
		    error: "",
		    to: 0,
		    from: 0,
		    convertFrom: "EUR",
		    convertTo: "USD",
		    isFetched: false
  		}
    });
  });

  store.dispatch = jest.fn();

  component = renderer.create(
    <Provider store={store}>
    	<Currency />
  	</Provider>
  );
  
  it('should render with given state from Redux store', () => {
    expect(component.toJSON()).toMatchSnapshot();
  });
  
  it('should dispatch an action on value change', () => {
    renderer.act(() => {
      component.root.findByType(<Input/>).props.onChange();
    });
    expect(store.dispatch).toHaveBeenCalledTimes(1);
    expect(store.dispatch).toHaveBeenCalledWith(
      myAction({ payload: '100' })
    );
  });
});