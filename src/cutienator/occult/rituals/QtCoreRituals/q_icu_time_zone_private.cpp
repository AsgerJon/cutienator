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
#if QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && !(defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)) && QT_CONFIG(icu)
#include <QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>

//  QIcuTimeZonePrivate *QIcuTimeZonePrivate::clone() const
extern "C" Q_DECL_EXPORT
QIcuTimeZonePrivate *ritual_ZNK19QIcuTimeZonePrivate5cloneEv(
    const QTimeZonePrivate *self) {
  return static_cast<QIcuTimeZonePrivate *>(self->clone());
}

//  QIcuTimeZonePrivate::~QIcuTimeZonePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIcuTimeZonePrivateD1Ev(QTimeZonePrivate *self) {
  delete self;
}

//  QString QIcuTimeZonePrivate::displayName(QTimeZone::TimeType timeType,
//      QTimeZone::NameType nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QIcuTimeZonePrivate11displayNameEN9QTimeZone8TimeTypeENS0_8NameTypeERK7QLocale(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(timeType, nameType, *locale));
}

//  int QIcuTimeZonePrivate::offsetFromUtc(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QIcuTimeZonePrivate13offsetFromUtcEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->offsetFromUtc(atMSecsSinceEpoch);
}

//  int QIcuTimeZonePrivate::standardTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QIcuTimeZonePrivate18standardTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->standardTimeOffset(atMSecsSinceEpoch);
}

//  int QIcuTimeZonePrivate::daylightTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QIcuTimeZonePrivate18daylightTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->daylightTimeOffset(atMSecsSinceEpoch);
}

//  bool QIcuTimeZonePrivate::hasDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIcuTimeZonePrivate15hasDaylightTimeEv(
    const QTimeZonePrivate *self) {
  return self->hasDaylightTime();
}

//  bool QIcuTimeZonePrivate::isDaylightTime(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIcuTimeZonePrivate14isDaylightTimeEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->isDaylightTime(atMSecsSinceEpoch);
}

//  Data QIcuTimeZonePrivate::data(qint64 forMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QIcuTimeZonePrivate4dataEx(
    const QTimeZonePrivate *self,
    qint64 forMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->data(forMSecsSinceEpoch));
}

//  bool QIcuTimeZonePrivate::hasTransitions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIcuTimeZonePrivate14hasTransitionsEv(
    const QTimeZonePrivate *self) {
  return self->hasTransitions();
}

//  Data QIcuTimeZonePrivate::nextTransition(qint64 afterMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QIcuTimeZonePrivate14nextTransitionEx(
    const QTimeZonePrivate *self,
    qint64 afterMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->nextTransition(afterMSecsSinceEpoch));
}

//  Data QIcuTimeZonePrivate::previousTransition(qint64
//      beforeMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QIcuTimeZonePrivate18previousTransitionEx(
    const QTimeZonePrivate *self,
    qint64 beforeMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->previousTransition(beforeMSecsSinceEpoch));
}

//  QByteArray QIcuTimeZonePrivate::systemTimeZoneId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QIcuTimeZonePrivate16systemTimeZoneIdEv(
    const QTimeZonePrivate *self) {
  return new QByteArray(self->systemTimeZoneId());
}

//  bool QIcuTimeZonePrivate::isTimeZoneIdAvailable(QByteArrayView ianaId)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIcuTimeZonePrivate21isTimeZoneIdAvailableE14QByteArrayView(
    const QTimeZonePrivate *self,
    const QByteArrayView *ianaId) {
  return self->isTimeZoneIdAvailable(*ianaId);
}

//  QList<QByteArray> QIcuTimeZonePrivate::availableTimeZoneIds() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK19QIcuTimeZonePrivate20availableTimeZoneIdsEv(
    const QTimeZonePrivate *self) {
  return new QList<QByteArray>(self->availableTimeZoneIds());
}

//  QList<QByteArray>
//      QIcuTimeZonePrivate::availableTimeZoneIds(QLocale::Territory
//      territory) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK19QIcuTimeZonePrivate20availableTimeZoneIdsEN7QLocale7CountryE(
    const QTimeZonePrivate *self,
    QLocale::Territory territory) {
  return new QList<QByteArray>(self->availableTimeZoneIds(territory));
}

//  QList<QByteArray> QIcuTimeZonePrivate::availableTimeZoneIds(int
//      utcOffset) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK19QIcuTimeZonePrivate20availableTimeZoneIdsEi(
    const QTimeZonePrivate *self,
    int utcOffset) {
  return new QList<QByteArray>(self->availableTimeZoneIds(utcOffset));
}

#endif  // QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && !(defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)) && QT_CONFIG(icu)
