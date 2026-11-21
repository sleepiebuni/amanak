
import streamlit as st
from amanak import AmanakSystem

st.set_page_config(
    page_title="أمانك | AMANAK",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 منظومة أمانك الذكية")
st.write("منظومة ذكية للكشف المبكر عن المخاطر")
st.info("نموذج تجريبي يعتمد على البيانات المدخلة يدويًا.")

st.header("⌚ الساعة الذكية")
oxygen = st.slider("نسبة الأكسجين المقروءة", 0, 100, 96)
harmful_gas = st.checkbox("هل توجد مؤشرات غازات ضارة؟")

st.header("🚗 كرسي السيارة الذكي")
accident = st.checkbox("هل تم رصد حادث؟")
driver_response = st.checkbox(
    "هل السائق مستجيب؟",
    value=True
)

st.header("🧤 القفاز الذكي")
skin_injury = st.checkbox("هل توجد مؤشرات إصابة جلدية؟")

st.header("🛣️ الطرق الذكية")
road_accident = st.checkbox("هل تم رصد حادث على الطريق؟")

if st.button("🔍 تحليل جميع البيانات", type="primary"):

    amanak = AmanakSystem()

    amanak.smart_watch(oxygen, harmful_gas)
    amanak.smart_car_seat(accident, driver_response)
    amanak.smart_glove(skin_injury)
    amanak.smart_road(road_accident)

    st.subheader("📊 نتائج التحليل")
    st.metric("درجة الخطورة", amanak.risk_score)
    st.write("مستوى الخطورة:", amanak.calculate_risk())

    st.subheader("🚨 التنبيهات")

    if amanak.alerts:
        for alert in amanak.alerts:
            st.warning(alert)
    else:
        st.success("لا توجد تنبيهات حسب البيانات المدخلة.")

st.caption(
    "هذا نموذج توعوي تجريبي، وليس جهاز كشف معتمدًا "
    "أو بديلًا عن خدمات الطوارئ والتقييم الطبي."
)
