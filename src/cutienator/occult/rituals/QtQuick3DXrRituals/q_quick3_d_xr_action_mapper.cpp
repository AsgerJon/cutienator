//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuick3DXrActionMapper'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 6 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QList>
#include <QtCore/QPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#include <QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 15, as local:qquick3dxractionmapper.cpp:actionIntKey
static inline quint32 actionIntKey(const QQuick3DXrInputAction::Action id, const QtQuick3DXr::Controller controller)
{
    return quint16(id) | (quint32(controller) << 16);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 20, as local:qquick3dxractionmapper.cpp:actionStringKey
static inline QString actionStringKey(const QString &name, const QtQuick3DXr::Controller controller)
{
    return QString::number(uint(controller)) + name;
}

//  from QtQuick3DXr__QQuick3DXrActionMapper.cpp, line 1, as moc:QQuick3DXrActionMapper
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QQuick3DXrActionMapperE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuick3DXrActionMapper::qt_create_metaobjectdata<qt_meta_tag_ZN22QQuick3DXrActionMapperE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuick3DXrActionMapper"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuick3DXrActionMapper, qt_meta_tag_ZN22QQuick3DXrActionMapperE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuick3DXrActionMapper::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuick3DXrActionMapperE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuick3DXrActionMapperE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QQuick3DXrActionMapperE_t>.metaTypes,
    nullptr
} };

