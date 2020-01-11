EESchema Schematic File Version 4
LIBS:Marantec-cache
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R R5
U 1 1 5DAAFF69
P 3900 2550
F 0 "R5" V 3693 2550 50  0000 C CNN
F 1 "2.2k" V 3784 2550 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3830 2550 50  0001 C CNN
F 3 "~" H 3900 2550 50  0001 C CNN
	1    3900 2550
	0    1    1    0   
$EndComp
$Comp
L Transistor_BJT:BC547 Q1
U 1 1 5DAB19B4
P 4200 3000
F 0 "Q1" H 4391 3046 50  0000 L CNN
F 1 "BC547" H 4391 2955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4400 2925 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 4200 3000 50  0001 L CNN
	1    4200 3000
	1    0    0    -1  
$EndComp
$Comp
L Connector:RJ12 J1
U 1 1 5DAB2609
P 1700 2800
F 0 "J1" H 1757 3367 50  0000 C CNN
F 1 "RJ12" H 1757 3276 50  0000 C CNN
F 2 "Connector_RJ:RJ12_Amphenol_54601" V 1700 2825 50  0001 C CNN
F 3 "~" V 1700 2825 50  0001 C CNN
	1    1700 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 2900 2900 2900
Wire Wire Line
	3400 2900 3400 2550
Wire Wire Line
	3400 2550 3750 2550
$Comp
L Isolator:LTV-847M U1
U 1 1 5DABDD89
P 4850 2650
F 0 "U1" H 4850 2975 50  0000 C CNN
F 1 "LTV-847M" H 4850 2884 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 2350 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 3050 50  0001 C CNN
	1    4850 2650
	1    0    0    -1  
$EndComp
$Comp
L Isolator:LTV-847M U1
U 2 1 5DABF053
P 4850 3400
F 0 "U1" H 4850 3725 50  0000 C CNN
F 1 "LTV-847M" H 4850 3634 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 3100 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 3800 50  0001 C CNN
	2    4850 3400
	-1   0    0    -1  
$EndComp
$Comp
L Isolator:LTV-847M U1
U 3 1 5DABFD07
P 4850 4100
F 0 "U1" H 4850 4425 50  0000 C CNN
F 1 "LTV-847M" H 4850 4334 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 3800 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 4500 50  0001 C CNN
	3    4850 4100
	1    0    0    -1  
$EndComp
$Comp
L Isolator:LTV-847M U1
U 4 1 5DAC0BDD
P 4850 4900
F 0 "U1" H 4850 5225 50  0000 C CNN
F 1 "LTV-847M" H 4850 5134 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 4600 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 5300 50  0001 C CNN
	4    4850 4900
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4050 2550 4550 2550
Wire Wire Line
	4550 2750 4300 2750
$Comp
L Device:R R1
U 1 1 5DAC7D16
P 3550 3000
F 0 "R1" V 3343 3000 50  0000 C CNN
F 1 "210k" V 3434 3000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3480 3000 50  0001 C CNN
F 3 "~" H 3550 3000 50  0001 C CNN
	1    3550 3000
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 5DAC851B
P 3800 3500
F 0 "R3" H 3730 3454 50  0000 R CNN
F 1 "20k" H 3730 3545 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3730 3500 50  0001 C CNN
F 3 "~" H 3800 3500 50  0001 C CNN
	1    3800 3500
	-1   0    0    1   
$EndComp
$Comp
L Device:CP C1
U 1 1 5DACABDC
P 4000 3500
F 0 "C1" H 4118 3546 50  0000 L CNN
F 1 "1uF" H 4118 3455 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D5.0mm_P2.00mm" H 4038 3350 50  0001 C CNN
F 3 "~" H 4000 3500 50  0001 C CNN
	1    4000 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 2750 4300 2800
Wire Wire Line
	4000 3000 3800 3000
Wire Wire Line
	3400 3300 3400 3000
Wire Wire Line
	3800 3350 3800 3000
Connection ~ 3800 3000
Wire Wire Line
	3800 3000 3700 3000
Wire Wire Line
	4000 3350 4000 3000
Wire Wire Line
	3400 3300 4550 3300
Connection ~ 4000 3000
Wire Wire Line
	4300 3200 4300 3700
Wire Wire Line
	4300 3700 4000 3700
Wire Wire Line
	3800 3700 3800 3650
Wire Wire Line
	4000 3650 4000 3700
Connection ~ 4000 3700
Wire Wire Line
	4000 3700 3800 3700
Wire Wire Line
	4550 3500 4500 3500
Wire Wire Line
	4500 3500 4500 3700
Wire Wire Line
	4500 3700 4300 3700
Connection ~ 4300 3700
Wire Wire Line
	2100 2800 2500 2800
Wire Wire Line
	2500 3700 3800 3700
Connection ~ 3800 3700
Wire Wire Line
	2100 2500 2600 2500
Wire Wire Line
	2600 2500 2600 3000
Wire Wire Line
	2600 3000 3400 3000
Connection ~ 3400 3000
$Comp
L Device:R R6
U 1 1 5DADE3BF
P 3950 4000
F 0 "R6" V 3743 4000 50  0000 C CNN
F 1 "2.2k" V 3834 4000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3880 4000 50  0001 C CNN
F 3 "~" H 3950 4000 50  0001 C CNN
	1    3950 4000
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 5DADEB2F
P 3550 4500
F 0 "R2" V 3343 4500 50  0000 C CNN
F 1 "210k" V 3434 4500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3480 4500 50  0001 C CNN
F 3 "~" H 3550 4500 50  0001 C CNN
	1    3550 4500
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5DADF54F
P 3800 5000
F 0 "R4" H 3730 4954 50  0000 R CNN
F 1 "20k" H 3730 5045 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3730 5000 50  0001 C CNN
F 3 "~" H 3800 5000 50  0001 C CNN
	1    3800 5000
	-1   0    0    1   
