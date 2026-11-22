//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcalendarwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcalendarwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qcalendar.h>
#include <QtGui/qtextformat.h>

//  const QMetaObject *QCalendarWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QCalendarWidget10metaObjectEv(
    const QCalendarWidget *self) {
  return self->metaObject();
}

//  QString QCalendarWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QCalendarWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCalendarWidget::tr(s, c, n));
}

//  QCalendarWidget::QCalendarWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QCalendarWidget *ritual_ZN15QCalendarWidgetC1EP7QWidget(QWidget *parent) {
  return new QCalendarWidget(parent);
}

//  QCalendarWidget::~QCalendarWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidgetD1Ev(QCalendarWidget *self) {
  delete self;
}

//  QSize QCalendarWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QCalendarWidget8sizeHintEv(const QCalendarWidget *self) {
  return new QSize(self->sizeHint());
}

//  QSize QCalendarWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QCalendarWidget15minimumSizeHintEv(
    const QCalendarWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  QDate QCalendarWidget::selectedDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK15QCalendarWidget12selectedDateEv(
    const QCalendarWidget *self) {
  return new QDate(self->selectedDate());
}

//  int QCalendarWidget::yearShown() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCalendarWidget9yearShownEv(const QCalendarWidget *self) {
  return self->yearShown();
}

//  int QCalendarWidget::monthShown() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCalendarWidget10monthShownEv(const QCalendarWidget *self) {
  return self->monthShown();
}

//  QDate QCalendarWidget::minimumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK15QCalendarWidget11minimumDateEv(
    const QCalendarWidget *self) {
  return new QDate(self->minimumDate());
}

//  void QCalendarWidget::setMinimumDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setMinimumDateE5QDate(
    QCalendarWidget *self,
    const QDate *date) {
  self->setMinimumDate(*date);
}

//  void QCalendarWidget::clearMinimumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16clearMinimumDateEv(QCalendarWidget *self) {
  self->clearMinimumDate();
}

//  QDate QCalendarWidget::maximumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK15QCalendarWidget11maximumDateEv(
    const QCalendarWidget *self) {
  return new QDate(self->maximumDate());
}

//  void QCalendarWidget::setMaximumDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setMaximumDateE5QDate(
    QCalendarWidget *self,
    const QDate *date) {
  self->setMaximumDate(*date);
}

//  void QCalendarWidget::clearMaximumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16clearMaximumDateEv(QCalendarWidget *self) {
  self->clearMaximumDate();
}

//  Qt::DayOfWeek QCalendarWidget::firstDayOfWeek() const
extern "C" Q_DECL_EXPORT
Qt::DayOfWeek ritual_ZNK15QCalendarWidget14firstDayOfWeekEv(
    const QCalendarWidget *self) {
  return self->firstDayOfWeek();
}

//  void QCalendarWidget::setFirstDayOfWeek(Qt::DayOfWeek dayOfWeek)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget17setFirstDayOfWeekEN2Qt9DayOfWeekE(
    QCalendarWidget *self,
    Qt::DayOfWeek dayOfWeek) {
  self->setFirstDayOfWeek(dayOfWeek);
}

//  bool QCalendarWidget::isNavigationBarVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCalendarWidget22isNavigationBarVisibleEv(
    const QCalendarWidget *self) {
  return self->isNavigationBarVisible();
}

//  bool QCalendarWidget::isGridVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCalendarWidget13isGridVisibleEv(
    const QCalendarWidget *self) {
  return self->isGridVisible();
}

//  QCalendar QCalendarWidget::calendar() const
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZNK15QCalendarWidget8calendarEv(
    const QCalendarWidget *self) {
  return new QCalendar(self->calendar());
}

//  void QCalendarWidget::setCalendar(QCalendar calendar)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget11setCalendarE9QCalendar(
    QCalendarWidget *self,
    const QCalendar *calendar) {
  self->setCalendar(*calendar);
}

//  SelectionMode QCalendarWidget::selectionMode() const
extern "C" Q_DECL_EXPORT
QCalendarWidget::SelectionMode ritual_ZNK15QCalendarWidget13selectionModeEv(
    const QCalendarWidget *self) {
  return self->selectionMode();
}

//  void QCalendarWidget::setSelectionMode(SelectionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16setSelectionModeENS_13SelectionModeE(
    QCalendarWidget *self,
    QCalendarWidget::SelectionMode mode) {
  self->setSelectionMode(mode);
}

//  HorizontalHeaderFormat QCalendarWidget::horizontalHeaderFormat() const
extern "C" Q_DECL_EXPORT
QCalendarWidget::HorizontalHeaderFormat ritual_ZNK15QCalendarWidget22horizontalHeaderFormatEv(
    const QCalendarWidget *self) {
  return self->horizontalHeaderFormat();
}

//  void QCalendarWidget::setHorizontalHeaderFormat(HorizontalHeaderFormat
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget25setHorizontalHeaderFormatENS_22HorizontalHeaderFormatE(
    QCalendarWidget *self,
    QCalendarWidget::HorizontalHeaderFormat format) {
  self->setHorizontalHeaderFormat(format);
}

