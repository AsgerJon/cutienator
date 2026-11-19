//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdatetime.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdatetime.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qstring.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qstringview.h>

//  QDateTime::QDateTime()
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTimeC1Ev() {
  return new QDateTime();
}

//  QDateTime::QDateTime(QDate date, QTime time, Qt::TimeSpec spec, int
//      offsetSeconds)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTimeC1E5QDate5QTimeN2Qt8TimeSpecEi(
    const QDate *date,
    const QTime *time,
    Qt::TimeSpec spec,
    int offsetSeconds) {
  return new QDateTime(*date, *time, spec, offsetSeconds);
}

//  QDateTime::QDateTime(QDate date, QTime time, const QTimeZone &timeZone,
//      TransitionResolution resolve)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTimeC1E5QDate5QTimeRK9QTimeZoneNS_20TransitionResolutionE(
    const QDate *date,
    const QTime *time,
    const QTimeZone *timeZone,
    QDateTime::TransitionResolution resolve) {
  return new QDateTime(*date, *time, *timeZone, resolve);
}

//  QDateTime::QDateTime(QDate date, QTime time, TransitionResolution
//      resolve)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTimeC1E5QDate5QTimeNS_20TransitionResolutionE(
    const QDate *date,
    const QTime *time,
    QDateTime::TransitionResolution resolve) {
  return new QDateTime(*date, *time, resolve);
}

//  QDateTime::QDateTime(const QDateTime &other)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTimeC1ERKS_(const QDateTime *other) {
  return new QDateTime(*other);
}

//  QDateTime::~QDateTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTimeD1Ev(QDateTime *self) {
  delete self;
}

//  bool QDateTime::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QDateTime6isNullEv(const QDateTime *self) {
  return self->isNull();
}

//  bool QDateTime::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QDateTime7isValidEv(const QDateTime *self) {
  return self->isValid();
}

//  QDate QDateTime::date() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK9QDateTime4dateEv(const QDateTime *self) {
  return new QDate(self->date());
}

//  QTime QDateTime::time() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK9QDateTime4timeEv(const QDateTime *self) {
  return new QTime(self->time());
}

//  Qt::TimeSpec QDateTime::timeSpec() const
extern "C" Q_DECL_EXPORT
Qt::TimeSpec ritual_ZNK9QDateTime8timeSpecEv(const QDateTime *self) {
  return self->timeSpec();
}

//  int QDateTime::offsetFromUtc() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QDateTime13offsetFromUtcEv(const QDateTime *self) {
  return self->offsetFromUtc();
}

//  QTimeZone QDateTime::timeRepresentation() const
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZNK9QDateTime18timeRepresentationEv(
    const QDateTime *self) {
  return new QTimeZone(self->timeRepresentation());
}

//  QTimeZone QDateTime::timeZone() const
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZNK9QDateTime8timeZoneEv(const QDateTime *self) {
  return new QTimeZone(self->timeZone());
}

//  QString QDateTime::timeZoneAbbreviation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QDateTime20timeZoneAbbreviationEv(
    const QDateTime *self) {
  return new QString(self->timeZoneAbbreviation());
}

//  bool QDateTime::isDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QDateTime14isDaylightTimeEv(const QDateTime *self) {
  return self->isDaylightTime();
}

//  qint64 QDateTime::toMSecsSinceEpoch() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QDateTime17toMSecsSinceEpochEv(const QDateTime *self) {
  return self->toMSecsSinceEpoch();
}

//  qint64 QDateTime::toSecsSinceEpoch() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QDateTime16toSecsSinceEpochEv(const QDateTime *self) {
  return self->toSecsSinceEpoch();
}

//  void QDateTime::setDate(QDate date, TransitionResolution resolve)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTime7setDateE5QDateNS_20TransitionResolutionE(
    QDateTime *self,
    const QDate *date,
    QDateTime::TransitionResolution resolve) {
  self->setDate(*date, resolve);
}

//  void QDateTime::setTime(QTime time, TransitionResolution resolve)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTime7setTimeE5QTimeNS_20TransitionResolutionE(
    QDateTime *self,
    const QTime *time,
    QDateTime::TransitionResolution resolve) {
  self->setTime(*time, resolve);
}

//  void QDateTime::setTimeSpec(Qt::TimeSpec spec)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTime11setTimeSpecEN2Qt8TimeSpecE(
    QDateTime *self,
    Qt::TimeSpec spec) {
  self->setTimeSpec(spec);
}

//  void QDateTime::setOffsetFromUtc(int offsetSeconds)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTime16setOffsetFromUtcEi(
    QDateTime *self,
    int offsetSeconds) {
  self->setOffsetFromUtc(offsetSeconds);
}

//  void QDateTime::setTimeZone(const QTimeZone &toZone, TransitionResolution
//      resolve)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTime11setTimeZoneERK9QTimeZoneNS_20TransitionResolutionE(
    QDateTime *self,
    const QTimeZone *toZone,
    QDateTime::TransitionResolution resolve) {
  self->setTimeZone(*toZone, resolve);
}

