//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdatetimeedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdatetimeedit.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QDateTimeEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QDateTimeEdit10metaObjectEv(
    const QDateTimeEdit *self) {
  return self->metaObject();
}

//  QString QDateTimeEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QDateTimeEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDateTimeEdit::tr(s, c, n));
}

//  QDateTimeEdit::QDateTimeEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1EP7QWidget(QWidget *parent) {
  return new QDateTimeEdit(parent);
}

//  QDateTimeEdit::QDateTimeEdit(const QDateTime &dt, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1ERK9QDateTimeP7QWidget(
    const QDateTime *dt,
    QWidget *parent) {
  return new QDateTimeEdit(*dt, parent);
}

//  QDateTimeEdit::QDateTimeEdit(QDate d, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1E5QDateP7QWidget(
    const QDate *d,
    QWidget *parent) {
  return new QDateTimeEdit(*d, parent);
}

//  QDateTimeEdit::QDateTimeEdit(QTime t, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN13QDateTimeEditC1E5QTimeP7QWidget(
    const QTime *t,
    QWidget *parent) {
  return new QDateTimeEdit(*t, parent);
}

//  QDateTimeEdit::~QDateTimeEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEditD1Ev(QDateTimeEdit *self) {
  delete self;
}

//  QDateTime QDateTimeEdit::dateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeEdit8dateTimeEv(const QDateTimeEdit *self) {
  return new QDateTime(self->dateTime());
}

//  QDate QDateTimeEdit::date() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK13QDateTimeEdit4dateEv(const QDateTimeEdit *self) {
  return new QDate(self->date());
}

//  QTime QDateTimeEdit::time() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK13QDateTimeEdit4timeEv(const QDateTimeEdit *self) {
  return new QTime(self->time());
}

//  QCalendar QDateTimeEdit::calendar() const
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZNK13QDateTimeEdit8calendarEv(const QDateTimeEdit *self) {
  return new QCalendar(self->calendar());
}

//  void QDateTimeEdit::setCalendar(QCalendar calendar)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setCalendarE9QCalendar(
    QDateTimeEdit *self,
    const QCalendar *calendar) {
  self->setCalendar(*calendar);
}

//  QDateTime QDateTimeEdit::minimumDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeEdit15minimumDateTimeEv(
    const QDateTimeEdit *self) {
  return new QDateTime(self->minimumDateTime());
}

//  void QDateTimeEdit::clearMinimumDateTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit20clearMinimumDateTimeEv(QDateTimeEdit *self) {
  self->clearMinimumDateTime();
}

//  void QDateTimeEdit::setMinimumDateTime(const QDateTime &dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit18setMinimumDateTimeERK9QDateTime(
    QDateTimeEdit *self,
    const QDateTime *dt) {
  self->setMinimumDateTime(*dt);
}

//  QDateTime QDateTimeEdit::maximumDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeEdit15maximumDateTimeEv(
    const QDateTimeEdit *self) {
  return new QDateTime(self->maximumDateTime());
}

//  void QDateTimeEdit::clearMaximumDateTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit20clearMaximumDateTimeEv(QDateTimeEdit *self) {
  self->clearMaximumDateTime();
}

//  void QDateTimeEdit::setMaximumDateTime(const QDateTime &dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit18setMaximumDateTimeERK9QDateTime(
    QDateTimeEdit *self,
    const QDateTime *dt) {
  self->setMaximumDateTime(*dt);
}

//  void QDateTimeEdit::setDateTimeRange(const QDateTime &min, const
//      QDateTime &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16setDateTimeRangeERK9QDateTimeS2_(
    QDateTimeEdit *self,
    const QDateTime *min,
    const QDateTime *max) {
  self->setDateTimeRange(*min, *max);
}

//  QDate QDateTimeEdit::minimumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK13QDateTimeEdit11minimumDateEv(const QDateTimeEdit *self) {
  return new QDate(self->minimumDate());
}

