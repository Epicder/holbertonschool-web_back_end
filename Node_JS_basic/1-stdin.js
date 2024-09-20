process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}`);
});
process.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
