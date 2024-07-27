export default function createInt8TypedArray(length, position, value) {
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const int8Array = new Int8Array(buffer);
  int8Array[position] = value;
  return buffer;
}
