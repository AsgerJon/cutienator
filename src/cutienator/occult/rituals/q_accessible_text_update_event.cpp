//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

//  QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(QObject *obj, int
//      position, const QString &oldText, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextUpdateEvent *ritual_ZN26QAccessibleTextUpdateEventC1EP7QObjectiRK7QStringS4_(
    QObject *obj,
    int position,
    const QString *oldText,
    const QString *text) {
  return new QAccessibleTextUpdateEvent(obj, position, *oldText, *text);
}

//  QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(QAccessibleInterfa
//      ce *iface, int position, const QString &oldText, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextUpdateEvent *ritual_ZN26QAccessibleTextUpdateEventC1EP20QAccessibleInterfaceiRK7QStringS4_(
    QAccessibleInterface *iface,
    int position,
    const QString *oldText,
    const QString *text) {
  return new QAccessibleTextUpdateEvent(iface, position, *oldText, *text);
}

//  QAccessibleTextUpdateEvent::~QAccessibleTextUpdateEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextUpdateEventD1Ev(
    QAccessibleTextUpdateEvent *self) {
  delete self;
}

//  QString QAccessibleTextUpdateEvent::textRemoved() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextUpdateEvent11textRemovedEv(
    const QAccessibleTextUpdateEvent *self) {
  return new QString(self->textRemoved());
}

//  QString QAccessibleTextUpdateEvent::textInserted() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextUpdateEvent12textInsertedEv(
    const QAccessibleTextUpdateEvent *self) {
  return new QString(self->textInserted());
}

//  int QAccessibleTextUpdateEvent::changePosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextUpdateEvent14changePositionEv(
    const QAccessibleTextUpdateEvent *self) {
  return self->changePosition();
}
