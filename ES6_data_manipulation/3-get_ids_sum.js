export default function getStudentIdsSum(students) {
  const initialValue = 0;
  return students.reduce((acc, student) => acc + student.id, initialValue);
}
