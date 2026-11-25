//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what
//  its header writes out.
//  Not written: 'serialize', taking a 'QDataStream &'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(timezone)
#include <QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>

//  QTimeZonePrivate *QTimeZonePrivate::clone() const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate *ritual_ZNK16QTimeZonePrivate5cloneEv(
    const QTimeZonePrivate *self) {
  return self->clone();
}

//  QTimeZonePrivate::~QTimeZonePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTimeZonePrivateD1Ev(QTimeZonePrivate *self) {
  delete self;
}

//  QLocale::Territory QTimeZonePrivate::territory() const
extern "C" Q_DECL_EXPORT
QLocale::Territory ritual_ZNK16QTimeZonePrivate9territoryEv(
    const QTimeZonePrivate *self) {
  return self->territory();
}

//  QString QTimeZonePrivate::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTimeZonePrivate7commentEv(
    const QTimeZonePrivate *self) {
  return new QString(self->comment());
}

//  QString QTimeZonePrivate::displayName(qint64 atMSecsSinceEpoch,
//      QTimeZone::NameType nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTimeZonePrivate11displayNameExN9QTimeZone8NameTypeERK7QLocale(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(atMSecsSinceEpoch, nameType, *locale));
}

//  QString QTimeZonePrivate::displayName(QTimeZone::TimeType timeType,
//      QTimeZone::NameType nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTimeZonePrivate11displayNameEN9QTimeZone8TimeTypeENS0_8NameTypeERK7QLocale(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(timeType, nameType, *locale));
}

//  QString QTimeZonePrivate::abbreviation(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QTimeZonePrivate12abbreviationEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return new QString(self->abbreviation(atMSecsSinceEpoch));
}

//  int QTimeZonePrivate::offsetFromUtc(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTimeZonePrivate13offsetFromUtcEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->offsetFromUtc(atMSecsSinceEpoch);
}

//  int QTimeZonePrivate::standardTimeOffset(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTimeZonePrivate18standardTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->standardTimeOffset(atMSecsSinceEpoch);
}

//  int QTimeZonePrivate::daylightTimeOffset(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTimeZonePrivate18daylightTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->daylightTimeOffset(atMSecsSinceEpoch);
}

//  bool QTimeZonePrivate::hasDaylightTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTimeZonePrivate15hasDaylightTimeEv(
    const QTimeZonePrivate *self) {
  return self->hasDaylightTime();
}

//  bool QTimeZonePrivate::isDaylightTime(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTimeZonePrivate14isDaylightTimeEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->isDaylightTime(atMSecsSinceEpoch);
}

//  Data QTimeZonePrivate::data(qint64 forMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK16QTimeZonePrivate4dataEx(
    const QTimeZonePrivate *self,
    qint64 forMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->data(forMSecsSinceEpoch));
}

//  Data QTimeZonePrivate::data(QTimeZone::TimeType timeType) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK16QTimeZonePrivate4dataEN9QTimeZone8TimeTypeE(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType) {
  return new QTimeZonePrivate::Data(self->data(timeType));
}

//  bool QTimeZonePrivate::isDataLocale(const QLocale &locale) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTimeZonePrivate12isDataLocaleERK7QLocale(
    const QTimeZonePrivate *self,
    const QLocale *locale) {
  return self->isDataLocale(*locale);
}

//  bool QTimeZonePrivate::isAnglicLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QTimeZonePrivate14isAnglicLocaleERK7QLocale(
    const QLocale *locale) {
  return QTimeZonePrivate::isAnglicLocale(*locale);
}

//  bool QTimeZonePrivate::hasTransitions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTimeZonePrivate14hasTransitionsEv(
    const QTimeZonePrivate *self) {
  return self->hasTransitions();
}

//  Data QTimeZonePrivate::nextTransition(qint64 afterMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK16QTimeZonePrivate14nextTransitionEx(
    const QTimeZonePrivate *self,
    qint64 afterMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->nextTransition(afterMSecsSinceEpoch));
}

//  Data QTimeZonePrivate::previousTransition(qint64 beforeMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK16QTimeZonePrivate18previousTransitionEx(
    const QTimeZonePrivate *self,
    qint64 beforeMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->previousTransition(beforeMSecsSinceEpoch));
}

//  QByteArray QTimeZonePrivate::systemTimeZoneId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QTimeZonePrivate16systemTimeZoneIdEv(
    const QTimeZonePrivate *self) {
  return new QByteArray(self->systemTimeZoneId());
}

//  bool QTimeZonePrivate::isTimeZoneIdAvailable(QByteArrayView ianaId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTimeZonePrivate21isTimeZoneIdAvailableE14QByteArrayView(
    const QTimeZonePrivate *self,
    const QByteArrayView *ianaId) {
  return self->isTimeZoneIdAvailable(*ianaId);
}

//  QList<QByteArray> QTimeZonePrivate::availableTimeZoneIds() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK16QTimeZonePrivate20availableTimeZoneIdsEv(
    const QTimeZonePrivate *self) {
  return new QList<QByteArray>(self->availableTimeZoneIds());
}

//  QList<QByteArray>
//      QTimeZonePrivate::availableTimeZoneIds(QLocale::Territory territory)
//      const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK16QTimeZonePrivate20availableTimeZoneIdsEN7QLocale7CountryE(
    const QTimeZonePrivate *self,
    QLocale::Territory territory) {
  return new QList<QByteArray>(self->availableTimeZoneIds(territory));
}

//  QList<QByteArray> QTimeZonePrivate::availableTimeZoneIds(int utcOffset)
//      const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK16QTimeZonePrivate20availableTimeZoneIdsEi(
    const QTimeZonePrivate *self,
    int utcOffset) {
  return new QList<QByteArray>(self->availableTimeZoneIds(utcOffset));
}

//  qint64 QTimeZonePrivate::maxMSecs()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QTimeZonePrivate8maxMSecsEv() {
  return QTimeZonePrivate::maxMSecs();
}

//  qint64 QTimeZonePrivate::minMSecs()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QTimeZonePrivate8minMSecsEv() {
  return QTimeZonePrivate::minMSecs();
}

//  qint64 QTimeZonePrivate::invalidMSecs()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QTimeZonePrivate12invalidMSecsEv() {
  return QTimeZonePrivate::invalidMSecs();
}

//  int QTimeZonePrivate::invalidSeconds()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QTimeZonePrivate14invalidSecondsEv() {
  return QTimeZonePrivate::invalidSeconds();
}

//  QString QTimeZonePrivate::utcQString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QTimeZonePrivate10utcQStringEv() {
  return new QString(QTimeZonePrivate::utcQString());
}

//  QByteArray QTimeZonePrivate::utcQByteArray()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN16QTimeZonePrivate13utcQByteArrayEv() {
  return new QByteArray(QTimeZonePrivate::utcQByteArray());
}

#endif  // QT_CONFIG(timezone)
