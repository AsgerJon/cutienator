//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DXr/6.
//  12.0/QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuick3DXrSimpleHapticEffect' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  4 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3DXr__QQuick3DXrSimpleHapticEffect.cpp, line 1, as moc:QQuick3DXrSimpleHapticEffect
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN28QQuick3DXrSimpleHapticEffectE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuick3DXrSimpleHapticEffect::qt_create_metaobjectdata<qt_meta_tag_ZN28QQuick3DXrSimpleHapticEffectE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuick3DXrSimpleHapticEffect",
        "QML.Element",
        "XrSimpleHapticEffect",
        "QML.AddedInVersion",
        "1545",
        "amplitudeChanged",
        "",
        "durationChanged",
        "frequencyChanged",
        "amplitude",
        "duration",
        "frequency"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'amplitudeChanged'
        QtMocHelpers::SignalData<void()>(5, 6, QMC::AccessPublic, QMetaType::Void),
        // Signal 'durationChanged'
        QtMocHelpers::SignalData<void()>(7, 6, QMC::AccessPublic, QMetaType::Void),
        // Signal 'frequencyChanged'
        QtMocHelpers::SignalData<void()>(8, 6, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'amplitude'
        QtMocHelpers::PropertyData<float>(9, QMetaType::Float, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 0),
        // property 'duration'
        QtMocHelpers::PropertyData<float>(10, QMetaType::Float, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 1),
        // property 'frequency'
        QtMocHelpers::PropertyData<float>(11, QMetaType::Float, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 2),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuick3DXrSimpleHapticEffect, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuick3DXrSimpleHapticEffect::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuick3DXrAbstractHapticEffect::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuick3DXrSimpleHapticEffectE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuick3DXrSimpleHapticEffectE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN28QQuick3DXrSimpleHapticEffectE_t>.metaTypes,
    nullptr
} };

void QQuick3DXrSimpleHapticEffect::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuick3DXrSimpleHapticEffect *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->amplitudeChanged(); break;
        case 1: _t->durationChanged(); break;
        case 2: _t->frequencyChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSimpleHapticEffect::*)()>(_a, &QQuick3DXrSimpleHapticEffect::amplitudeChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSimpleHapticEffect::*)()>(_a, &QQuick3DXrSimpleHapticEffect::durationChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuick3DXrSimpleHapticEffect::*)()>(_a, &QQuick3DXrSimpleHapticEffect::frequencyChanged, 2))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<float*>(_v) = _t->amplitude(); break;
        case 1: *reinterpret_cast<float*>(_v) = _t->duration(); break;
        case 2: *reinterpret_cast<float*>(_v) = _t->frequency(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setAmplitude(*reinterpret_cast<float*>(_v)); break;
        case 1: _t->setDuration(*reinterpret_cast<float*>(_v)); break;
        case 2: _t->setFrequency(*reinterpret_cast<float*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuick3DXrSimpleHapticEffect::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuick3DXrSimpleHapticEffect::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuick3DXrSimpleHapticEffectE_t>.strings))
        return static_cast<void*>(this);
    return QQuick3DXrAbstractHapticEffect::qt_metacast(_clname);
}

int QQuick3DXrSimpleHapticEffect::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuick3DXrAbstractHapticEffect::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void QQuick3DXrSimpleHapticEffect::amplitudeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuick3DXrSimpleHapticEffect::durationChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuick3DXrSimpleHapticEffect::frequencyChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}
QT_WARNING_POP

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 49, as _ZN28QQuick3DXrSimpleHapticEffect9amplitudeEv
inline float QQuick3DXrSimpleHapticEffect::amplitude()
{
    return m_amplitude;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 54, as _ZN28QQuick3DXrSimpleHapticEffect12setAmplitudeEf
inline void QQuick3DXrSimpleHapticEffect::setAmplitude(float newAmplitude)
{
    if (m_amplitude == newAmplitude)
        return;
    m_amplitude = newAmplitude;
    emit amplitudeChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 67, as _ZN28QQuick3DXrSimpleHapticEffect8durationEv
inline float QQuick3DXrSimpleHapticEffect::duration()
{
    return m_duration;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 72, as _ZN28QQuick3DXrSimpleHapticEffect11setDurationEf
inline void QQuick3DXrSimpleHapticEffect::setDuration(float newDuration)
{
    if (m_duration == newDuration)
        return;
    m_duration = newDuration;
    emit durationChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 86, as _ZN28QQuick3DXrSimpleHapticEffect9frequencyEv
inline float QQuick3DXrSimpleHapticEffect::frequency()
{
    return m_frequency;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 91, as _ZN28QQuick3DXrSimpleHapticEffect12setFrequencyEf
inline void QQuick3DXrSimpleHapticEffect::setFrequency(float newFrequency)
{
    if (m_frequency == newFrequency)
        return;
    m_frequency = newFrequency;
    emit frequencyChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrSimpleHapticEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DXrSimpleHapticEffect10metaObjectEv(
    const QQuick3DXrSimpleHapticEffect *self) {
  return self->metaObject();
}

//  void *QQuick3DXrSimpleHapticEffect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuick3DXrSimpleHapticEffect11qt_metacastEPKc(
    QQuick3DXrSimpleHapticEffect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrSimpleHapticEffect::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuick3DXrSimpleHapticEffect11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrSimpleHapticEffect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrSimpleHapticEffect::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuick3DXrSimpleHapticEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrSimpleHapticEffect::tr(s, c, n));
}

//  float QQuick3DXrSimpleHapticEffect::amplitude()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect9amplitudeEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->amplitude();
}

//  void QQuick3DXrSimpleHapticEffect::setAmplitude(float newAmplitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect12setAmplitudeEf(
    QQuick3DXrSimpleHapticEffect *self,
    float newAmplitude) {
  self->setAmplitude(newAmplitude);
}

//  float QQuick3DXrSimpleHapticEffect::duration()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect8durationEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->duration();
}

//  void QQuick3DXrSimpleHapticEffect::setDuration(float newDuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect11setDurationEf(
    QQuick3DXrSimpleHapticEffect *self,
    float newDuration) {
  self->setDuration(newDuration);
}

//  float QQuick3DXrSimpleHapticEffect::frequency()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect9frequencyEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->frequency();
}

//  void QQuick3DXrSimpleHapticEffect::setFrequency(float newFrequency)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect12setFrequencyEf(
    QQuick3DXrSimpleHapticEffect *self,
    float newFrequency) {
  self->setFrequency(newFrequency);
}

//  void QQuick3DXrSimpleHapticEffect::amplitudeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect16amplitudeChangedEv(
    QQuick3DXrSimpleHapticEffect *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSimpleHapticEffect")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "amplitudeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "amplitudeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSimpleHapticEffect::durationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect15durationChangedEv(
    QQuick3DXrSimpleHapticEffect *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSimpleHapticEffect")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "durationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "durationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrSimpleHapticEffect::frequencyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DXrSimpleHapticEffect16frequencyChangedEv(
    QQuick3DXrSimpleHapticEffect *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrSimpleHapticEffect")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "frequencyChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "frequencyChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
