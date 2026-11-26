//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandinput_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuick3DXrHandInput' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 5 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#include <QtQuick3DXr/private/qquick3dxrinputmanager_p.h>
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxrinputmanager_visionos_p.h"
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3DXr__QQuick3DXrHandInput.cpp, line 1, as moc:QQuick3DXrHandInput
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN19QQuick3DXrHandInputE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuick3DXrHandInput::qt_create_metaobjectdata<qt_meta_tag_ZN19QQuick3DXrHandInputE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuick3DXrHandInput",
        "isActiveChanged",
        "",
        "poseSpaceChanged",
        "posePositionChanged",
        "poseRotationChanged",
        "jointPositionsChanged",
        "jointRotationsChanged",
        "jointDataUpdated",
        "pokePositionChanged",
        "isHandTrackingChanged"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'isActiveChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'poseSpaceChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'posePositionChanged'
        QtMocHelpers::SignalData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'poseRotationChanged'
        QtMocHelpers::SignalData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'jointPositionsChanged'
        QtMocHelpers::SignalData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'jointRotationsChanged'
        QtMocHelpers::SignalData<void()>(7, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'jointDataUpdated'
        QtMocHelpers::SignalData<void()>(8, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'pokePositionChanged'
        QtMocHelpers::SignalData<void()>(9, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'isHandTrackingChanged'
        QtMocHelpers::SignalData<void()>(10, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuick3DXrHandInput, qt_meta_tag_ZN19QQuick3DXrHandInputE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuick3DXrHandInput::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QQuick3DXrHandInputE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QQuick3DXrHandInputE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN19QQuick3DXrHandInputE_t>.metaTypes,
    nullptr
} };

void QQuick3DXrHandInput::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuick3DXrHandInput *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->isActiveChanged(); break;
        case 1: _t->poseSpaceChanged(); break;
        case 2: _t->posePositionChanged(); break;
        case 3: _t->poseRotationChanged(); break;
        case 4: _t->jointPositionsChanged(); break;
        case 5: _t->jointRotationsChanged(); break;
        case 6: _t->jointDataUpdated(); break;
        case 7: _t->pokePositionChanged(); break;
        case 8: _t->isHandTrackingChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::isActiveChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::poseSpaceChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::posePositionChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::poseRotationChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::jointPositionsChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::jointRotationsChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::jointDataUpdated, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::pokePositionChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrHandInput::*)()>(_a, &QQuick3DXrHandInput::isHandTrackingChanged, 8))
            return;
    }
}

const QMetaObject *QQuick3DXrHandInput::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuick3DXrHandInput::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QQuick3DXrHandInputE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuick3DXrHandInput::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 9)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 9;
    }
    return _id;
}

