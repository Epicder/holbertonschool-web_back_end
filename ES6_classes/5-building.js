class Building {
  constructor(sqft) {
      if (this.constructor === Building) {
          throw new Error('');
      }
      this._sqft = sqft;
  }

  get sqft() {
    return this._sqft
  }

  set sqft(sqft) {
    if (typeof sqft === 'number') {
      this._sqft = sqft
    }
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
