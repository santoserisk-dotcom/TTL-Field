export interface TechnicianStatus {
  technicianId: number;
  name: string;
  online: boolean;
  latitude: number;
  longitude: number;
  speedKmh: number;
  batteryLevel: number;
  updatedAt: string;
}
