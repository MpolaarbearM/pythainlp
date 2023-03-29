# -*- coding: utf-8 -*-
import core
kv = core.KhaveeVerifier()


# การเช็คสระ
print('เริง',kv.check_sara('เริง'))
# 'เออ'

# การเช็คมาตราตัวสะกด
print('สาว',kv.check_marttra('สาว'))
# 'เกอว'

# การตรวจสอบคำสำผัสที่ถูกต้อง
print('สรร อัน',kv.check_sumpus('สรร','อัน'))
# True

# การตรวจสอบคำสำผัสที่ผิด
print('สรร อัน',kv.check_sumpus('หมัน','อัน'))
# False

# การตรวจสอบกลอน 8 ที่ถูกฉันทลักษณ์
print(kv.check_klon('''ณรงค์วุฒิผู้เปี่ยมวุฒิสมสง่า มากวิชาหาความรู้ไปสู่ผล 
เรื่องฟิสิกส์คณิตศาสตร์เอิร์นอดทน เล่นเกมเก่งลำดับต้นของโรงเรียน
ต่อมาหยกธนัชพรชอบนอนหลับ แต่ผลลัพธ์คือฉลาดเรื่องอ่านเขียน 
เหมือนจะเล่นแต่เขายังพากเพียร ในการเรียนการเล่นบ้างคละกันไป
นรภัทรพุกกะมานป่านจอมแก่น ทั่วแว่นแคว้นโดนเขาแกล้งไม่สงสัย
เรื่องวิศวะเก่งกาจประหลาดใจ เรื่องฟิสิกส์ไร้ผู้ใดมาต่อกร
นริศราอีฟเก่งกว่าใครเพื่อน คอยช่วยเตือนเรื่องงานคอยสั่งสอน
อ่านตำราหาความรู้ไม่ละทอน เป็นคนดีศรีนครของจิตรลดา
ภัสนันท์นาคลออหรือมีมี่ เรื่องเกมนี้เก่งกาจไม่กังขา 
เกมอะไรก็เล่นได้ไม่ลดวา สุดฉลาดมากปัญญามาครบครัน''',k_type=8))
# -> The poem is correct according to the principle.

# การตรวจสอบกลอน 8 ที่ผิดฉันทลักษณ์
print(kv.check_klon('''ณรงค์วุฒิผู้เปี่ยมวุฒิสมสง่า มากวิชาหาความรู้ไปสู่ผล 
เรื่องฟิสิกส์คณิตศาสตร์เอิร์นอดทน เล่นเกมเก่งลำดับต้นของโรงเรียน
ต่อมาหยกธนัชพรชอบนอนหลับ แต่ผลลัพธ์คือฉลาดเรื่องอ่านเขียน 
เหมือนจะเล่นแต่เขายังพากเพียร ในการเรียนการเล่นบ้างคละกันไป
นรภัทรพุกกะมานป่านจอมแก่น ทั่วแว่นแคว้นโดนเขาแกล้งไม่สงสัย
เรื่องวิศวะเก่งกาจประหลาดใจ เรื่องฟิสิกส์ไร้ผู้ใดมาต่อไป
นริศราอีฟเก่งกว่าใครเพื่อน คอยช่วยเตือนเรื่องงานคอยสั่งสอน
อ่านตำราหาความรู้ไม่ละทอน เป็นคนดีศรีนครของจิตรลดา
ภัสนันท์นาคลออหรือมีมี่ เรื่องเกมเอ่อเก่งกาจไม่กังขา 
เกมอะไรก็เล่นได้ไม่ลดวา สุดฉลาดมากปัญญามาครบครัน''',k_type=8))
# -> ["Cant find rhyme between paragraphs ('สอน', 'ไป')in paragraph 4", "Cant find rhyme between paragraphs ('มี่', ['เกม', 'เอ่อ', 'เก่ง', 'กาจ'])in paragraph 5"]


# การตรวจสอบกลอน 4 ที่ถูกฉันทลักษณ์
print(kv.check_klon('''ฉันชื่อหมูกรอบ ฉันชอบกินไก่ แล้วก็วิ่งไล่ หมาชื่อนํ้าทอง ลคคนเก่ง เอ๋งเอ๋งคะนอง มีคนจับจอง เขาชื่อน้องเธียร''',k_type=4))
# -> The poem is correct according to the principle.

# การตรวจสอบกลอน 4 ที่ผิดฉันทลักษณ์
print(kv.check_klon('''ฉันชื่อหมูกรอบ ฉันชอบกินไก่ แล้วก็วิ่งไล่ หมาชื่อนํ้าทอง ลคคนเก่ง เอ๋งเอ๋งเสียงหมา มีคนจับจอง เขาชื่อน้องเธียร''',k_type=4))
# -> ["Cant find rhyme between paragraphs ('หมา', 'จอง')in paragraph 2", "Cant find rhyme between paragraphs ('หมา', 'ทอง')in paragraph 2"]

# การเช็คคำเอกโท
print(kv.check_aek_too('เอง'), kv.check_aek_too('เอ่ง'), kv.check_aek_too('เอ้ง'))
# -> False, aek, too
print(kv.check_aek_too(['เอง', 'เอ่ง', 'เอ้ง'])) # ใช้ List ได้เหมือนกัน
# -> [False, 'aek', 'too']
