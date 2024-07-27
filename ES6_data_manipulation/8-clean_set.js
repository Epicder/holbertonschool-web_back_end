export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
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