$EndComp
$Comp
L Device:CP C2
U 1 1 5DADFA2B
P 4000 5000
F 0 "C2" H 4118 5046 50  0000 L CNN
F 1 "1uF" H 4118 4955 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D5.0mm_P2.00mm" H 4038 4850 50  0001 C CNN
F 3 "~" H 4000 5000 50  0001 C CNN
	1    4000 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 4000 4100 4000
Wire Wire Line
	3800 4000 3300 4000
Wire Wire Line
	3300 4000 3300 2900
Connection ~ 3300 2900
Wire Wire Line
	3300 2900 3400 2900
$Comp
L Transistor_BJT:BC547 Q2
U 1 1 5DAE7CB2
P 4200 4500
F 0 "Q2" H 4391 4546 50  0000 L CNN
F 1 "BC547" H 4391 4455 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4400 4425 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 4200 4500 50  0001 L CNN
	1    4200 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 4200 4300 4200
Wire Wire Line
	4300 4200 4300 4300
Wire Wire Line
	4000 4500 3800 4500
Wire Wire Line
	4550 4800 3400 4800
Wire Wire Line
	3400 4800 3400 4500
Wire Wire Line
	4000 4850 4000 4500
Connection ~ 4000 4500
Wire Wire Line
	3800 4850 3800 4500
Connection ~ 3800 4500
Wire Wire Line
	3800 4500 3700 4500
Wire Wire Line
	4550 5000 4500 5000
Wire Wire Line
	4500 5000 4500 5200
Wire Wire Line
	4500 5200 4300 5200
Wire Wire Line
	4000 5200 4000 5150
Wire Wire Line
	4000 5200 3800 5200
Wire Wire Line
	3800 5200 3800 5150
Connection ~ 4000 5200
Connection ~ 3800 5200
Wire Wire Line
	4300 4700 4300 5200
Connection ~ 4300 5200
Wire Wire Line
	4300 5200 4000 5200
Wire Wire Line
	2100 2700 2700 2700
Wire Wire Line
	2700 2700 2700 4500
Wire Wire Line
	2700 4500 3400 4500
Connection ~ 3400 4500
$Comp
L Isolator:LTV-847M U2
U 1 1 5DAF710A
P 4850 5450
F 0 "U2" H 4850 5775 50  0000 C CNN
F 1 "LTV-847M" H 4850 5684 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 5150 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 5850 50  0001 C CNN
	1    4850 5450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2100 2600 2800 2600
Wire Wire Line
	2400 3000 2400 5350
$Comp
L Device:R R11
U 1 1 5DB0BB58
P 5550 2550
F 0 "R11" V 5343 2550 50  0000 C CNN
F 1 "330" V 5434 2550 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 2550 50  0001 C CNN
F 3 "~" H 5550 2550 50  0001 C CNN
	1    5550 2550
	0    1    1    0   
$EndComp
$Comp
L Device:R R12
U 1 1 5DB0C456
P 5550 3300
F 0 "R12" V 5343 3300 50  0000 C CNN
F 1 "330" V 5434 3300 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 3300 50  0001 C CNN
F 3 "~" H 5550 3300 50  0001 C CNN
	1    5550 3300
	0    1    1    0   
$EndComp
$Comp
L Device:R R13
U 1 1 5DB0CA4C
P 5550 4000
F 0 "R13" V 5343 4000 50  0000 C CNN
F 1 "330" V 5434 4000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 4000 50  0001 C CNN
F 3 "~" H 5550 4000 50  0001 C CNN
	1    5550 4000
	0    1    1    0   
$EndComp
$Comp
L Device:R R14
U 1 1 5DB0D07E
P 5550 4800
F 0 "R14" V 5343 4800 50  0000 C CNN
F 1 "330k" V 5434 4800 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 4800 50  0001 C CNN
F 3 "~" H 5550 4800 50  0001 C CNN
	1    5550 4800
	0    1    1    0   
$EndComp
Wire Wire Line
	5800 3300 5700 3300
Wire Wire Line
	5900 4000 5700 4000
Wire Wire Line
	6000 4800 5700 4800
$Comp
L Device:R R15
U 1 1 5DB1C840
P 5550 5350
F 0 "R15" V 5343 5350 50  0000 C CNN
F 1 "330" V 5434 5350 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 5350 50  0001 C CNN
F 3 "~" H 5550 5350 50  0001 C CNN
	1    5550 5350
	0    1    1    0   
$EndComp
$Comp
L Device:R R16
U 1 1 5DB1D0F0
P 6050 6000
F 0 "R16" V 5843 6000 50  0000 C CNN
F 1 "330" V 5934 6000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5980 6000 50  0001 C CNN
F 3 "~" H 6050 6000 50  0001 C CNN
	1    6050 6000
	0    1    1    0   
$EndComp
Wire Wire Line
	6100 5350 5700 5350
Wire Wire Line
	5150 2750 5200 2750
Wire Wire Line
	5200 3500 5150 3500
Wire Wire Line
	5200 4200 5150 4200
Connection ~ 5200 3500
Wire Wire Line
	5200 5000 5150 5000
Connection ~ 5200 4200
Connection ~ 5200 5000
Wire Wire Line
	11450 1700 11500 1700
$Comp
L Device:R R17
U 1 1 5DB9EEFB
P 10750 1900
F 0 "R17" H 10680 1854 50  0000 R CNN
F 1 "4.7k" H 10680 1945 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 10680 1900 50  0001 C CNN
F 3 "~" H 10750 1900 50  0001 C CNN
	1    10750 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	11150 2050 11150 2000
