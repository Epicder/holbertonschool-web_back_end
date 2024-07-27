export default function hasValuesFromArray(set, array) {
 for (i = 0; i <= set.length; i++) {
   if (set[i] === array[i]) {
     return true;
   }
 }
 return false;
}
