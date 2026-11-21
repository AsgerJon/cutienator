//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>

//  QAccessibleEvent::QAccessibleEvent(QObject *obj, QAccessible::Event typ)
extern "C" Q_DECL_EXPORT
QAccessibleEvent *ritual_ZN16QAccessibleEventC1EP7QObjectN11QAccessible5EventE(
    QObject *obj,
    QAccessible::Event typ) {
  return new QAccessibleEvent(obj, typ);
}

//  QAccessibleEvent::QAccessibleEvent(QAccessibleInterface *iface,
//      QAccessible::Event typ)
extern "C" Q_DECL_EXPORT
QAccessibleEvent *ritual_ZN16QAccessibleEventC1EP20QAccessibleInterfaceN11QAccessible5EventE(
    QAccessibleInterface *iface,
    QAccessible::Event typ) {
  return new QAccessibleEvent(iface, typ);
}

//  QAccessibleEvent::~QAccessibleEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleEventD1Ev(QAccessibleEvent *self) {
  delete self;
}

//  QAccessible::Event QAccessibleEvent::type() const
extern "C" Q_DECL_EXPORT
QAccessible::Event ritual_ZNK16QAccessibleEvent4typeEv(
    const QAccessibleEvent *self) {
  return self->type();
}

//  QObject *QAccessibleEvent::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QAccessibleEvent6objectEv(
    const QAccessibleEvent *self) {
  return self->object();
}

//  QAccessible::Id QAccessibleEvent::uniqueId() const
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZNK16QAccessibleEvent8uniqueIdEv(
    const QAccessibleEvent *self) {
  return self->uniqueId();
}

//  void QAccessibleEvent::setChild(int chld)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleEvent8setChildEi(
    QAccessibleEvent *self,
    int chld) {
  self->setChild(chld);
}

//  int QAccessibleEvent::child() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleEvent5childEv(const QAccessibleEvent *self) {
  return self->child();
}

//  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleEvent19accessibleInterfaceEv(
    const QAccessibleEvent *self) {
  return self->accessibleInterface();
}
