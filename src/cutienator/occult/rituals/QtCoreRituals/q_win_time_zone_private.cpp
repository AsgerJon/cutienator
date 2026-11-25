//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what
//  its header writes out.
//  It is final, so 'self' is taken as a QTimeZonePrivate, and the
//  calls stay virtual.
//  Not written: 'ruleToData', which Qt's library offers not.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && !(defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)) && !QT_CONFIG(icu) && defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>

//  QWinTimeZonePrivate *QWinTimeZonePrivate::clone() const
extern "C" Q_DECL_EXPORT
QWinTimeZonePrivate *ritual_ZNK19QWinTimeZonePrivate5cloneEv(
    const QTimeZonePrivate *self) {
  return static_cast<QWinTimeZonePrivate *>(self->clone());
}

//  QWinTimeZonePrivate::~QWinTimeZonePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWinTimeZonePrivateD1Ev(QTimeZonePrivate *self) {
  delete self;
}

//  QString QWinTimeZonePrivate::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWinTimeZonePrivate7commentEv(
    const QTimeZonePrivate *self) {
  return new QString(self->comment());
}

//  QString QWinTimeZonePrivate::displayName(QTimeZone::TimeType timeType,
//      QTimeZone::NameType nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWinTimeZonePrivate11displayNameEN9QTimeZone8TimeTypeENS0_8NameTypeERK7QLocale(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(timeType, nameType, *locale));
}

//  QString QWinTimeZonePrivate::abbreviation(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWinTimeZonePrivate12abbreviationEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return new QString(self->abbreviation(atMSecsSinceEpoch));
}

//  int QWinTimeZonePrivate::offsetFromUtc(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWinTimeZonePrivate13offsetFromUtcEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->offsetFromUtc(atMSecsSinceEpoch);
}

//  int QWinTimeZonePrivate::standardTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWinTimeZonePrivate18standardTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->standardTimeOffset(atMSecsSinceEpoch);
}

//  int QWinTimeZonePrivate::daylightTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWinTimeZonePrivate18daylightTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->daylightTimeOffset(atMSecsSinceEpoch);
}

//  bool QWinTimeZonePrivate::hasDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWinTimeZonePrivate15hasDaylightTimeEv(
    const QTimeZonePrivate *self) {
  return self->hasDaylightTime();
}

//  bool QWinTimeZonePrivate::isDaylightTime(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWinTimeZonePrivate14isDaylightTimeEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->isDaylightTime(atMSecsSinceEpoch);
}

//  Data QWinTimeZonePrivate::data(qint64 forMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QWinTimeZonePrivate4dataEx(
    const QTimeZonePrivate *self,
    qint64 forMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->data(forMSecsSinceEpoch));
}

//  bool QWinTimeZonePrivate::hasTransitions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWinTimeZonePrivate14hasTransitionsEv(
    const QTimeZonePrivate *self) {
  return self->hasTransitions();
}

//  Data QWinTimeZonePrivate::nextTransition(qint64 afterMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QWinTimeZonePrivate14nextTransitionEx(
    const QTimeZonePrivate *self,
    qint64 afterMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->nextTransition(afterMSecsSinceEpoch));
}

//  Data QWinTimeZonePrivate::previousTransition(qint64
//      beforeMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QWinTimeZonePrivate18previousTransitionEx(
    const QTimeZonePrivate *self,
    qint64 beforeMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->previousTransition(beforeMSecsSinceEpoch));
}

//  QByteArray QWinTimeZonePrivate::systemTimeZoneId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QWinTimeZonePrivate16systemTimeZoneIdEv(
    const QTimeZonePrivate *self) {
  return new QByteArray(self->systemTimeZoneId());
}

//  QList<QByteArray> QWinTimeZonePrivate::availableTimeZoneIds() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK19QWinTimeZonePrivate20availableTimeZoneIdsEv(
    const QTimeZonePrivate *self) {
  return new QList<QByteArray>(self->availableTimeZoneIds());
}

#endif  // QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && !(defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)) && !QT_CONFIG(icu) && defined(Q_OS_WIN)
