//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcalendar.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcalendar.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlist.h>

//  QCalendar::QCalendar()
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZN9QCalendarC1Ev() {
  return new QCalendar();
}

//  QCalendar::QCalendar(System system)
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZN9QCalendarC1ENS_6SystemE(QCalendar::System system) {
  return new QCalendar(system);
}

//  QCalendar::QCalendar(QAnyStringView name)
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZN9QCalendarC1E14QAnyStringView(const QString *name) {
  return new QCalendar(QAnyStringView(*name));
}

//  QCalendar::QCalendar(SystemId id)
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZN9QCalendarC1ENS_8SystemIdE(
    const QCalendar::SystemId *id) {
  return new QCalendar(*id);
}

//  bool QCalendar::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar7isValidEv(const QCalendar *self) {
  return self->isValid();
}

//  int QCalendar::daysInMonth(int month, int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCalendar11daysInMonthEii(
    const QCalendar *self,
    int month,
    int year) {
  return self->daysInMonth(month, year);
}

//  int QCalendar::daysInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCalendar10daysInYearEi(const QCalendar *self, int year) {
  return self->daysInYear(year);
}

//  int QCalendar::monthsInYear(int year) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCalendar12monthsInYearEi(const QCalendar *self, int year) {
  return self->monthsInYear(year);
}

//  bool QCalendar::isDateValid(int year, int month, int day) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar11isDateValidEiii(
    const QCalendar *self,
    int year,
    int month,
    int day) {
  return self->isDateValid(year, month, day);
}

//  bool QCalendar::isLeapYear(int year) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar10isLeapYearEi(const QCalendar *self, int year) {
  return self->isLeapYear(year);
}

//  bool QCalendar::isGregorian() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar11isGregorianEv(const QCalendar *self) {
  return self->isGregorian();
}

//  bool QCalendar::isLunar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar7isLunarEv(const QCalendar *self) {
  return self->isLunar();
}

//  bool QCalendar::isLuniSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar11isLuniSolarEv(const QCalendar *self) {
  return self->isLuniSolar();
}

//  bool QCalendar::isSolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar7isSolarEv(const QCalendar *self) {
  return self->isSolar();
}

//  bool QCalendar::isProleptic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar11isProlepticEv(const QCalendar *self) {
  return self->isProleptic();
}

//  bool QCalendar::hasYearZero() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar11hasYearZeroEv(const QCalendar *self) {
  return self->hasYearZero();
}

//  int QCalendar::maximumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCalendar18maximumDaysInMonthEv(const QCalendar *self) {
  return self->maximumDaysInMonth();
}

//  int QCalendar::minimumDaysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCalendar18minimumDaysInMonthEv(const QCalendar *self) {
  return self->minimumDaysInMonth();
}

//  int QCalendar::maximumMonthsInYear() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCalendar19maximumMonthsInYearEv(const QCalendar *self) {
  return self->maximumMonthsInYear();
}

//  QString QCalendar::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QCalendar4nameEv(const QCalendar *self) {
  return new QString(self->name());
}

//  QDate QCalendar::dateFromParts(int year, int month, int day) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK9QCalendar13dateFromPartsEiii(
    const QCalendar *self,
    int year,
    int month,
    int day) {
  return new QDate(self->dateFromParts(year, month, day));
}

//  QDate QCalendar::dateFromParts(const YearMonthDay &parts) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK9QCalendar13dateFromPartsERKNS_12YearMonthDayE(
    const QCalendar *self,
    const QCalendar::YearMonthDay *parts) {
  return new QDate(self->dateFromParts(*parts));
}

//  QDate QCalendar::matchCenturyToWeekday(const YearMonthDay &parts, int
//      dow) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK9QCalendar21matchCenturyToWeekdayERKNS_12YearMonthDayEi(
    const QCalendar *self,
    const QCalendar::YearMonthDay *parts,
    int dow) {
  return new QDate(self->matchCenturyToWeekday(*parts, dow));
}

//  YearMonthDay QCalendar::partsFromDate(QDate date) const
extern "C" Q_DECL_EXPORT
QCalendar::YearMonthDay *ritual_ZNK9QCalendar13partsFromDateE5QDate(
    const QCalendar *self,
    const QDate *date) {
  return new QCalendar::YearMonthDay(self->partsFromDate(*date));
}

//  int QCalendar::dayOfWeek(QDate date) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCalendar9dayOfWeekE5QDate(
    const QCalendar *self,
    const QDate *date) {
  return self->dayOfWeek(*date);
}

//  QString QCalendar::monthName(const QLocale &locale, int month, int year,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QCalendar9monthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QCalendar *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(self->monthName(*locale, month, year, format));
}

//  QString QCalendar::standaloneMonthName(const QLocale &locale, int month,
//      int year, QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QCalendar19standaloneMonthNameERK7QLocaleiiNS0_10FormatTypeE(
    const QCalendar *self,
    const QLocale *locale,
    int month,
    int year,
    QLocale::FormatType format) {
  return new QString(
      self->standaloneMonthName(
          *locale,
          month,
          year,
          format));
}

//  QString QCalendar::weekDayName(const QLocale &locale, int day,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QCalendar11weekDayNameERK7QLocaleiNS0_10FormatTypeE(
    const QCalendar *self,
    const QLocale *locale,
    int day,
    QLocale::FormatType format) {
  return new QString(self->weekDayName(*locale, day, format));
}

//  QString QCalendar::standaloneWeekDayName(const QLocale &locale, int day,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QCalendar21standaloneWeekDayNameERK7QLocaleiNS0_10FormatTypeE(
    const QCalendar *self,
    const QLocale *locale,
    int day,
    QLocale::FormatType format) {
  return new QString(self->standaloneWeekDayName(*locale, day, format));
}

//  QString QCalendar::dateTimeToString(QStringView format, const QDateTime
//      &datetime, QDate dateOnly, QTime timeOnly, const QLocale &locale)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QCalendar16dateTimeToStringE11QStringViewRK9QDateTime5QDate5QTimeRK7QLocale(
    const QCalendar *self,
    const QString *format,
    const QDateTime *datetime,
    const QDate *dateOnly,
    const QTime *timeOnly,
    const QLocale *locale) {
  return new QString(
      self->dateTimeToString(
          QStringView(*format),
          *datetime,
          *dateOnly,
          *timeOnly,
          *locale));
}

//  QStringList QCalendar::availableCalendars()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN9QCalendar18availableCalendarsEv() {
  return new QList<QString>(QCalendar::availableCalendars());
}

//  QCalendar::~QCalendar()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCalendarD1Ev(QCalendar *self) {
  delete self;
}
