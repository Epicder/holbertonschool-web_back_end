export default function getListStudentIds(...args) {
  if (typeof args === Array) {
    return [args.id];
  }
  else {
   return [];
  }
}
