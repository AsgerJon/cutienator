//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qparameter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qparameter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>

//  A Qt3DRender::QParameterPrivate that Python can take functions over in. Every Qt3DRender::QParameterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QParameterPrivateCall0)(const void *, const QVariant *, int *);
typedef void (*CuteQt3DRender_QParameterPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QParameterPrivateCall2)(const void *, int *);
class CuteQt3DRender_QParameterPrivate : public Qt3DRender::QParameterPrivate {
public:
  using Qt3DRender::QParameterPrivate::QParameterPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender17QParameterPrivate8setValueERK8QVariant")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::QParameterPrivate::setValue(const QVariant &v)
  void setValue(const QVariant &v) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QParameterPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QParameterPrivateCall0>(taken[0]);
      call(this, &v, &handled);
      if (handled) return;
    }
    Qt3DRender::QParameterPrivate::setValue(v);
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QParameterPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QParameterPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QParameterPrivateCall2 call = reinterpret_cast<CuteQt3DRender_QParameterPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QParameter *Qt3DRender::QParameterPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QParameter *ritual_ZN10Qt3DRender17QParameterPrivate6q_funcEv(
    Qt3DRender::QParameterPrivate *self) {
  return self->q_func();
}

//  const QParameter *Qt3DRender::QParameterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QParameter *ritual_ZNK10Qt3DRender17QParameterPrivate6q_funcEv(
    const Qt3DRender::QParameterPrivate *self) {
  return self->q_func();
}

//  void Qt3DRender::QParameterPrivate::setValue(const QVariant &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QParameterPrivate8setValueERK8QVariant(
    Qt3DRender::QParameterPrivate *self,
    const QVariant *v) {
  self->setValue(*v);
}

//  a Python function taken by a CuteQt3DRender_QParameterPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QParameterPrivate(
    Qt3DRender::QParameterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QParameterPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::QParameterPrivate::setValue(const QVariant &v)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender17QParameterPrivate8setValueERK8QVariant(
    Qt3DRender::QParameterPrivate *self,
    const QVariant *v) {
  self->Qt3DRender::QParameterPrivate::setValue(*v);
}