//  void QDateTime::setMSecsSinceEpoch(qint64 msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTime18setMSecsSinceEpochEx(
    QDateTime *self,
    qint64 msecs) {
  self->setMSecsSinceEpoch(msecs);
}

//  void QDateTime::setSecsSinceEpoch(qint64 secs)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateTime17setSecsSinceEpochEx(QDateTime *self, qint64 secs) {
  self->setSecsSinceEpoch(secs);
}

//  QString QDateTime::toString(Qt::DateFormat format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QDateTime8toStringEN2Qt10DateFormatE(
    const QDateTime *self,
    Qt::DateFormat format) {
  return new QString(self->toString(format));
}

//  QString QDateTime::toString(const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QDateTime8toStringERK7QString(
    const QDateTime *self,
    const QString *format) {
  return new QString(self->toString(*format));
}

//  QString QDateTime::toString(const QString &format, QCalendar cal) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QDateTime8toStringERK7QString9QCalendar(
    const QDateTime *self,
    const QString *format,
    const QCalendar *cal) {
  return new QString(self->toString(*format, *cal));
}

//  QString QDateTime::toString(QStringView format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QDateTime8toStringE11QStringView(
    const QDateTime *self,
    const QString *format) {
  return new QString(self->toString(QStringView(*format)));
}

//  QString QDateTime::toString(QStringView format, QCalendar cal) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QDateTime8toStringE11QStringView9QCalendar(
    const QDateTime *self,
    const QString *format,
    const QCalendar *cal) {
  return new QString(self->toString(QStringView(*format), *cal));
}

//  QDateTime QDateTime::addDays(qint64 days) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime7addDaysEx(
    const QDateTime *self,
    qint64 days) {
  return new QDateTime(self->addDays(days));
}

//  QDateTime QDateTime::addMonths(int months) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime9addMonthsEi(
    const QDateTime *self,
    int months) {
  return new QDateTime(self->addMonths(months));
}

//  QDateTime QDateTime::addYears(int years) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime8addYearsEi(
    const QDateTime *self,
    int years) {
  return new QDateTime(self->addYears(years));
}

//  QDateTime QDateTime::addSecs(qint64 secs) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime7addSecsEx(
    const QDateTime *self,
    qint64 secs) {
  return new QDateTime(self->addSecs(secs));
}

//  QDateTime QDateTime::addMSecs(qint64 msecs) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime8addMSecsEx(
    const QDateTime *self,
    qint64 msecs) {
  return new QDateTime(self->addMSecs(msecs));
}

//  QDateTime QDateTime::toTimeSpec(Qt::TimeSpec spec) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime10toTimeSpecEN2Qt8TimeSpecE(
    const QDateTime *self,
    Qt::TimeSpec spec) {
  return new QDateTime(self->toTimeSpec(spec));
}

//  QDateTime QDateTime::toLocalTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime11toLocalTimeEv(const QDateTime *self) {
  return new QDateTime(self->toLocalTime());
}

//  QDateTime QDateTime::toUTC() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime5toUTCEv(const QDateTime *self) {
  return new QDateTime(self->toUTC());
}

//  QDateTime QDateTime::toOffsetFromUtc(int offsetSeconds) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime15toOffsetFromUtcEi(
    const QDateTime *self,
    int offsetSeconds) {
  return new QDateTime(self->toOffsetFromUtc(offsetSeconds));
}

//  QDateTime QDateTime::toTimeZone(const QTimeZone &toZone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QDateTime10toTimeZoneERK9QTimeZone(
    const QDateTime *self,
    const QTimeZone *toZone) {
  return new QDateTime(self->toTimeZone(*toZone));
}

//  qint64 QDateTime::daysTo(const QDateTime &a0) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QDateTime6daysToERKS_(
    const QDateTime *self,
    const QDateTime *a0) {
  return self->daysTo(*a0);
}

//  qint64 QDateTime::secsTo(const QDateTime &a0) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QDateTime6secsToERKS_(
    const QDateTime *self,
    const QDateTime *a0) {
  return self->secsTo(*a0);
}

//  qint64 QDateTime::msecsTo(const QDateTime &a0) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QDateTime7msecsToERKS_(
    const QDateTime *self,
    const QDateTime *a0) {
  return self->msecsTo(*a0);
}

//  QDateTime QDateTime::currentDateTime(const QTimeZone &zone)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime15currentDateTimeERK9QTimeZone(
    const QTimeZone *zone) {
  return new QDateTime(QDateTime::currentDateTime(*zone));
}

//  QDateTime QDateTime::currentDateTime()
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime15currentDateTimeEv() {
  return new QDateTime(QDateTime::currentDateTime());
}

//  QDateTime QDateTime::currentDateTimeUtc()
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime18currentDateTimeUtcEv() {
  return new QDateTime(QDateTime::currentDateTimeUtc());
}

//  QDateTime QDateTime::fromString(QStringView string, Qt::DateFormat
//      format)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringE11QStringViewN2Qt10DateFormatE(
    const QString *string,
    Qt::DateFormat format) {
  return new QDateTime(QDateTime::fromString(QStringView(*string), format));
}

