//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlfinalizer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlfinalizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlFinalizerHook that Python can take functions over in. Every QQmlFinalizerHook
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlFinalizerHookCall0)(const void *, int *);
class CuteQQmlFinalizerHook : public QQmlFinalizerHook {
public:
  using QQmlFinalizerHook::QQmlFinalizerHook;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQmlFinalizerHook18componentFinalizedEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQmlFinalizerHook::componentFinalized()
  void componentFinalized() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlFinalizerHookCall0 call = reinterpret_cast<CuteQQmlFinalizerHookCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QQmlFinalizerHook::~QQmlFinalizerHook()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlFinalizerHookD1Ev(QQmlFinalizerHook *self) {
  delete self;
}

//  void QQmlFinalizerHook::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlFinalizerHook18componentFinalizedEv(
    QQmlFinalizerHook *self) {
  self->componentFinalized();
}

//  a Python function taken by a CuteQQmlFinalizerHook, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlFinalizerHook(
    QQmlFinalizerHook *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlFinalizerHook *>(self)->take(key, call);
}
