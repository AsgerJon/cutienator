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
#if QT_CONFIG(timezone) && QT_CONFIG(timezone_tzdb)
#include <QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>

//  QChronoTimeZonePrivate *QChronoTimeZonePrivate::clone() const
extern "C" Q_DECL_EXPORT
QChronoTimeZonePrivate *ritual_ZNK22QChronoTimeZonePrivate5cloneEv(
    const QTimeZonePrivate *self) {
  return static_cast<QChronoTimeZonePrivate *>(self->clone());
}

//  QChronoTimeZonePrivate::~QChronoTimeZonePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QChronoTimeZonePrivateD1Ev(QTimeZonePrivate *self) {
  delete self;
}

//  QByteArray QChronoTimeZonePrivate::systemTimeZoneId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QChronoTimeZonePrivate16systemTimeZoneIdEv(
    const QTimeZonePrivate *self) {
  return new QByteArray(self->systemTimeZoneId());
}

//  QString QChronoTimeZonePrivate::abbreviation(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QChronoTimeZonePrivate12abbreviationEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return new QString(self->abbreviation(atMSecsSinceEpoch));
}

//  int QChronoTimeZonePrivate::offsetFromUtc(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QChronoTimeZonePrivate13offsetFromUtcEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->offsetFromUtc(atMSecsSinceEpoch);
}

//  int QChronoTimeZonePrivate::standardTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QChronoTimeZonePrivate18standardTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->standardTimeOffset(atMSecsSinceEpoch);
}

//  int QChronoTimeZonePrivate::daylightTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QChronoTimeZonePrivate18daylightTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->daylightTimeOffset(atMSecsSinceEpoch);
}

//  bool QChronoTimeZonePrivate::isTimeZoneIdAvailable(QByteArrayView ianaId)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QChronoTimeZonePrivate21isTimeZoneIdAvailableE14QByteArrayView(
    const QTimeZonePrivate *self,
    const QByteArrayView *ianaId) {
  return self->isTimeZoneIdAvailable(*ianaId);
}

//  QList<QByteArray> QChronoTimeZonePrivate::availableTimeZoneIds() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK22QChronoTimeZonePrivate20availableTimeZoneIdsEv(
    const QTimeZonePrivate *self) {
  return new QList<QByteArray>(self->availableTimeZoneIds());
}

//  QList<QByteArray> QChronoTimeZonePrivate::availableTimeZoneIds(int
//      utcOffset) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK22QChronoTimeZonePrivate20availableTimeZoneIdsEi(
    const QTimeZonePrivate *self,
    int utcOffset) {
  return new QList<QByteArray>(self->availableTimeZoneIds(utcOffset));
}

//  bool QChronoTimeZonePrivate::hasDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QChronoTimeZonePrivate15hasDaylightTimeEv(
    const QTimeZonePrivate *self) {
  return self->hasDaylightTime();
}

//  bool QChronoTimeZonePrivate::isDaylightTime(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QChronoTimeZonePrivate14isDaylightTimeEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->isDaylightTime(atMSecsSinceEpoch);
}

//  Data QChronoTimeZonePrivate::data(qint64 forMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK22QChronoTimeZonePrivate4dataEx(
    const QTimeZonePrivate *self,
    qint64 forMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->data(forMSecsSinceEpoch));
}

//  bool QChronoTimeZonePrivate::hasTransitions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QChronoTimeZonePrivate14hasTransitionsEv(
    const QTimeZonePrivate *self) {
  return self->hasTransitions();
}

//  Data QChronoTimeZonePrivate::nextTransition(qint64 afterMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK22QChronoTimeZonePrivate14nextTransitionEx(
    const QTimeZonePrivate *self,
    qint64 afterMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->nextTransition(afterMSecsSinceEpoch));
}

//  Data QChronoTimeZonePrivate::previousTransition(qint64
//      beforeMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK22QChronoTimeZonePrivate18previousTransitionEx(
    const QTimeZonePrivate *self,
    qint64 beforeMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->previousTransition(beforeMSecsSinceEpoch));
}

#endif  // QT_CONFIG(timezone) && QT_CONFIG(timezone_tzdb)
