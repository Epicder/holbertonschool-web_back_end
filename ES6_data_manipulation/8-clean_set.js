export default function cleanSet(set, startString) {
  if (startString.length === 0 || (typeof startString !== 'string')) {
    return '';
  }
  const result = [];
  for (const i of set) {
    if (i.startsWith(startString)) {
      result.push(i.slice(startString.length));
    }
  }
  return result.join('-');
}
