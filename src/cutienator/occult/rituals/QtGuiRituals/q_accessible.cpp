//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>

//  void QAccessible::installActivationObserver(ActivationObserver *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible25installActivationObserverEPNS_18ActivationObserverE(
    QAccessible::ActivationObserver *a0) {
  QAccessible::installActivationObserver(a0);
}

//  void QAccessible::removeActivationObserver(ActivationObserver *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible24removeActivationObserverEPNS_18ActivationObserverE(
    QAccessible::ActivationObserver *a0) {
  QAccessible::removeActivationObserver(a0);
}

//  QAccessibleInterface *QAccessible::queryAccessibleInterface(QObject *a0)
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZN11QAccessible24queryAccessibleInterfaceEP7QObject(
    QObject *a0) {
  return QAccessible::queryAccessibleInterface(a0);
}

//  Id QAccessible::uniqueId(QAccessibleInterface *iface)
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZN11QAccessible8uniqueIdEP20QAccessibleInterface(
    QAccessibleInterface *iface) {
  return QAccessible::uniqueId(iface);
}

//  QAccessibleInterface *QAccessible::accessibleInterface(Id uniqueId)
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZN11QAccessible19accessibleInterfaceEj(
    QAccessible::Id uniqueId) {
  return QAccessible::accessibleInterface(uniqueId);
}

//  Id QAccessible::registerAccessibleInterface(QAccessibleInterface *iface)
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZN11QAccessible27registerAccessibleInterfaceEP20QAccessibleInterface(
    QAccessibleInterface *iface) {
  return QAccessible::registerAccessibleInterface(iface);
}

//  void QAccessible::deleteAccessibleInterface(Id uniqueId)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible25deleteAccessibleInterfaceEj(
    QAccessible::Id uniqueId) {
  QAccessible::deleteAccessibleInterface(uniqueId);
}

//  void QAccessible::updateAccessibility(QAccessibleEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible19updateAccessibilityEP16QAccessibleEvent(
    QAccessibleEvent *event) {
  QAccessible::updateAccessibility(event);
}

//  bool QAccessible::isActive()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QAccessible8isActiveEv() {
  return QAccessible::isActive();
}

//  void QAccessible::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible9setActiveEb(bool active) {
  QAccessible::setActive(active);
}

//  void QAccessible::setRootObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible13setRootObjectEP7QObject(QObject *object) {
  QAccessible::setRootObject(object);
}

//  void QAccessible::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible7cleanupEv() {
  QAccessible::cleanup();
}

//  QAccessible::QAccessible()
extern "C" Q_DECL_EXPORT
QAccessible *ritual_ZN11QAccessibleC1Ev() {
  return new QAccessible();
}

//  QAccessible::~QAccessible()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessibleD1Ev(QAccessible *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
