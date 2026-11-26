//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimezone.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtimezone.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlocale.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/QTimeZone>
#include <QtCore/QByteArray>
#include <QtCore/QString>
#include <QtCore/QLocale>
#include <QtCore/QDateTime>
#include <QtCore/QList>

//  QTimeZone::QTimeZone(ShortData sd)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ENS_9ShortDataE(
    const QTimeZone::ShortData *sd) {
  return new QTimeZone(*sd);
}

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

#if QT_CONFIG(timezone)
//  QTimeZone::QTimeZone(int offsetSeconds)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1Ei(int offsetSeconds) {
  return new QTimeZone(offsetSeconds);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QTimeZone::QTimeZone(const QByteArray &ianaId)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ERK10QByteArray(const QByteArray *ianaId) {
  return new QTimeZone(*ianaId);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QTimeZone::QTimeZone(const QByteArray &zoneId, int offsetSeconds, const
//      QString &name, const QString &abbreviation, QLocale::Territory
//      territory, const QString &comment)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ERK10QByteArrayiRK7QStringS5_N7QLocale7CountryES5_(
    const QByteArray *zoneId,
    int offsetSeconds,
    const QString *name,
    const QString *abbreviation,
    const QLocale::Territory *territory,
    const QString *comment) {
  return new QTimeZone(
      *zoneId,
      offsetSeconds,
      *name,
      *abbreviation,
      *territory,
      *comment);
}
#endif  // QT_CONFIG(timezone)

//  QTimeZone::QTimeZone(const QTimeZone &other)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ERKS_(const QTimeZone *other) {
  return new QTimeZone(*other);
}

//  QTimeZone::QTimeZone(QTimeZone &&other)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1EOS_(QTimeZone *other) {
  return new QTimeZone(std::move(*other));
}

//  QTimeZone::~QTimeZone()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeZoneD1Ev(QTimeZone *self) {
  delete self;
}

//  QTimeZone &QTimeZone::operator=(const QTimeZone &other)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneaSERKS_(
    QTimeZone *self,
    const QTimeZone *other) {
  return &(self->operator=(*other));
}

//  QTimeZone &QTimeZone::operator=(QTimeZone &&other)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneaSEOS_(QTimeZone *self, QTimeZone *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QTimeZone::swap(QTimeZone &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeZone4swapERS_(QTimeZone *self, QTimeZone *other) {
  self->swap(*other);
}

//  bool QTimeZone::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone7isValidEv(const QTimeZone *self) {
  return self->isValid();
}

