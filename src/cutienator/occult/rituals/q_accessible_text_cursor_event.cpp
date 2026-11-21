//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>

//  QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(QObject *obj, int
//      cursorPos)
extern "C" Q_DECL_EXPORT
QAccessibleTextCursorEvent *ritual_ZN26QAccessibleTextCursorEventC1EP7QObjecti(
    QObject *obj,
    int cursorPos) {
  return new QAccessibleTextCursorEvent(obj, cursorPos);
}

//  QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(QAccessibleInterfa
//      ce *iface, int cursorPos)
extern "C" Q_DECL_EXPORT
QAccessibleTextCursorEvent *ritual_ZN26QAccessibleTextCursorEventC1EP20QAccessibleInterfacei(
    QAccessibleInterface *iface,
    int cursorPos) {
  return new QAccessibleTextCursorEvent(iface, cursorPos);
}

//  QAccessibleTextCursorEvent::~QAccessibleTextCursorEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextCursorEventD1Ev(
    QAccessibleTextCursorEvent *self) {
  delete self;
}

//  void QAccessibleTextCursorEvent::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextCursorEvent17setCursorPositionEi(
    QAccessibleTextCursorEvent *self,
    int position) {
  self->setCursorPosition(position);
}

//  int QAccessibleTextCursorEvent::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextCursorEvent14cursorPositionEv(
    const QAccessibleTextCursorEvent *self) {
  return self->cursorPosition();
}