//  VerticalHeaderFormat QCalendarWidget::verticalHeaderFormat() const
extern "C" Q_DECL_EXPORT
QCalendarWidget::VerticalHeaderFormat ritual_ZNK15QCalendarWidget20verticalHeaderFormatEv(
    const QCalendarWidget *self) {
  return self->verticalHeaderFormat();
}

//  void QCalendarWidget::setVerticalHeaderFormat(VerticalHeaderFormat
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget23setVerticalHeaderFormatENS_20VerticalHeaderFormatE(
    QCalendarWidget *self,
    QCalendarWidget::VerticalHeaderFormat format) {
  self->setVerticalHeaderFormat(format);
}

//  QTextCharFormat QCalendarWidget::headerTextFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK15QCalendarWidget16headerTextFormatEv(
    const QCalendarWidget *self) {
  return new QTextCharFormat(self->headerTextFormat());
}

//  void QCalendarWidget::setHeaderTextFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget19setHeaderTextFormatERK15QTextCharFormat(
    QCalendarWidget *self,
    const QTextCharFormat *format) {
  self->setHeaderTextFormat(*format);
}

//  QTextCharFormat QCalendarWidget::weekdayTextFormat(Qt::DayOfWeek
//      dayOfWeek) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK15QCalendarWidget17weekdayTextFormatEN2Qt9DayOfWeekE(
    const QCalendarWidget *self,
    Qt::DayOfWeek dayOfWeek) {
  return new QTextCharFormat(self->weekdayTextFormat(dayOfWeek));
}

//  void QCalendarWidget::setWeekdayTextFormat(Qt::DayOfWeek dayOfWeek, const
//      QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget20setWeekdayTextFormatEN2Qt9DayOfWeekERK15QTextCharFormat(
    QCalendarWidget *self,
    Qt::DayOfWeek dayOfWeek,
    const QTextCharFormat *format) {
  self->setWeekdayTextFormat(dayOfWeek, *format);
}

//  QTextCharFormat QCalendarWidget::dateTextFormat(QDate date) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK15QCalendarWidget14dateTextFormatE5QDate(
    const QCalendarWidget *self,
    const QDate *date) {
  return new QTextCharFormat(self->dateTextFormat(*date));
}

//  void QCalendarWidget::setDateTextFormat(QDate date, const QTextCharFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget17setDateTextFormatE5QDateRK15QTextCharFormat(
    QCalendarWidget *self,
    const QDate *date,
    const QTextCharFormat *format) {
  self->setDateTextFormat(*date, *format);
}

//  bool QCalendarWidget::isDateEditEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCalendarWidget17isDateEditEnabledEv(
    const QCalendarWidget *self) {
  return self->isDateEditEnabled();
}

//  void QCalendarWidget::setDateEditEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget18setDateEditEnabledEb(
    QCalendarWidget *self,
    bool enable) {
  self->setDateEditEnabled(enable);
}

//  int QCalendarWidget::dateEditAcceptDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCalendarWidget19dateEditAcceptDelayEv(
    const QCalendarWidget *self) {
  return self->dateEditAcceptDelay();
}

//  void QCalendarWidget::setDateEditAcceptDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget22setDateEditAcceptDelayEi(
    QCalendarWidget *self,
    int delay) {
  self->setDateEditAcceptDelay(delay);
}

//  void QCalendarWidget::setSelectedDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget15setSelectedDateE5QDate(
    QCalendarWidget *self,
    const QDate *date) {
  self->setSelectedDate(*date);
}

//  void QCalendarWidget::setDateRange(QDate min, QDate max)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget12setDateRangeE5QDateS0_(
    QCalendarWidget *self,
    const QDate *min,
    const QDate *max) {
  self->setDateRange(*min, *max);
}

//  void QCalendarWidget::setCurrentPage(int year, int month)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setCurrentPageEii(
    QCalendarWidget *self,
    int year,
    int month) {
  self->setCurrentPage(year, month);
}

//  void QCalendarWidget::setGridVisible(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setGridVisibleEb(
    QCalendarWidget *self,
    bool show) {
  self->setGridVisible(show);
}

//  void QCalendarWidget::setNavigationBarVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget23setNavigationBarVisibleEb(
    QCalendarWidget *self,
    bool visible) {
  self->setNavigationBarVisible(visible);
}

//  void QCalendarWidget::showNextMonth()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget13showNextMonthEv(QCalendarWidget *self) {
  self->showNextMonth();
}

//  void QCalendarWidget::showPreviousMonth()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget17showPreviousMonthEv(QCalendarWidget *self) {
  self->showPreviousMonth();
}

//  void QCalendarWidget::showNextYear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget12showNextYearEv(QCalendarWidget *self) {
  self->showNextYear();
}

//  void QCalendarWidget::showPreviousYear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16showPreviousYearEv(QCalendarWidget *self) {
  self->showPreviousYear();
}

//  void QCalendarWidget::showSelectedDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16showSelectedDateEv(QCalendarWidget *self) {
  self->showSelectedDate();
}

//  void QCalendarWidget::showToday()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget9showTodayEv(QCalendarWidget *self) {
  self->showToday();
}
