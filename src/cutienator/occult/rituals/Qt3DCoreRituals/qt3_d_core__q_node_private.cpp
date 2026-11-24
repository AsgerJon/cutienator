//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QNodePrivate that Python can take functions over in. Every Qt3DCore::QNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QNodePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_QNodePrivateCall1)(const void *, int *);
class CuteQt3DCore_QNodePrivate : public Qt3DCore::QNodePrivate {
public:
  using Qt3DCore::QNodePrivate::QNodePrivate;
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
      CuteQt3DCore_QNodePrivateCall0 call = reinterpret_cast<CuteQt3DCore_QNodePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QNodePrivateCall1 call = reinterpret_cast<CuteQt3DCore_QNodePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  void Qt3DCore::QNodePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate6updateEv(
    Qt3DCore::QNodePrivate *self) {
  self->update();
}

//  QNode *Qt3DCore::QNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN8Qt3DCore12QNodePrivate6q_funcEv(
    Qt3DCore::QNodePrivate *self) {
  return self->q_func();
}

//  const QNode *Qt3DCore::QNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QNode *ritual_ZNK8Qt3DCore12QNodePrivate6q_funcEv(
    const Qt3DCore::QNodePrivate *self) {
  return self->q_func();
}

//  void Qt3DCore::QNodePrivate::unregisterDestructionHelper(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate27unregisterDestructionHelperEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *node) {
  self->unregisterDestructionHelper(node);
}

//  a Python function taken by a CuteQt3DCore_QNodePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QNodePrivate(
    Qt3DCore::QNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QNodePrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QScene *scene) {
  self->Qt3DCore::QNodePrivate::setScene(scene);
}

//  void Qt3DCore::QNodePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore12QNodePrivate6updateEv(
    Qt3DCore::QNodePrivate *self) {
  self->Qt3DCore::QNodePrivate::update();
}
