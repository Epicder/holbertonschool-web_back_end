export default function cleanSet(set, startSting) {
  const result = [];

  for (const i of set) {
    if (i.startsWith(startSting)) {
      result.push(i);
    }
  }
  return result.join('-');
}