//  QDateTime QDateTime::fromString(const QString &string, Qt::DateFormat
//      format)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringERK7QStringN2Qt10DateFormatE(
    const QString *string,
    Qt::DateFormat format) {
  return new QDateTime(QDateTime::fromString(*string, format));
}

//  QDateTime QDateTime::fromString(QStringView string, QStringView format,
//      QCalendar cal)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringE11QStringViewS0_9QCalendar(
    const QString *string,
    const QString *format,
    const QCalendar *cal) {
  return new QDateTime(
      QDateTime::fromString(
          QStringView(*string),
          QStringView(*format),
          *cal));
}

//  QDateTime QDateTime::fromString(const QString &string, QStringView
//      format, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringERK7QString11QStringView9QCalendar(
    const QString *string,
    const QString *format,
    const QCalendar *cal) {
  return new QDateTime(
      QDateTime::fromString(
          *string,
          QStringView(*format),
          *cal));
}

//  QDateTime QDateTime::fromString(const QString &string, const QString
//      &format, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringERK7QStringS2_9QCalendar(
    const QString *string,
    const QString *format,
    const QCalendar *cal) {
  return new QDateTime(QDateTime::fromString(*string, *format, *cal));
}

//  QDateTime QDateTime::fromString(QStringView string, QStringView format,
//      int baseYear)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringE11QStringViewS0_i(
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDateTime(
      QDateTime::fromString(
          QStringView(*string),
          QStringView(*format),
          baseYear));
}

//  QDateTime QDateTime::fromString(QStringView string, QStringView format,
//      int baseYear, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringE11QStringViewS0_i9QCalendar(
    const QString *string,
    const QString *format,
    int baseYear,
    const QCalendar *cal) {
  return new QDateTime(
      QDateTime::fromString(
          QStringView(*string),
          QStringView(*format),
          baseYear,
          *cal));
}

//  QDateTime QDateTime::fromString(const QString &string, QStringView
//      format, int baseYear)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringERK7QString11QStringViewi(
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDateTime(
      QDateTime::fromString(
          *string,
          QStringView(*format),
          baseYear));
}

//  QDateTime QDateTime::fromString(const QString &string, QStringView
//      format, int baseYear, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringERK7QString11QStringViewi9QCalendar(
    const QString *string,
    const QString *format,
    int baseYear,
    const QCalendar *cal) {
  return new QDateTime(
      QDateTime::fromString(
          *string,
          QStringView(*format),
          baseYear,
          *cal));
}

//  QDateTime QDateTime::fromString(const QString &string, const QString
//      &format, int baseYear)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringERK7QStringS2_i(
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDateTime(QDateTime::fromString(*string, *format, baseYear));
}

//  QDateTime QDateTime::fromString(const QString &string, const QString
//      &format, int baseYear, QCalendar cal)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime10fromStringERK7QStringS2_i9QCalendar(
    const QString *string,
    const QString *format,
    int baseYear,
    const QCalendar *cal) {
  return new QDateTime(
      QDateTime::fromString(
          *string,
          *format,
          baseYear,
          *cal));
}

//  QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs, Qt::TimeSpec spec,
//      int offsetFromUtc)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime19fromMSecsSinceEpochExN2Qt8TimeSpecEi(
    qint64 msecs,
    Qt::TimeSpec spec,
    int offsetFromUtc) {
  return new QDateTime(
      QDateTime::fromMSecsSinceEpoch(
          msecs,
          spec,
          offsetFromUtc));
}

//  QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs, Qt::TimeSpec spec,
//      int offsetFromUtc)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime18fromSecsSinceEpochExN2Qt8TimeSpecEi(
    qint64 secs,
    Qt::TimeSpec spec,
    int offsetFromUtc) {
  return new QDateTime(
      QDateTime::fromSecsSinceEpoch(
          secs,
          spec,
          offsetFromUtc));
}

//  QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs, const QTimeZone
//      &timeZone)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime19fromMSecsSinceEpochExRK9QTimeZone(
    qint64 msecs,
    const QTimeZone *timeZone) {
  return new QDateTime(QDateTime::fromMSecsSinceEpoch(msecs, *timeZone));
}

//  QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs, const QTimeZone
//      &timeZone)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime18fromSecsSinceEpochExRK9QTimeZone(
    qint64 secs,
    const QTimeZone *timeZone) {
  return new QDateTime(QDateTime::fromSecsSinceEpoch(secs, *timeZone));
}

//  QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime19fromMSecsSinceEpochEx(qint64 msecs) {
  return new QDateTime(QDateTime::fromMSecsSinceEpoch(msecs));
}

//  QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN9QDateTime18fromSecsSinceEpochEx(qint64 secs) {
  return new QDateTime(QDateTime::fromSecsSinceEpoch(secs));
}

//  qint64 QDateTime::currentMSecsSinceEpoch()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QDateTime22currentMSecsSinceEpochEv() {
  return QDateTime::currentMSecsSinceEpoch();
}

//  qint64 QDateTime::currentSecsSinceEpoch()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QDateTime21currentSecsSinceEpochEv() {
  return QDateTime::currentSecsSinceEpoch();
}
