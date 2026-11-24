//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdatetime.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdatetime.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QDate::QDate(qint64 julianDay)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDateC1Ex(qint64 julianDay) {
  return new QDate(julianDay);
}

//  QDate::QDate()
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDateC1Ev() {
  return new QDate();
}

//  QDate::QDate(int y, int m, int d)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDateC1Eiii(int y, int m, int d) {
  return new QDate(y, m, d);
}

//  QDate::QDate(int y, int m, int d, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDateC1Eiii9QCalendar(
    int y,
    int m,
    int d,
    const QCalendar *cal) {
  return new QDate(y, m, d, *cal);
}

//  bool QDate::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QDate6isNullEv(const QDate *self) {
  return self->isNull();
}

//  bool QDate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QDate7isValidEv(const QDate *self) {
  return self->isValid();
}

//  int QDate::year() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate4yearEv(const QDate *self) {
  return self->year();
}

//  int QDate::month() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate5monthEv(const QDate *self) {
  return self->month();
}

//  int QDate::day() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate3dayEv(const QDate *self) {
  return self->day();
}

//  int QDate::dayOfWeek() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate9dayOfWeekEv(const QDate *self) {
  return self->dayOfWeek();
}

//  int QDate::dayOfYear() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate9dayOfYearEv(const QDate *self) {
  return self->dayOfYear();
}

//  int QDate::daysInMonth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate11daysInMonthEv(const QDate *self) {
  return self->daysInMonth();
}

//  int QDate::daysInYear() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate10daysInYearEv(const QDate *self) {
  return self->daysInYear();
}

//  int QDate::weekNumber(int *yearNum) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate10weekNumberEPi(const QDate *self, int *yearNum) {
  return self->weekNumber(yearNum);
}

//  int QDate::year(QCalendar cal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate4yearE9QCalendar(
    const QDate *self,
    const QCalendar *cal) {
  return self->year(*cal);
}

//  int QDate::month(QCalendar cal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate5monthE9QCalendar(
    const QDate *self,
    const QCalendar *cal) {
  return self->month(*cal);
}

//  int QDate::day(QCalendar cal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate3dayE9QCalendar(
    const QDate *self,
    const QCalendar *cal) {
  return self->day(*cal);
}

//  int QDate::dayOfWeek(QCalendar cal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate9dayOfWeekE9QCalendar(
    const QDate *self,
    const QCalendar *cal) {
  return self->dayOfWeek(*cal);
}

//  int QDate::dayOfYear(QCalendar cal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate9dayOfYearE9QCalendar(
    const QDate *self,
    const QCalendar *cal) {
  return self->dayOfYear(*cal);
}

//  int QDate::daysInMonth(QCalendar cal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate11daysInMonthE9QCalendar(
    const QDate *self,
    const QCalendar *cal) {
  return self->daysInMonth(*cal);
}

