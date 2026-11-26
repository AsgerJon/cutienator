//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DPhysi
//  cs/6.12.0/QtQuick3DPhysics/private/qabstractphysicsbody_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QAbstractPhysicsBody' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qabstractphysicsbody_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3DPhysics/private/qabstractphysicsbody_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3DPhysics__QAbstractPhysicsBody.cpp, line 1, as moc:QAbstractPhysicsBody
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QAbstractPhysicsBodyE_t {};
} // unnamed namespace

template <> constexpr inline auto QAbstractPhysicsBody::qt_create_metaobjectdata<qt_meta_tag_ZN20QAbstractPhysicsBodyE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QAbstractPhysicsBody",
        "QML.Element",
        "PhysicsBody",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "abstract interface",
        "physicsMaterialChanged",
        "",
        "simulationEnabledChanged",
        "physicsMaterial",
        "QPhysicsMaterial*",
        "simulationEnabled"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'physicsMaterialChanged'
        QtMocHelpers::SignalData<void()>(7, 8, QMC::AccessPublic, QMetaType::Void),
        // Signal 'simulationEnabledChanged'
        QtMocHelpers::SignalData<void()>(9, 8, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'physicsMaterial'
        QtMocHelpers::PropertyData<QPhysicsMaterial*>(10, 0x80000000 | 11, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 0),
        // property 'simulationEnabled'
        QtMocHelpers::PropertyData<bool>(12, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
    });
    return QtMocHelpers::metaObjectData<QAbstractPhysicsBody, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QAbstractPhysicsBody::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractPhysicsNode::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QAbstractPhysicsBodyE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QAbstractPhysicsBodyE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QAbstractPhysicsBodyE_t>.metaTypes,
    nullptr
} };

void QAbstractPhysicsBody::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QAbstractPhysicsBody *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->physicsMaterialChanged(); break;
        case 1: _t->simulationEnabledChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QAbstractPhysicsBody::*)()>(_a, &QAbstractPhysicsBody::physicsMaterialChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QAbstractPhysicsBody::*)()>(_a, &QAbstractPhysicsBody::simulationEnabledChanged, 1))
            return;
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 0:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QPhysicsMaterial* >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QPhysicsMaterial**>(_v) = _t->physicsMaterial(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->simulationEnabled(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setPhysicsMaterial(*reinterpret_cast<QPhysicsMaterial**>(_v)); break;
        case 1: _t->setSimulationEnabled(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QAbstractPhysicsBody::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QAbstractPhysicsBody::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QAbstractPhysicsBodyE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractPhysicsNode::qt_metacast(_clname);
}

int QAbstractPhysicsBody::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractPhysicsNode::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void QAbstractPhysicsBody::physicsMaterialChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QAbstractPhysicsBody::simulationEnabledChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP

//  from ../qtquick3dphysics/src/quick3dphysics/qabstractphysicsbody.cpp, line 48, as _ZNK20QAbstractPhysicsBody15physicsMaterialEv
inline QPhysicsMaterial *QAbstractPhysicsBody::physicsMaterial() const
{
    return m_physicsMaterial;
}

//  from ../qtquick3dphysics/src/quick3dphysics/qabstractphysicsbody.cpp, line 53, as _ZN20QAbstractPhysicsBody18setPhysicsMaterialEP16QPhysicsMaterial
inline void QAbstractPhysicsBody::setPhysicsMaterial(QPhysicsMaterial *newPhysicsMaterial)
{
    if (m_physicsMaterial == newPhysicsMaterial)
        return;
    m_physicsMaterial = newPhysicsMaterial;
    emit physicsMaterialChanged();
}

//  from ../qtquick3dphysics/src/quick3dphysics/qabstractphysicsbody.cpp, line 61, as _ZNK20QAbstractPhysicsBody17simulationEnabledEv
inline bool QAbstractPhysicsBody::simulationEnabled() const
{
    return m_simulationEnabled;
}

//  from ../qtquick3dphysics/src/quick3dphysics/qabstractphysicsbody.cpp, line 66, as _ZN20QAbstractPhysicsBody20setSimulationEnabledEb
inline void QAbstractPhysicsBody::setSimulationEnabled(bool newSimulationEnabled)
{
    if (m_simulationEnabled == newSimulationEnabled)
        return;
    m_simulationEnabled = newSimulationEnabled;
    emit simulationEnabledChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QAbstractPhysicsBody::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QAbstractPhysicsBody10metaObjectEv(
    const QAbstractPhysicsBody *self) {
  return self->metaObject();
}

//  void *QAbstractPhysicsBody::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QAbstractPhysicsBody11qt_metacastEPKc(
    QAbstractPhysicsBody *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractPhysicsBody::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QAbstractPhysicsBody11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractPhysicsBody *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractPhysicsBody::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QAbstractPhysicsBody2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractPhysicsBody::tr(s, c, n));
}

//  void QAbstractPhysicsBody::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsBody24qt_qmlMarker_uncreatableEv(
    QAbstractPhysicsBody *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QPhysicsMaterial *QAbstractPhysicsBody::physicsMaterial() const
extern "C" Q_DECL_EXPORT
QPhysicsMaterial *ritual_ZNK20QAbstractPhysicsBody15physicsMaterialEv(
    const QAbstractPhysicsBody *self) {
  return self->physicsMaterial();
}

//  void QAbstractPhysicsBody::setPhysicsMaterial(QPhysicsMaterial
//      *newPhysicsMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsBody18setPhysicsMaterialEP16QPhysicsMaterial(
    QAbstractPhysicsBody *self,
    QPhysicsMaterial *newPhysicsMaterial) {
  self->setPhysicsMaterial(newPhysicsMaterial);
}

//  bool QAbstractPhysicsBody::simulationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractPhysicsBody17simulationEnabledEv(
    const QAbstractPhysicsBody *self) {
  return self->simulationEnabled();
}

//  void QAbstractPhysicsBody::setSimulationEnabled(bool
//      newSimulationEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsBody20setSimulationEnabledEb(
    QAbstractPhysicsBody *self,
    bool newSimulationEnabled) {
  self->setSimulationEnabled(newSimulationEnabled);
}

//  void QAbstractPhysicsBody::physicsMaterialChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsBody22physicsMaterialChangedEv(
    QAbstractPhysicsBody *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractPhysicsBody")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "physicsMaterialChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "physicsMaterialChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractPhysicsBody::simulationEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsBody24simulationEnabledChangedEv(
    QAbstractPhysicsBody *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractPhysicsBody")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "simulationEnabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "simulationEnabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
