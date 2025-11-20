## **Tasklar: SQLAlchemy bilan Tasks CRUD**

### 1️⃣ **Create Task**

**Vazifa:**
`create_task(title, description)` funksiyasi yangi task yaratishi kerak.

* `title` — majburiy
* `description` — ixtiyoriy
* Yaratilgan task bazaga yozilishi kerak
* `completed` default holatda `False` bo‘lsin

**Talab:**
Funksiya create query bajarib, yangi taskni saqlashi kerak.

---

### 2️⃣ **Get Tasks**

**Vazifa:**
`get_tasks()` funksiyasi bazadagi barcha tasklarni olish va qaytarishi kerak.

**Talab:**

* barcha ustunlarni qaytarsin (`id, title, description, completed`)
* tartib `id` bo‘yicha oshib boruvchi

---

### 3️⃣ **Update Task**

**Vazifa:**
`update_task(pk, title, description)` funksiyasi taskni yangilashi kerak.

* `pk` — qaysi task o‘zgartirilishi
* `title` — agar berilsa yangilansin
* `description` — agar berilsa yangilansin

**Talab:**

* Faqat berilgan qiymatlar update qilinsin
* Task mavjud bo‘lmasa — xatolik qaytarsin (o‘ylab topish o‘zingga)

---

### 4️⃣ **Delete Task**

**Vazifa:**
`delete_task(pk)` funksiyasi taskni o‘chirishi kerak.

**Talab:**

* `pk` bo‘yicha task o‘chirilsin
* Yo‘q bo‘lsa — xabar qaytarsin

---

### 5️⃣ **Change Task Status**

**Vazifa:**
`change_task_status(pk)` funksiyasi taskning `completed` statusini teskarisiga o‘zgartirishi kerak.
Agar `False` bo‘lsa → `True`
Agar `True` bo‘lsa → `False`

**Talab:**

* avval taskni top
* `completed` qiymatini “toggle” qil
* yangilang taskni qaytar
