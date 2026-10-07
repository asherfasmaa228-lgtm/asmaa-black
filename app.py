
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Barik Pro - منظم وقتك الأسبوعي بني سويف</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:system-ui,Tajawal}
body{background:#0a1910;color:#f5e6c8;padding:8px}
.card{background:rgba(255,255,255,.06);border:1px solid rgba(212,175,55,.3);border-radius:20px;padding:14px;margin:10px auto;max-width:520px}
.logo{font-size:22px;font-weight:900;color:#d4af37}
.tab{display:flex;gap:6px;overflow-x:auto;margin:10px 0}
.tab button{min-width:70px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:#f5e6c8;border-radius:12px;padding:8px 12px;font-size:11px}
.tab button.on{background:#d4af37;color:#000;font-weight:800}
.sec{display:none}
.sec.on{display:block}
.pills{display:flex;gap:6px;overflow-x:auto}
.pill{min-width:62px;background:rgba(255,255,255,.06);border-radius:12px;padding:7px;text-align:center;font-size:10px;border:1px solid rgba(255,255,255,.1)}
.pill.next{background:#d4af37;color:#000;font-weight:800}
.day-grid{display:grid;grid-template-columns:60px 1fr;gap:6px}
.time{font-size:10px;opacity:.7;padding:8px 0;text-align:center;border-left:1px dashed rgba(212,175,55,.3)}
.slot{background:linear-gradient(90deg,rgba(212,175,55,.15),rgba(255,255,255,.03));border-radius:12px;padding:10px;margin:4px 0;border-right:4px solid #d4af37;display:flex;justify-content:space-between;align-items:center}
.slot.done{opacity:.5;border-right-color:#4caf50;background:rgba(76,175,80,.1)}
.btn{width:100%;background:#d4af37;color:#000;border:none;border-radius:14px;padding:12px;font-weight:900;margin-top:8px}
input,select,textarea{width:100%;background:rgba(0,0,0,.4);border:1px solid rgba(212,175,55,.3);color:#fff;border-radius:10px;padding:10px;margin:5px 0;font-size:13px}
.azkar{max-height:400px;overflow-y:auto}
.zekr{background:rgba(212,175,55,.1);border-radius:12px;padding:12px;margin:8px 0;border-right:3px solid #d4af37}
.quran-item{display:flex;justify-content:space-between;padding:10px;background:rgba(255,255,255,.04);border-radius:10px;margin:5px 0}
.small{font-size:10px;opacity:.7}
.note{background:rgba(255,255,255,.05);border:1px dashed #d4af37;border-radius:12px;padding:10px;margin:8px 0}
.progress{height:8px;background:rgba(255,255,255,.1);border-radius:10px;overflow:hidden;margin:8px 0}
.progress i{display:block;height:100%;background:#d4af37;width:0%}
.compass{width:120px;height:120px;border:3px solid #d4af37;border-radius:50%;margin:10px auto;position:relative}
.needle{position:absolute;top:50%;left:50%;width:3px;height:55px;background:red;transform-origin:bottom;transform:translate(-50%,-100%) rotate(132deg)}
</style>
</head>
<body>

<div class="card" style="display:flex;justify-content:space-between;align-items:center">
<div><div class="logo">بريك | Barik Pro</div><div class="small">بني سويف - الشروق 6:52 | الظهر 12:43 | منظم أسبوعي شامل</div></div>
<div id="now" style="font-size:11px;background:#d4af37;color:#000;padding:5px 10px;border-radius:20px;font-weight:800">6:20 م</div>
</div>

<div class="card">
<div class="pills" id="pills"></div>
<div class="small" style="margin-top:6px">الفجر 5:27 - الشروق 6:52 - الظهر 12:43 - العصر 4:04 - المغرب 6:34 - العشاء 7:50</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px">
<div style="background:rgba(212,175,55,.15);padding:8px;border-radius:12px;text-align:center"><div class="small">القادمة</div><div style="font-weight:900" id="nextP">المغرب 6:34</div><div class="small" id="count">بعد 14:00</div></div>
<div class="qibla" style="background:rgba(0,0,0,.3);padding:8px;border-radius:12px;text-align:center"><div class="small">القبلة 132°</div><div class="compass" style="width:70px;height:70px;margin:5px auto"><div style="position:absolute;top:5%;left:50%;transform:translateX(-50%);font-size:12px">🕋</div><div class="needle" id="needle"></div></div><button onclick="startQ()" style="font-size:9px;background:#fff;border:none;border-radius:8px;padding:3px 8px">فعّلي البوصلة</button></div>
</div>
</div>

<div class="card">
<div class="tab">
<button class="on" onclick="openTab('week')">📅 الأسبوع</button>
<button onclick="openTab('azkar')">📿 الأذكار</button>
<button onclick="openTab('quran')">📖 القرآن</button>
<button onclick="openTab('learn')">📚 فقه وقصص</button>
<button onclick="openTab('review')">📝 يومي</button>
</div>

<!-- الأسبوع -->
<div id="week" class="sec on">
<div style="display:flex;justify-content:space-between;align-items:center"><b>جدولك الأسبوعي</b><select id="daySel" onchange="renderWeek()" style="width:auto"><option value="0">السبت</option><option value="1">الأحد</option><option value="2">الإثنين</option><option value="3" selected>الثلاثاء</option><option value="4">الأربعاء</option><option value="5">الخميس</option><option value="6">الجمعة</option></select></div>
<div class="progress"><i id="prog"></i></div>
<div class="small" id="progT">0% مكتمل اليوم</div>
<div id="weekGrid"></div>
<div style="background:rgba(255,255,255,.04);border-radius:14px;padding:10px;margin-top:10px">
<b style="font-size:12px">+ أضيفي وقت جديد</b>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
<select id="nType"><option>📚 درس / مذاكرة</option><option>🚿 عناية بالنفس - شاور</option><option>💪 رياضة - مشي / يوجا</option><option>🈶 لغة جديدة - كوري</option><option>🎨 رسم / برمجة / تطبيق</option><option>🗣️ ثقة بالنفس / إلقاء</option><option>🧘‍♀️ وقت لنفسك</option><option>👩‍👧‍👦 عائلة</option></select>
<input id="nTime" type="time" value="17:00">
</div>
<input id="nTitle" placeholder="مثلاً: مذاكرة كوري TOPIK / مشي 30 دقيقة / شاور واسترخاء / تعلم برمجة تطبيق">
<button class="btn" onclick="addSlot()">+ أضيفي للجدول</button>
</div>
</div>

<!-- الأذكار -->
<div id="azkar" class="sec">
<div class="tab" style="margin-top:0"><button class="on" onclick="filterZ('all')">الكل</button><button onclick="filterZ('morning')">الصباح</button><button onclick="filterZ('evening')">المساء</button><button onclick="filterZ('prayer')">بعد الصلاة</button><button onclick="filterZ('sleep')">النوم</button></div>
<div class="azkar" id="azkarList"></div>
</div>

<!-- القرآن -->
<div id="quran" class="sec">
<input id="qSearch" placeholder="ابحثي عن سورة... مثلاً البقرة / يس / الملك" oninput="searchQ()">
<div id="quranList" style="max-height:400px;overflow-y:auto;margin-top:8px"></div>
<div class="card" style="background:rgba(212,175,55,.1);margin:10px 0">
<b>📖 مصحف القراءة</b>
<div id="quranRead" style="font-size:14px;line-height:2;margin-top:8px;max-height:300px;overflow-y:auto">اختاري سورة للقراءة...<br><br>بسم الله الرحمن الرحيم<br>مصحف كامل - تقدري تقري أي سورة - لو عايزة المصحف الكامل افتحي: quran.com</div>
<button class="btn" style="background:#fff;color:#000" onclick="window.open('https://quran.com/ar','_blank')">افتحي المصحف الكامل</button>
</div>
</div>

<!-- فقه وقصص -->
<div id="learn" class="sec">
<div class="quran-item"><div><b>📘 فقه الصلاة</b><div class="small">أركان - واجبات - سنن - مبطلات</div></div><button onclick="showFiqh('salah')" style="background:#d4af37;border:none;border-radius:8px;padding:6px 10px">اقرأي</button></div>
<div class="quran-item"><div><b>📗 فقه الوضوء</b><div class="small">فرائض وسنن الوضوء</div></div><button onclick="showFiqh('wudu')" style="background:#d4af37;border:none;border-radius:8px;padding:6px 10px">اقرأي</button></div>
<div class="quran-item"><div><b>📕 قصص الأنبياء</b><div class="small">قصص للعبرة - يوسف - مريم - موسى</div></div><button onclick="showFiqh('stories')" style="background:#d4af37;border:none;border-radius:8px;padding:6px 10px">اقرأي</button></div>
<div class="quran-item"><div><b>💡 تعلم مهارة</b><div class="small">برمجة تطبيقات - رسم - ثقة بالنفس</div></div><button onclick="showFiqh('skill')" style="background:#d4af37;border:none;border-radius:8px;padding:6px 10px">ابدأي</button></div>
<div id="fiqhBox" class="card" style="display:none"></div>
</div>

<!-- المراجعة اليومية -->
<div id="review" class="sec">
<b>📝 مراجعة يوم الثلاثاء - 6 أكتوبر</b>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:8px 0">
<div style="background:rgba(76,175,80,.15);padding:10px;border-radius:12px;text-align:center"><div style="font-size:22px;font-weight:900" id="doneC">0</div><div class="small">عملت</div></div>
<div style="background:rgba(255,59,48,.15);padding:10px;border-radius:12px;text-align:center"><div style="font-size:22px;font-weight:900" id="missC">0</div><div class="small">معملتش</div></div>
</div>
<textarea id="dailyNote" rows="4" placeholder="اكتبي هنا: النهارده عملت ايه؟ ايه اللي معملتوش؟ حسيتي بإيه؟ بكرة هتحسني ايه؟ - النوتة دي بتتحفظ تلقائي..."></textarea>
<button class="btn" onclick="saveNote()">💾 احفظي نوتة اليوم</button>
<div id="notesHistory" style="margin-top:10px"></div>
</div>

</div>
</div>

<script>
const prayers=[{n:'الفجر',t:'05:27'},{n:'الشروق',t:'06:52'},{n:'الظهر',t:'12:43'},{n:'العصر',t:'16:04'},{n:'المغرب',t:'18:34'},{n:'العشاء',t:'19:50'}];
function renderP(){
let el=document.getElementById('pills'); el.innerHTML='';
prayers.forEach(p=>{
let cls=p.t=='06:52'?'pill next':(p.t=='12:43'?'pill next':'pill');
if(p.n=='المغرب') cls='pill next';
el.innerHTML+=`<div class="${cls}"><div>${p.n}</div><b>${p.t}</b></div>`;
});
}
let weekData=JSON.parse(localStorage.getItem('barikWeek')||'null') || {
0:[{time:'08:00',type:'📚 درس / مذاكرة',title:'مذاكرة المنحة الكورية',done:false},{time:'11:00',type:'💪 رياضة - مشي / يوجا',title:'مشي 30 دقيقة أو يوجا',done:false},{time:'13:00',type:'🚿 عناية بالنفس - شاور',title:'شاور + عناية',done:false},{time:'17:00',type:'🈶 لغة جديدة - كوري',title:'كوري 20 كلمة',done:false}],
1:[],2:[],3:[{time:'05:40',type:'📿 الأذكار',title:'أذكار بعد الفجر 5:27',done:false},{time:'06:52',type:'📖 قرآن',title:'قراءة قرآن بعد الشروق 6:52',done:false},{time:'09:00',type:'📚 درس / مذاكرة',title:'دروس المنحة',done:false},{time:'12:50',type:'📚 درس / مذاكرة',title:'مراجعة بعد الظهر 12:43',done:false},{time:'15:00',type:'🚿 عناية بالنفس - شاور',title:'وقت لنفسك - شاور',done:false},{time:'16:30',type:'💪 رياضة - مشي / يوجا',title:'يوجا أو مشي',done:false},{time:'17:30',type:'🎨 رسم / برمجة / تطبيق',title:'تعلم برمجة تطبيق أو رسم',done:false},{time:'18:40',type:'📿 الأذكار',title:'أذكار المساء قبل المغرب',done:false}],4:[],5:[],6:[]
};
let curDay=3;
function renderWeek(){
curDay=parseInt(document.getElementById('daySel').value);
let list=weekData[curDay]||[];
list.sort((a,b)=>a.time.localeCompare(b.time));
let el=document.getElementById('weekGrid'); el.innerHTML='';
let done=0;
list.forEach((s,i)=>{
if(s.done) done++;
el.innerHTML+=`<div class="day-grid"><div class="time">${s.time}</div><div class="slot ${s.done?'done':''}" onclick="toggleSlot(${i})"><div><div style="font-size:12px;font-weight:700">${s.type}</div><div style="font-size:11px">${s.title}</div></div><div>${s.done?'✅':'⭕'}</div></div></div>`;
});
let perc=list.length?Math.round(done/list.length*100):0;
document.getElementById('prog').style.width=perc+'%';
document.getElementById('progT').innerText=perc+'% مكتمل - '+done+' من '+list.length;
document.getElementById('doneC').innerText=done;
document.getElementById('missC').innerText=list.length-done;
localStorage.setItem('barikWeek',JSON.stringify(weekData));
}
function toggleSlot(i){ weekData[curDay][i].done=!weekData[curDay][i].done; renderWeek(); saveNoteAuto(); }
function addSlot(){
let t=document.getElementById('nTime').value, ty=document.getElementById('nType').value, ti=document.getElementById('nTitle').value;
if(!ti) ti=ty;
weekData[curDay].push({time:t,type:ty,title:ti,done:false});
document.getElementById('nTitle').value=''; renderWeek();
}

const allAzkar=[
{cat:'morning',title:'أذكار الصباح (بعد الفجر 5:27)',text:'أصبحنا وأصبح الملك لله، لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير. (3 مرات)'},
{cat:'morning',title:'آية الكرسي',text:'الله لا إله إلا هو الحي القيوم...'},
{cat:'morning',title:'المعوذات',text:'قل هو الله أحد والمعوذتين 3 مرات'},
{cat:'evening',title:'أذكار المساء (قبل المغرب 6:34)',text:'أمسينا وأمسى الملك لله، لا إله إلا الله وحده لا شريك له...'},
{cat:'evening',title:'أذكار المساء - التسبيح',text:'سبحان الله وبحمده 100 مرة'},
{cat:'prayer',title:'بعد الصلاة',text:'أستغفر الله 3، اللهم أنت السلام ومنك السلام، لا إله إلا الله وحده لا شريك له...'},
{cat:'prayer',title:'التسبيح بعد الصلاة',text:'سبحان الله 33، الحمد لله 33، الله أكبر 33، ثم لا إله إلا الله'},
{cat:'sleep',title:'أذكار النوم',text:'باسمك اللهم أموت وأحيا، آية الكرسي، سورة الملك'},
{cat:'sleep',title:'دعاء قبل النوم',text:'اللهم أسلمت نفسي إليك ووجهت وجهي إليك...'},
{cat:'all',title:'دعاء الهم',text:'لا إله إلا الله العظيم الحليم، لا إله إلا الله رب العرش العظيم...'},
{cat:'all',title:'الاستغفار',text:'أستغفر الله العظيم الذي لا إله إلا هو الحي القيوم وأتوب إليه 100 مرة'}
];
function renderAzkar(filter='all'){
let el=document.getElementById('azkarList'); el.innerHTML='';
allAzkar.filter(z=>filter=='all'||z.cat==filter).forEach(z=>{
el.innerHTML+=`<div class="zekr"><b style="font-size:12px">${z.title}</b><div style="font-size:12px;margin-top:6px;line-height:1.8">${z.text}</div><div style="margin-top:8px"><button onclick="this.innerText='✅ تم'" style="background:#d4af37;border:none;border-radius:8px;padding:4px 10px;font-size:10px">قرأته ✅</button></div></div>`;
});
}
function filterZ(c){ renderAzkar(c); }

const surahs=['الفاتحة','البقرة','آل عمران','النساء','المائدة','الأنعام','الأعراف','الأنفال','التوبة','يونس','هود','يوسف','الرعد','إبراهيم','الحجر','النحل','الإسراء','الكهف','مريم','طه','الأنبياء','الحج','المؤمنون','النور','الفرقان','الشعراء','النمل','القصص','العنكبوت','الروم','لقمان','السجدة','الأحزاب','سبأ','فاطر','يس','الصافات','ص','الزمر','غافر','فصلت','الشورى','الزخرف','الدخان','الجاثية','الأحقاف','محمد','الفتح','الحجرات','ق','الذاريات','الطور','النجم','القمر','الرحمن','الواقعة','الحديد','المجادلة','الحشر','الممتحنة','الصف','الجمعة','المنافقون','التغابن','الطلاق','التحريم','الملك','القلم','الحاقة','المعارج','نوح','الجن','المزمل','المدثر','القيامة','الإنسان','المرسلات','النبأ','النازعات','عبس','التكوير','الانفطار','المطففين','الانشقاق','البروج','الطارق','الأعلى','الغاشية','الفجر','البلد','الشمس','الليل','الضحى','الشرح','التين','العلق','القدر','البينة','الزلزلة','العاديات','القارعة','التكاثر','العصر','الهمزة','الفيل','قريش','الماعون','الكوثر','الكافرون','النصر','المسد','الإخلاص','الفلق','الناس'];
function renderQuran(){
let el=document.getElementById('quranList'); el.innerHTML='';
surahs.forEach((s,i)=>{ el.innerHTML+=`<div class="quran-item"><div><b>${i+1}. ${s}</b><div class="small">الجزء ${Math.ceil((i+1)/4)}</div></div><button onclick="readSura('${s}')" style="background:#d4af37;border:none;border-radius:8px;padding:6px 10px">اقرأي</button></div>`; });
}
function searchQ(){ let q=document.getElementById('qSearch').value; let el=document.getElementById('quranList'); el.innerHTML=''; surahs.filter(s=>s.includes(q)).forEach((s,i)=>{ el.innerHTML+=`<div class="quran-item"><div><b>${s}</b></div><button onclick="readSura('${s}')" style="background:#d4af37;border:none;border-radius:8px;padding:6px 10px">اقرأي</button></div>`; }); }
function readSura(name){ document.getElementById('quranRead').innerHTML=`<b>سورة ${name}</b><br><br>جاري تحميل السورة...<br><br><i>بسم الله الرحمن الرحيم</i><br>افتحي المصحف الكامل من الزر تحت للقراءة الكاملة بجودة عالية مع التفسير.`; window.open('https://quran.com/ar/'+(surahs.indexOf(name)+1),'_blank'); }

function showFiqh(type){
let box=document.getElementById('fiqhBox'); box.style.display='block';
let content={
salah:'<b>فقه الصلاة - بني سويف 12:43 ظهراً</b><br><br>أركان الصلاة: النية، القيام، الفاتحة، الركوع، السجود...<br>الظهر 12:43 - 4 ركعات فرض، 4 سنة قبل، 2 بعد<br>العصر 4:04 - 4 فرض<br>المغرب 6:34 - 3 فرض + 2 سنة',
wudu:'<b>فقه الوضوء</b><br>فرائض: غسل الوجه، اليدين للمرفقين، مسح الرأس، غسل الرجلين<br>سنن: البسملة، السواك، المضمضة 3، الاستنشاق 3...',
stories:'<b>قصص الأنبياء</b><br>قصة يوسف: صبر على البلاء فصار عزيز مصر<br>قصة مريم: طهارة وعفة<br>قصة موسى: مواجهة الظلم',
skill:'<b>تعلم مهارة جديدة</b><br>1. برمجة تطبيقات: ابدأي بـ MIT App Inventor<br>2. رسم: 10 دقائق يومياً<br>3. ثقة بالنفس: قفي أمام المرآة وتكلمي 2 دقيقة يومياً<br>4. لغة كورية: تطبيق Duolingo + كلمات يومية'
};
box.innerHTML=content[type];
}

function openTab(id){ document.querySelectorAll('.sec').forEach(s=>s.classList.remove('on')); document.getElementById(id).classList.add('on'); document.querySelectorAll('.tab button').forEach(b=>b.classList.remove('on')); event.target.classList.add('on'); }
function saveNote(){
let txt=document.getElementById('dailyNote').value; if(!txt) return;
let notes=JSON.parse(localStorage.getItem('barikNotes')||'[]');
notes.push({date:new Date().toLocaleDateString('ar-EG'),day:'الثلاثاء 6 أكتوبر',text:txt});
localStorage.setItem('barikNotes',JSON.stringify(notes));
document.getElementById('dailyNote').value=''; renderNotes();
}
function saveNoteAuto(){}
function renderNotes(){
let notes=JSON.parse(localStorage.getItem('barikNotes')||'[]');
let el=document.getElementById('notesHistory'); el.innerHTML='<b style="font-size:11px">نوتاتك السابقة:</b>';
notes.slice(-3).reverse().forEach(n=>{ el.innerHTML+=`<div class="note"><div class="small">${n.date} - ${n.day}</div><div style="font-size:11px;margin-top:4px">${n.text}</div></div>`; });
}
function startQ(){ if(DeviceOrientationEvent.requestPermission){ DeviceOrientationEvent.requestPermission().then(p=>{ if(p=='granted') window.addEventListener('deviceorientation',e=>{ let h=e.webkitCompassHeading||(360-e.alpha); document.getElementById('needle').style.transform=`translate(-50%,-100%) rotate(${132-h}deg)`; }); }); } }

let base=new Date(); base.setHours(18,20,0);
setInterval(()=>{ base.setSeconds(base.getSeconds()+1); let h=base.getHours(); let m=String(base.getMinutes()).padStart(2,'0'); document.getElementById('now').innerText=h+':'+m+' - بني سويف'; let target=new Date(base); target.setHours(18,34,0); let diff=Math.floor((target-base)/1000); if(diff>0){ let mm=Math.floor(diff/60), ss=diff%60; document.getElementById('count').innerText='بعد '+mm+':'+String(ss).padStart(2,'0')+' للمغرب'; document.getElementById('nextP').innerText='المغرب 6:34 بعد '+mm+' د'; } },1000);

renderP(); renderWeek(); renderAzkar(); renderQuran(); renderNotes();
</script>
</body>
</html>