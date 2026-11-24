//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextinterface_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickTextInterface that Python can take functions over in. Every QQuickTextInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextInterfaceCall0)(const void *, int *);
class CuteQQuickTextInterface : public QQuickTextInterface {
public:
  using QQuickTextInterface::QQuickTextInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickTextInterface10invalidateEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuickTextInterface::invalidate()
  void invalidate() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextInterfaceCall0 call = reinterpret_cast<CuteQQuickTextInterfaceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  void QQuickTextInterface::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTextInterface10invalidateEv(
    QQuickTextInterface *self) {
  self->invalidate();
}

//  a Python function taken by a CuteQQuickTextInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextInterface(
    QQuickTextInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextInterface *>(self)->take(key, call);
}
