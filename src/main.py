from src.reservas.gestor import GestorReservas


def main():
    print("🤖 Bot de barbería iniciado")
    gestor = GestorReservas()

    # Prueba rápida
    gestor.crear_reserva("Juan", "2026-09-20 15:00", "corte")
    gestor.crear_reserva("Pedro", "2026-09-20 16:00", "barba")

    print("\n📋 Reservas actuales:")
    for r in gestor.listar_reservas():
        print(f"  - {r['cliente']} | {r['fecha']} | {r['servicio']}")


if __name__ == "__main__":
    main()