export default function cleanSet(set, startSting) {
  const result = [];

  for (const i of set) {
    if (i.startsWith(startSting)) {
      result.push(i.slice(startSting.length));
    }
  }
  return result.join('-');
}
