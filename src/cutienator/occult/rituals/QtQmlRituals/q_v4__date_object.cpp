//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#include <QtCore/qtimezone.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 761, as _ZN3QV410DateObject14dateTimeToDateERK9QDateTime
namespace QV4 {
inline QDate DateObject::dateTimeToDate(const QDateTime &dateTime)
{
    // If the Date object was parse()d from a string with no time part
    // or zone specifier it's really the UTC start of the relevant day,
    // but it's here represented as a local time, which may fall in the
    // preceding day. See QTBUG-92466 for the gory details.
    const auto utc = dateTime.toUTC();
    if (utc.date() != dateTime.date() && utc.addSecs(-1).date() == dateTime.date())
        return utc.date();

    // This may, of course, be The Wrong Thing if the date was
    // constructed as a full local date-time that happens to coincide
    // with the start of a UTC day; however, that would be an odd value
    // to give to something that, apparently, someone thinks belongs in
    // a QDate.
    return dateTime.date();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 746, as _ZN3QV410DateObject19timestampToDateTimeEd9QTimeZone
namespace QV4 {
inline QDateTime DateObject::timestampToDateTime(double timestamp, QTimeZone zone)
{
    return ToDateTime(timestamp, zone);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::DateObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410DateObject10__dataTestEv(QV4::DateObject *self) {
  self->__dataTest();
}

//  QV4::Heap::DateObject *QV4::DateObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZNK3QV410DateObject11d_uncheckedEv(
    const QV4::DateObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::DateObject *QV4::DateObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZNK3QV410DateObject1dEv(
    const QV4::DateObject *self) {
  return self->d();
}

//  QV4::Object *QV4::DateObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV410DateObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::DateObject::defaultPrototype(e);
}

//  double QV4::DateObject::date() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV410DateObject4dateEv(const QV4::DateObject *self) {
  return self->date();
}

//  QDateTime QV4::DateObject::toQDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK3QV410DateObject11toQDateTimeEv(
    const QV4::DateObject *self) {
  return new QDateTime(self->toQDateTime());
}

//  QDate QV4::DateObject::dateTimeToDate(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN3QV410DateObject14dateTimeToDateERK9QDateTime(
    const QDateTime *dateTime) {
  return new QDate(QV4::DateObject::dateTimeToDate(*dateTime));
}

//  QDateTime QV4::DateObject::timestampToDateTime(double timestamp,
//      QTimeZone zone)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN3QV410DateObject19timestampToDateTimeEd9QTimeZone(
    double timestamp,
    const QTimeZone *zone) {
  return new QDateTime(
      QV4::DateObject::timestampToDateTime(
          timestamp,
          *zone));
}