//  void QDateTimeEdit::setMinimumDate(QDate min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMinimumDateE5QDate(
    QDateTimeEdit *self,
    const QDate *min) {
  self->setMinimumDate(*min);
}

//  void QDateTimeEdit::clearMinimumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMinimumDateEv(QDateTimeEdit *self) {
  self->clearMinimumDate();
}

//  QDate QDateTimeEdit::maximumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK13QDateTimeEdit11maximumDateEv(const QDateTimeEdit *self) {
  return new QDate(self->maximumDate());
}

//  void QDateTimeEdit::setMaximumDate(QDate max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMaximumDateE5QDate(
    QDateTimeEdit *self,
    const QDate *max) {
  self->setMaximumDate(*max);
}

//  void QDateTimeEdit::clearMaximumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMaximumDateEv(QDateTimeEdit *self) {
  self->clearMaximumDate();
}

//  void QDateTimeEdit::setDateRange(QDate min, QDate max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit12setDateRangeE5QDateS0_(
    QDateTimeEdit *self,
    const QDate *min,
    const QDate *max) {
  self->setDateRange(*min, *max);
}

//  QTime QDateTimeEdit::minimumTime() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK13QDateTimeEdit11minimumTimeEv(const QDateTimeEdit *self) {
  return new QTime(self->minimumTime());
}

//  void QDateTimeEdit::setMinimumTime(QTime min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMinimumTimeE5QTime(
    QDateTimeEdit *self,
    const QTime *min) {
  self->setMinimumTime(*min);
}

//  void QDateTimeEdit::clearMinimumTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMinimumTimeEv(QDateTimeEdit *self) {
  self->clearMinimumTime();
}

//  QTime QDateTimeEdit::maximumTime() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK13QDateTimeEdit11maximumTimeEv(const QDateTimeEdit *self) {
  return new QTime(self->maximumTime());
}

//  void QDateTimeEdit::setMaximumTime(QTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit14setMaximumTimeE5QTime(
    QDateTimeEdit *self,
    const QTime *max) {
  self->setMaximumTime(*max);
}

//  void QDateTimeEdit::clearMaximumTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16clearMaximumTimeEv(QDateTimeEdit *self) {
  self->clearMaximumTime();
}

//  void QDateTimeEdit::setTimeRange(QTime min, QTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit12setTimeRangeE5QTimeS0_(
    QDateTimeEdit *self,
    const QTime *min,
    const QTime *max) {
  self->setTimeRange(*min, *max);
}

//  Sections QDateTimeEdit::displayedSections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDateTimeEdit17displayedSectionsEv(
    const QDateTimeEdit *self) {
  return static_cast<int>(self->displayedSections().toInt());
}

//  Section QDateTimeEdit::currentSection() const
extern "C" Q_DECL_EXPORT
QDateTimeEdit::Section ritual_ZNK13QDateTimeEdit14currentSectionEv(
    const QDateTimeEdit *self) {
  return self->currentSection();
}

//  Section QDateTimeEdit::sectionAt(int index) const
extern "C" Q_DECL_EXPORT
QDateTimeEdit::Section ritual_ZNK13QDateTimeEdit9sectionAtEi(
    const QDateTimeEdit *self,
    int index) {
  return self->sectionAt(index);
}

//  void QDateTimeEdit::setCurrentSection(Section section)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit17setCurrentSectionENS_7SectionE(
    QDateTimeEdit *self,
    QDateTimeEdit::Section section) {
  self->setCurrentSection(section);
}

//  int QDateTimeEdit::currentSectionIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDateTimeEdit19currentSectionIndexEv(
    const QDateTimeEdit *self) {
  return self->currentSectionIndex();
}

//  void QDateTimeEdit::setCurrentSectionIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit22setCurrentSectionIndexEi(
    QDateTimeEdit *self,
    int index) {
  self->setCurrentSectionIndex(index);
}

//  QCalendarWidget *QDateTimeEdit::calendarWidget() const
extern "C" Q_DECL_EXPORT
QCalendarWidget *ritual_ZNK13QDateTimeEdit14calendarWidgetEv(
    const QDateTimeEdit *self) {
  return self->calendarWidget();
}

