export default function cleanSet(set, startSting) {
  const result = [];
  if (startSting.length === 0 || startSting !== (typeof 'string')) {
    return '';
  }
  
  for (const i of set) {
    if (i.startsWith(startSting)) {
      result.push(i.slice(startSting.length));
    }
  }
  return result.join('-');
}
