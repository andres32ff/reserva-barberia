import json
from pathlib import Path


class GestorReservas:
    def __init__(self, archivo="data/reservas.json"):
        self.archivo = Path(archivo)
        self.archivo.parent.mkdir(parents=True, exist_ok=True)
        if not self.archivo.exists():
            self.archivo.write_text("[]", encoding="utf-8")

    def _leer(self):
        return json.loads(self.archivo.read_text(encoding="utf-8"))

    def _guardar(self, datos):
        self.archivo.write_text(
            json.dumps(datos, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    def crear_reserva(self, cliente, fecha, servicio):
        reservas = self._leer()
        reservas.append({
            "cliente": cliente,
            "fecha": fecha,
            "servicio": servicio
        })
        self._guardar(reservas)

    def listar_reservas(self):
        return self._leer()