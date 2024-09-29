const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    const studentsByField = {};
    let totalStudents = 0;

    lines.slice(1).forEach((line) => {
      const [firstname, lastname, age, field] = line.split(',');
      if (!firstname || !lastname || !age || !field) {
        return;
      }

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }

      studentsByField[field].push(firstname);
      totalStudents += 1;
    });

    console.log(`Number of students: ${totalStudents}`);

    for (const [field, students] of Object.entries(studentsByField)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }

  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