Wire Wire Line
	5150 4000 5400 4000
Wire Wire Line
	5150 2550 5400 2550
Wire Wire Line
	5200 2750 5200 3500
$Comp
L Regulator_Linear:L7805 U3
U 1 1 5DB0893F
P 6950 950
F 0 "U3" H 6950 1192 50  0000 C CNN
F 1 "L7805" H 6950 1101 50  0000 C CNN
F 2 "Package_TO_SOT_THT:TO-220F-3_Vertical" H 6975 800 50  0001 L CIN
F 3 "http://www.st.com/content/ccc/resource/technical/document/datasheet/41/4f/b3/b0/12/d4/47/88/CD00000444.pdf/files/CD00000444.pdf/jcr:content/translations/en.CD00000444.pdf" H 6950 900 50  0001 C CNN
	1    6950 950 
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J2
U 1 1 5DB0A00D
P 5150 950
F 0 "J2" H 5068 1167 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 5068 1076 50  0000 C CNN
F 2 "Connector_Wago:Wago_734-132_1x02_P3.50mm_Vertical" H 5150 950 50  0001 C CNN
F 3 "~" H 5150 950 50  0001 C CNN
	1    5150 950 
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5950 700  5350 700 
Wire Wire Line
	5350 700  5350 950 
Wire Wire Line
	5950 1300 5350 1300
Wire Wire Line
	5350 1300 5350 1050
Wire Wire Line
	5650 1000 5650 1350
Wire Wire Line
	6950 1350 6950 1250
Wire Wire Line
	6950 1350 7600 1350
Connection ~ 6950 1350
Wire Wire Line
	7250 950  7600 950 
$Comp
L Device:CP C4
U 1 1 5DB8C6E9
P 7600 1200
F 0 "C4" H 7718 1246 50  0000 L CNN
F 1 "100uF" H 7718 1155 50  0000 L CNN
F 2 "Capacitor_THT:C_Axial_L12.0mm_D9.5mm_P15.00mm_Horizontal" H 7638 1050 50  0001 C CNN
F 3 "~" H 7600 1200 50  0001 C CNN
	1    7600 1200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 1350 6500 1350
$Comp
L Device:CP C3
U 1 1 5DB9F2AD
P 6500 1200
F 0 "C3" H 6618 1246 50  0000 L CNN
F 1 "100uF" H 6618 1155 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P5.00mm" H 6538 1050 50  0001 C CNN
F 3 "~" H 6500 1200 50  0001 C CNN
	1    6500 1200
	1    0    0    -1  
$EndComp
Connection ~ 6500 1350
Wire Wire Line
	6500 1350 6950 1350
Wire Wire Line
	6250 1000 6500 1000
Wire Wire Line
	6500 1000 6500 1050
Wire Wire Line
	7600 1050 7600 1000
Wire Wire Line
	6500 1000 6500 950 
Wire Wire Line
	6500 950  6650 950 
Connection ~ 6500 1000
Wire Wire Line
	5150 3300 5400 3300
Wire Wire Line
	5200 3500 5200 4200
Wire Wire Line
	5150 4800 5400 4800
Wire Wire Line
	9000 2500 8900 2500
Wire Wire Line
	9000 2500 9000 2600
Wire Wire Line
	9000 2600 8900 2600
Wire Wire Line
	9200 2450 9200 2400
Wire Wire Line
	8300 2800 8400 2800
Wire Wire Line
	8400 2600 8200 2600
Wire Wire Line
	8200 2600 8200 2550
Wire Wire Line
	5700 2550 8200 2550
Wire Wire Line
	5800 2700 8400 2700
Wire Wire Line
	5800 2700 5800 3300
Wire Wire Line
	8400 3000 5900 3000
Wire Wire Line
	5900 3000 5900 4000
Wire Wire Line
	8400 3100 6000 3100
Wire Wire Line
	6000 3100 6000 4800
Wire Wire Line
	8400 3200 6100 3200
Wire Wire Line
	6100 3200 6100 5350
Wire Wire Line
	8400 3400 6200 3400
Wire Wire Line
	5200 4200 5200 5000
Wire Wire Line
	8400 2900 6950 2900
Wire Wire Line
	6950 2900 6950 2750
Wire Wire Line
	5200 2750 6950 2750
Connection ~ 5200 2750
Connection ~ 6950 2750
Wire Wire Line
	6950 2750 6950 1350
Wire Wire Line
	10600 2900 10850 2900
Wire Wire Line
	10600 2700 10850 2700
$Comp
L Device:R R19
U 1 1 5DBAFBF7
P 10450 2900
F 0 "R19" V 10243 2900 50  0000 C CNN
F 1 "330" V 10334 2900 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 10380 2900 50  0001 C CNN
F 3 "~" H 10450 2900 50  0001 C CNN
	1    10450 2900
	0    1    1    0   
$EndComp
$Comp
L Device:R R18
U 1 1 5DBAF2C8
P 10450 2700
F 0 "R18" V 10243 2700 50  0000 C CNN
F 1 "330" V 10334 2700 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 10380 2700 50  0001 C CNN
F 3 "~" H 10450 2700 50  0001 C CNN
	1    10450 2700
	0    1    1    0   
$EndComp
$Comp
L Device:LED_Dual_AAC D2
U 1 1 5DBA9850
P 11150 2800
F 0 "D2" H 11150 3225 50  0000 C CNN
F 1 "LED_Dual_AAC" H 11150 3134 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm-3" H 11150 2800 50  0001 C CNN
F 3 "~" H 11150 2800 50  0001 C CNN
	1    11150 2800
	-1   0    0    -1  
