export default function getListStudentIds(...args) {
  if (typeof args === Array) {
    return args.map((arg) => arg.id);
  }
  else {
   return [];
  }
}
