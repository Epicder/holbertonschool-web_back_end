import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const obj = [];
  obj.push(new ClassRoom(19));
  obj.push(new ClassRoom(20));
  obj.push(new ClassRoom(34));
  return obj;
}
