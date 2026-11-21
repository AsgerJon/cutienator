//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

//  QAccessibleTextRemoveEvent::QAccessibleTextRemoveEvent(QObject *obj, int
//      position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextRemoveEvent *ritual_ZN26QAccessibleTextRemoveEventC1EP7QObjectiRK7QString(
    QObject *obj,
    int position,
    const QString *text) {
  return new QAccessibleTextRemoveEvent(obj, position, *text);
}

//  QAccessibleTextRemoveEvent::QAccessibleTextRemoveEvent(QAccessibleInterfa
//      ce *iface, int position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextRemoveEvent *ritual_ZN26QAccessibleTextRemoveEventC1EP20QAccessibleInterfaceiRK7QString(
    QAccessibleInterface *iface,
    int position,
    const QString *text) {
  return new QAccessibleTextRemoveEvent(iface, position, *text);
}

//  QAccessibleTextRemoveEvent::~QAccessibleTextRemoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextRemoveEventD1Ev(
    QAccessibleTextRemoveEvent *self) {
  delete self;
}

//  QString QAccessibleTextRemoveEvent::textRemoved() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextRemoveEvent11textRemovedEv(
    const QAccessibleTextRemoveEvent *self) {
  return new QString(self->textRemoved());
}

//  int QAccessibleTextRemoveEvent::changePosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextRemoveEvent14changePositionEv(
    const QAccessibleTextRemoveEvent *self) {
  return self->changePosition();
}
