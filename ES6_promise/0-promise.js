export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        status: 200,
        
      });
    }, 2000);
  });
}
