//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimezone.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtimezone.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlocale.h>

//  QTimeZone::QTimeZone()
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1Ev() {
  return new QTimeZone();
}

//  QTimeZone::QTimeZone(Initialization spec)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ENS_14InitializationE(
    QTimeZone::Initialization spec) {
  return new QTimeZone(spec);
}

//  QTimeZone::QTimeZone(int offsetSeconds)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1Ei(int offsetSeconds) {
  return new QTimeZone(offsetSeconds);
}

//  QTimeZone::QTimeZone(const QByteArray &ianaId)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ERK10QByteArray(const QByteArray *ianaId) {
  return new QTimeZone(*ianaId);
}

//  QTimeZone::QTimeZone(const QTimeZone &other)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ERKS_(const QTimeZone *other) {
  return new QTimeZone(*other);
}

//  QTimeZone::~QTimeZone()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeZoneD1Ev(QTimeZone *self) {
  delete self;
}

//  bool QTimeZone::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone7isValidEv(const QTimeZone *self) {
  return self->isValid();
}

//  QTimeZone QTimeZone::fromSecondsAheadOfUtc(int offset)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZone21fromSecondsAheadOfUtcEi(int offset) {
  return new QTimeZone(QTimeZone::fromSecondsAheadOfUtc(offset));
}

//  Qt::TimeSpec QTimeZone::timeSpec() const
extern "C" Q_DECL_EXPORT
Qt::TimeSpec ritual_ZNK9QTimeZone8timeSpecEv(const QTimeZone *self) {
  return self->timeSpec();
}

//  int QTimeZone::fixedSecondsAheadOfUtc() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeZone22fixedSecondsAheadOfUtcEv(const QTimeZone *self) {
  return self->fixedSecondsAheadOfUtc();
}

//  bool QTimeZone::isUtcOrFixedOffset(Qt::TimeSpec spec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTimeZone18isUtcOrFixedOffsetEN2Qt8TimeSpecE(
    Qt::TimeSpec spec) {
  return QTimeZone::isUtcOrFixedOffset(spec);
}

//  bool QTimeZone::isUtcOrFixedOffset() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone18isUtcOrFixedOffsetEv(const QTimeZone *self) {
  return self->isUtcOrFixedOffset();
}

//  QTimeZone QTimeZone::asBackendZone() const
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZNK9QTimeZone13asBackendZoneEv(const QTimeZone *self) {
  return new QTimeZone(self->asBackendZone());
}

//  bool QTimeZone::hasAlternativeName(QByteArrayView alias) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone18hasAlternativeNameE14QByteArrayView(
    const QTimeZone *self,
    const QByteArrayView *alias) {
  return self->hasAlternativeName(*alias);
}

//  QByteArray QTimeZone::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QTimeZone2idEv(const QTimeZone *self) {
  return new QByteArray(self->id());
}

//  QLocale::Country QTimeZone::country() const
extern "C" Q_DECL_EXPORT
QLocale::Country ritual_ZNK9QTimeZone7countryEv(const QTimeZone *self) {
  return self->country();
}

//  QString QTimeZone::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTimeZone7commentEv(const QTimeZone *self) {
  return new QString(self->comment());
}

//  QString QTimeZone::displayName(const QDateTime &atDateTime, NameType
//      nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTimeZone11displayNameERK9QDateTimeNS_8NameTypeERK7QLocale(
    const QTimeZone *self,
    const QDateTime *atDateTime,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(*atDateTime, nameType, *locale));
}

//  QString QTimeZone::displayName(TimeType timeType, NameType nameType,
//      const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTimeZone11displayNameENS_8TimeTypeENS_8NameTypeERK7QLocale(
    const QTimeZone *self,
    QTimeZone::TimeType timeType,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(timeType, nameType, *locale));
}

//  QString QTimeZone::abbreviation(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTimeZone12abbreviationERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return new QString(self->abbreviation(*atDateTime));
}

//  int QTimeZone::offsetFromUtc(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeZone13offsetFromUtcERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->offsetFromUtc(*atDateTime);
}

//  int QTimeZone::standardTimeOffset(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeZone18standardTimeOffsetERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->standardTimeOffset(*atDateTime);
}

//  int QTimeZone::daylightTimeOffset(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeZone18daylightTimeOffsetERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->daylightTimeOffset(*atDateTime);
}

//  bool QTimeZone::hasDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone15hasDaylightTimeEv(const QTimeZone *self) {
  return self->hasDaylightTime();
}

//  bool QTimeZone::isDaylightTime(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone14isDaylightTimeERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->isDaylightTime(*atDateTime);
}

//  OffsetData QTimeZone::offsetData(const QDateTime &forDateTime) const
extern "C" Q_DECL_EXPORT
QTimeZone::OffsetData *ritual_ZNK9QTimeZone10offsetDataERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *forDateTime) {
  return new QTimeZone::OffsetData(self->offsetData(*forDateTime));
}

//  bool QTimeZone::hasTransitions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone14hasTransitionsEv(const QTimeZone *self) {
  return self->hasTransitions();
}

//  OffsetData QTimeZone::nextTransition(const QDateTime &afterDateTime)
//      const
extern "C" Q_DECL_EXPORT
QTimeZone::OffsetData *ritual_ZNK9QTimeZone14nextTransitionERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *afterDateTime) {
  return new QTimeZone::OffsetData(self->nextTransition(*afterDateTime));
}

//  OffsetData QTimeZone::previousTransition(const QDateTime &beforeDateTime)
//      const
extern "C" Q_DECL_EXPORT
QTimeZone::OffsetData *ritual_ZNK9QTimeZone18previousTransitionERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *beforeDateTime) {
  return new QTimeZone::OffsetData(
      self->previousTransition(
          *beforeDateTime));
}

//  QByteArray QTimeZone::systemTimeZoneId()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QTimeZone16systemTimeZoneIdEv() {
  return new QByteArray(QTimeZone::systemTimeZoneId());
}

//  QTimeZone QTimeZone::systemTimeZone()
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZone14systemTimeZoneEv() {
  return new QTimeZone(QTimeZone::systemTimeZone());
}

//  QTimeZone QTimeZone::utc()
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZone3utcEv() {
  return new QTimeZone(QTimeZone::utc());
}

//  bool QTimeZone::isTimeZoneIdAvailable(QByteArrayView ianaId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTimeZone21isTimeZoneIdAvailableE14QByteArrayView(
    const QByteArrayView *ianaId) {
  return QTimeZone::isTimeZoneIdAvailable(*ianaId);
}

//  QByteArray QTimeZone::ianaIdToWindowsId(const QByteArray &ianaId)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QTimeZone17ianaIdToWindowsIdERK10QByteArray(
    const QByteArray *ianaId) {
  return new QByteArray(QTimeZone::ianaIdToWindowsId(*ianaId));
}

//  QByteArray QTimeZone::windowsIdToDefaultIanaId(const QByteArray
//      &windowsId)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QTimeZone24windowsIdToDefaultIanaIdERK10QByteArray(
    const QByteArray *windowsId) {
  return new QByteArray(QTimeZone::windowsIdToDefaultIanaId(*windowsId));
}
