//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qdatetime.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/QDebug>
#include <QtCore/QDateTime>
#include <QtCore/private/qlocaltime_p.h>
#include <QtCore/QStringList>
#include <QtCore/QTimeZone>
#include <QtQml/private/qv4referenceobject_p.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4dateobject.cpp, line 690, as _ZNK3QV44Date11toQDateTimeEv
namespace QV4 {
inline QDateTime Date::toQDateTime() const
{
    return ToDateTime(operator double(), QTimeZone::LocalTime);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4referenceobject.cpp, line 553, as _ZN3QV415ReferenceObject13shouldConnectEPNS_4Heap15ReferenceObjectE
namespace QV4 {
inline bool ReferenceObject::shouldConnect(Heap::ReferenceObject *ref)
{
    if (ref->isAlwaysDirty())
        return false;

    // We want to connect when we are reading the reference object from a statement that is not
    // its creation statement. In other words, when first storing it in a variable and then
    // reusing it, potentially multiple times. This ensures that the cost of the connection itself
    // is only paid when the user separated the declaration from the usage in their code, in the
    // hope that this catches more complex and frequent uses, like accesses in a loop, where
    // unnecessary copies would impact performance more significantly, and not one time accesses.
    if (CppStackFrame *frame = ref->internalClass->engine->currentStackFrame) {
        const auto *refObject = static_cast<Heap::ReferenceObject *>(ref);
        if (frame->v4Function && frame->v4Function == refObject->function()
            && frame->statementNumber() == refObject->statementIndex()) {
            return false;
        }
    }
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4referenceobject.cpp, line 574, as _ZN3QV415ReferenceObject7connectEPNS_4Heap15ReferenceObjectE
namespace QV4 {
inline void ReferenceObject::connect(Heap::ReferenceObject *ref)
{
    int property = ref->property();
    Heap::Object *object = ref->object();

    while (object
           && object->internalClass->vtable->type != Managed::Type_V4QObjectWrapper
           && object->internalClass->vtable->type != Managed::Type_QMLTypeWrapper)
    {
        const auto type = object->internalClass->vtable->type;
        if (type != Managed::Type_V4ReferenceObject
            && type != Managed::Type_V4Sequence
            && type != Managed::Type_DateObject
            && type != Managed::Type_QMLValueTypeWrapper) {
            break;
        }

        property = static_cast<QV4::Heap::ReferenceObject *>(object)->property();
        object = static_cast<QV4::Heap::ReferenceObject *>(object)->object();
    }

    const auto doConnect = [&](auto wrapper) {
        // The object may be valid on the first read but not on the second, check for that.
        if (QObject *obj = wrapper->object()) {
            auto *refObject = static_cast<Heap::ReferenceObject *>(ref);

            auto *qmlEngine = object->internalClass->engine->qmlEngine();
            if (qmlEngine && obj->metaObject()->property(property).isBindable())
                refObject->connectToBindable(obj, property, qmlEngine);
            else if (qmlEngine && obj->metaObject()->property(property).hasNotifySignal())
                refObject->connectToNotifySignal(obj, property, qmlEngine);
        }
    };

    if (object && object->internalClass->vtable->type == Managed::Type_V4QObjectWrapper) {
        doConnect(static_cast<QV4::Heap::QObjectWrapper *>(object));
    } else if (object && object->internalClass->vtable->type == Managed::Type_QMLTypeWrapper) {
        auto wrapper = static_cast<QV4::Heap::QQmlTypeWrapper *>(object);
        Scope scope(object->internalClass->engine);
        Scoped<QV4::QQmlTypeWrapper> scopedWrapper(scope, wrapper);
        doConnect(scopedWrapper);
    }

    if (!ref->isConnected()) {
        // Mark AlwaysDirty to prevent further connection failures on every read
        ref->setAlwaysDirty(true);
    }
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
//  -----------------------------------------------------------------------

//  void QV4::Heap::DateObject::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::DateObject::markObjects(b, stack);
}

//  void QV4::Heap::DateObject::doSetLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject13doSetLocationEv(
    QV4::Heap::DateObject *self) {
  self->doSetLocation();
}

//  void QV4::Heap::DateObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject4initEv(QV4::Heap::DateObject *self) {
  self->init();
}

//  void QV4::Heap::DateObject::init(Date date)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject4initENS_4DateE(
    QV4::Heap::DateObject *self,
    const QV4::Date *date) {
  self->init(*date);
}

//  double QV4::Heap::DateObject::date() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV44Heap10DateObject4dateEv(
    const QV4::Heap::DateObject *self) {
  return self->date();
}

//  QVariant QV4::Heap::DateObject::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV44Heap10DateObject9toVariantEv(
    const QV4::Heap::DateObject *self) {
  return new QVariant(self->toVariant());
}

//  QDateTime QV4::Heap::DateObject::toQDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK3QV44Heap10DateObject11toQDateTimeEv(
    const QV4::Heap::DateObject *self) {
  return new QDateTime(self->toQDateTime());
}

//  bool QV4::Heap::DateObject::writeBack(int internalIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap10DateObject9writeBackEi(
    QV4::Heap::DateObject *self,
    int internalIndex) {
  return self->writeBack(internalIndex);
}

//  QV4::Heap::DateObject as the QV4::Heap::DateObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObjectData *ritual_cast_QV4_Heap_DateObject_QV4_Heap_DateObjectData(
    QV4::Heap::DateObject *self) {
  return static_cast<QV4::Heap::DateObjectData *>(self);
}
