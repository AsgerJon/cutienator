//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>

//  QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(QObject
//      *obj, int start, int end)
extern "C" Q_DECL_EXPORT
QAccessibleTextSelectionEvent *ritual_ZN29QAccessibleTextSelectionEventC1EP7QObjectii(
    QObject *obj,
    int start,
    int end) {
  return new QAccessibleTextSelectionEvent(obj, start, end);
}

//  QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(QAccessibleI
//      nterface *iface, int start, int end)
extern "C" Q_DECL_EXPORT
QAccessibleTextSelectionEvent *ritual_ZN29QAccessibleTextSelectionEventC1EP20QAccessibleInterfaceii(
    QAccessibleInterface *iface,
    int start,
    int end) {
  return new QAccessibleTextSelectionEvent(iface, start, end);
}

//  QAccessibleTextSelectionEvent::~QAccessibleTextSelectionEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleTextSelectionEventD1Ev(
    QAccessibleTextSelectionEvent *self) {
  delete self;
}

//  void QAccessibleTextSelectionEvent::setSelection(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleTextSelectionEvent12setSelectionEii(
    QAccessibleTextSelectionEvent *self,
    int start,
    int end) {
  self->setSelection(start, end);
}

//  int QAccessibleTextSelectionEvent::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTextSelectionEvent14selectionStartEv(
    const QAccessibleTextSelectionEvent *self) {
  return self->selectionStart();
}

//  int QAccessibleTextSelectionEvent::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTextSelectionEvent12selectionEndEv(
    const QAccessibleTextSelectionEvent *self) {
  return self->selectionEnd();
}
