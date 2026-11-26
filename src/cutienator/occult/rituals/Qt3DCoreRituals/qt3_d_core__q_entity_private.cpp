//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qentity_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 3.
//  Kept as it is when the generator runs again.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qentity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qstring.h>
#include <cstring>
#include <Qt3DCore/qcomponent.h>
#include <Qt3DCore/qtransform.h>
#include <QtCore/qlist.h>

//  A Qt3DCore::QEntityPrivate that Python can take functions over in. Every Qt3DCore::QEntityPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QEntityPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_QEntityPrivateCall1)(const void *, int *);
class CuteQt3DCore_QEntityPrivate : public Qt3DCore::QEntityPrivate {
public:
  using Qt3DCore::QEntityPrivate::QEntityPrivate;
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
      CuteQt3DCore_QEntityPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QEntityPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QEntityPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QEntityPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DCore::QEntityPrivate::QEntityPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntityPrivate *ritual_ZN8Qt3DCore14QEntityPrivateC1Ev() {
  return new CuteQt3DCore_QEntityPrivate();
}

//  Qt3DCore::QEntityPrivate::~QEntityPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QEntityPrivateD1Ev(Qt3DCore::QEntityPrivate *self) {
  delete self;
}

//  QEntity *Qt3DCore::QEntityPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZN8Qt3DCore14QEntityPrivate6q_funcEv(
    Qt3DCore::QEntityPrivate *self) {
  return self->q_func();
}

//  const QEntity *Qt3DCore::QEntityPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QEntity *ritual_ZNK8Qt3DCore14QEntityPrivate6q_funcEv(
    const Qt3DCore::QEntityPrivate *self) {
  return self->q_func();
}

//  QEntityPrivate *Qt3DCore::QEntityPrivate::get(QEntity *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntityPrivate *ritual_ZN8Qt3DCore14QEntityPrivate3getEPNS_7QEntityE(
    Qt3DCore::QEntity *q) {
  return Qt3DCore::QEntityPrivate::get(q);
}

//  QNodeId Qt3DCore::QEntityPrivate::parentEntityId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK8Qt3DCore14QEntityPrivate14parentEntityIdEv(
    const Qt3DCore::QEntityPrivate *self) {
  return new Qt3DCore::QNodeId(self->parentEntityId());
}

//  void Qt3DCore::QEntityPrivate::updateComponentRelationShip(QComponent
//      *component, ComponentRelationshipChange::RelationShip change)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QEntityPrivate27updateComponentRelationShipEPNS_10QComponentENS_27ComponentRelationshipChange12RelationShipE(
    Qt3DCore::QEntityPrivate *self,
    Qt3DCore::QComponent *component,
    Qt3DCore::ComponentRelationshipChange::RelationShip change) {
  self->updateComponentRelationShip(component, change);
}

//  QString Qt3DCore::QEntityPrivate::dumpSceneGraph() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore14QEntityPrivate14dumpSceneGraphEv(
    const Qt3DCore::QEntityPrivate *self) {
  return new QString(self->dumpSceneGraph());
}

//  void Qt3DCore::QEntityPrivate::removeDestroyedComponent(QComponent *comp)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QEntityPrivate24removeDestroyedComponentEPNS_10QComponentE(
    Qt3DCore::QEntityPrivate *self,
    Qt3DCore::QComponent *comp) {
  self->removeDestroyedComponent(comp);
}

//  a Python function taken by a CuteQt3DCore_QEntityPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QEntityPrivate(
    Qt3DCore::QEntityPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QEntityPrivate *>(self)->take(key, call);
}

//  QList<QObject *> Qt3DCore::QEntityPrivate::componentsOfType<QObject>()
//      const
extern "C" Q_DECL_EXPORT
QList<QObject *> * ritual_ZNK8Qt3DCore14QEntityPrivate16componentsOfTypeI7QObjectEE5QListIPT_Ev(
    const Qt3DCore::QEntityPrivate *self) {
  return new QList<QObject *>(self->componentsOfType<QObject>());
}

//  QList<Qt3DCore::QComponent *>
//      Qt3DCore::QEntityPrivate::componentsOfType<Qt3DCore::QComponent>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QComponent *> * ritual_ZNK8Qt3DCore14QEntityPrivate16componentsOfTypeINS_10QComponentEEE5QListIPT_Ev(
    const Qt3DCore::QEntityPrivate *self) {
  return new QList<Qt3DCore::QComponent *>(self->componentsOfType<Qt3DCore::QComponent>());
}

//  QList<Qt3DCore::QTransform *>
//      Qt3DCore::QEntityPrivate::componentsOfType<Qt3DCore::QTransform>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QTransform *> * ritual_ZNK8Qt3DCore14QEntityPrivate16componentsOfTypeINS_10QTransformEEE5QListIPT_Ev(
    const Qt3DCore::QEntityPrivate *self) {
  return new QList<Qt3DCore::QTransform *>(self->componentsOfType<Qt3DCore::QTransform>());
}