$EndComp
$Comp
L Sensor_Temperature:DS18B20 U4
U 1 1 5DAB8695
P 11150 1700
F 0 "U4" V 10783 1700 50  0000 C CNN
F 1 "DS18B20" V 10874 1700 50  0000 C CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 10150 1450 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 11000 1950 50  0001 C CNN
	1    11150 1700
	0    -1   1    0   
$EndComp
Wire Wire Line
	10600 3550 10850 3550
Wire Wire Line
	10600 3350 10850 3350
$Comp
L Device:R R8
U 1 1 5DCB2ECC
P 10450 3550
F 0 "R8" V 10243 3550 50  0000 C CNN
F 1 "330" V 10334 3550 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 10380 3550 50  0001 C CNN
F 3 "~" H 10450 3550 50  0001 C CNN
	1    10450 3550
	0    1    1    0   
$EndComp
$Comp
L Device:R R7
U 1 1 5DCB2ED6
P 10450 3350
F 0 "R7" V 10243 3350 50  0000 C CNN
F 1 "330" V 10334 3350 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 10380 3350 50  0001 C CNN
F 3 "~" H 10450 3350 50  0001 C CNN
	1    10450 3350
	0    1    1    0   
$EndComp
$Comp
L Device:LED_Dual_AAC D3
U 1 1 5DCB2EE0
P 11150 3450
F 0 "D3" H 11150 3875 50  0000 C CNN
F 1 "LED_Dual_AAC" H 11150 3784 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm-3" H 11150 3450 50  0001 C CNN
F 3 "~" H 11150 3450 50  0001 C CNN
	1    11150 3450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	10300 2700 9500 2700
Wire Wire Line
	9500 2700 9500 2800
Wire Wire Line
	9500 2800 8900 2800
Wire Wire Line
	10300 2900 8900 2900
Wire Wire Line
	10300 3350 9500 3350
Wire Wire Line
	9500 3350 9500 3000
Wire Wire Line
	9500 3000 8900 3000
Wire Wire Line
	10300 3550 9450 3550
Wire Wire Line
	9450 3550 9450 3200
Wire Wire Line
	9450 3200 8900 3200
Wire Wire Line
	11500 1700 11500 2800
Wire Wire Line
	11500 3450 11450 3450
Wire Wire Line
	11450 2800 11500 2800
Connection ~ 11500 2800
Wire Wire Line
	11500 2800 11500 3100
Wire Wire Line
	8900 3100 11500 3100
Connection ~ 11500 3100
Wire Wire Line
	11500 3100 11500 3450
$Comp
L Device:R R22
U 1 1 5DB617D9
P 3900 7050
F 0 "R22" V 3693 7050 50  0000 C CNN
F 1 "2.2k" V 3784 7050 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3830 7050 50  0001 C CNN
F 3 "~" H 3900 7050 50  0001 C CNN
	1    3900 7050
	0    1    1    0   
$EndComp
$Comp
L Transistor_BJT:BC547 Q3
U 1 1 5DB617E3
P 4200 7500
F 0 "Q3" H 4391 7546 50  0000 L CNN
F 1 "BC547" H 4391 7455 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4400 7425 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 4200 7500 50  0001 L CNN
	1    4200 7500
	1    0    0    -1  
$EndComp
$Comp
L Connector:RJ12 J4
U 1 1 5DB617ED
P 1700 7300
F 0 "J4" H 1757 7867 50  0000 C CNN
F 1 "RJ12" H 1757 7776 50  0000 C CNN
F 2 "Connector_RJ:RJ12_Amphenol_54601" V 1700 7325 50  0001 C CNN
F 3 "~" V 1700 7325 50  0001 C CNN
	1    1700 7300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 7400 2900 7400
Wire Wire Line
	3400 7400 3400 7050
Wire Wire Line
	3400 7050 3750 7050
$Comp
L Isolator:LTV-847M U2
U 3 1 5DB617FA
P 4850 7150
F 0 "U2" H 4850 7475 50  0000 C CNN
F 1 "LTV-847M" H 4850 7384 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 6850 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 7550 50  0001 C CNN
	3    4850 7150
	1    0    0    -1  
$EndComp
$Comp
L Isolator:LTV-847M U2
U 4 1 5DB61804
P 4850 7900
F 0 "U2" H 4850 8225 50  0000 C CNN
F 1 "LTV-847M" H 4850 8134 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 7600 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 8300 50  0001 C CNN
	4    4850 7900
	-1   0    0    -1  
$EndComp
$Comp
L Isolator:LTV-847M U5
U 1 1 5DB6180E
P 4850 8600
F 0 "U5" H 4850 8925 50  0000 C CNN
F 1 "LTV-847M" H 4850 8834 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 8300 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 9000 50  0001 C CNN
	1    4850 8600
	1    0    0    -1  
$EndComp
$Comp
L Isolator:LTV-847M U5
U 2 1 5DB61818
P 4850 9400
F 0 "U5" H 4850 9725 50  0000 C CNN
F 1 "LTV-847M" H 4850 9634 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 9100 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 9800 50  0001 C CNN
	2    4850 9400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4050 7050 4550 7050
Wire Wire Line
	4550 7250 4300 7250
$Comp
L Device:R R9
U 1 1 5DB61824
P 3550 7500
F 0 "R9" V 3343 7500 50  0000 C CNN
F 1 "210k" V 3434 7500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3480 7500 50  0001 C CNN
F 3 "~" H 3550 7500 50  0001 C CNN
	1    3550 7500
	0    1    1    0   