//  int QDate::daysInYear(QCalendar cal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDate10daysInYearE9QCalendar(
    const QDate *self,
    const QCalendar *cal) {
  return self->daysInYear(*cal);
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QDateTime QDate::startOfDay(Qt::TimeSpec spec, int offsetSeconds) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK5QDate10startOfDayEN2Qt8TimeSpecEi(
    const QDate *self,
    Qt::TimeSpec spec,
    int offsetSeconds) {
  return new QDateTime(self->startOfDay(spec, offsetSeconds));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QDateTime QDate::endOfDay(Qt::TimeSpec spec, int offsetSeconds) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK5QDate8endOfDayEN2Qt8TimeSpecEi(
    const QDate *self,
    Qt::TimeSpec spec,
    int offsetSeconds) {
  return new QDateTime(self->endOfDay(spec, offsetSeconds));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  QDateTime QDate::startOfDay(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK5QDate10startOfDayERK9QTimeZone(
    const QDate *self,
    const QTimeZone *zone) {
  return new QDateTime(self->startOfDay(*zone));
}

//  QDateTime QDate::endOfDay(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK5QDate8endOfDayERK9QTimeZone(
    const QDate *self,
    const QTimeZone *zone) {
  return new QDateTime(self->endOfDay(*zone));
}

//  QDateTime QDate::startOfDay() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK5QDate10startOfDayEv(const QDate *self) {
  return new QDateTime(self->startOfDay());
}

//  QDateTime QDate::endOfDay() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK5QDate8endOfDayEv(const QDate *self) {
  return new QDateTime(self->endOfDay());
}

#if QT_CONFIG(datestring)
//  QString QDate::toString(Qt::DateFormat format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QDate8toStringEN2Qt10DateFormatE(
    const QDate *self,
    Qt::DateFormat format) {
  return new QString(self->toString(format));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QString QDate::toString(const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QDate8toStringERK7QString(
    const QDate *self,
    const QString *format) {
  return new QString(self->toString(*format));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QString QDate::toString(const QString &format, QCalendar cal) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QDate8toStringERK7QString9QCalendar(
    const QDate *self,
    const QString *format,
    const QCalendar *cal) {
  return new QString(self->toString(*format, *cal));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QString QDate::toString(QStringView format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QDate8toStringE11QStringView(
    const QDate *self,
    const QString *format) {
  return new QString(self->toString(QStringView(*format)));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QString QDate::toString(QStringView format, QCalendar cal) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QDate8toStringE11QStringView9QCalendar(
    const QDate *self,
    const QString *format,
    const QCalendar *cal) {
  return new QString(self->toString(QStringView(*format), *cal));
}
#endif  // QT_CONFIG(datestring)

//  bool QDate::setDate(int year, int month, int day)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDate7setDateEiii(QDate *self, int year, int month, int day) {
  return self->setDate(year, month, day);
}

//  bool QDate::setDate(int year, int month, int day, QCalendar cal)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDate7setDateEiii9QCalendar(
    QDate *self,
    int year,
    int month,
    int day,
    const QCalendar *cal) {
  return self->setDate(year, month, day, *cal);
}

//  void QDate::getDate(int *year, int *month, int *day) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK5QDate7getDateEPiS0_S0_(
    const QDate *self,
    int *year,
    int *month,
    int *day) {
  self->getDate(year, month, day);
}

//  QDate QDate::addDays(qint64 days) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK5QDate7addDaysEx(const QDate *self, qint64 days) {
  return new QDate(self->addDays(days));
}

//  QDate QDate::addMonths(int months) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK5QDate9addMonthsEi(const QDate *self, int months) {
  return new QDate(self->addMonths(months));
}

//  QDate QDate::addYears(int years) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK5QDate8addYearsEi(const QDate *self, int years) {
  return new QDate(self->addYears(years));
}

//  QDate QDate::addMonths(int months, QCalendar cal) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK5QDate9addMonthsEi9QCalendar(
    const QDate *self,
    int months,
    const QCalendar *cal) {
  return new QDate(self->addMonths(months, *cal));
}

//  QDate QDate::addYears(int years, QCalendar cal) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK5QDate8addYearsEi9QCalendar(
    const QDate *self,
    int years,
    const QCalendar *cal) {
  return new QDate(self->addYears(years, *cal));
}

//  qint64 QDate::daysTo(QDate d) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK5QDate6daysToES_(const QDate *self, const QDate *d) {
  return self->daysTo(*d);
}

