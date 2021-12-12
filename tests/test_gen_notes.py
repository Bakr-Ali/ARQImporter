import unittest

from src.gen_notes import *

# TODO: put chapter markers
test_text = """
# النظم الصغير
مقدمة النظم الصغير؟
01- أَحْمَدُ رَبِّي وَاهِبَ العُقُولِ .. وَصَلِّ يَارَبِّ عَلَى الرَّسُولِ **
02- وَاكْتُبْ قَبُولَ نَظْمِيَ الصَّغِيرِ .. كَأَصْلِهِ مُخْتَصَرِ التَّحْرِيرِ **
03- إذْ مِنْهُ لَخَّصْتُ بِلا تَبْوِيبِ .. رَتَّبْتُهُ بِنَمَطٍ قَرِيبِ **
ما هو الكتاب المعتمد في النظم الصغير؟
02- وَاكْتُبْ قَبُولَ نَظْمِيَ الصَّغِيرِ .. كَأَصْلِهِ مُخْتَصَرِ التَّحْرِيرِ **
03- إذْ مِنْهُ لَخَّصْتُ بِلا تَبْوِيبِ .. رَتَّبْتُهُ بِنَمَطٍ قَرِيبِ **
أبواب علم أصول الفقه؟
04- عِلْمُ الأُصُولِ أَرْبَعٌ: [1]أَحْكَامُ .. [2]أَدِلَّةٌ، [3]دَلَالَةٌ، [4]حُكَّامُ **
أقسام الأحكام الفقهية؟
05- فَالأَوَّلُ: الأَحْكَامُ فِي قِسْمَيْنِ: .. تَكْلِيْفٌ اوْ وَضْعٌ بِغَيرِ مَيْنِ **
أقسام الأحكام التكليفية؟
06- أَمَّا التَّكَالِيفُ: فَفَرْضٌ سُنَّةُ .. إِبَاحَةٌ، كَرَاهَةٌ، وَحُرْمَةُ **
تعريف الواجب والمستحب؟
07- مَا كَانَ مَأْمُورًا بِهِ فَذَا وَجَبْ .. إِنْ كَانَ جَازِمًا وَإِلَّا مُسْتَحَبّْ **
تقسيم الواجب بعدة اعتبارات؟
08- مُوَسَّعٌ، مُخَيَّرٌ، وَمَا طُلِبْ .. كِفَايَةً، وَعَكْسُهَا، كُلٌّ يجِبْ **
09- مَا لا يَتِمُّ وَاجِبٌ إِلا بِهِ .. فَوَاجِبٌ، فَاحْرِصْ عَلَى طِلَابِهِ **
تعريف الحرام والمكروه؟
10- أَمَّا الحَرَامُ فَهْوَ مَا عَنْهُ نُهِيْ .. جَزْمًا، وَدُونَ الجَزْمِ فِعْلَهُ اكْرَهِ **
تعريف المباح؟ وكيف يُعرَف؟
11- وَإِنْ أَتَى التَّخْيِيرُ فَالإِبَاحَهْ .. بِالأَصْلِ أَوْ مَا النَّصُّ قَدْ أَبَاحَهْ **
أقسام الأحكام الوضعية؟
12- أَحْكَامُ وَضْعٍ: سَبَبٌ وَعِلَّهْ .. وَالشَّرطُ، وَالـمَوَانِعُ الـمُخِلَّهْ **
13- وَرُخْصَةٌ، وَعَكْسُهَا العَزِيـمَهْ .. ثُمَّ فَسَادٌ، صِحَّةٌ قَوِيـمَهْ **
تعريف الأسباب والشروط والموانع؟
14- فَسَبَبٌ دَلَّ عَلَى الوُجُودِ .. وَفَقْدُهُ دَلَّ عَلَى الفُقُودِ **
15- وَعَدَمُ الشَّرْطِ يُفِيدُ العَدَمَا .. وُجُودُ مَانِعٍ كَذَاكَ فَاعْلَمَا **
تعريف الصحة والفساد؟
16- وَمَا بِهِ تَرَتَّبَ الـمُرَادُ .. فَصِحَّةٌ، وَضِدُّهَا الفَسَادُ **
تعريف الرخصة؟
17- وَثَابِتٌ عَلَى خِلَافِ الأَصْلِ .. فَرُخْصَةٌ، وَقَيِّدَنْ بِالسَّهْلِ **
تعريف العلة؟
18- وَالعِلَّةُ الوَصْفُ الَّذِي قَدِ اقْتَضَى .. حُكْمًا.بِهذَا مَبْحَثُ الحُكْمِ انْقَضَى **
أقسام الأدلة الشرعية؟ عدِّدْ أفراد كل قسم.
19- وَثَانِيًا: أَدِلَّةٌ مِنْهَا اخْتُلِفْ .. فِيهِ، وَبَعْضٌ بِالوِفَاقِ يَتَّصِفْ **
20- وَهْيَ: الكِتَابُ، السُّنَّةُ، الإِجْمَاعُ .. قِيَاسُهَا. فِي غَيْرِهَا نِزَاعُ: **
21- شَرْعٌ مَضَى، مَا قَالَهُ الأَصْحَابُ .. مَصَالحٌ، مَا اسْتُحْسِنَ، اسْتِصْحَابُ **
الأدلة المُتفَق عليها؟
20- وَهْيَ: الكِتَابُ، السُّنَّةُ، الإِجْمَاعُ .. قِيَاسُهَا. فِي غَيْرِهَا نِزَاعُ: **
الأدلة المُُختلَف فيها؟
21- شَرْعٌ مَضَى، مَا قَالَهُ الأَصْحَابُ .. مَصَالحٌ، مَا اسْتُحْسِنَ، اسْتِصْحَابُ **
الأخذ بالقرآن كدليل؟
22- أمّا الكِتَابُ فَتَوَاتَرَ السَّنَدْ .. قِرَاءَةُ الآحَادِ فِيهِ مُسْتَنَدْ **
الأخذ بالأحاديث كدليل؟
23- ثُمَّ الحَدِيثُ مِنْهُ ذُو تَوَاتُرِ .. وَمِنْهُ آحَادٌ. فَحُكْمُ الآخِرِ: **
24- قَبُولُ مُسْنَدٍ وَمُرْسَلٍ وَرَدْ .. بِنَقْلِ عَدْلٍ ضَابِطٍ. سِوَاهُ رَدّْ **
أقسام السُّنة؟ ودلالة كل منها على الأحكام؟
25- وَمَا رُوِيْ مِنْ سُنَّةِ الـمُخْتَارِ: .. قَوْلٌ، وَفِعْلٌ، سُنَّةُ الإِقْرَارِ **
26- وَفِعْلُهُ: إِنْ كَانَ لِلْعِبَادَهْ .. فَوَاجِبٌ، وَجَازَ مَا لِلْعَادَهْ **
27- إِلا إِذَا اخْتَصَّ بِهِ أَوْ كَانَا .. مِنْ فِعْلِهِ لـمُجْمَلٍ بَيَانَا **
28- فَالحُكْمُ فِي المُخْتَصِّ غَيْرُ مُشْكِلِ .. وَالحُكْمُ فِي البَيَانِ حُكْمُ المُجْمَلِ **
29- إِقْرَارُهُ دَلَّ عَلَى الجَوَازِ .. كَذَا الجِبِلِّيُّ بِلَا احْتِرَازِ **
أنواع النسخ وجواز كل منها؟
30- وَالنَّسْخُ لِلْقُرْآنِ بِالْقُرْآنِ .. وَسُنَّةٍ بِسُنَّةِ العَدْنَانِي **
31- وَتُنْسَخُ السُّنَّةُ بِالْقُرْآنِ .. لا العَكْسُ عِنْدَ أَكْثَرِ الأَعْيَانِ **
شروط النسخ؟
32- شُرُوطُ نَسْخٍ: كَوْنُهُ إِنْشَاءَا .. تَعَذُّرُ الجَمْعِ، تَرَاخٍ جَاءَا **
كيف نعرف النسخ؟
33- يُعْرَفُ بِالنَّصِّ أَوِ الإِجْمَاعِ .. أَوْ قَوْلِ رَاوٍ فَالزَّمَانَ رَاعِ **
الإجماع وأنواعه؟
34- وَخُذْ بِالِاجْمَاعِ أَيِ: الصَّرِيحِ .. ثُمَّ السُّكُوتِيِّ عَلَى الصَّحِيحِ **
شروط الإجماع؟
35- وَشَرْطُهُ: اتِّفَاقُهُمْ جَمِيعَا .. أَيْ فُقَهَاءِ عَصْرِهِ، تَشْرِيعَا **
36- وَلمْ يَكُنْ قَبْلُ خِلافٌ اسْتَقَرّْ .. أَوْ أَجْمَعَ الـمَاضُونَ فِيهِ وَاسْتَمَرّْ **
اعتبار العصر والفقيه الناشئ؟
37- وَاعْتَبِرِ انْقِرَاضَ عَصْرٍ فِيهِ .. وَاقْبَلْ خِلَافَ نَاشِئٍ فَقِيهِ **
اختلف العلماء في حكم الوتر، فيجوز أن نقول أنه مكروه؟
38- إِنْ حُصِرَ الخِلَافُ فِي قَوْلَينِ .. فَثَالِثٌ أُحْدِثَ غَيْرُ زَيْنِ **
أنواع القياس؟
39- ثُمَّ القِيَاسُ: عِلَّةٌ، دَلَالَهْ .. وَشَبَهٌ، وَنَفْيُ فَرْقٍ نَالَهْ **
أركان القياس؟
40- أَرْكَانُهُ ذَكَرَهَا الأَجِلَّهْ: .. فَرْعٌ، وَأَصْلٌ، حُكْمُهُ، وَالعِلَّهْ **
شروط القياس؟
41- وَشَرْطُ الَاصْلِ: العَقْلُ لِلْمَعَانِي .. إِحْكَامُهُ، لا بِقِيَاسٍ ثَانِي **
42- لا نَصَّ فِي الفَرْعِ، وُجُودُ الجَامِعِ .. وَحُكْمُهُ كَأَصْلِهِ فَتَابِعِ **
43- عِلَّتُهُ: انْضِبَاطُهَا، الظُّهُورُ .. لا تُبْطِلُ الأَصْلَ، وَكَمْ تَدُورُ **
شروط الحكم الأصلي في القياس؟
41- وَشَرْطُ الَاصْلِ: العَقْلُ لِلْمَعَانِي .. إِحْكَامُهُ، لا بِقِيَاسٍ ثَانِي **
شروط الفرع في القياس؟
42- لا نَصَّ فِي الفَرْعِ، وُجُودُ الجَامِعِ .. وَحُكْمُهُ كَأَصْلِهِ فَتَابِعِ **
شروط العلة في القياس؟
43- عِلَّتُهُ: انْضِبَاطُهَا، الظُّهُورُ .. لا تُبْطِلُ الأَصْلَ، وَكَمْ تَدُورُ **
مسالك العلة بالتفصيل؟
44- وَتَثْبُتُ العِلَّةُ بِالـمَسَالِكْ: .. إِجْمَاعٌ، اوْ نَصٌّ، وَغَيْرُ ذَلكْ: **
45- السَّبْرُ وَالتَّقْسِيمُ، وَالـمُنَاسَبَهْ .. وَشَبَهٌ، وَالدَّوَرَانُ صَاحَبَهْ **
46- وَمَسْلَكُ النَّصِّ: إِلى الصَّرِيحِ .. فَالظَّاهِرِ، الإِيـمَاءِ ذِي التَّلْمِيحِ **
تفصيل الأدلة المختلف فيها؟
47- وَشَرْعُ مَنْ مَضَى لَنَا دَلِيلُ .. إِنْ لَمْ يُخَالِفْ شَرْعُنَا الجَلِيلُ **
48- وَقَوْلُ صَاحِبٍ إِذَا لَمْ يَرِدِ .. عَنْ صَاحِبٍ خِلَافُهُ فَاعْتَمِدِ **
49- وَإِنْ يَكُنْ بِالرَّأْيِ لا يُقَالُ .. فَحُكْمُهُ الرَّفْعُ عَلَى مَا قَالُوا **
50- مَصَالحُ العِبَادِ أَعْنِيْ الـمُرْسَلَهْ .. لَيْسَتْ بِحُجَّةٍ، وَقِيلَ: مُعْمَلَهْ **
51- وَهْيَ: الضَّرُورِيَّاتُ وَالحَاجَاتُ .. تَحْسِينُهَا، رَتَّبَهَا الثِّقَاتُ **
52- أَوَّلُها: الدِّينُ –احْفَظَنْ- فَالنَّفْسُ .. فَالنَّسْلُ، فَالعَقْلُ، فَمَالٌ، خَمْسُ **
53- ثُمَّ العُدُولَ سَمِّهِ اسْتِحْسَانَا .. أَيْ: عَنْ نَظِيرٍ. خُذْ بِهِ أَحْيَانَا **
54- وَاسْتَصْحِبِ البَرَاءَةَ الأَصْلِيَّهْ .. إِنْ لَمْ يَرِدْ مَا يَنْقُلُ القَضِيَّهْ **
55- مُسْتَصْحِبُ الإِجْمَاعِ فِي مَحَلِّ .. خِلَافِهِمْ أَخْطَأَ عِنْدَ الجُلِّ **
أحكام الاستصحاب؟
54- وَاسْتَصْحِبِ البَرَاءَةَ الأَصْلِيَّهْ .. إِنْ لَمْ يَرِدْ مَا يَنْقُلُ القَضِيَّهْ **
55- مُسْتَصْحِبُ الإِجْمَاعِ فِي مَحَلِّ .. خِلَافِهِمْ أَخْطَأَ عِنْدَ الجُلِّ **
تقسيم الدلالات باعتبارات؟ (قوة الدلالة ومحل الدلالة)
56- وَثَالِثًا: دَلَالَةُ اللَّفْظِ، انْجَلَى .. نَصًّا، وَظَاهِرًا، وَجَاءَ مُجْمَلا **
57- مِنْ جِهَةٍ أُخْرَى إِلَى: الـمَفْهُومِ .. وَعَكْسِهِ الـمَنْطُوقِ فِي الـمَنْظُومِ **
تعريف الأمر والنهي؟
58- وَطَلَبُ الفِعْلِ بِقَوْلٍ أَمْرُ .. وَعَكْسُهُ النَّهْيُ كَـ(لَا تُصَرُّوا) **
دلالة الأمر؟
59- وَذَكَرُوا مِنْ جُمْلَةِ الظَّوَاهِرِ .. الفَوْرَ وَالوُجُوبَ فِي الأَوَامِرِ **
60- تَكْرَارَهُ، فِي الفَائِتِ القَضَاءُ .. وَالنَّهْيَ عَنْ ضِدٍّ، كَذَا الإِجْزَاءُ **
ما الذي يدل على الأمر؟
61- بِفِعْلِ أَمْرٍ، وَاسْمِهِ، أَوْ مَا وُصِلْ .. بِلَامِهِ اعْرِفْ، وَ(أُمِرْنَا) فَامْتَثِلْ **
دلالة النهي؟
62- وَالنَّهْيُ لِلتَّكْرَارِ وَالتَّحْرِيمِ .. وَالفَوْرِ وَالفَسَادِ كَالعَدِيمِ **
ما الذي يدل على النهي؟
63- بِنَحْوِ: (لَا تَفْعَلْ)، وَمِثْلِ: (قَدْ نَهَى) .. يُعْرَفُ نَهْيٌ، فَازَ مَنْ عَنْهُ انْتَهَى **
أنواع العموم؟
64- وَحَدُّ ذِي العُمُومِ لَفْظٌ قَدْ شَمَلْ .. أَجْزَاءَ مَاهِيَّةِ مَا عَلَيْهِ دَلّْ **
65- وَإِنْ يَكُنْ دَلَّ بِلا اسْتِغْرَاقِ .. عَلَى حَقِيقَةٍ فَذُو الإِطْلَاقِ **
ما الذي يدل على العموم؟
66- وَصِيَغُ العُمُومِ: (كُلٌّ)، (أَجْمَعُ) .. وَ(مَنْ) وَ(مَا) وَ(أَلْ) وَ(أَيٌّ) فَاسْمَعُوا **
67- نَكِرَةٌ فِيمَا نُهِيْ أَوْ مَا نُفِي .. وَهَكَذَا الـمُضَافُ لِلْمُعَرَّفِ **
هل يُخصَص العام؟ وبماذا؟
68- وَخَصِّصِ العُمُومَ بِالخُصُوصِ .. مِنْ عَقْلٍ اوْ نَقْلٍ مِنَ النُّصُوصِ **
69- كَالنُّطْقِ وَالـمَفْهُومِ وَالإِجْمَاعِ .. وَالفِعْلِ، قَولِ صَاحِبٍ فَرَاعِ **
70- وَالحِسِّ وَالقِيَاسِ، هَذَا الـمُنْفَصِلْ .. وَالشَّرْطِ، الاسْتِثْنَاءِ، هَذَا الـمُتَّصِلْ **
متى يُحمل المطلق على المقيد؟
71- وَالـمُطْلَقَ احْمِلْهُ عَلَى الـمُقَيَّدِ .. عِنْدَ اتِّفَاقِ حُكْمِهِ الـمُعْتَمَدِ **
متى يؤخذ بكل قسم من دلالات الألفاظ باعتبار قوتها؟
72- وَيُتْرَكُ الظَّاهِرُ لِلدَّلِيلِ .. وَسَمِّ هَذَا التَّرْكَ بِالتَّأْوِيلِ **
73- وَالـمُجْمَلَ اوْقِفْهُ عَلَى البَيَانِ .. وَالنَّصُّ لا يَـحْمِلُ مَعْنًى ثَانِ **
تقسيم دلالة المنطوق؟
74- وَقَسِّمِ الـمَنْطُوقَ: للصَّرِيحِ .. وَغَيْرِهِ فِي الـمَذْهَبِ الصَّحِيحِ **
75- فَغَيْرُهُ: دَلَالَةُ اقْتِضَاءِ .. إِشَارَةٌ، دَلالَةُ الإِيـمَاءِ **
تعاريف دلالات المنطوق غير الصريح؟
76- فَالِاقْتِضَا التَّقْدِيرُ فِي العِبَارَهْ .. مَا لمْ يُسَقْ مِنْ أَجْلِهِ: إِشَارَهْ **
77- إِنْ قُرِنَ الحُكْمُ بِوَصْفٍ جَاءَا .. عَلِّلْ بِهِ وَسَمِّهِ الإِيـمَاءَا **
أقسام دلالة المفهوم بالتفصيل؟
78- أَمَّا الـمَفَاهِيمُ فَقِسْمَانِ هُمَا: .. مُوَافِقٌ، مُخَالِفٌ قَدْ قُسِمَا: **
79- لِلشَّرْطِ، وَالوَصْفِ، وَقِسْمَةٍ، عَدَدْ .. وَغَايَةٍ، وَلَقَبٍ فَلْتُعْتَمَدْ **
هل يُعمل بمفهوم المخالفة دائماً؟
80- وَشَرْطُهَا: أَلَّا تَكُونَ خَرَجَتْ .. لِغَالِبٍ، أَوْ حَالَةٍ، أَوْ فُخِّمَتْ **
81- وَمِثْلُهَا: الجَوَابُ عَنْ سُؤَالِ .. زِيَادَةُ امْتِنَانِ ذِي الجَلَالِ **
هل الحصر من دلالة المنطوق أم المفهوم؟
82- وَ(إِنَّـمَا) نُطْقًا تُفِيدُ الحَصْرَا .. كَـ(النَّاظِمُ المَرِّيْ)، (صَدِيقِي الفَرَّا) **
الحُكام (المستدلون)؟
83- وَرَابِعًا: مَبَاحِثُ الـمُجْتَهِدِ .. وَضِدُّهُ الـمَوْصُوفُ بِالـمُقَلِّدِ **
شروط المجتهد؟
84- فَالأَوَّلُ العَالِمُ بِالأَدِلَّةِ .. ثُبُوتِها وَفَهْمِهَا وَاللُّغَةِ **
85- مَعْ فِقْهِ نَفْسٍ سَمِّهِ بِالـمَلَكَهْ .. بِجِدِّهِ فِي العِلْمِ حَتَّى مَلَكَهْ **
مجتهد في باب واحد؟
86- وَجَائِزٌ تَجَزُّؤُ اجْتِهَادِهِ .. فِيْ بَابٍ اوْ مَسْأَلةٍ مِنْ زَادِهِ **
حالات التعارض؟
87- لَدَى تَعَارُضِ الدَّلِيلَينِ اجْمَعِ .. فَانْسَخْ فَرَجّحْ ثُمَّ قِفْ لَا تَدَّعِي **
المرجحات؟
88- وَرَجِّحِ الأَقْوَى مِنَ الظُّنُونِ .. فِي الجِنْسِ وَالإِسْنَادِ وَالـمُتُونِ **
89- وَفِي دَلَالَةٍ وَأَمْرٍ خَارِجِ .. لَا حَصْرَ لِلتَّرْجِيحِ. تَمَّ مَا رُجِيْ **
90- وَاكْتَمَلَتْ مَبَاحِثُ الأُصُولِ .. وَصَلِّ يَارَبِّ عَلَى الرَّسُولِ **
"""


