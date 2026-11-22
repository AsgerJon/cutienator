//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

//  QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QObject *obj, int
//      position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextInsertEvent *ritual_ZN26QAccessibleTextInsertEventC1EP7QObjectiRK7QString(
    QObject *obj,
    int position,
    const QString *text) {
  return new QAccessibleTextInsertEvent(obj, position, *text);
}

//  QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QAccessibleInterfa
//      ce *iface, int position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextInsertEvent *ritual_ZN26QAccessibleTextInsertEventC1EP20QAccessibleInterfaceiRK7QString(
    QAccessibleInterface *iface,
    int position,
    const QString *text) {
  return new QAccessibleTextInsertEvent(iface, position, *text);
}

//  QAccessibleTextInsertEvent::~QAccessibleTextInsertEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextInsertEventD1Ev(
    QAccessibleTextInsertEvent *self) {
  delete self;
}

//  QString QAccessibleTextInsertEvent::textInserted() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextInsertEvent12textInsertedEv(
    const QAccessibleTextInsertEvent *self) {
  return new QString(self->textInserted());
}

//  int QAccessibleTextInsertEvent::changePosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextInsertEvent14changePositionEv(
    const QAccessibleTextInsertEvent *self) {
  return self->changePosition();
}
