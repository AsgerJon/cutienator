//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessiblebridge.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessiblebridge.h>
#include <cstring>

//  A QAccessibleBridge that Python can take functions over in. Every QAccessibleBridge
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleBridgeCall0)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleBridgeCall1)(const void *, QAccessibleEvent *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleBridge : public QAccessibleBridge {
public:
  using QAccessibleBridge::QAccessibleBridge;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QAccessibleBridge13setRootObjectEP20QAccessibleInterface")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QAccessibleBridge25notifyAccessibilityUpdateEP16QAccessibleEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  void QAccessibleBridge::setRootObject(QAccessibleInterface *a0)
  void setRootObject(QAccessibleInterface *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleBridgeCall0 call = reinterpret_cast<CuteQAccessibleBridgeCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleBridge::notifyAccessibilityUpdate(QAccessibleEvent
  //      *event)
  void notifyAccessibilityUpdate(QAccessibleEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleBridgeCall1 call = reinterpret_cast<CuteQAccessibleBridgeCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleBridge::~QAccessibleBridge()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleBridgeD1Ev(QAccessibleBridge *self) {
  delete self;
}

//  void QAccessibleBridge::setRootObject(QAccessibleInterface *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleBridge13setRootObjectEP20QAccessibleInterface(
    QAccessibleBridge *self,
    QAccessibleInterface *a0) {
  self->setRootObject(a0);
}

//  void QAccessibleBridge::notifyAccessibilityUpdate(QAccessibleEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleBridge25notifyAccessibilityUpdateEP16QAccessibleEvent(
    QAccessibleBridge *self,
    QAccessibleEvent *event) {
  self->notifyAccessibilityUpdate(event);
}

//  a Python function taken by a CuteQAccessibleBridge, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleBridge(
    QAccessibleBridge *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleBridge *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
