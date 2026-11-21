# ==========================================
# مشروع أمانك | AMANAK
# منظومة ذكية للكشف المبكر عن المخاطر
# ==========================================

class AmanakSystem:

    def __init__(self):
        self.alerts = []
        self.risk_score = 0

    # تحليل بيانات الساعة الذكية
    def smart_watch(self, oxygen, harmful_gas):

        if oxygen < 90:
            self.risk_score += 40
            self.alerts.append(
                "تحذير: انخفاض قراءة الأكسجين، "
                "يرجى طلب تقييم طبي."
            )

        if harmful_gas:
            self.risk_score += 40
            self.alerts.append(
                "تحذير: احتمال وجود أبخرة ضارة! "
                "ابتعد عن المكان واتبع إجراءات السلامة."
            )

    # تحليل بيانات كرسي السيارة
    def smart_car_seat(self, accident, driver_response):

        if accident:
            self.risk_score += 50
            self.alerts.append(
                "تحذير: تم اكتشاف مؤشر حادث مروري!"
            )

        if not driver_response:
            self.risk_score += 30
            self.alerts.append(
                "تحذير: لا توجد استجابة من السائق، "
                "يرجى التحقق من سلامته."
            )

    # تحليل بيانات القفاز الذكي
    def smart_glove(self, skin_injury):

        if skin_injury:
            self.risk_score += 20
            self.alerts.append(
                "تنبيه: توجد مؤشرات إصابة جلدية، "
                "يرجى تقييم الحالة طبيًا."
            )

    # تحليل بيانات الطرق الذكية
    def smart_road(self, road_accident):

        if road_accident:
            self.risk_score += 50
            self.alerts.append(
                "تنبيه: تم رصد مؤشر حادث على الطريق، "
                "يرجى التحقق من الموقع."
            )

    # تحديد مستوى الخطورة
    def calculate_risk(self):

        if self.risk_score >= 70:
            return "🔴 خطر مرتفع"

        elif self.risk_score >= 40:
            return "🟠 خطر متوسط"

        elif self.risk_score > 0:
            return "🟡 خطر منخفض"

        else:
            return "🟢 الوضع آمن حسب البيانات المدخلة"

    # عرض النتائج
    def display_results(self):

        print("\n" + "=" * 40)
        print("       نظام أمانك الذكي")
        print("=" * 40)

        print("\nدرجة الخطورة:", self.risk_score)
        print("مستوى الخطورة:", self.calculate_risk())

        print("\nالتنبيهات:")

        if self.alerts:
            for alert in self.alerts:
                print("⚠️", alert)
        else:
            print("لا توجد تنبيهات.")

        print("\n" + "=" * 40)


# ==========================================
# تشغيل النظام
# ==========================================

amanak = AmanakSystem()

# بيانات الساعة الذكية
amanak.smart_watch(
    oxygen=96,
    harmful_gas=False
)

# بيانات كرسي السيارة
amanak.smart_car_seat(
    accident=False,
    driver_response=True
)

# بيانات القفاز الذكي
amanak.smart_glove(
    skin_injury=False
)

# بيانات الطرق الذكية
amanak.smart_road(
    road_accident=False
)

# عرض النتائج
amanak.display_results()