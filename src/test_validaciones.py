
# ============================================================
# SMARTPAY
# PRUEBAS AUTOMATIZADAS DE VALIDACIONES
# Autora: Linda Ortiz
# ============================================================

import unittest

from validaciones import (
    validar_cuenta,
    validar_credito,
    validar_campos_obligatorios,
    validar_valor_pago,
    validar_valor_operacion
)


class TestValidacionesSmartPay(unittest.TestCase):

    # --------------------------------------------------------
    # 1. PRUEBAS DE NUMERO DE CUENTA
    # --------------------------------------------------------

    def test_cuenta_11_digitos(self):
        self.assertTrue(
            validar_cuenta("12345678901")[0]
        )

    def test_cuenta_10_digitos(self):
        self.assertFalse(
            validar_cuenta("1234567890")[0]
        )

    def test_cuenta_12_digitos(self):
        self.assertFalse(
            validar_cuenta("123456789012")[0]
        )

    def test_cuenta_con_letras(self):
        self.assertFalse(
            validar_cuenta("12345678ABC")[0]
        )

    def test_cuenta_vacia(self):
        self.assertFalse(
            validar_cuenta("")[0]
        )

    # --------------------------------------------------------
    # 2. PRUEBAS DE NUMERO DE CREDITO
    # --------------------------------------------------------

    def test_credito_11_digitos(self):
        self.assertTrue(
            validar_credito("98765432101")[0]
        )

    def test_credito_10_digitos(self):
        self.assertFalse(
            validar_credito("9876543210")[0]
        )

    def test_credito_12_digitos(self):
        self.assertFalse(
            validar_credito("987654321012")[0]
        )

    def test_credito_con_letras(self):
        self.assertFalse(
            validar_credito("98765432ABC")[0]
        )

    # --------------------------------------------------------
    # 3. PRUEBAS DE CAMPOS OBLIGATORIOS
    # --------------------------------------------------------

    def test_campos_completos(self):

        datos = {
            "nit": "900123456",
            "nombre_cliente": "Cliente Ficticio",
            "numero_cuenta": "12345678901",
            "tipo_cuenta": "Ahorros",
            "numero_credito": "98765432101",
            "tipo_operacion": "Pago de cuota",
            "valor_pago": "490000"
        }

        self.assertEqual(
            validar_campos_obligatorios(datos),
            []
        )

    def test_campo_obligatorio_vacio(self):

        datos = {
            "nit": "",
            "nombre_cliente": "Cliente Ficticio",
            "numero_cuenta": "12345678901",
            "tipo_cuenta": "Ahorros",
            "numero_credito": "98765432101",
            "tipo_operacion": "Pago de cuota",
            "valor_pago": "490000"
        }

        self.assertGreater(
            len(validar_campos_obligatorios(datos)),
            0
        )

    # --------------------------------------------------------
    # 4. PRUEBAS DEL VALOR DEL PAGO
    # --------------------------------------------------------

    def test_pago_positivo(self):
        self.assertTrue(
            validar_valor_pago("100000")[0]
        )

    def test_pago_cero(self):
        self.assertFalse(
            validar_valor_pago("0")[0]
        )

    def test_pago_negativo(self):
        self.assertFalse(
            validar_valor_pago("-100")[0]
        )

    def test_pago_no_numerico(self):
        self.assertFalse(
            validar_valor_pago("ABC")[0]
        )

    # --------------------------------------------------------
    # 5. PRUEBAS DE LAS CUATRO OPERACIONES
    # --------------------------------------------------------

    def test_pago_cuota_correcto(self):

        self.assertTrue(
            validar_valor_operacion(
                "Pago de cuota",
                490000,
                cuota_pendiente=490000
            )[0]
        )

    def test_pago_cuota_incorrecto(self):

        self.assertFalse(
            validar_valor_operacion(
                "Pago de cuota",
                450000,
                cuota_pendiente=490000
            )[0]
        )

    def test_abono_capital_correcto(self):

        self.assertTrue(
            validar_valor_operacion(
                "Abono a capital",
                300000,
                capital_pendiente=1000000
            )[0]
        )

    def test_abono_capital_superior(self):

        self.assertFalse(
            validar_valor_operacion(
                "Abono a capital",
                1200000,
                capital_pendiente=1000000
            )[0]
        )

    def test_abono_intereses_correcto(self):

        self.assertTrue(
            validar_valor_operacion(
                "Abono a intereses",
                100000,
                intereses_pendientes=250000
            )[0]
        )

    def test_abono_intereses_superior(self):

        self.assertFalse(
            validar_valor_operacion(
                "Abono a intereses",
                300000,
                intereses_pendientes=250000
            )[0]
        )

    def test_pago_total_correcto(self):

        self.assertTrue(
            validar_valor_operacion(
                "Pago total",
                4500000,
                valor_liquidacion=4500000
            )[0]
        )

    def test_pago_total_incorrecto(self):

        self.assertFalse(
            validar_valor_operacion(
                "Pago total",
                4000000,
                valor_liquidacion=4500000
            )[0]
        )

    def test_operacion_no_reconocida(self):

        self.assertFalse(
            validar_valor_operacion(
                "Operacion desconocida",
                100000
            )[0]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
