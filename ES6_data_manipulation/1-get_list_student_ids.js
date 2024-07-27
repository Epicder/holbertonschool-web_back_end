export default function getListStudentIds(args) {
  if (!Array.isArray(args)) {
    return [];
  }
  return args.map((args) => args.id);
}
