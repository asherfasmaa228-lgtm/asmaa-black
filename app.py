import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Barik Pro - بني سويف", page_icon="🕌", layout="centered")

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Barik Pro - بني سويف</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:system-ui,Tajawal,Cairo}
body{background:#07120b;color:#f5e6c8;padding:8px}
.card{background:rgba(255,255,255,.06);border:1px solid rgba(212,175,55,.32);border-radius:20px;padding:14px;margin:10px auto;max-width:560px;backdrop-filter:blur(6px)}
.logo{font-size:22px;font-weight:900;color:#d4af37}
.tab{display:flex;gap:6px;overflow-x:auto;margin:10px 0;padding-bottom:4px}
.tab button{min-width:74px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);color:#f5e6c8;border-radius:12px;padding:9px 12px;font-size:11px;cursor:pointer}
.tab button.on{background:#d4af37;color:#000;font-weight:900}
.sec{display:none}
.sec.on{display:block}
.pills{display:flex;gap:6px;overflow-x:auto}
.pill{min-width:70px;background:rgba(255,255,255,.06);border-radius:14px;padding:8px;text-align:center;font-size:10px;border:1px solid rgba(255,255,255,.1)}
.pill.next{background:#d4af37;color:#000;font-weight:900;transform:scale(1.06)}
.day-grid{display:grid;grid-template-columns:58px 1fr;gap:6px}
.time{font-size:10px;opacity:.75;padding:10px 0;text-align:center;border-left:1px dashed rgba(212,175,55,.35)}
.slot{background:linear-gradient(90deg,rgba(212,175,55,.18),rgba(255,255,255,.04));border-radius:14px;padding:11px;margin:5px 0;border-right:5px solid #d4af37;display:flex;justify-content:space-between;align-items:center;cursor:pointer}
.slot.done{opacity:.5;border-right-color:#4caf50;background:rgba(76,175,80,.12)}
.slot.study{border-right-color:#4da3ff}
.slot.sport{border-right-color:#ff6b6b}
.slot.self{border-right-color:#c792ea}
.slot.skill{border-right-color:#ffd166}
.btn{width:100%;background:#d4af37;color:#000;border:none;border-radius:14px;padding:13px;font-weight:900;margin-top:8px;cursor:pointer}
.btn2{background:#fff;color:#000;border-radius:10px;border:none;padding:8px 14px;font-weight:800;cursor:pointer}
input,select,textarea{width:100%;background:rgba(0,0,0,.45);border:1px solid rgba(212,175,55,.35);color:#fff;border-radius:12px;padding:11px;margin:6px 0;font-size:13px}
.zekr{background:rgba(212,175,55,.1);border-radius:14px;padding:12px;margin:9px 0;border-right:4px solid #d4af37}
.quran-item{display:flex;justify-content:space-between;align-items:center;padding:11px;background:rgba(255,255,255,.05);border-radius:12px;margin:6px 0}
.small{font-size:11px;opacity:.75}
.progress{height:10px;background:rgba(255,255,255,.1);border-radius:10px;overflow:hidden;margin:10px 0}
.progress i{display:block;height:100%;background:linear-gradient(90deg,#d4af37,#ffef8a);width:0%;transition:.4s}
.counter{font-size:34px;font-weight:900;text-align:center;margin:8px 0}
.note{background:rgba(255,255,255,.05);border:1px dashed #d4af37;border-radius:12px;padding:10px;margin:8px 0}
</style>
</head>
<body>

<audio id="adhanAudio" src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>

<div class="card" style="display:flex;justify-content:space-between;align-items:center">
<div><div class="logo">بريك | Barik Pro</div><div class="small" id="hijri">بني سويف - جاري تحميل المواقيت...</div></div>
<div id="now" style="font-size:12px;background:#d4af37;color:#000;padding:6px 12px;border-radius:20px;font-weight:900">--:--</div>
</div>

<div class="card">
<div class="pills" id="pills"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px">
<div style="background:rgba(212,175,55,.16);padding:12px;border-radius:14px;text-align:center">
<div class="small">الصلاة القادمة</div><div style="font-weight:900;font-size:18px" id="nextP">--</div><div class="small" id="count">--</div>
<button class="btn2" style="margin-top:8px" onclick="enableNotif()">🔔 فعلي التذكير والأذان</button>
</div>
<div style="background:rgba(0,0,0,.35);padding:12px;border-radius:14px;text-align:center">
<div class="small">القبلة - بني سويف 132°</div><div style="font-size:36px;margin:6px 0">🕋</div>
<div class="small">الفجر القادم: <b id="fajrNext">--</b></div>
</div>
</div>
</div>

<div class="card">
<div class="tab">
<button class="on" onclick="openTab('week',this)">📅 أسبوعي</button>
<button onclick="openTab('azkar',this)">📿 أذكار</button>
<button onclick="openTab('sala',this)">ﷺ النبي</button>
<button onclick="openTab('quran',this)">📖 قرآن</button>
<button onclick="openTab('skills',this)">💡 مهارات</button>
</div>

<div id="week" class="sec on">
<div style="display:flex;justify-content:space-between;align-items:center"><b>جدولك - دروس/رياضة/نفسك</b><select id="daySel" onchange="renderWeek()" style="width:auto"><option value="0">السبت</option><option value="1">الأحد</option><option value="2">الإثنين</option><option value="3" selected>الثلاثاء</option><option value="4">الأربعاء</option><option value="5">الخميس</option><option value="6">الجمعة</option></select></div>
<div class="progress"><i id="prog"></i></div>
<div class="small" id="progT">0%</div>
<div id="weekGrid"></div>
<div style="background:rgba(255,255,255,.04);border-radius:14px;padding:12px;margin-top:12px">
<b style="font-size:12px">+ أضيفي مهمة</b>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
<select id="nType">
<option value="📚 درس / مذاكرة">📚 درس / مذاكرة</option>
<option value="💪 رياضة - مشي / يوجا">💪 رياضة - مشي / يوجا</option>
<option value="🚿 وقت لنفسك - شاور">🚿 وقت لنفسك - شاور</option>
<option value="🈶 مهارة جديدة - كوري">🈶 مهارة جديدة - كوري</option>
<option value="🎨 مهارة جديدة - برمجة">🎨 مهارة جديدة - برمجة</option>
<option value="✍️ مهارة جديدة - رسم">✍️ مهارة جديدة - رسم</option>
<option value="🗣️ ثقة بالنفس">🗣️ ثقة بالنفس / إلقاء</option>
</select>
<input id="nTime" type="time" value="17:00">
</div>
<input id="nTitle" placeholder="مثال: TOPIK كوري 20 كلمة / مشي 30د / برمجة تطبيق / مذاكرة منحة">
<button class="btn" onclick="addSlot()">+ أضيفي مع تذكير</button>
</div>
</div>

<div id="azkar" class="sec"><div id="azkarList"></div></div>

<div id="sala" class="sec">
<div style="text-align:center;padding:10px">
<div style="font-size:18px;font-weight:900">الصلاة على النبي ﷺ</div>
<div class="small">قال ﷺ: من صلى علي واحدة صلى الله عليه عشرا</div>
<div class="counter" id="salaCount">0</div>
<button class="btn" onclick="incSala()">ﷺ صلي على النبي</button>
<button class="btn" style="background:#fff;margin-top:6px" onclick="resetSala()">تصفير</button>
<div class="small" style="margin-top:10px">هدف اليوم: 100 مرة - هتوصلي؟</div>
<div class="progress"><i id="salaProg"></i></div>
</div>
</div>

<div id="quran" class="sec">
<input id="qSearch" placeholder="ابحثي: البقرة، الكهف، يس، الملك..." oninput="searchQ()">
<div id="quranList" style="max-height:380px;overflow-y:auto;margin-top:8px"></div>
<button class="btn" style="background:#fff;color:#000" onclick="window.open('https://quran.com/ar','_blank')">افتحي المصحف الكامل مع التفسير</button>
</div>

<div id="skills" class="sec">
<div class="quran-item"><div><b>🈶 كوري - TOPIK</b><div class="small">20 كلمة يوميا + جملة</div></div><button class="btn2" onclick="startSkill('كوري')">ابدأي</button></div>
<div class="quran-item"><div><b>🎨 برمجة تطبيقات</b><div class="small">MIT App Inventor - تطبيقك Barik</div></div><button class="btn2" onclick="startSkill('برمجة')">ابدأي</button></div>
<div class="quran-item"><div><b>💪 رياضة - يوجا / مشي</b><div class="small">30 دقيقة يوميا لبني سويف</div></div><button class="btn2" onclick="startSkill('رياضة')">ابدأي</button></div>
<div class="quran-item"><div><b>🚿 وقت لنفسك</b><div class="small">شاور + سكين كير + استرخاء</div></div><button class="btn2" onclick="startSkill('نفسك')">وقتي</button></div>
<div id="skillBox" class="card" style="display:none;margin:10px 0"></div>
</div>

</div>
</div>

<script>
let prayersToday=[];
let prayerDateStr="";
async function loadPrayers(){
 try{
  let res= await fetch('https://api.aladhan.com/v1/timingsByCity/07-10-2026?city=Beni%20Suef&country=Egypt&method=5');
  let data= await res.json();
  let t=data.data.timings;
  let d=data.data.date.hijri;
  document.getElementById('hijri').innerText=`بني سويف - ${d.day} ${d.month.ar} ${d.year} هـ | ميلادي: ${data.data.date.gregorian.date}`;
  prayersToday=[
   {n:'الفجر',t:t.Fajr},
   {n:'الشروق',t:t.Sunrise},
   {n:'الظهر',t:t.Dhuhr},
   {n:'العصر',t:t.Asr},
   {n:'المغرب',t:t.Maghrib},
   {n:'العشاء',t:t.Isha}
  ];
  document.getElementById('fajrNext').innerText=prayersToday[0].t;
  renderP();
 }catch(e){
  prayersToday=[{n:'الفجر',t:'04:42'},{n:'الشروق',t:'06:05'},{n:'الظهر',t:'11:55'},{n:'العصر',t:'15:16'},{n:'المغرب',t:'17:43'},{n:'العشاء',t:'19:00'}];
  renderP();
 }
}
function renderP(){
 let el=document.getElementById('pills'); el.innerHTML='';
 prayersToday.forEach(p=>{ el.innerHTML+=`<div class="pill" id="pill-${p.n}"><div>${p.n}</div><b>${p.t}</b></div>`;});
}

function parseTime(str){let [h,m]=str.split(':').map(Number);let d=new Date();d.setHours(h,m,0,0);return d;}

let lastAdhan="";
function updateNext(){
 if(!prayersToday.length) return;
 let now=new Date();
 document.getElementById('now').innerText=now.toLocaleTimeString('ar-EG',{hour:'2-digit',minute:'2-digit'})+' - بني سويف';
 let next=null; let nextTime=null;
 for(let p of prayersToday){
   let pt=parseTime(p.t);
   if(pt>now){next=p;nextTime=pt;break;}
 }
 if(!next){ // بعد العشاء -> الفجر بكرة
   let pt=parseTime(prayersToday[0].t); pt.setDate(pt.getDate()+1);
   next={n:'الفجر (بكرة)',t:prayersToday[0].t}; nextTime=pt;
   document.getElementById('fajrNext').innerText=prayersToday[0].t + ' بكرة';
 }
 document.querySelectorAll('.pill').forEach(e=>e.classList.remove('next'));
 let baseName=next.n.replace(' (بكرة)','');
 let pill=document.getElementById('pill-'+baseName); if(pill) pill.classList.add('next');
 document.getElementById('nextP').innerText=next.n+' '+next.t;
 let diff=Math.floor((nextTime-now)/1000);
 let mm=Math.floor(diff/60), ss=diff%60, hh=Math.floor(mm/60);
 let left=hh>0? `${hh} س ${mm%60} د` : `${mm} د ${ss} ث`;
 document.getElementById('count').innerText='بعد '+left;
 // أذان
 let nowHM=now.getHours()+':'+String(now.getMinutes()).padStart(2,'0');
 if(prayersToday.some(p=>p.t===nowHM) && lastAdhan!==nowHM){
   lastAdhan=nowHM;
   let p=prayersToday.find(x=>x.t===nowHM);
   triggerAdhan(p.n);
 }
 // تذكير دراسة / رياضة
 checkStudyReminder(now);
}

function triggerAdhan(name){
 document.getElementById('adhanAudio').play().catch(()=>{});
 if(Notification && Notification.permission==='granted'){
   new Notification(`🕌 حان الآن ${name} - بني سويف`,{body:`قومي صلي يا أسماء - ${name} ${prayersToday.find(p=>p.n.includes(name))?.t||''}`});
 }
 alert(`🕌 حان الآن وقت ${name} - بني سويف\\nقومي للصلاة يا أسماء`);
}

function enableNotif(){
 if(Notification){Notification.requestPermission().then(p=>{ if(p==='granted') alert('تمام! هذكرك بالصلاة والمذاكرة والرياضة');});}
 document.getElementById('adhanAudio').play().then(()=>{document.getElementById('adhanAudio').pause();}).catch(()=>{});
}

let weekData=JSON.parse(localStorage.getItem('barikWeekV2')||'null') || {
0:[{time:'08:00',type:'📚 درس / مذاكرة',title:'مذاكرة المنحة الكورية - كلمات TOPIK',done:false},{time:'11:00',type:'💪 رياضة - مشي / يوجا',title:'مشي 30 دقيقة',done:false},{time:'15:00',type:'🚿 وقت لنفسك - شاور',title:'شاور + عناية',done:false}],
1:[],2:[],
3:[{time:'04:50',type:'📿 الأذكار',title:'أذكار + صلاة على النبي قبل الفجر',done:false},{time:'05:30',type:'📖 قرآن',title:'قراءة بعد الشروق',done:false},{time:'09:00',type:'📚 درس / مذاكرة',title:'دروس المنحة',done:false},{time:'12:10',type:'📚 درس / مذاكرة',title:'مراجعة بعد الظهر',done:false},{time:'16:00',type:'💪 رياضة - مشي / يوجا',title:'يوجا 20د',done:false},{time:'17:30',type:'🈶 مهارة جديدة - كوري',title:'كوري 20 كلمة',done:false},{time:'18:00',type:'🎨 مهارة جديدة - برمجة',title:'تعلم برمجة تطبيق Barik',done:false},{time:'19:30',type:'🚿 وقت لنفسك - شاور',title:'وقت لنفسك',done:false}],
4:[],5:[],6:[]
};
let curDay=3;
function renderWeek(){
 curDay=parseInt(document.getElementById('daySel').value);
 let list=weekData[curDay]||[]; list.sort((a,b)=>a.time.localeCompare(b.time));
 let el=document.getElementById('weekGrid'); el.innerHTML=''; let done=0;
 list.forEach((s,i)=>{
  if(s.done) done++;
  let cls=''; if(s.type.includes('درس')) cls='study'; if(s.type.includes('رياضة')) cls='sport'; if(s.type.includes('نفسك')) cls='self'; if(s.type.includes('مهارة')) cls='skill';
  el.innerHTML+=`<div class="day-grid"><div class="time">${s.time}</div><div class="slot ${cls} ${s.done?'done':''}" onclick="toggleSlot(${i})"><div><div style="font-size:12px;font-weight:800">${s.type}</div><div style="font-size:11px">${s.title}</div></div><div>${s.done?'✅':'⭕'}</div></div></div>`;
 });
 let perc=list.length?Math.round(done/list.length*100):0;
 document.getElementById('prog').style.width=perc+'%';
 document.getElementById('progT').innerText=perc+'% مكتمل - '+done+' من '+list.length;
 localStorage.setItem('barikWeekV2',JSON.stringify(weekData));
}
function toggleSlot(i){weekData[curDay][i].done=!weekData[curDay][i].done; renderWeek();}
function addSlot(){
 let t=document.getElementById('nTime').value, ty=document.getElementById('nType').value, ti=document.getElementById('nTitle').value||ty;
 weekData[curDay].push({time:t,type:ty,title:ti,done:false});
 document.getElementById('nTitle').value=''; renderWeek();
}
function checkStudyReminder(now){
 let list=weekData[curDay]||[];
 let hm=now.getHours()+':'+String(now.getMinutes()).padStart(2,'0');
 list.forEach(s=>{
   if(s.time===hm &&!s.done && Notification && Notification.permission==='granted'){
     new Notification(`⏰ ${s.type}`,{body:s.title});
   }
 });
}

const allAzkar=[
{title:'أذكار الصباح بعد الفجر',text:'أصبحنا وأصبح الملك لله، لا إله إلا الله وحده لا شريك له... 3 مرات'},
{title:'آية الكرسي',text:'الله لا إله إلا هو الحي القيوم لا تأخذه سنة ولا نوم...'},
{title:'أذكار المساء قبل المغرب 6:34',text:'أمسينا وأمسى الملك لله، سبحان الله وبحمده 100 مرة'},
{title:'بعد الصلاة',text:'أستغفر الله 3، اللهم أنت السلام ومنك السلام، سبحان الله 33 الحمد لله 33 الله أكبر 33'},
{title:'أذكار النوم + الملك',text:'باسمك اللهم أموت وأحيا، سورة الملك تنجي من عذاب القبر'},
];
function renderAzkar(){let el=document.getElementById('azkarList'); el.innerHTML=''; allAzkar.forEach(z=>{el.innerHTML+=`<div class="zekr"><b>${z.title}</b><div style="margin-top:6px;line-height:1.8">${z.text}</div><div style="margin-top:8px"><button class="btn2" onclick="this.innerText='✅ تم'">قرأته ✅</button></div></div>`;});}

let sala=parseInt(localStorage.getItem('salaCount')||'0');
function renderSala(){document.getElementById('salaCount').innerText=sala; document.getElementById('salaProg').style.width=Math.min(100,sala)+'%';}
function incSala(){sala++; localStorage.setItem('salaCount',sala); renderSala(); if(sala%33===0 && Notification.permission==='granted') new Notification('ﷺ أحسنتي!',{body:`صليتي ${sala} مرة على النبي`});}
function resetSala(){sala=0; localStorage.setItem('salaCount','0'); renderSala();}

const surahs=['الفاتحة','البقرة','آل عمران','النساء','المائدة','الأنعام','الأعراف','الأنفال','التوبة','يونس','هود','يوسف','الرعد','إبراهيم','الحجر','النحل','الإسراء','الكهف','مريم','طه','الأنبياء','الحج','المؤمنون','النور','الفرقان','الشعراء','النمل','القصص','العنكبوت','الروم','لقمان','السجدة','الأحزاب','سبأ','فاطر','يس','الصافات','ص','الزمر','غافر','فصلت','الشورى','الزخرف','الدخان','الجاثية','الأحقاف','محمد','الفتح','الحجرات','ق','الذاريات','الطور','النجم','القمر','الرحمن','الواقعة','الحديد','المجادلة','الحشر','الممتحنة','الصف','الجمعة','المنافقون','التغابن','الطلاق','التحريم','الملك','القلم','الحاقة','المعارج','نوح','الجن','المزمل','المدثر','القيامة','الإنسان','المرسلات','النبأ','النازعات','عبس','التكوير','الانفطار','المطففين','الانشقاق','البروج','الطارق','الأعلى','الغاشية','الفجر','البلد','الشمس','الليل','الضحى','الشرح','التين','العلق','القدر','البينة','الزلزلة','العاديات','القارعة','التكاثر','العصر','الهمزة','الفيل','قريش','الماعون','الكوثر','الكافرون','النصر','المسد','الإخلاص','الفلق','الناس'];
function renderQuran(){let el=document.getElementById('quranList'); el.innerHTML=''; surahs.forEach((s,i)=>{el.innerHTML+=`<div class="quran-item"><div><b>${i+1}. ${s}</b></div><button class="btn2" onclick="window.open('https://quran.com/ar/${i+1}','_blank')">اقرأي</button></div>`;});}
function searchQ(){let q=document.getElementById('qSearch').value; let el=document.getElementById('quranList'); el.innerHTML=''; surahs.filter(s=>s.includes(q)).forEach((s,i)=>{el.innerHTML+=`<div class="quran-item"><div><b>${s}</b></div><button class="btn2">اقرأي</button></div>`;});}
function openTab(id,btn){document.querySelectorAll('.sec').forEach(s=>s.classList.remove('on')); document.getElementById(id).classList.add('on'); document.querySelectorAll('.tab button').forEach(b=>b.classList.remove('on')); if(btn) btn.classList.add('on');}
function startSkill(type){
 let box=document.getElementById('skillBox'); box.style.display='block';
 let maps={
  'كوري':'<b>🇰🇷 كوري - مهارة جديدة</b><br>اليوم: 20 كلمة<br>안녕하세요=مرحبا<br>감사합니다=شكرا<br>استخدمي Duolingo + ذاكري من Barik',
  'برمجة':'<b>💻 برمجة - مهارة جديدة</b><br>افتحي MIT App Inventor<br>اعملي زر يذكرك بالصلاة<br>ده مشروع Barik Pro بتاعك!',
  'رياضة':'<b>💪 رياضة</b><br>بني سويف - مشي 30د أو يوجا 20د<br>تذكير: اشربي مياه + استرتشات',
  'نفسك':'<b>🚿 وقت لنفسك</b><br>شاور دافي + سكين كير + 10 د تنفس<br>انتي تستاهلي وقت لنفسك يا أسماء'
 };
 box.innerHTML=maps[type]||type;
}

loadPrayers();
renderWeek(); renderAzkar(); renderSala(); renderQuran();
setInterval(updateNext,1000);
updateNext();
</script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)

st.markdown("""
<style>
div[data-testid="stComponent"]{border-radius:20px;overflow:hidden}
</style>
""", unsafe_allow_html=True)

st.toast("🕌 مواقيت بني سويف مظبوطة - الفجر القادم جاهز", icon="🌙")
