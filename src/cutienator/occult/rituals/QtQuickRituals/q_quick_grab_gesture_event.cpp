//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickGrabGestureEvent'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickGrabGestureEvent.cpp, line 1, as moc:QQuickGrabGestureEvent
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QQuickGrabGestureEventE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickGrabGestureEvent::qt_create_metaobjectdata<qt_meta_tag_ZN22QQuickGrabGestureEventE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickGrabGestureEvent",
        "QML.Element",
        "GestureEvent",
        "QML.AddedInVersion",
        "512",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "GestureEvent is only available in the context of handling the gest"
        "ureStarted signal from MultiPointTouchArea.",
        "grab",
        "",
        "touchPoints",
        "QQmlListProperty<QObject>",
        "dragThreshold"
    };

    QtMocHelpers::UintData qt_methods {
        // Method 'grab'
        QtMocHelpers::MethodData<void()>(9, 10, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'touchPoints'
        QtMocHelpers::PropertyData<QQmlListProperty<QObject>>(11, 0x80000000 | 12, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Constant | QMC::Final),
        // property 'dragThreshold'
        QtMocHelpers::PropertyData<qreal>(13, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Constant | QMC::Final),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
            {    7,    8 },
    });
    return QtMocHelpers::metaObjectData<QQuickGrabGestureEvent, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickGrabGestureEvent::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickGrabGestureEventE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickGrabGestureEventE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QQuickGrabGestureEventE_t>.metaTypes,
    nullptr
} };

void QQuickGrabGestureEvent::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickGrabGestureEvent *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->grab(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQmlListProperty<QObject>*>(_v) = _t->touchPoints(); break;
        case 1: *reinterpret_cast<qreal*>(_v) = _t->dragThreshold(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickGrabGestureEvent::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickGrabGestureEvent::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickGrabGestureEventE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickGrabGestureEvent::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickGrabGestureEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickGrabGestureEvent10metaObjectEv(
    const QQuickGrabGestureEvent *self) {
  return self->metaObject();
}

//  void *QQuickGrabGestureEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickGrabGestureEvent11qt_metacastEPKc(
    QQuickGrabGestureEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGrabGestureEvent::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickGrabGestureEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGrabGestureEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGrabGestureEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickGrabGestureEvent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGrabGestureEvent::tr(s, c, n));
}

//  void QQuickGrabGestureEvent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickGrabGestureEvent24qt_qmlMarker_uncreatableEv(
    QQuickGrabGestureEvent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickGrabGestureEvent::QQuickGrabGestureEvent()
extern "C" Q_DECL_EXPORT
QQuickGrabGestureEvent *ritual_ZN22QQuickGrabGestureEventC1Ev() {
  return new QQuickGrabGestureEvent();
}

//  void QQuickGrabGestureEvent::grab()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickGrabGestureEvent4grabEv(QQuickGrabGestureEvent *self) {
  self->grab();
}

//  bool QQuickGrabGestureEvent::wantsGrab() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickGrabGestureEvent9wantsGrabEv(
    const QQuickGrabGestureEvent *self) {
  return self->wantsGrab();
}

//  QQmlListProperty<QObject> QQuickGrabGestureEvent::touchPoints()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN22QQuickGrabGestureEvent11touchPointsEv(
    QQuickGrabGestureEvent *self) {
  return new QQmlListProperty<QObject>(self->touchPoints());
}

//  qreal QQuickGrabGestureEvent::dragThreshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickGrabGestureEvent13dragThresholdEv(
    const QQuickGrabGestureEvent *self) {
  return self->dragThreshold();
}

//  a QQmlListProperty<QObject> a ritual of QQuickGrabGestureEvent gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGrabGestureEvent__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
