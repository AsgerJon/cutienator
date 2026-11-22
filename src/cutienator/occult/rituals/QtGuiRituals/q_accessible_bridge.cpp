//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessiblebridge.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessiblebridge.h>

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
