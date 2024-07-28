export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('Ok');
    }, 2000);
  });
}
