export default function uploadPhoto(fileName) {
  return new Promise((_, reject) => {
    reject(new Error(`${fileName} cannot be processed`));
  });
}