$EndComp
$Comp
L Device:R R20
U 1 1 5DB6182E
P 3800 8000
F 0 "R20" H 3730 7954 50  0000 R CNN
F 1 "20k" H 3730 8045 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3730 8000 50  0001 C CNN
F 3 "~" H 3800 8000 50  0001 C CNN
	1    3800 8000
	-1   0    0    1   
$EndComp
$Comp
L Device:CP C5
U 1 1 5DB61838
P 4000 8000
F 0 "C5" H 4118 8046 50  0000 L CNN
F 1 "1uF" H 4118 7955 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D5.0mm_P2.00mm" H 4038 7850 50  0001 C CNN
F 3 "~" H 4000 8000 50  0001 C CNN
	1    4000 8000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 7250 4300 7300
Wire Wire Line
	4000 7500 3800 7500
Wire Wire Line
	3400 7800 3400 7500
Wire Wire Line
	3800 7850 3800 7500
Connection ~ 3800 7500
Wire Wire Line
	3800 7500 3700 7500
Wire Wire Line
	4000 7850 4000 7500
Wire Wire Line
	3400 7800 4550 7800
Connection ~ 4000 7500
Wire Wire Line
	4300 7700 4300 8200
Wire Wire Line
	4300 8200 4000 8200
Wire Wire Line
	3800 8200 3800 8150
Wire Wire Line
	4000 8150 4000 8200
Connection ~ 4000 8200
Wire Wire Line
	4000 8200 3800 8200
Wire Wire Line
	4550 8000 4500 8000
Wire Wire Line
	4500 8000 4500 8200
Wire Wire Line
	4500 8200 4300 8200
Connection ~ 4300 8200
Wire Wire Line
	2500 8200 3800 8200
Connection ~ 3800 8200
Wire Wire Line
	2100 7000 2600 7000
Wire Wire Line
	2600 7000 2600 7500
Wire Wire Line
	2600 7500 3400 7500
Connection ~ 3400 7500
$Comp
L Device:R R23
U 1 1 5DB6185D
P 3950 8500
F 0 "R23" V 3743 8500 50  0000 C CNN
F 1 "2.2k" V 3834 8500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3880 8500 50  0001 C CNN
F 3 "~" H 3950 8500 50  0001 C CNN
	1    3950 8500
	0    1    1    0   
$EndComp
$Comp
L Device:R R10
U 1 1 5DB61867
P 3550 9000
F 0 "R10" V 3343 9000 50  0000 C CNN
F 1 "210k" V 3434 9000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3480 9000 50  0001 C CNN
F 3 "~" H 3550 9000 50  0001 C CNN
	1    3550 9000
	0    1    1    0   
$EndComp
$Comp
L Device:R R21
U 1 1 5DB61871
P 3800 9500
F 0 "R21" H 3730 9454 50  0000 R CNN
F 1 "20k" H 3730 9545 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 3730 9500 50  0001 C CNN
F 3 "~" H 3800 9500 50  0001 C CNN
	1    3800 9500
	-1   0    0    1   
$EndComp
$Comp
L Device:CP C6
U 1 1 5DB6187B
P 4000 9500
F 0 "C6" H 4118 9546 50  0000 L CNN
F 1 "1uF" H 4118 9455 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D5.0mm_P2.00mm" H 4038 9350 50  0001 C CNN
F 3 "~" H 4000 9500 50  0001 C CNN
	1    4000 9500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 8500 4100 8500
Wire Wire Line
	3800 8500 3300 8500
Wire Wire Line
	3300 8500 3300 7400
Connection ~ 3300 7400
Wire Wire Line
	3300 7400 3400 7400
$Comp
L Transistor_BJT:BC547 Q4
U 1 1 5DB6188A
P 4200 9000
F 0 "Q4" H 4391 9046 50  0000 L CNN
F 1 "BC547" H 4391 8955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4400 8925 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 4200 9000 50  0001 L CNN
	1    4200 9000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 8700 4300 8700
Wire Wire Line
	4300 8700 4300 8800
Wire Wire Line
	4000 9000 3800 9000
Wire Wire Line
	4550 9300 3400 9300
Wire Wire Line
	3400 9300 3400 9000
Wire Wire Line
	4000 9350 4000 9000
Connection ~ 4000 9000
Wire Wire Line
	3800 9350 3800 9000
Connection ~ 3800 9000
Wire Wire Line
	3800 9000 3700 9000
Wire Wire Line
	4550 9500 4500 9500
Wire Wire Line
	4500 9500 4500 9700
Wire Wire Line
	4500 9700 4300 9700
Wire Wire Line
	4000 9700 4000 9650
Wire Wire Line
	4000 9700 3800 9700
Wire Wire Line
	3800 9700 3800 9650
Connection ~ 4000 9700
Wire Wire Line
	4300 9200 4300 9700
Connection ~ 4300 9700
Wire Wire Line
	4300 9700 4000 9700
Wire Wire Line
	2100 7200 2700 7200
Wire Wire Line
	2700 7200 2700 9000
Wire Wire Line
	2700 9000 3400 9000
Connection ~ 3400 9000
$Comp
L Isolator:LTV-847M U5
U 3 1 5DB618B1
P 4850 9950
F 0 "U5" H 4850 10275 50  0000 C CNN
F 1 "LTV-847M" H 4850 10184 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W10.16mm" H 4850 9650 50  0001 C CNN
F 3 "http://www.us.liteon.com/downloads/LTV-817-827-847.PDF" H 4400 10350 50  0001 C CNN
	3    4850 9950
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2100 7100 2800 7100
$Comp
L Device:R R24
U 1 1 5DB618D0
P 5550 7050
F 0 "R24" V 5343 7050 50  0000 C CNN
F 1 "330" V 5434 7050 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 7050 50  0001 C CNN
F 3 "~" H 5550 7050 50  0001 C CNN
	1    5550 7050
	0    1    1    0   
