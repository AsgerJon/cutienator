//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/QDebug>
#include <QtCore/QDateTime>
#include <QtCore/private/qlocaltime_p.h>
#include <QtCore/QStringList>
#include <QtCore/QTimeZone>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 20, as local:qv4dateobject.cpp:MinutesPerHour
static const double MinutesPerHour = 60.0;

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 21, as local:qv4dateobject.cpp:SecondsPerMinute
static const double SecondsPerMinute = 60.0;

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 22, as local:qv4dateobject.cpp:msPerSecond
static const double msPerSecond = 1000.0;

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 25, as local:qv4dateobject.cpp:msPerDay
static const double msPerDay = 86400000.0;

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 76, as local:qv4dateobject.cpp:DayFromYear
static inline double DayFromYear(double y)
{
    return 365 * (y - 1970)
        + ::floor((y - 1969) / 4)
        - ::floor((y - 1901) / 100)
        + ::floor((y - 1601) / 400);
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 188, as local:qv4dateobject.cpp:MakeTime
static inline double MakeTime(double hour, double min, double sec, double ms)
{
    if (!qIsFinite(hour) || !qIsFinite(min) || !qIsFinite(sec) || !qIsFinite(ms))
        return qQNaN();
    hour = QV4::Value::toInteger(hour);
    min = QV4::Value::toInteger(min);
    sec = QV4::Value::toInteger(sec);
    ms = QV4::Value::toInteger(ms);
    return ((hour * MinutesPerHour + min) * SecondsPerMinute + sec) * msPerSecond + ms;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 199, as local:qv4dateobject.cpp:DayFromMonth
static inline double DayFromMonth(double month, double leap)
{
    switch ((int) month) {
    case 0: return 0;
    case 1: return 31.0;
    case 2: return 59.0 + leap;
    case 3: return 90.0 + leap;
    case 4: return 120.0 + leap;
    case 5: return 151.0 + leap;
    case 6: return 181.0 + leap;
    case 7: return 212.0 + leap;
    case 8: return 243.0 + leap;
    case 9: return 273.0 + leap;
    case 10: return 304.0 + leap;
    case 11: return 334.0 + leap;
    }

    return qt_qnan(); // ### assert?
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 279, as local:qv4dateobject.cpp:DaylightSavingTA
static inline double DaylightSavingTA(double t, double localTZA) // t is a UTC time
{
    return QLocalTime::getUtcOffset(qint64(t)) * 1e3 - localTZA;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 293, as local:qv4dateobject.cpp:UTC
static inline double UTC(double t, double localTZA)
{
    // Flawed, yet verbatim from the spec:
    return t - localTZA - DaylightSavingTA(t - localTZA, localTZA);
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 555, as local:qv4dateobject.cpp:ToDateTime
static inline QDateTime ToDateTime(double t, QTimeZone zone)
{
    if (std::isnan(t))
        return QDateTime().toTimeZone(zone);
    return QDateTime::fromMSecsSinceEpoch(t, zone);
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 639, as _ZN3QV44Date4initEd
namespace QV4 {
inline void Date::init(double value)
{
    storage = encode(value);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 644, as _ZN3QV44Date4initERK9QDateTime
namespace QV4 {
inline void Date::init(const QDateTime &when)
{
    storage = encode(when) | HasQDate | HasQTime;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 649, as _ZN3QV44Date4initE5QDate
namespace QV4 {
inline void Date::init(QDate date)
{
    storage = encode(date.startOfDay(QTimeZone::UTC)) | HasQDate;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 680, as _ZNK3QV44Date7toQDateEv
namespace QV4 {
inline QDate Date::toQDate() const
{
    return toQDateTime().date();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 685, as _ZNK3QV44Date7toQTimeEv
namespace QV4 {
inline QTime Date::toQTime() const
{
    return toQDateTime().time();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 690, as _ZNK3QV44Date11toQDateTimeEv
namespace QV4 {
inline QDateTime Date::toQDateTime() const
{
    return ToDateTime(operator double(), QTimeZone::LocalTime);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 695, as _ZNK3QV44Date9toVariantEv
namespace QV4 {
inline QVariant Date::toVariant() const
{
    // Note that we shouldn't and don't read-back here, compared to
    // most other methods, as this is only used when we perform a
    // write-back, that is we are sending our version of the data back
    // to the originating element.
    switch (storage & (HasQDate | HasQTime)) {
    case HasQDate:
        return toQDate();
    case HasQTime:
        return toQTime();
    case (HasQDate | HasQTime):
        return toQDateTime();
    default:
        return QVariant();
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 621, as _ZN3QV44Date6encodeEd
namespace QV4 {
inline quint64 Date::encode(double value)
{
    if (std::isnan(value) || fabs(value) > MaxDateVal)
        return InvalidDateVal;

    // Do the addition in qint64. This way we won't overflow if value is negative
    // and we will round value in the right direction.
    // We know we can do this because we know we have more than one bit left in quint64.
    const quint64 encoded = quint64(qint64(value) + qint64(MaxDateVal));

    return encoded + Extra;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 634, as _ZN3QV44Date6encodeERK9QDateTime
namespace QV4 {
inline quint64 Date::encode(const QDateTime &dateTime)
{
    return encode(dateTime.isValid() ? dateTime.toMSecsSinceEpoch() : qt_qnan());
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Date::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Date4initEv(QV4::Date *self) {
  self->init();
}

//  void QV4::Date::init(Date date)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Date4initES0_(QV4::Date *self, const QV4::Date *date) {
  self->init(*date);
}

//  void QV4::Date::init(double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Date4initEd(QV4::Date *self, double value) {
  self->init(value);
}

//  void QV4::Date::init(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Date4initERK9QDateTime(
    QV4::Date *self,
    const QDateTime *dateTime) {
  self->init(*dateTime);
}

//  void QV4::Date::init(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Date4initE5QDate(QV4::Date *self, const QDate *date) {
  self->init(*date);
}

//  Date &QV4::Date::operator=(double value)
extern "C" Q_DECL_EXPORT
QV4::Date *ritual_ZN3QV44DateaSEd(QV4::Date *self, double value) {
  return &(self->operator=(value));
}

//  double QV4::Date::operator double() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV44DatecvdEv(const QV4::Date *self) {
  return self->operator double();
}

//  QDate QV4::Date::toQDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK3QV44Date7toQDateEv(const QV4::Date *self) {
  return new QDate(self->toQDate());
}

//  QTime QV4::Date::toQTime() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK3QV44Date7toQTimeEv(const QV4::Date *self) {
  return new QTime(self->toQTime());
}

//  QDateTime QV4::Date::toQDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK3QV44Date11toQDateTimeEv(const QV4::Date *self) {
  return new QDateTime(self->toQDateTime());
}

//  QVariant QV4::Date::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV44Date9toVariantEv(const QV4::Date *self) {
  return new QVariant(self->toVariant());
}

//  quint64 QV4::Date::encode(double value)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN3QV44Date6encodeEd(double value) {
  return QV4::Date::encode(value);
}

//  quint64 QV4::Date::encode(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN3QV44Date6encodeERK9QDateTime(const QDateTime *dateTime) {
  return QV4::Date::encode(*dateTime);
}

//  QV4::Date::~Date()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44DateD1Ev(QV4::Date *self) {
  delete self;
}
