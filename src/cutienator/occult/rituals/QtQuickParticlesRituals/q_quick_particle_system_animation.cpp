//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickParticleSystemAnimation' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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

//  from QtQuickParticles__QQuickParticleSystemAnimation.cpp, line 1, as moc:QQuickParticleSystemAnimation
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN29QQuickParticleSystemAnimationE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickParticleSystemAnimation::qt_create_metaobjectdata<qt_meta_tag_ZN29QQuickParticleSystemAnimationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickParticleSystemAnimation"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickParticleSystemAnimation, qt_meta_tag_ZN29QQuickParticleSystemAnimationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickParticleSystemAnimation::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractAnimation::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickParticleSystemAnimationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickParticleSystemAnimationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN29QQuickParticleSystemAnimationE_t>.metaTypes,
    nullptr
} };

void QQuickParticleSystemAnimation::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickParticleSystemAnimation *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickParticleSystemAnimation::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickParticleSystemAnimation::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickParticleSystemAnimationE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractAnimation::qt_metacast(_clname);
}

int QQuickParticleSystemAnimation::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractAnimation::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  Only a class built on QQuickParticleSystemAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickParticleSystemAnimation : QQuickParticleSystemAnimation {
  using QQuickParticleSystemAnimation::updateCurrentTime;
  using QQuickParticleSystemAnimation::duration;
};

//  const QMetaObject *QQuickParticleSystemAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickParticleSystemAnimation10metaObjectEv(
    const QQuickParticleSystemAnimation *self) {
  return self->metaObject();
}

//  void *QQuickParticleSystemAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuickParticleSystemAnimation11qt_metacastEPKc(
    QQuickParticleSystemAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickParticleSystemAnimation::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuickParticleSystemAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickParticleSystemAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickParticleSystemAnimation::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuickParticleSystemAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParticleSystemAnimation::tr(s, c, n));
}

//  QQuickParticleSystemAnimation::QQuickParticleSystemAnimation(QQuickPartic
//      leSystem *system)
extern "C" Q_DECL_EXPORT
QQuickParticleSystemAnimation *ritual_ZN29QQuickParticleSystemAnimationC1EP20QQuickParticleSystem(
    QQuickParticleSystem *system) {
  return new QQuickParticleSystemAnimation(system);
}

//  void QQuickParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickParticleSystemAnimation17updateCurrentTimeEi(
    QQuickParticleSystemAnimation *self,
    int t) {
  self->updateCurrentTime(t);
}

//  int QQuickParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickParticleSystemAnimation8durationEv(
    const QQuickParticleSystemAnimation *self) {
  return self->duration();
}

//  void QQuickParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickParticleSystemAnimation17updateCurrentTimeEi(
    QQuickParticleSystemAnimation *self,
    int t) {
  static_cast<OwnQQuickParticleSystemAnimation *>(self)->OwnQQuickParticleSystemAnimation::updateCurrentTime(
      t);
}

//  int QQuickParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QQuickParticleSystemAnimation8durationEv(
    const QQuickParticleSystemAnimation *self) {
  return static_cast<const OwnQQuickParticleSystemAnimation *>(self)->OwnQQuickParticleSystemAnimation::duration();
}