$EndComp
$Comp
L Device:R R25
U 1 1 5DB618DA
P 5550 7800
F 0 "R25" V 5343 7800 50  0000 C CNN
F 1 "330" V 5434 7800 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 7800 50  0001 C CNN
F 3 "~" H 5550 7800 50  0001 C CNN
	1    5550 7800
	0    1    1    0   
$EndComp
$Comp
L Device:R R26
U 1 1 5DB618E4
P 5550 8500
F 0 "R26" V 5343 8500 50  0000 C CNN
F 1 "330" V 5434 8500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 8500 50  0001 C CNN
F 3 "~" H 5550 8500 50  0001 C CNN
	1    5550 8500
	0    1    1    0   
$EndComp
$Comp
L Device:R R27
U 1 1 5DB618EE
P 5550 9300
F 0 "R27" V 5343 9300 50  0000 C CNN
F 1 "330k" V 5434 9300 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 9300 50  0001 C CNN
F 3 "~" H 5550 9300 50  0001 C CNN
	1    5550 9300
	0    1    1    0   
$EndComp
$Comp
L Device:R R28
U 1 1 5DB618FB
P 5550 9850
F 0 "R28" V 5343 9850 50  0000 C CNN
F 1 "330" V 5434 9850 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5480 9850 50  0001 C CNN
F 3 "~" H 5550 9850 50  0001 C CNN
	1    5550 9850
	0    1    1    0   
$EndComp
$Comp
L Device:R R29
U 1 1 5DB61905
P 6600 10600
F 0 "R29" V 6393 10600 50  0000 C CNN
F 1 "330" V 6484 10600 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 6530 10600 50  0001 C CNN
F 3 "~" H 6600 10600 50  0001 C CNN
	1    6600 10600
	0    1    1    0   
$EndComp
Wire Wire Line
	5150 7250 5200 7250
Wire Wire Line
	5200 8000 5150 8000
Wire Wire Line
	5200 8700 5150 8700
Connection ~ 5200 8000
Wire Wire Line
	5200 9500 5150 9500
Connection ~ 5200 8700
Connection ~ 5200 9500
Wire Wire Line
	5200 10050 5150 10050
Wire Wire Line
	5150 8500 5400 8500
Wire Wire Line
	5150 7050 5400 7050
Wire Wire Line
	5200 7250 5200 8000
Wire Wire Line
	5150 7800 5400 7800
Wire Wire Line
	5200 8000 5200 8700
Wire Wire Line
	5150 9300 5400 9300
Wire Wire Line
	5150 9850 5400 9850
Wire Wire Line
	5200 9500 5200 10050
Wire Wire Line
	5200 8700 5200 9500
Wire Wire Line
	5700 7050 6750 7050
Wire Wire Line
	6750 7050 6750 3500
Wire Wire Line
	6750 3500 8400 3500
Wire Wire Line
	5700 7800 6850 7800
Wire Wire Line
	6850 7800 6850 3600
Wire Wire Line
	6850 3600 8400 3600
Wire Wire Line
	5700 8500 6950 8500
Wire Wire Line
	6950 8500 6950 3900
Wire Wire Line
	6950 3900 8400 3900
Wire Wire Line
	5700 9300 7050 9300
Wire Wire Line
	7050 9300 7050 4000
Wire Wire Line
	7050 4000 8400 4000
Wire Wire Line
	5700 9850 7150 9850
Wire Wire Line
	7150 9850 7150 4100
Wire Wire Line
	7150 4100 8400 4100
Wire Wire Line
	7250 4200 8400 4200
Connection ~ 5200 7250
Wire Wire Line
	7600 1000 9000 1000
Wire Wire Line
	9000 1000 9000 2500
Connection ~ 7600 1000
Wire Wire Line
	7600 1000 7600 950 
Connection ~ 9000 2500
Wire Wire Line
	11150 2050 10750 2050
Wire Wire Line
	10750 2050 8300 2050
Connection ~ 10750 2050
Wire Wire Line
	8300 2050 8300 2800
Wire Wire Line
	10850 1700 10750 1700
Wire Wire Line
	10750 1700 10750 1750
Wire Wire Line
	10750 1700 8400 1700
Wire Wire Line
	8400 1700 8400 2500
Connection ~ 10750 1700
$Comp
L Connector:RJ12 J6
U 1 1 5DBB52F3
P 1700 5750
F 0 "J6" H 1757 6317 50  0000 C CNN
F 1 "RJ12" H 1757 6226 50  0000 C CNN
F 2 "Connector_RJ:RJ12_Amphenol_54601" V 1700 5775 50  0001 C CNN
F 3 "~" V 1700 5775 50  0001 C CNN
	1    1700 5750
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 3000 2600 5450
Wire Wire Line
	2600 5450 2100 5450
Connection ~ 2600 3000
Wire Wire Line
	2700 4500 2700 5650
Wire Wire Line
	2700 5650 2100 5650
Connection ~ 2700 4500
Wire Wire Line
	2500 5750 2100 5750
Wire Wire Line
	2500 2800 2500 3700
Connection ~ 2500 3700
Wire Wire Line
	2900 2900 2900 5850
Wire Wire Line
	2900 5850 2100 5850
Connection ~ 2900 2900
Wire Wire Line
	2400 3000 2100 3000
