import React, { Fragment, useEffect } from "react";
import { connect } from "react-redux";

import {
  GlobalStyle,
  AppWrapper,
  Error,
  CurrencyConverter,
  CurrencyInfo,
  Input,
  Loading,
} from "../styles";

import { Select } from "../Select.jsx";

import {
  getRate,
  fromChangeInput,
  toChangeInput,
  fromCurrencyChange,
  toCurrencyChange
} from "../../store/actions/currencyActions";

import currencyExchangeList from "../../consts/CurrencyCodes";
import { displayCurrency } from "../../utils/currencyUtils";

function Currency({
  error,
  isFetched,
  from,
  to,
  convertFrom,
  convertTo,
  fromChangeInput,
  fromCurrencyChange,
  toChangeInput,
  toCurrencyChange,
  getRate
}) {
  useEffect(() => {
    getRate(convertFrom, convertTo);
  }, []);

  const currencyList = Object.values(currencyExchangeList);
  return (
    <Fragment>
      <GlobalStyle />
      {error && <Error>{error.message}</Error>}
      {!isFetched && !error && <Loading>Loading...</Loading>}
      {isFetched && (
        <AppWrapper>
          <CurrencyInfo>
            <p>
              {displayCurrency({
                currencyList,
                currencyId: convertFrom,
                number: from
              })}{" "}
              equals{" "}
            </p>
            <h4>
              {displayCurrency({
                currencyList,
                currencyId: convertTo,
                number: to
              })}
            </h4>
          </CurrencyInfo>

          <CurrencyConverter>
            <Input
              type="number"
              value={from}
              onChange={e => fromChangeInput(e.target.value)}
            />

            <Select
              value={convertFrom}
              onChange={e => fromCurrencyChange(e.target.value)}
              currencyList={currencyList}
            />
          </CurrencyConverter>
          <CurrencyConverter>
            <Input
              type="number"
              value={to}
              onChange={e => toChangeInput(e.target.value)}
            />

            <Select
              value={convertTo}
              onChange={e => toCurrencyChange(e.target.value)}
              currencyList={currencyList}
            />
          </CurrencyConverter>
        </AppWrapper>
      )}
    </Fragment>
  );
}

const mapStateToProps = ({ currency }) => ({
  currency: currency.data,
  error: currency.error,
  isFetched: currency.isFetched,
  from: currency.from,
  to: currency.to,
  convertFrom: currency.convertFrom,
  convertTo: currency.convertTo,
  toChangeInput: currency.toChangeInput,
  fromChangeInput: currency.fromChangeInput,
  fromCurrencyChange: currency.fromCurrencyChange,
  toCurrencyChange: currency.toCurrencyChange,
  getRate: currency.getRate
});

const mapDispatchToProps = dispatch => ({
  getRate: (fromCurrency, toCurrency) => {
    dispatch(getRate(fromCurrency, toCurrency));
  },
  toChangeInput: value => {
    dispatch(toChangeInput(value));
  },
  fromChangeInput: value => {
    dispatch(fromChangeInput(value));
  },
  fromCurrencyChange: payload => {
    dispatch(fromCurrencyChange(payload));
  },
  toCurrencyChange: payload => {
    dispatch(toCurrencyChange(payload));
  }
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Currency);