//  void QDateTimeEdit::setCalendarWidget(QCalendarWidget *calendarWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit17setCalendarWidgetEP15QCalendarWidget(
    QDateTimeEdit *self,
    QCalendarWidget *calendarWidget) {
  self->setCalendarWidget(calendarWidget);
}

//  int QDateTimeEdit::sectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDateTimeEdit12sectionCountEv(const QDateTimeEdit *self) {
  return self->sectionCount();
}

//  void QDateTimeEdit::setSelectedSection(Section section)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit18setSelectedSectionENS_7SectionE(
    QDateTimeEdit *self,
    QDateTimeEdit::Section section) {
  self->setSelectedSection(section);
}

//  QString QDateTimeEdit::sectionText(Section section) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDateTimeEdit11sectionTextENS_7SectionE(
    const QDateTimeEdit *self,
    QDateTimeEdit::Section section) {
  return new QString(self->sectionText(section));
}

//  QString QDateTimeEdit::displayFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDateTimeEdit13displayFormatEv(
    const QDateTimeEdit *self) {
  return new QString(self->displayFormat());
}

//  void QDateTimeEdit::setDisplayFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16setDisplayFormatERK7QString(
    QDateTimeEdit *self,
    const QString *format) {
  self->setDisplayFormat(*format);
}

//  bool QDateTimeEdit::calendarPopup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDateTimeEdit13calendarPopupEv(const QDateTimeEdit *self) {
  return self->calendarPopup();
}

//  void QDateTimeEdit::setCalendarPopup(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit16setCalendarPopupEb(
    QDateTimeEdit *self,
    bool enable) {
  self->setCalendarPopup(enable);
}

//  Qt::TimeSpec QDateTimeEdit::timeSpec() const
extern "C" Q_DECL_EXPORT
Qt::TimeSpec ritual_ZNK13QDateTimeEdit8timeSpecEv(
    const QDateTimeEdit *self) {
  return self->timeSpec();
}

//  void QDateTimeEdit::setTimeSpec(Qt::TimeSpec spec)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setTimeSpecEN2Qt8TimeSpecE(
    QDateTimeEdit *self,
    Qt::TimeSpec spec) {
  self->setTimeSpec(spec);
}

//  QTimeZone QDateTimeEdit::timeZone() const
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZNK13QDateTimeEdit8timeZoneEv(const QDateTimeEdit *self) {
  return new QTimeZone(self->timeZone());
}

//  void QDateTimeEdit::setTimeZone(const QTimeZone &zone)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setTimeZoneERK9QTimeZone(
    QDateTimeEdit *self,
    const QTimeZone *zone) {
  self->setTimeZone(*zone);
}

//  QSize QDateTimeEdit::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QDateTimeEdit8sizeHintEv(const QDateTimeEdit *self) {
  return new QSize(self->sizeHint());
}

//  void QDateTimeEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit5clearEv(QDateTimeEdit *self) {
  self->clear();
}

//  void QDateTimeEdit::stepBy(int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit6stepByEi(QDateTimeEdit *self, int steps) {
  self->stepBy(steps);
}

//  bool QDateTimeEdit::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDateTimeEdit5eventEP6QEvent(
    QDateTimeEdit *self,
    QEvent *event) {
  return self->event(event);
}

//  void QDateTimeEdit::setDateTime(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit11setDateTimeERK9QDateTime(
    QDateTimeEdit *self,
    const QDateTime *dateTime) {
  self->setDateTime(*dateTime);
}

//  void QDateTimeEdit::setDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit7setDateE5QDate(
    QDateTimeEdit *self,
    const QDate *date) {
  self->setDate(*date);
}

//  void QDateTimeEdit::setTime(QTime time)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeEdit7setTimeE5QTime(
    QDateTimeEdit *self,
    const QTime *time) {
  self->setTime(*time);
}
