export default class Currency {
    constructor(code, name) {
        this.code = code;
        this.name = name;
    } 
  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(code) {
    if (typeof code === 'string') {
      this._code = code;
    }
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    }
  }

  displayFullCurrency(name, code) {
    return `${name} (${code})`;
  }
}