void QQuick3DXrActionMapper::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuick3DXrActionMapper *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuick3DXrActionMapper::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuick3DXrActionMapper::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuick3DXrActionMapperE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuick3DXrActionMapper::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 163, as _ZN21QQuick3DXrInputAction10setPressedEb
inline void QQuick3DXrInputAction::setPressed(bool newPressed)
{
    if (m_pressed == newPressed)
        return;
    m_pressed = newPressed;
    emit pressedChanged();
    if (newPressed)
        emit triggered();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 142, as _ZN21QQuick3DXrInputAction8setValueEf
inline void QQuick3DXrInputAction::setValue(float newValue)
{
    if (qFuzzyCompare(m_value, newValue))
        return;
    m_value = newValue;
    emit valueChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 353, as _ZNK21QQuick3DXrInputAction7enabledEv
inline bool QQuick3DXrInputAction::enabled() const
{
    return m_enabled;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 432, as _ZNK24QQuick3DXrHapticFeedback10controllerEv
inline QQuick3DXrHapticFeedback::Controller QQuick3DXrHapticFeedback::controller() const
{
    return m_controller;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 25, as _ZN22QQuick3DXrActionMapper8instanceEv
inline QQuick3DXrActionMapper *QQuick3DXrActionMapper::instance()
{
    static QQuick3DXrActionMapper instance;
    return &instance;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 55, as _ZN22QQuick3DXrActionMapper16getHapticEffectsEN11QtQuick3DXr10ControllerE
inline QList<QPointer<QQuick3DXrHapticFeedback>> QQuick3DXrActionMapper::getHapticEffects(QtQuick3DXr::Controller controller)
{
    auto *that = instance();
    return that->m_hapticData[uint(controller)].m_hapticEffects;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 31, as _ZN22QQuick3DXrActionMapper11handleInputEN21QQuick3DXrInputAction6ActionEN11QtQuick3DXr10ControllerEPKcf
inline void QQuick3DXrActionMapper::handleInput(QQuick3DXrInputAction::Action id, QtQuick3DXr::Controller controller, const char *shortName, float value)
{
    auto *that = instance();
    auto set = [](auto action, auto value) {
        action->setValue(value);
        // TODO: distinguish between bool and float values
        action->setPressed(value > 0.9);
    };

    const QLatin1StringView name(shortName);
    // emit that->inputValueChange(id, name, value); // TODO: emit a signal from public class

    QList<QQuick3DXrInputAction *> actions;
    if (id == QQuick3DXrInputAction::CustomAction) {
        actions = that->m_customActions.values(actionStringKey(name, controller));
    } else {
        actions = that->m_actions.values(actionIntKey(id, controller));
    }

    for (const auto &action : std::as_const(actions))
        if (action->enabled())
            set(action, value);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 79, as _ZN22QQuick3DXrActionMapper20registerHapticEffectE8QPointerI24QQuick3DXrHapticFeedbackE
inline void QQuick3DXrActionMapper::registerHapticEffect(QPointer<QQuick3DXrHapticFeedback> action)
{
    auto *that = instance();

    that->m_hapticData[size_t(action->controller())].m_hapticEffects.append(action);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 102, as _ZN22QQuick3DXrActionMapper18removeHapticEffectEP24QQuick3DXrHapticFeedback
inline void QQuick3DXrActionMapper::removeHapticEffect(QQuick3DXrHapticFeedback *action)
{
    auto *that = instance();
    QList<QPointer<QQuick3DXrHapticFeedback>> list = that->m_hapticData[size_t(action->controller())].m_hapticEffects;
    list.removeAt(list.indexOf(action));
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 11, as _ZN22QQuick3DXrActionMapperC1EP7QObject
inline QQuick3DXrActionMapper::QQuick3DXrActionMapper(QObject *parent) : QObject(parent)
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrActionMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DXrActionMapper10metaObjectEv(
    const QQuick3DXrActionMapper *self) {
  return self->metaObject();
}

//  void *QQuick3DXrActionMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DXrActionMapper11qt_metacastEPKc(
    QQuick3DXrActionMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrActionMapper::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DXrActionMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrActionMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrActionMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DXrActionMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrActionMapper::tr(s, c, n));
}

//  QQuick3DXrActionMapper *QQuick3DXrActionMapper::instance()
extern "C" Q_DECL_EXPORT
QQuick3DXrActionMapper *ritual_ZN22QQuick3DXrActionMapper8instanceEv() {
  return QQuick3DXrActionMapper::instance();
}

//  QList<QPointer<QQuick3DXrHapticFeedback>>
//      QQuick3DXrActionMapper::getHapticEffects(QtQuick3DXr::Controller
//      controller)
extern "C" Q_DECL_EXPORT
QList<QPointer<QQuick3DXrHapticFeedback>> *ritual_ZN22QQuick3DXrActionMapper16getHapticEffectsEN11QtQuick3DXr10ControllerE(
    QtQuick3DXr::Controller controller) {
  return new QList<QPointer<QQuick3DXrHapticFeedback>>(
      QQuick3DXrActionMapper::getHapticEffects(
          controller));
}

//  void QQuick3DXrActionMapper::registerHapticEffect(QPointer<QQuick3DXrHapt
//      icFeedback> a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrActionMapper20registerHapticEffectE8QPointerI24QQuick3DXrHapticFeedbackE(
    const QPointer<QQuick3DXrHapticFeedback> *a0) {
  QQuick3DXrActionMapper::registerHapticEffect(*a0);
}

//  void QQuick3DXrActionMapper::removeHapticEffect(QQuick3DXrHapticFeedback
//      *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DXrActionMapper18removeHapticEffectEP24QQuick3DXrHapticFeedback(
    QQuick3DXrHapticFeedback *action) {
  QQuick3DXrActionMapper::removeHapticEffect(action);
}

//  QQuick3DXrActionMapper::QQuick3DXrActionMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrActionMapper *ritual_ZN22QQuick3DXrActionMapperC1EP7QObject(
    QObject *parent) {
  return new QQuick3DXrActionMapper(parent);
}

//  a QList<QPointer<QQuick3DXrHapticFeedback>> a ritual of
//      QQuick3DXrActionMapper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DXrActionMapper__QList_QPointer_QQuick3DXrHapticFeedback(
    QList<QPointer<QQuick3DXrHapticFeedback>> *self) {
  delete self;
}
