import streamlit as st

st.set_page_config(page_title="Calculadora de Fee", layout="centered")

st.title("💸 Calculadora de Fee")
st.markdown("Calculá el fee correspondiente según el monto de inversión en pauta que querés hacer.")

# Tabla de tramos
tramos = [
    {"min": 0, "max": 400_000, "tipo": "fijo", "valor": 80_000},
    {"min": 400_001, "max": 1_000_000, "tipo": "porcentaje", "valor": 0.18},
    {"min": 1_000_001, "max": 2_000_000, "tipo": "porcentaje", "valor": 0.13},
    {"min": 2_000_001, "max": 3_000_000, "tipo": "porcentaje", "valor": 0.10},
    {"min": 3_000_001, "max": 4_000_000, "tipo": "porcentaje", "valor": 0.08},
    {"min": 4_000_001, "max": 6_000_000, "tipo": "porcentaje", "valor": 0.05},
    {"min": 6_000_001, "max": float("inf"), "tipo": "porcentaje", "valor": 0.01},
]

# Entrada de usuario
monto = st.number_input("¿Cuánto dinero te gustaría invertir?", min_value=0, step=1000, format="%d")

def calcular_fee(monto):
    fee_total = 0
    for tramo in tramos:
        if monto > tramo["min"]:
            monto_en_tramo = min(monto, tramo["max"]) - tramo["min"]
            if tramo["tipo"] == "fijo":
                fee_total += tramo["valor"]
            else:
                fee_total += monto_en_tramo * tramo["valor"]
    return round(fee_total, 2)

# Resultado
if monto > 0:
    fee = calcular_fee(monto)
    porcentaje_aplicado = (fee / monto) * 100
    st.success(f"🧮 El fee total a pagar por una inversión de ARS {monto:,.0f} es: **ARS {fee:,.2f}**")

    st.markdown("---")
    if monto <= 400_000:
        st.caption("💡 El fee mínimo de gestión es de ARS 80.000.")
    else:
        st.info(f"📊 Esto significa que el fee es de **{porcentaje_aplicado:.2f}%**.")
        st.caption("El fee se calcula por tramos: el porcentaje se aplica solo a la parte del monto que cae en cada tramo.")