$Comp
L Connector:RJ12 J5
U 1 1 5DC8A530
P 1650 10300
F 0 "J5" H 1707 10867 50  0000 C CNN
F 1 "RJ12" H 1707 10776 50  0000 C CNN
F 2 "Connector_RJ:RJ12_Amphenol_54601" V 1650 10325 50  0001 C CNN
F 3 "~" V 1650 10325 50  0001 C CNN
	1    1650 10300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 7500 2600 10000
Wire Wire Line
	2600 10000 2050 10000
Connection ~ 2600 7500
Wire Wire Line
	2700 9000 2700 10200
Wire Wire Line
	2700 10200 2050 10200
Connection ~ 2700 9000
Wire Wire Line
	2900 7400 2900 10400
Wire Wire Line
	2900 10400 2050 10400
Connection ~ 2900 7400
Wire Wire Line
	2400 7500 2100 7500
$Comp
L Connector_Generic_MountingPin:Conn_02x20_Odd_Even_MountingPin J3
U 1 1 5DB86D7C
P 8600 3400
F 0 "J3" H 8650 4517 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even_MountingPin" H 8650 4426 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 8600 3400 50  0001 C CNN
F 3 "~" H 8600 3400 50  0001 C CNN
	1    8600 3400
	1    0    0    -1  
$EndComp
$Comp
L Device:D_Bridge_+-AA D1
U 1 1 5DB31132
P 5950 1000
F 0 "D1" H 6294 1046 50  0000 L CNN
F 1 "D_Bridge_+-AA" H 6294 955 50  0000 L CNN
F 2 "Diode_THT:Diode_Bridge_DIP-4_W7.62mm_P5.08mm" H 5950 1000 50  0001 C CNN
F 3 "~" H 5950 1000 50  0001 C CNN
	1    5950 1000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 5DEAFD11
P 7600 1500
F 0 "#PWR0101" H 7600 1250 50  0001 C CNN
F 1 "GND" H 7605 1327 50  0000 C CNN
F 2 "" H 7600 1500 50  0001 C CNN
F 3 "" H 7600 1500 50  0001 C CNN
	1    7600 1500
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0102
U 1 1 5DEB0C07
P 7600 850
F 0 "#PWR0102" H 7600 700 50  0001 C CNN
F 1 "+5V" H 7615 1023 50  0000 C CNN
F 2 "" H 7600 850 50  0001 C CNN
F 3 "" H 7600 850 50  0001 C CNN
	1    7600 850 
	1    0    0    -1  
$EndComp
Wire Wire Line
	7600 950  7600 850 
Connection ~ 7600 950 
Wire Wire Line
	7600 1350 7600 1500
Connection ~ 7600 1350
$Comp
L power:VAC #PWR0103
U 1 1 5DEF8A0C
P 5350 700
F 0 "#PWR0103" H 5350 600 50  0001 C CNN
F 1 "VAC" H 5350 975 50  0000 C CNN
F 2 "" H 5350 700 50  0001 C CNN
F 3 "" H 5350 700 50  0001 C CNN
	1    5350 700 
	1    0    0    -1  
$EndComp
Connection ~ 5350 700 
$Comp
L power:VAC #PWR0104
U 1 1 5DEFE8B1
P 5350 1300
F 0 "#PWR0104" H 5350 1200 50  0001 C CNN
F 1 "VAC" H 5350 1575 50  0000 C CNN
F 2 "" H 5350 1300 50  0001 C CNN
F 3 "" H 5350 1300 50  0001 C CNN
	1    5350 1300
	-1   0    0    1   
$EndComp
Connection ~ 5350 1300
$Comp
L power:GND #PWR0105
U 1 1 5DF06D16
P 11500 3750
F 0 "#PWR0105" H 11500 3500 50  0001 C CNN
F 1 "GND" H 11505 3577 50  0000 C CNN
F 2 "" H 11500 3750 50  0001 C CNN
F 3 "" H 11500 3750 50  0001 C CNN
	1    11500 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	11500 3450 11500 3750
Connection ~ 11500 3450
$Comp
L Relay:FINDER-32.21-x000 K2
U 1 1 5DC53103
P 4900 10750
F 0 "K2" H 4470 10796 50  0000 R CNN
F 1 "FINDER-32.21-x000" H 4470 10705 50  0000 R CNN
F 2 "Relay_THT:Relay_SPST_Finder_32.21-x300" H 6170 10720 50  0001 C CNN
F 3 "https://gfinder.findernet.com/assets/Series/355/S32EN.pdf" H 4900 10750 50  0001 C CNN
	1    4900 10750
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5200 5000 5200 5550
Wire Wire Line
	4550 5350 2400 5350
Connection ~ 2400 5350
Wire Wire Line
	4550 9850 2400 9850
Wire Wire Line
	2400 9850 2400 7500
Wire Wire Line
	2400 9850 2400 10500
Wire Wire Line
	2050 10500 2400 10500
Connection ~ 2400 9850
Wire Wire Line
	4550 10050 3000 10050
Wire Wire Line
	3000 10050 3000 10300
Wire Wire Line
	2900 7400 3300 7400
Wire Wire Line
	2100 7300 2500 7300
Wire Wire Line
	2050 10300 2500 10300
Wire Wire Line
	2500 10300 2500 9700
Connection ~ 2500 10300
Wire Wire Line
	2500 10300 3000 10300
Connection ~ 2500 8200
Wire Wire Line
	2500 8200 2500 7300
Wire Wire Line
	3800 9700 2500 9700
Connection ~ 3800 9700
Connection ~ 2500 9700
Wire Wire Line
	2500 9700 2500 8200
Wire Wire Line
	2050 10100 2250 10100
Wire Wire Line
	2250 10100 2250 11050
Wire Wire Line
	2250 11050 4700 11050
