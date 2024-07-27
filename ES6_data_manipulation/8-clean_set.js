export default function cleanSet(set, startSting) {
  if (startSting.length === 0 || (typeof startSting !== 'string')) {
    return '';
  }
  const result = [];
  for (const i of set) {
    if (i.startsWith(startSting)) {
      result.push(i.slice(startSting.length));
    }
  }
  return result.join('-');
}
