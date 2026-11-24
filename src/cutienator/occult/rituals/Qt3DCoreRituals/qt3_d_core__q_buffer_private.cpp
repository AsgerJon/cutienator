//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qbuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <QtCore/qbuffer.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QBufferPrivate that Python can take functions over in. Every Qt3DCore::QBufferPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QBufferPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QBufferPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
class CuteQt3DCore_QBufferPrivate : public Qt3DCore::QBufferPrivate {
public:
  using Qt3DCore::QBufferPrivate::QBufferPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QBufferPrivate::update()
  void update() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QBufferPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QBufferPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QBufferPrivate::update();
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QBufferPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QBufferPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }
};

//  QBuffer *Qt3DCore::QBufferPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QBuffer *ritual_ZN8Qt3DCore14QBufferPrivate6q_funcEv(
    Qt3DCore::QBufferPrivate *self) {
  return self->q_func();
}

//  const QBuffer *Qt3DCore::QBufferPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QBuffer *ritual_ZNK8Qt3DCore14QBufferPrivate6q_funcEv(
    const Qt3DCore::QBufferPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DCore_QBufferPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QBufferPrivate(
    Qt3DCore::QBufferPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QBufferPrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QBufferPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore14QBufferPrivate6updateEv(
    Qt3DCore::QBufferPrivate *self) {
  self->Qt3DCore::QBufferPrivate::update();
}