class MockModel:
    def __init__(self):
        self.properties = {}

    def __call__(self):
        return self.properties

    def by_name(self, name):
        return self


class MockCollection:
    def __init__(self):
        self.notes = []

    def add_note(self, note, deck_id):
        self.notes.append(note)

    @property
    def models(self):
        return MockModel()


class MockNote:
    def __init__(self, collection, ntype):
        self.collection = collection
        self.note_type = ntype
        self.tags = []
        self.properties = {}

    def __getitem__(self, item):
        return self.properties[item]

    def __setitem__(self, item, value):
        self.properties[item] = value

    def __delitem__(self, item):
        del self.properties[item]

    def __contains__(self, item):
        return item in self.properties


def mock_note():
    col = MockCollection()
    note_constructor = MockNote
    title = "Hello"
    tags = ["test"]
    deck_id = 1
    separator = "؟"
    question_marker = True
    chapter_marker = "#"
    text = cleanse_text(test_text)
    return dict(locals())


class TestGenNotes(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.mock_note = mock_note()

    def test_question_marker(self):
        added = add_notes(**self.mock_note)
        self.assertEqual(added, 57)
        notes = self.mock_note["col"].notes
        self.assertEqual(notes[0]["سؤال"], "مقدمة النظم الصغير؟")
        self.assertEqual(
            notes[0]["جواب"],
            "01- أَحْمَدُ رَبِّي وَاهِبَ العُقُولِ .. وَصَلِّ يَارَبِّ عَلَى الرَّسُولِ **<br>"
            "02- وَاكْتُبْ قَبُولَ نَظْمِيَ الصَّغِيرِ .. كَأَصْلِهِ مُخْتَصَرِ التَّحْرِيرِ **<br>"
            "03- إذْ مِنْهُ لَخَّصْتُ بِلا تَبْوِيبِ .. رَتَّبْتُهُ بِنَمَطٍ قَرِيبِ **",
        )
        self.assertEqual(notes[-1]["سؤال"], "المرجحات؟")
        self.assertEqual(
            notes[-1]["جواب"],
            "88- وَرَجِّحِ الأَقْوَى مِنَ الظُّنُونِ .. فِي الجِنْسِ وَالإِسْنَادِ وَالـمُتُونِ **<br>"
            "89- وَفِي دَلَالَةٍ وَأَمْرٍ خَارِجِ .. لَا حَصْرَ لِلتَّرْجِيحِ. تَمَّ مَا رُجِيْ **<br>"
            "90- وَاكْتَمَلَتْ مَبَاحِثُ الأُصُولِ .. وَصَلِّ يَارَبِّ عَلَى الرَّسُولِ **",
        )
        for note in notes:
            self.assertEqual(note["باب"], "النظم الصغير")

    def test_answer_marker(self):
        self.mock_note["question_marker"] = False
        self.mock_note["separator"] = "-"
        added = add_notes(**self.mock_note)
        self.assertEqual(added, 57)
        notes = self.mock_note["col"].notes
        self.assertEqual(notes[0]["سؤال"], "مقدمة النظم الصغير؟")
        self.assertEqual(
            notes[0]["جواب"],
            "01- أَحْمَدُ رَبِّي وَاهِبَ العُقُولِ .. وَصَلِّ يَارَبِّ عَلَى الرَّسُولِ **<br>"
            "02- وَاكْتُبْ قَبُولَ نَظْمِيَ الصَّغِيرِ .. كَأَصْلِهِ مُخْتَصَرِ التَّحْرِيرِ **<br>"
            "03- إذْ مِنْهُ لَخَّصْتُ بِلا تَبْوِيبِ .. رَتَّبْتُهُ بِنَمَطٍ قَرِيبِ **",
        )
        self.assertEqual(notes[-1]["سؤال"], "المرجحات؟")
        self.assertEqual(
            notes[-1]["جواب"],
            "88- وَرَجِّحِ الأَقْوَى مِنَ الظُّنُونِ .. فِي الجِنْسِ وَالإِسْنَادِ وَالـمُتُونِ **<br>"
            "89- وَفِي دَلَالَةٍ وَأَمْرٍ خَارِجِ .. لَا حَصْرَ لِلتَّرْجِيحِ. تَمَّ مَا رُجِيْ **<br>"
            "90- وَاكْتَمَلَتْ مَبَاحِثُ الأُصُولِ .. وَصَلِّ يَارَبِّ عَلَى الرَّسُولِ **",
        )
        for note in notes:
            self.assertEqual(note["باب"], "النظم الصغير")


if __name__ == "__main__":
    unittest.main()
