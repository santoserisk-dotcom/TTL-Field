import type { TechnicianStatus } from '../types/operations';

const sample: TechnicianStatus = {
  technicianId: 1,
  name: 'Técnico 01',
  online: true,
  latitude: -23.5505,
  longitude: -46.6333,
  speedKmh: 42,
  batteryLevel: 78,
  updatedAt: new Date().toISOString(),
};

export function DashboardPage(): JSX.Element {
  return (
    <main style={{ fontFamily: 'Inter, sans-serif', padding: '1.5rem' }}>
      <h1>TTL Field - NOC Operacional</h1>
      <p>Dashboard web para monitoramento em tempo real (fase inicial).</p>
      <pre>{JSON.stringify(sample, null, 2)}</pre>
    </main>
  );
}
