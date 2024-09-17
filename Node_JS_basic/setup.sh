#!/bin/bash

# Create the CSV file
cat <<EOL > database.csv
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
EOL

echo "Created database.csv"

# Create the package.json file
cat <<EOL > package.json
{
  "name": "node_js_basics",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
    "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "lint": "*",
    "eslint": "^6.8.0",
    "eslint-config-airbnb-base": "^14.2.1",
    "eslint-plugin-import": "^2.29.1",
    "eslint-plugin-jest": "^22.21.0",
    "nodemon": "^2.0.22",
    "chai": "^4.4.1",
    "mocha": "^6.2.3",
    "request": "^2.88.2",
    "sinon": "^7.5.0"
  }
}
EOL

echo "Created package.json"

# Create the babel.config.js file
cat <<EOL > babel.config.js
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
EOL

echo "Created babel.config.js"

# Create the .eslintrc.js file
cat <<EOL > .eslintrc.js
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides: [
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
EOL

echo "Created .eslintrc.js"

# Install the required node modules
echo "Installing npm packages..."
npm install

echo "Setup complete!"