//  QDate QDate::currentDate()
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate11currentDateEv() {
  return new QDate(QDate::currentDate());
}

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(QStringView string, Qt::DateFormat format)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringE11QStringViewN2Qt10DateFormatE(
    const QString *string,
    Qt::DateFormat format) {
  return new QDate(QDate::fromString(QStringView(*string), format));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(const QString &string, Qt::DateFormat format)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringERK7QStringN2Qt10DateFormatE(
    const QString *string,
    Qt::DateFormat format) {
  return new QDate(QDate::fromString(*string, format));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(QStringView string, QStringView format, QCalendar
//      cal)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringE11QStringViewS0_9QCalendar(
    const QString *string,
    const QString *format,
    const QCalendar *cal) {
  return new QDate(
      QDate::fromString(
          QStringView(*string),
          QStringView(*format),
          *cal));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(const QString &string, QStringView format,
//      QCalendar cal)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringERK7QString11QStringView9QCalendar(
    const QString *string,
    const QString *format,
    const QCalendar *cal) {
  return new QDate(QDate::fromString(*string, QStringView(*format), *cal));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(const QString &string, const QString &format,
//      QCalendar cal)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringERK7QStringS2_9QCalendar(
    const QString *string,
    const QString *format,
    const QCalendar *cal) {
  return new QDate(QDate::fromString(*string, *format, *cal));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(QStringView string, QStringView format, int
//      baseYear)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringE11QStringViewS0_i(
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDate(
      QDate::fromString(
          QStringView(*string),
          QStringView(*format),
          baseYear));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(QStringView string, QStringView format, int
//      baseYear, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringE11QStringViewS0_i9QCalendar(
    const QString *string,
    const QString *format,
    int baseYear,
    const QCalendar *cal) {
  return new QDate(
      QDate::fromString(
          QStringView(*string),
          QStringView(*format),
          baseYear,
          *cal));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(const QString &string, QStringView format, int
//      baseYear)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringERK7QString11QStringViewi(
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDate(
      QDate::fromString(
          *string,
          QStringView(*format),
          baseYear));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(const QString &string, QStringView format, int
//      baseYear, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringERK7QString11QStringViewi9QCalendar(
    const QString *string,
    const QString *format,
    int baseYear,
    const QCalendar *cal) {
  return new QDate(
      QDate::fromString(
          *string,
          QStringView(*format),
          baseYear,
          *cal));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(const QString &string, const QString &format, int
//      baseYear)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringERK7QStringS2_i(
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDate(QDate::fromString(*string, *format, baseYear));
}
#endif  // QT_CONFIG(datestring)

#if QT_CONFIG(datestring)
//  QDate QDate::fromString(const QString &string, const QString &format, int
//      baseYear, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate10fromStringERK7QStringS2_i9QCalendar(
    const QString *string,
    const QString *format,
    int baseYear,
    const QCalendar *cal) {
  return new QDate(QDate::fromString(*string, *format, baseYear, *cal));
}
#endif  // QT_CONFIG(datestring)

//  bool QDate::isValid(int y, int m, int d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDate7isValidEiii(int y, int m, int d) {
  return QDate::isValid(y, m, d);
}

//  bool QDate::isLeapYear(int year)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDate10isLeapYearEi(int year) {
  return QDate::isLeapYear(year);
}

//  QDate QDate::fromJulianDay(qint64 jd_)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN5QDate13fromJulianDayEx(qint64 jd_) {
  return new QDate(QDate::fromJulianDay(jd_));
}

//  qint64 QDate::toJulianDay() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK5QDate11toJulianDayEv(const QDate *self) {
  return self->toJulianDay();
}

//  qint64 QDate::nullJd()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN5QDate6nullJdEv() {
  return QDate::nullJd();
}

//  qint64 QDate::minJd()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN5QDate5minJdEv() {
  return QDate::minJd();
}

//  qint64 QDate::maxJd()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN5QDate5maxJdEv() {
  return QDate::maxJd();
}

//  qint64 QDate::unixEpochJd()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN5QDate11unixEpochJdEv() {
  return QDate::unixEpochJd();
}

//  bool operator==(const QDate &lhs, const QDate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QDateS1_(const QDate *lhs, const QDate *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QDate &lhs, const QDate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QDateS1_(const QDate *lhs, const QDate *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QDate &lhs, const QDate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QDateS1_(const QDate *lhs, const QDate *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QDate &lhs, const QDate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QDateS1_(const QDate *lhs, const QDate *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QDate &lhs, const QDate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QDateS1_(const QDate *lhs, const QDate *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QDate &lhs, const QDate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QDateS1_(const QDate *lhs, const QDate *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QDate::~QDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDateD1Ev(QDate *self) {
  delete self;
}
