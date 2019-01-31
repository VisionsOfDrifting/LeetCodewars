module.exports = {
  env: {
    es6: true,
    browser: true
  },
  extends: 'airbnb',
  rules: {
    'no-console': 0,
    'no-unused-vars': 1,
    'arrow-parens': ['error', 'as-needed'],
    'comma-dangle': ['error', 'never']
  }
};
