//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what
//  its header writes out.
//  It is final, so 'self' is taken as a QTimeZonePrivate, and the
//  calls stay virtual.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)
#include <QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>

//  QTzTimeZonePrivate *QTzTimeZonePrivate::clone() const
extern "C" Q_DECL_EXPORT
QTzTimeZonePrivate *ritual_ZNK18QTzTimeZonePrivate5cloneEv(
    const QTimeZonePrivate *self) {
  return static_cast<QTzTimeZonePrivate *>(self->clone());
}

//  QTzTimeZonePrivate::~QTzTimeZonePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTzTimeZonePrivateD1Ev(QTimeZonePrivate *self) {
  delete self;
}

//  QLocale::Territory QTzTimeZonePrivate::territory() const
extern "C" Q_DECL_EXPORT
QLocale::Territory ritual_ZNK18QTzTimeZonePrivate9territoryEv(
    const QTimeZonePrivate *self) {
  return self->territory();
}

//  QString QTzTimeZonePrivate::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QTzTimeZonePrivate7commentEv(
    const QTimeZonePrivate *self) {
  return new QString(self->comment());
}

//  QString QTzTimeZonePrivate::displayName(QTimeZone::TimeType timeType,
//      QTimeZone::NameType nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QTzTimeZonePrivate11displayNameEN9QTimeZone8TimeTypeENS0_8NameTypeERK7QLocale(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(timeType, nameType, *locale));
}

//  QString QTzTimeZonePrivate::abbreviation(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QTzTimeZonePrivate12abbreviationEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return new QString(self->abbreviation(atMSecsSinceEpoch));
}

//  int QTzTimeZonePrivate::offsetFromUtc(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QTzTimeZonePrivate13offsetFromUtcEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->offsetFromUtc(atMSecsSinceEpoch);
}

//  int QTzTimeZonePrivate::standardTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QTzTimeZonePrivate18standardTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->standardTimeOffset(atMSecsSinceEpoch);
}

//  int QTzTimeZonePrivate::daylightTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QTzTimeZonePrivate18daylightTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->daylightTimeOffset(atMSecsSinceEpoch);
}

//  bool QTzTimeZonePrivate::hasDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTzTimeZonePrivate15hasDaylightTimeEv(
    const QTimeZonePrivate *self) {
  return self->hasDaylightTime();
}

//  bool QTzTimeZonePrivate::isDaylightTime(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTzTimeZonePrivate14isDaylightTimeEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->isDaylightTime(atMSecsSinceEpoch);
}

//  Data QTzTimeZonePrivate::data(qint64 forMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK18QTzTimeZonePrivate4dataEx(
    const QTimeZonePrivate *self,
    qint64 forMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->data(forMSecsSinceEpoch));
}

//  Data QTzTimeZonePrivate::data(QTimeZone::TimeType timeType) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK18QTzTimeZonePrivate4dataEN9QTimeZone8TimeTypeE(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType) {
  return new QTimeZonePrivate::Data(self->data(timeType));
}

//  bool QTzTimeZonePrivate::isDataLocale(const QLocale &locale) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTzTimeZonePrivate12isDataLocaleERK7QLocale(
    const QTimeZonePrivate *self,
    const QLocale *locale) {
  return self->isDataLocale(*locale);
}

//  bool QTzTimeZonePrivate::hasTransitions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTzTimeZonePrivate14hasTransitionsEv(
    const QTimeZonePrivate *self) {
  return self->hasTransitions();
}

//  Data QTzTimeZonePrivate::nextTransition(qint64 afterMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK18QTzTimeZonePrivate14nextTransitionEx(
    const QTimeZonePrivate *self,
    qint64 afterMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->nextTransition(afterMSecsSinceEpoch));
}

//  Data QTzTimeZonePrivate::previousTransition(qint64 beforeMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK18QTzTimeZonePrivate18previousTransitionEx(
    const QTimeZonePrivate *self,
    qint64 beforeMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->previousTransition(beforeMSecsSinceEpoch));
}

//  QByteArray QTzTimeZonePrivate::systemTimeZoneId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QTzTimeZonePrivate16systemTimeZoneIdEv(
    const QTimeZonePrivate *self) {
  return new QByteArray(self->systemTimeZoneId());
}

//  bool QTzTimeZonePrivate::isTimeZoneIdAvailable(QByteArrayView ianaId)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTzTimeZonePrivate21isTimeZoneIdAvailableE14QByteArrayView(
    const QTimeZonePrivate *self,
    const QByteArrayView *ianaId) {
  return self->isTimeZoneIdAvailable(*ianaId);
}

//  QList<QByteArray> QTzTimeZonePrivate::availableTimeZoneIds() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK18QTzTimeZonePrivate20availableTimeZoneIdsEv(
    const QTimeZonePrivate *self) {
  return new QList<QByteArray>(self->availableTimeZoneIds());
}

//  QList<QByteArray>
//      QTzTimeZonePrivate::availableTimeZoneIds(QLocale::Territory
//      territory) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK18QTzTimeZonePrivate20availableTimeZoneIdsEN7QLocale7CountryE(
    const QTimeZonePrivate *self,
    QLocale::Territory territory) {
  return new QList<QByteArray>(self->availableTimeZoneIds(territory));
}

//  const QList<QTzTransitionTime> &QTzTimeZonePrivate::tranCache() const
extern "C" Q_DECL_EXPORT
const QList<QTzTransitionTime> *ritual_ZNK18QTzTimeZonePrivate9tranCacheEv(
    const QTzTimeZonePrivate *self) {
  return &self->tranCache();
}

#endif  // QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)
