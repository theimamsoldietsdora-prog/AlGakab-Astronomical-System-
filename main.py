# ==============================================================================
# Al-Gakab Astronomical System - Core Engine
# نظام المهندس آل عكاب الفلكي - المحرك الحسابي والتطبيقي
# ==============================================================================

import math

class AlGakabEngine:
    """
    المحرك الرياضي لنظرية المهندس آل عكاب الفلكية
    """
    def __init__(self):
        # ذروة الأوج (21/12) - طول الشهر الأول
        self.M_apex = 29.25
        # ذروة الحضيض (21/6) - طول الشهر السابع
        self.M_perigee = 29.0875
        # التغير الشهري لطول الشهر
        self.delta_M = 0.125
        
        # أسماء الأشهر في تقويم آل عكاب
        self.months_names = [
            "شهر الأوج (ذروة الشتاء)",
            "شهر النزول الأول",
            "شهر النزول الثاني",
            "شهر الاعتدال الهابط",
            "شهر الاقتراب الصيفي",
            "شهر الحضيض (ذروة الصيف)",
            "شهر الصعود الأول",
            "شهر الصعود الثاني",
            "شهر رمضان (الاعتدال الصاعد)",
            "شهر العيد والصعود الثالث",
            "شهر الاقتراب من الأوج",
            "شهر ذروة الثبات"
        ]

    def get_month_duration(self, month_index):
        """
        حساب طول الشهر القمري بناءً على موقعه في عمود السبرنك (1 إلى 12)
        """
        if month_index <= 6:
            # طور الهبوط من الأوج إلى الحضيض
            return self.M_apex - ((month_index - 1) * self.delta_M)
        else:
            # طور الصعود من الحضيض إلى الأوج
            return self.M_perigee + ((month_index - 6) * self.delta_M)

    def calculate_vertical_z(self, day_of_year):
        """
        حساب موقع القمر الرأسي Z على عمود السبرنك (0 = الحضيض، 100 = الأوج)
        """
        angle = (day_of_year / 365.0) * 2 * math.pi
        z_position = 50 + 50 * math.cos(angle)
        return round(z_position, 2)

    def predict_weather_and_season(self, day_of_year):
        """
        التنبؤ الدقيق بالطقس والظواهر المناخية اعتماداً على موضع القمر Z
        """
        z = self.calculate_vertical_z(day_of_year)
        
        if z >= 85:
            season = "ذروة الشتاء (الأوج القمري)"
            weather = "برد قارس، تساقط أمطار غزيرة وثلوج، رياح باردة"
        elif 50 <= z < 85 and day_of_year < 180:
            season = "فصل الربيع والانحراف النازل"
            weather = "أجواء معتدلة، أمطار موسمية خفيفة، هواء عليل"
        elif z < 25:
            season = "ذروة الصيف (الحضيض القمري)"
            weather = "حرارة مرتفعة، استقرار جوي تام، جفاف"
        elif 25 <= z < 50 and day_of_year > 180:
            season = "فصل الخريف والانحراف الصاعد"
            weather = "انخفاض تدريجي بالحرارة، تكثف سحب، بدايات تساقط المطر"
        else:
            season = "فصل انتقالي مداري"
            weather = "طقس متقلب معتدل"
            
        return season, weather, z

    def get_ramadan_and_eids(self):
        """
        تحديد شهر رمضان والأعياد بناءً على تقاطع الاعتدال المداري الصاعد
        """
        ramadan_month = 9  # شهر الاعتدال الصاعد
        eid_fitr_day = "1 من شهر العيد والصعود الثالث (الشهر 10)"
        eid_adha_day = "10 من شهر الأضحى والنسك (الشهر 11)"
        
        return {
            "شهر رمضان": self.months_names[ramadan_month - 1],
            "مدة شهر رمضان": f"{self.get_month_duration(ramadan_month)} يوم",
            "عيد الفطر المبارك": eid_fitr_day,
            "عيد الأضحى المبارك": eid_adha_day
        }

if __name__ == "__main__":
    engine = AlGakabEngine()
    print("=== نظام المهندس آل عكاب الفلكي ===")
    for i in range(1, 13):
        print(f"الشهر {i}: {engine.get_month_duration(i)} يوم")
