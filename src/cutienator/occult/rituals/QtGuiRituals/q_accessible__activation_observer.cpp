//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>
#include <cstring>

//  A QAccessible::ActivationObserver that Python can take functions over in. Every QAccessible::ActivationObserver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAccessible_ActivationObserverCall0)(const void *, bool, int *);
class CuteQAccessible_ActivationObserver : public QAccessible::ActivationObserver {
public:
  using QAccessible::ActivationObserver::ActivationObserver;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QAccessible::ActivationObserver::accessibilityActiveChanged(bool
  //      active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessible_ActivationObserverCall0 call = reinterpret_cast<CuteQAccessible_ActivationObserverCall0>(taken[0]);
      call(this, active, &handled);
      if (handled) return;
    }
  }
};

//  QAccessible::ActivationObserver::~ActivationObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible18ActivationObserverD1Ev(
    QAccessible::ActivationObserver *self) {
  delete self;
}

//  void QAccessible::ActivationObserver::accessibilityActiveChanged(bool
//      active)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb(
    QAccessible::ActivationObserver *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}

//  a Python function taken by a CuteQAccessible_ActivationObserver, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessible_ActivationObserver(
    QAccessible::ActivationObserver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessible_ActivationObserver *>(self)->take(key, call);
}
