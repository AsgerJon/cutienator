//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qanimationcallback.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qanimationcallback.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A Qt3DAnimation::QAnimationCallback that Python can take functions over in. Every Qt3DAnimation::QAnimationCallback
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QAnimationCallbackCall0)(const void *, const QVariant *, int *);
class CuteQt3DAnimation_QAnimationCallback : public Qt3DAnimation::QAnimationCallback {
public:
  using Qt3DAnimation::QAnimationCallback::QAnimationCallback;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13Qt3DAnimation18QAnimationCallback12valueChangedERK8QVariant")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DAnimation::QAnimationCallback::valueChanged(const QVariant
  //      &value)
  void valueChanged(const QVariant &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationCallbackCall0 call = reinterpret_cast<CuteQt3DAnimation_QAnimationCallbackCall0>(taken[0]);
      call(this, &value, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DAnimation::QAnimationCallback::~QAnimationCallback()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationCallbackD1Ev(
    Qt3DAnimation::QAnimationCallback *self) {
  delete self;
}

//  void Qt3DAnimation::QAnimationCallback::valueChanged(const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationCallback12valueChangedERK8QVariant(
    Qt3DAnimation::QAnimationCallback *self,
    const QVariant *value) {
  self->valueChanged(*value);
}

//  a Python function taken by a CuteQt3DAnimation_QAnimationCallback, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAnimationCallback(
    Qt3DAnimation::QAnimationCallback *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAnimationCallback *>(self)->take(key, call);
}