//  QTimeZone QTimeZone::fromDurationAheadOfUtc(std::chrono::seconds offset)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZone22fromDurationAheadOfUtcENSt6chrono8durationIlSt5ratioILl1ELl1EEEE(
    long long offset) {
  return new QTimeZone(
      QTimeZone::fromDurationAheadOfUtc(
          std::chrono::seconds(offset)));
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

#if QT_CONFIG(timezone)
//  QTimeZone QTimeZone::asBackendZone() const
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZNK9QTimeZone13asBackendZoneEv(const QTimeZone *self) {
  return new QTimeZone(self->asBackendZone());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  bool QTimeZone::hasAlternativeName(QByteArrayView alias) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone18hasAlternativeNameE14QByteArrayView(
    const QTimeZone *self,
    const QByteArrayView *alias) {
  return self->hasAlternativeName(*alias);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QByteArray QTimeZone::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QTimeZone2idEv(const QTimeZone *self) {
  return new QByteArray(self->id());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QLocale::Territory QTimeZone::territory() const
extern "C" Q_DECL_EXPORT
QLocale::Territory *ritual_ZNK9QTimeZone9territoryEv(const QTimeZone *self) {
  return new QLocale::Territory(self->territory());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
#if QT_DEPRECATED_SINCE(6, 6)
//  QLocale::Country QTimeZone::country() const
extern "C" Q_DECL_EXPORT
QLocale::Country ritual_ZNK9QTimeZone7countryEv(const QTimeZone *self) {
  return self->country();
}
#endif  // QT_DEPRECATED_SINCE(6, 6)
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QString QTimeZone::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTimeZone7commentEv(const QTimeZone *self) {
  return new QString(self->comment());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
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
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
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
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QString QTimeZone::abbreviation(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTimeZone12abbreviationERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return new QString(self->abbreviation(*atDateTime));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  int QTimeZone::offsetFromUtc(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeZone13offsetFromUtcERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->offsetFromUtc(*atDateTime);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  int QTimeZone::standardTimeOffset(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeZone18standardTimeOffsetERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->standardTimeOffset(*atDateTime);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  int QTimeZone::daylightTimeOffset(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTimeZone18daylightTimeOffsetERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->daylightTimeOffset(*atDateTime);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  bool QTimeZone::hasDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone15hasDaylightTimeEv(const QTimeZone *self) {
  return self->hasDaylightTime();
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  bool QTimeZone::isDaylightTime(const QDateTime &atDateTime) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone14isDaylightTimeERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *atDateTime) {
  return self->isDaylightTime(*atDateTime);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  OffsetData QTimeZone::offsetData(const QDateTime &forDateTime) const
extern "C" Q_DECL_EXPORT
QTimeZone::OffsetData *ritual_ZNK9QTimeZone10offsetDataERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *forDateTime) {
  return new QTimeZone::OffsetData(self->offsetData(*forDateTime));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  bool QTimeZone::hasTransitions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTimeZone14hasTransitionsEv(const QTimeZone *self) {
  return self->hasTransitions();
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  OffsetData QTimeZone::nextTransition(const QDateTime &afterDateTime)
//      const
extern "C" Q_DECL_EXPORT
QTimeZone::OffsetData *ritual_ZNK9QTimeZone14nextTransitionERK9QDateTime(
    const QTimeZone *self,
    const QDateTime *afterDateTime) {
  return new QTimeZone::OffsetData(self->nextTransition(*afterDateTime));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
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
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  OffsetDataList QTimeZone::transitions(const QDateTime &fromDateTime,
//      const QDateTime &toDateTime) const
extern "C" Q_DECL_EXPORT
QTimeZone::OffsetDataList *ritual_ZNK9QTimeZone11transitionsERK9QDateTimeS2_(
    const QTimeZone *self,
    const QDateTime *fromDateTime,
    const QDateTime *toDateTime) {
  return new QTimeZone::OffsetDataList(
      self->transitions(
          *fromDateTime,
          *toDateTime));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QByteArray QTimeZone::systemTimeZoneId()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QTimeZone16systemTimeZoneIdEv() {
  return new QByteArray(QTimeZone::systemTimeZoneId());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QTimeZone QTimeZone::systemTimeZone()
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZone14systemTimeZoneEv() {
  return new QTimeZone(QTimeZone::systemTimeZone());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QTimeZone QTimeZone::utc()
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZone3utcEv() {
  return new QTimeZone(QTimeZone::utc());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  bool QTimeZone::isTimeZoneIdAvailable(QByteArrayView ianaId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTimeZone21isTimeZoneIdAvailableE14QByteArrayView(
    const QByteArrayView *ianaId) {
  return QTimeZone::isTimeZoneIdAvailable(*ianaId);
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QList<QByteArray> QTimeZone::availableTimeZoneIds()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QTimeZone20availableTimeZoneIdsEv() {
  return new QList<QByteArray>(QTimeZone::availableTimeZoneIds());
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QList<QByteArray> QTimeZone::availableTimeZoneIds(QLocale::Territory
//      territory)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QTimeZone20availableTimeZoneIdsEN7QLocale7CountryE(
    const QLocale::Territory *territory) {
  return new QList<QByteArray>(QTimeZone::availableTimeZoneIds(*territory));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QList<QByteArray> QTimeZone::availableTimeZoneIds(int offsetSeconds)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QTimeZone20availableTimeZoneIdsEi(
    int offsetSeconds) {
  return new QList<QByteArray>(
      QTimeZone::availableTimeZoneIds(
          offsetSeconds));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QByteArray QTimeZone::ianaIdToWindowsId(const QByteArray &ianaId)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QTimeZone17ianaIdToWindowsIdERK10QByteArray(
    const QByteArray *ianaId) {
  return new QByteArray(QTimeZone::ianaIdToWindowsId(*ianaId));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QByteArray QTimeZone::windowsIdToDefaultIanaId(const QByteArray
//      &windowsId)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QTimeZone24windowsIdToDefaultIanaIdERK10QByteArray(
    const QByteArray *windowsId) {
  return new QByteArray(QTimeZone::windowsIdToDefaultIanaId(*windowsId));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QByteArray QTimeZone::windowsIdToDefaultIanaId(const QByteArray
//      &windowsId, QLocale::Territory territory)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QTimeZone24windowsIdToDefaultIanaIdERK10QByteArrayN7QLocale7CountryE(
    const QByteArray *windowsId,
    const QLocale::Territory *territory) {
  return new QByteArray(
      QTimeZone::windowsIdToDefaultIanaId(
          *windowsId,
          *territory));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QList<QByteArray> QTimeZone::windowsIdToIanaIds(const QByteArray
//      &windowsId)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QTimeZone18windowsIdToIanaIdsERK10QByteArray(
    const QByteArray *windowsId) {
  return new QList<QByteArray>(QTimeZone::windowsIdToIanaIds(*windowsId));
}
#endif  // QT_CONFIG(timezone)

#if QT_CONFIG(timezone)
//  QList<QByteArray> QTimeZone::windowsIdToIanaIds(const QByteArray
//      &windowsId, QLocale::Territory territory)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN9QTimeZone18windowsIdToIanaIdsERK10QByteArrayN7QLocale7CountryE(
    const QByteArray *windowsId,
    const QLocale::Territory *territory) {
  return new QList<QByteArray>(
      QTimeZone::windowsIdToIanaIds(
          *windowsId,
          *territory));
}
#endif  // QT_CONFIG(timezone)

//  bool operator==(const QTimeZone &lhs, const QTimeZone &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QTimeZoneS1_(const QTimeZone *lhs, const QTimeZone *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QTimeZone &lhs, const QTimeZone &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QTimeZoneS1_(const QTimeZone *lhs, const QTimeZone *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &ds, const QTimeZone &tz)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK9QTimeZone(
    QDataStream *ds,
    const QTimeZone *tz) {
  return &(operator<<(*ds, *tz));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QTimeZone &tz)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK9QTimeZone(
    const QDebug *dbg,
    const QTimeZone *tz) {
  return new QDebug(operator<<(*dbg, *tz));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QTimeZone::QTimeZone(QTimeZonePrivate &dd)
extern "C" Q_DECL_EXPORT
QTimeZone *ritual_ZN9QTimeZoneC1ER16QTimeZonePrivate(QTimeZonePrivate *dd) {
  return new QTimeZone(*dd);
}

//  a QLocale::Territory a ritual of QTimeZone gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimeZone__QLocale_Territory(QLocale::Territory *self) {
  delete self;
}

//  a QTimeZone::OffsetDataList a ritual of QTimeZone gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimeZone__QTimeZone_OffsetDataList(
    QTimeZone::OffsetDataList *self) {
  delete self;
}
