//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuick3DParticleSystemAnimation' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3DParticles__QQuick3DParticleSystemAnimation.cpp, line 1, as moc:QQuick3DParticleSystemAnimation
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN31QQuick3DParticleSystemAnimationE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuick3DParticleSystemAnimation::qt_create_metaobjectdata<qt_meta_tag_ZN31QQuick3DParticleSystemAnimationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuick3DParticleSystemAnimation"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuick3DParticleSystemAnimation, qt_meta_tag_ZN31QQuick3DParticleSystemAnimationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuick3DParticleSystemAnimation::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractAnimation::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQuick3DParticleSystemAnimationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQuick3DParticleSystemAnimationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN31QQuick3DParticleSystemAnimationE_t>.metaTypes,
    nullptr
} };

void QQuick3DParticleSystemAnimation::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuick3DParticleSystemAnimation *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuick3DParticleSystemAnimation::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuick3DParticleSystemAnimation::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQuick3DParticleSystemAnimationE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractAnimation::qt_metacast(_clname);
}

int QQuick3DParticleSystemAnimation::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractAnimation::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  Only a class built on QQuick3DParticleSystemAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleSystemAnimation : QQuick3DParticleSystemAnimation {
  using QQuick3DParticleSystemAnimation::updateCurrentTime;
  using QQuick3DParticleSystemAnimation::duration;
};

//  const QMetaObject *QQuick3DParticleSystemAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuick3DParticleSystemAnimation10metaObjectEv(
    const QQuick3DParticleSystemAnimation *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleSystemAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuick3DParticleSystemAnimation11qt_metacastEPKc(
    QQuick3DParticleSystemAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleSystemAnimation::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuick3DParticleSystemAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleSystemAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleSystemAnimation::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuick3DParticleSystemAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleSystemAnimation::tr(s, c, n));
}

//  QQuick3DParticleSystemAnimation::QQuick3DParticleSystemAnimation(QQuick3D
//      ParticleSystem *system)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSystemAnimation *ritual_ZN31QQuick3DParticleSystemAnimationC1EP22QQuick3DParticleSystem(
    QQuick3DParticleSystem *system) {
  return new QQuick3DParticleSystemAnimation(system);
}

//  void QQuick3DParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleSystemAnimation17updateCurrentTimeEi(
    QQuick3DParticleSystemAnimation *self,
    int t) {
  self->updateCurrentTime(t);
}

//  int QQuick3DParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQuick3DParticleSystemAnimation8durationEv(
    const QQuick3DParticleSystemAnimation *self) {
  return self->duration();
}

//  void QQuick3DParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQuick3DParticleSystemAnimation17updateCurrentTimeEi(
    QQuick3DParticleSystemAnimation *self,
    int t) {
  static_cast<OwnQQuick3DParticleSystemAnimation *>(self)->OwnQQuick3DParticleSystemAnimation::updateCurrentTime(
      t);
}

//  int QQuick3DParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK31QQuick3DParticleSystemAnimation8durationEv(
    const QQuick3DParticleSystemAnimation *self) {
  return static_cast<const OwnQQuick3DParticleSystemAnimation *>(self)->OwnQQuick3DParticleSystemAnimation::duration();
}