Wire Wire Line
	4800 10350 2800 10350
Wire Wire Line
	2800 10350 2800 7100
Wire Wire Line
	4800 10350 4800 10450
$Comp
L Transistor_BJT:BC547 Q6
U 1 1 5E06B29F
P 6200 10800
F 0 "Q6" H 6391 10846 50  0000 L CNN
F 1 "BC547" H 6391 10755 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 6400 10725 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 6200 10800 50  0001 L CNN
	1    6200 10800
	0    -1   1    0   
$EndComp
$Comp
L Device:D D5
U 1 1 5E0720BA
P 5550 10750
F 0 "D5" V 5504 10671 50  0000 R CNN
F 1 "D" V 5595 10671 50  0000 R CNN
F 2 "Diode_THT:D_A-405_P5.08mm_Vertical_KathodeUp" H 5550 10750 50  0001 C CNN
F 3 "~" H 5550 10750 50  0001 C CNN
	1    5550 10750
	0    -1   1    0   
$EndComp
Wire Wire Line
	5100 10300 5100 10450
Connection ~ 9000 2600
Wire Wire Line
	5550 10600 5550 10300
Connection ~ 5550 10300
Wire Wire Line
	5550 10300 5100 10300
Wire Wire Line
	5100 11050 5550 11050
Wire Wire Line
	5550 11050 5550 10900
Wire Wire Line
	5550 10300 9000 10300
Wire Wire Line
	6000 10900 5550 10900
Connection ~ 5550 10900
Wire Wire Line
	6450 10600 6200 10600
Wire Wire Line
	6400 10900 6400 10050
Wire Wire Line
	6400 10050 5200 10050
Connection ~ 5200 10050
Wire Wire Line
	7250 4200 7250 10600
Wire Wire Line
	7250 10600 6750 10600
Wire Wire Line
	5150 5550 5200 5550
Connection ~ 5200 5550
Wire Wire Line
	5400 5350 5150 5350
Wire Wire Line
	5200 5550 5200 6750
Wire Wire Line
	2100 5950 2400 5950
Wire Wire Line
	2400 5350 2400 5950
Wire Wire Line
	2900 2900 3300 2900
Wire Wire Line
	2500 5200 3800 5200
Wire Wire Line
	2500 3700 2500 5200
Connection ~ 2500 5200
Wire Wire Line
	2500 5200 2500 5750
Wire Wire Line
	4550 5550 3000 5550
Wire Wire Line
	3000 5550 3000 5750
Wire Wire Line
	3000 5750 2500 5750
Connection ~ 2500 5750
$Comp
L Relay:FINDER-32.21-x000 K1
U 1 1 5E2C2AF6
P 4550 6300
F 0 "K1" H 4120 6346 50  0000 R CNN
F 1 "FINDER-32.21-x000" H 4120 6255 50  0000 R CNN
F 2 "Relay_THT:Relay_SPST_Finder_32.21-x300" H 5820 6270 50  0001 C CNN
F 3 "https://gfinder.findernet.com/assets/Series/355/S32EN.pdf" H 4550 6300 50  0001 C CNN
	1    4550 6300
	-1   0    0    -1  
$EndComp
$Comp
L Device:D D4
U 1 1 5E2C5CFC
P 5100 6300
F 0 "D4" V 5054 6221 50  0000 R CNN
F 1 "D" V 5145 6221 50  0000 R CNN
F 2 "Diode_THT:D_A-405_P5.08mm_Vertical_KathodeUp" H 5100 6300 50  0001 C CNN
F 3 "~" H 5100 6300 50  0001 C CNN
	1    5100 6300
	0    -1   1    0   
$EndComp
$Comp
L Transistor_BJT:BC547 Q5
U 1 1 5E2C7561
P 5650 6350
F 0 "Q5" H 5841 6396 50  0000 L CNN
F 1 "BC547" H 5841 6305 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 5850 6275 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC547.pdf" H 5650 6350 50  0001 L CNN
	1    5650 6350
	0    1    1    0   
$EndComp
Wire Wire Line
	6200 3400 6200 6000
Wire Wire Line
	5900 6000 5650 6000
Wire Wire Line
	5450 6450 5100 6450
Wire Wire Line
	5100 6450 5100 6650
Wire Wire Line
	5100 6650 4750 6650
Wire Wire Line
	4750 6650 4750 6600
Connection ~ 5100 6450
Wire Wire Line
	5850 6450 5850 6750
Wire Wire Line
	5850 6750 5200 6750
Connection ~ 5200 6750
Wire Wire Line
	5200 6750 5200 7250
Wire Wire Line
	5100 6150 5100 6100
Wire Wire Line
	5100 5950 4750 5950
Wire Wire Line
	4750 5950 4750 6000
Wire Wire Line
	9000 2600 9000 6100
Wire Wire Line
	5650 6150 5650 6000
Wire Wire Line
	5100 6100 9000 6100
Connection ~ 5100 6100
Wire Wire Line
	5100 6100 5100 5950
Connection ~ 9000 6100
Wire Wire Line
	9000 6100 9000 10300
Wire Wire Line
	4350 6600 4350 6650
Wire Wire Line
	4350 6650 2300 6650
Wire Wire Line
	2300 6650 2300 5550
Wire Wire Line
	2300 5550 2100 5550
Wire Wire Line
	4450 6000 4450 5700
Wire Wire Line
	4450 5700 2800 5700
Wire Wire Line
	2800 2600 2800 5700
Text Label 5950 700  0    50   ~ 0
VAC
Text Label 5350 1300 0    50   ~ 0
VAC
Text Label 6250 1000 0    50   ~ 0
VDC
$EndSCHEMATC