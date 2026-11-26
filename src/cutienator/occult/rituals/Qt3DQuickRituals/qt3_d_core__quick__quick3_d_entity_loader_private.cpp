//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentityloader_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentityloader_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/private/quick3dentityloader_p_p.h>
#include <QtQml/QQmlContext>
#include <QtQml/QQmlEngine>
#include <QtQml/QQmlIncubator>
#include <QtQml/private/qqmlengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3d/items/quick3dentityloader.cpp, line 18, as local:quick3dentityloader.cpp:Quick3DQmlOwner
namespace Qt3DCore::Quick {
namespace {
struct Quick3DQmlOwner
{
    Quick3DQmlOwner(QQmlEngine *e, QObject *o)
        : engine(e)
        , object(o)
    {}

    QQmlEngine *engine;
    QObject *object;

    QQmlContext *context() const
    {
        return engine->contextForObject(object);
    }
};
}  // namespace
}  // namespace Qt3DCore::Quick

//  from ../qt3d/src/quick3d/quick3d/items/quick3dentityloader.cpp, line 194, as _ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivateC1Ev
namespace Qt3DCore::Quick {
inline Quick3DEntityLoaderPrivate::Quick3DEntityLoaderPrivate()
    : QEntityPrivate(),
      m_incubator(nullptr),
      m_context(nullptr),
      m_component(nullptr),
      m_sourceComponent(nullptr),
      m_entity(nullptr),
      m_status(Quick3DEntityLoader::Null)
{
}
}  // namespace Qt3DCore::Quick

//  from ../qt3d/src/quick3d/quick3d/items/quick3dentityloader.cpp, line 301, as _ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivate9setStatusENS0_19Quick3DEntityLoader6StatusE
namespace Qt3DCore::Quick {
inline void Quick3DEntityLoaderPrivate::setStatus(Quick3DEntityLoader::Status status)
{
    Q_Q(Quick3DEntityLoader);
    if (status != m_status) {
        m_status = status;
        const bool blocked = q->blockNotifications(true);
        emit q->statusChanged(m_status);
        q->blockNotifications(blocked);
    }
}
}  // namespace Qt3DCore::Quick
//  -----------------------------------------------------------------------

//  A Qt3DCore::Quick::Quick3DEntityLoaderPrivate that Python can take functions over in. Every Qt3DCore::Quick::Quick3DEntityLoaderPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_Quick_Quick3DEntityLoaderPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_Quick_Quick3DEntityLoaderPrivateCall1)(const void *, int *);
class CuteQt3DCore_Quick_Quick3DEntityLoaderPrivate : public Qt3DCore::Quick::Quick3DEntityLoaderPrivate {
public:
  using Qt3DCore::Quick::Quick3DEntityLoaderPrivate::Quick3DEntityLoaderPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_Quick_Quick3DEntityLoaderPrivateCall0 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_Quick_Quick3DEntityLoaderPrivateCall1 call = reinterpret_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DCore::Quick::Quick3DEntityLoaderPrivate::Quick3DEntityLoaderPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DEntityLoaderPrivate *ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivateC1Ev() {
  return new CuteQt3DCore_Quick_Quick3DEntityLoaderPrivate();
}

//  Quick3DEntityLoader
//      *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DEntityLoader *ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivate6q_funcEv(
    Qt3DCore::Quick::Quick3DEntityLoaderPrivate *self) {
  return self->q_func();
}

//  const Quick3DEntityLoader
//      *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::Quick::Quick3DEntityLoader *ritual_ZNK8Qt3DCore5Quick26Quick3DEntityLoaderPrivate6q_funcEv(
    const Qt3DCore::Quick::Quick3DEntityLoaderPrivate *self) {
  return self->q_func();
}

//  void Qt3DCore::Quick::Quick3DEntityLoaderPrivate::setStatus(Quick3DEntity
//      Loader::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivate9setStatusENS0_19Quick3DEntityLoader6StatusE(
    Qt3DCore::Quick::Quick3DEntityLoaderPrivate *self,
    Qt3DCore::Quick::Quick3DEntityLoader::Status status) {
  self->setStatus(status);
}

//  Quick3DEntityLoaderPrivate
//      *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::get(Quick3DEntityLoader
//      *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DEntityLoaderPrivate *ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivate3getEPNS0_19Quick3DEntityLoaderE(
    Qt3DCore::Quick::Quick3DEntityLoader *q) {
  return Qt3DCore::Quick::Quick3DEntityLoaderPrivate::get(q);
}

//  a Python function taken by a
//      CuteQt3DCore_Quick_Quick3DEntityLoaderPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_Quick_Quick3DEntityLoaderPrivate(
    Qt3DCore::Quick::Quick3DEntityLoaderPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_Quick_Quick3DEntityLoaderPrivate *>(self)->take(key, call);
}
