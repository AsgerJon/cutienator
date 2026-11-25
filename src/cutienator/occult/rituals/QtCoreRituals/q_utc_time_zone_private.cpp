//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what
//  its header writes out.
//  It is final, so 'self' is taken as a QTimeZonePrivate, and the
//  calls stay virtual.
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

//  QUtcTimeZonePrivate *QUtcTimeZonePrivate::clone() const
extern "C" Q_DECL_EXPORT
QUtcTimeZonePrivate *ritual_ZNK19QUtcTimeZonePrivate5cloneEv(
    const QTimeZonePrivate *self) {
  return static_cast<QUtcTimeZonePrivate *>(self->clone());
}

//  QUtcTimeZonePrivate::~QUtcTimeZonePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QUtcTimeZonePrivateD1Ev(QTimeZonePrivate *self) {
  delete self;
}

//  Data QUtcTimeZonePrivate::data(qint64 forMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QUtcTimeZonePrivate4dataEx(
    const QTimeZonePrivate *self,
    qint64 forMSecsSinceEpoch) {
  return new QTimeZonePrivate::Data(self->data(forMSecsSinceEpoch));
}

//  Data QUtcTimeZonePrivate::data(QTimeZone::TimeType timeType) const
extern "C" Q_DECL_EXPORT
QTimeZonePrivate::Data *ritual_ZNK19QUtcTimeZonePrivate4dataEN9QTimeZone8TimeTypeE(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType) {
  return new QTimeZonePrivate::Data(self->data(timeType));
}

//  bool QUtcTimeZonePrivate::isDataLocale(const QLocale &locale) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QUtcTimeZonePrivate12isDataLocaleERK7QLocale(
    const QTimeZonePrivate *self,
    const QLocale *locale) {
  return self->isDataLocale(*locale);
}

//  QLocale::Territory QUtcTimeZonePrivate::territory() const
extern "C" Q_DECL_EXPORT
QLocale::Territory ritual_ZNK19QUtcTimeZonePrivate9territoryEv(
    const QTimeZonePrivate *self) {
  return self->territory();
}

//  QString QUtcTimeZonePrivate::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QUtcTimeZonePrivate7commentEv(
    const QTimeZonePrivate *self) {
  return new QString(self->comment());
}

//  QString QUtcTimeZonePrivate::displayName(qint64 atMSecsSinceEpoch,
//      QTimeZone::NameType nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QUtcTimeZonePrivate11displayNameExN9QTimeZone8NameTypeERK7QLocale(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(atMSecsSinceEpoch, nameType, *locale));
}

//  QString QUtcTimeZonePrivate::displayName(QTimeZone::TimeType timeType,
//      QTimeZone::NameType nameType, const QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QUtcTimeZonePrivate11displayNameEN9QTimeZone8TimeTypeENS0_8NameTypeERK7QLocale(
    const QTimeZonePrivate *self,
    QTimeZone::TimeType timeType,
    QTimeZone::NameType nameType,
    const QLocale *locale) {
  return new QString(self->displayName(timeType, nameType, *locale));
}

//  QString QUtcTimeZonePrivate::abbreviation(qint64 atMSecsSinceEpoch) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QUtcTimeZonePrivate12abbreviationEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return new QString(self->abbreviation(atMSecsSinceEpoch));
}

//  int QUtcTimeZonePrivate::standardTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QUtcTimeZonePrivate18standardTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->standardTimeOffset(atMSecsSinceEpoch);
}

//  int QUtcTimeZonePrivate::daylightTimeOffset(qint64 atMSecsSinceEpoch)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QUtcTimeZonePrivate18daylightTimeOffsetEx(
    const QTimeZonePrivate *self,
    qint64 atMSecsSinceEpoch) {
  return self->daylightTimeOffset(atMSecsSinceEpoch);
}

//  QByteArray QUtcTimeZonePrivate::systemTimeZoneId() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QUtcTimeZonePrivate16systemTimeZoneIdEv(
    const QTimeZonePrivate *self) {
  return new QByteArray(self->systemTimeZoneId());
}

//  bool QUtcTimeZonePrivate::isTimeZoneIdAvailable(QByteArrayView ianaId)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QUtcTimeZonePrivate21isTimeZoneIdAvailableE14QByteArrayView(
    const QTimeZonePrivate *self,
    const QByteArrayView *ianaId) {
  return self->isTimeZoneIdAvailable(*ianaId);
}

//  QList<QByteArray> QUtcTimeZonePrivate::availableTimeZoneIds() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK19QUtcTimeZonePrivate20availableTimeZoneIdsEv(
    const QTimeZonePrivate *self) {
  return new QList<QByteArray>(self->availableTimeZoneIds());
}

//  QList<QByteArray>
//      QUtcTimeZonePrivate::availableTimeZoneIds(QLocale::Territory
//      territory) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK19QUtcTimeZonePrivate20availableTimeZoneIdsEN7QLocale7CountryE(
    const QTimeZonePrivate *self,
    QLocale::Territory territory) {
  return new QList<QByteArray>(self->availableTimeZoneIds(territory));
}

//  QList<QByteArray> QUtcTimeZonePrivate::availableTimeZoneIds(int
//      utcOffset) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK19QUtcTimeZonePrivate20availableTimeZoneIdsEi(
    const QTimeZonePrivate *self,
    int utcOffset) {
  return new QList<QByteArray>(self->availableTimeZoneIds(utcOffset));
}

#endif  // QT_CONFIG(timezone)