// SIGNAL 0
void QQuick3DXrHandInput::isActiveChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuick3DXrHandInput::poseSpaceChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuick3DXrHandInput::posePositionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QQuick3DXrHandInput::poseRotationChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QQuick3DXrHandInput::jointPositionsChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void QQuick3DXrHandInput::jointRotationsChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void QQuick3DXrHandInput::jointDataUpdated()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void QQuick3DXrHandInput::pokePositionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void QQuick3DXrHandInput::isHandTrackingChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}
QT_WARNING_POP

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 17, as _ZN19QQuick3DXrHandInputC1EP7QObject
inline QQuick3DXrHandInput::QQuick3DXrHandInput(QObject *parent)
    : QObject(parent)
{

}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 23, as _ZNK19QQuick3DXrHandInput8isActiveEv
inline bool QQuick3DXrHandInput::isActive() const
{
    return m_isActive;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 28, as _ZN19QQuick3DXrHandInput11setIsActiveEb
inline void QQuick3DXrHandInput::setIsActive(bool isActive)
{
    if (m_isActive == isActive)
        return;

    m_isActive = isActive;
    emit isActiveChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 52, as _ZNK19QQuick3DXrHandInput14jointPositionsEv
inline QList<QVector3D> QQuick3DXrHandInput::jointPositions() const
{
    return m_jointPositions;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 57, as _ZNK19QQuick3DXrHandInput14jointRotationsEv
inline QList<QQuaternion> QQuick3DXrHandInput::jointRotations() const
{
    return m_jointRotations;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 62, as _ZNK19QQuick3DXrHandInput12pokePositionEv
inline QVector3D QQuick3DXrHandInput::pokePosition() const
{
    return m_pokePosition;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 67, as _ZN19QQuick3DXrHandInput15setPokePositionERK9QVector3D
inline void QQuick3DXrHandInput::setPokePosition(const QVector3D &newPokePosition)
{
    if (m_pokePosition == newPokePosition)
        return;
    m_pokePosition = newPokePosition;
    emit pokePositionChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 75, as _ZNK19QQuick3DXrHandInput20isHandTrackingActiveEv
inline bool QQuick3DXrHandInput::isHandTrackingActive() const
{
    return m_isHandTracking;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 80, as _ZN19QQuick3DXrHandInput23setIsHandTrackingActiveEb
inline void QQuick3DXrHandInput::setIsHandTrackingActive(bool newIsHandTracking)
{
    if (m_isHandTracking == newIsHandTracking)
        return;
    m_isHandTracking = newIsHandTracking;
    emit isHandTrackingChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrHandInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DXrHandInput10metaObjectEv(
    const QQuick3DXrHandInput *self) {
  return self->metaObject();
}

//  void *QQuick3DXrHandInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuick3DXrHandInput11qt_metacastEPKc(
    QQuick3DXrHandInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrHandInput::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DXrHandInput11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrHandInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrHandInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuick3DXrHandInput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrHandInput::tr(s, c, n));
}

//  QQuick3DXrHandInput::QQuick3DXrHandInput(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrHandInput *ritual_ZN19QQuick3DXrHandInputC1EP7QObject(
    QObject *parent) {
  return new QQuick3DXrHandInput(parent);
}

//  bool QQuick3DXrHandInput::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DXrHandInput8isActiveEv(
    const QQuick3DXrHandInput *self) {
  return self->isActive();
}

//  void QQuick3DXrHandInput::setIsActive(bool isActive)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput11setIsActiveEb(
    QQuick3DXrHandInput *self,
    bool isActive) {
  self->setIsActive(isActive);
}

//  QList<QVector3D> QQuick3DXrHandInput::jointPositions() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK19QQuick3DXrHandInput14jointPositionsEv(
    const QQuick3DXrHandInput *self) {
  return new QList<QVector3D>(self->jointPositions());
}

//  QList<QQuaternion> QQuick3DXrHandInput::jointRotations() const
extern "C" Q_DECL_EXPORT
QList<QQuaternion> *ritual_ZNK19QQuick3DXrHandInput14jointRotationsEv(
    const QQuick3DXrHandInput *self) {
  return new QList<QQuaternion>(self->jointRotations());
}

//  QVector3D QQuick3DXrHandInput::pokePosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK19QQuick3DXrHandInput12pokePositionEv(
    const QQuick3DXrHandInput *self) {
  return new QVector3D(self->pokePosition());
}

//  void QQuick3DXrHandInput::setPokePosition(const QVector3D
//      &newPokePosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput15setPokePositionERK9QVector3D(
    QQuick3DXrHandInput *self,
    const QVector3D *newPokePosition) {
  self->setPokePosition(*newPokePosition);
}

//  bool QQuick3DXrHandInput::isHandTrackingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DXrHandInput20isHandTrackingActiveEv(
    const QQuick3DXrHandInput *self) {
  return self->isHandTrackingActive();
}

//  void QQuick3DXrHandInput::setIsHandTrackingActive(bool newIsHandTracking)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput23setIsHandTrackingActiveEb(
    QQuick3DXrHandInput *self,
    bool newIsHandTracking) {
  self->setIsHandTrackingActive(newIsHandTracking);
}

//  void QQuick3DXrHandInput::isActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput15isActiveChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isActiveChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isActiveChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::poseSpaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput16poseSpaceChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "poseSpaceChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "poseSpaceChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::posePositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput19posePositionChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "posePositionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "posePositionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::poseRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput19poseRotationChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "poseRotationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "poseRotationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::jointPositionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput21jointPositionsChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "jointPositionsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "jointPositionsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::jointRotationsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput21jointRotationsChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "jointRotationsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "jointRotationsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::jointDataUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput16jointDataUpdatedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "jointDataUpdated()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "jointDataUpdated()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::pokePositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput19pokePositionChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pokePositionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pokePositionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::isHandTrackingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput21isHandTrackingChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isHandTrackingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isHandTrackingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
