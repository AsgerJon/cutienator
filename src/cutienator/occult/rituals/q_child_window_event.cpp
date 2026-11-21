//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QChildWindowEvent *QChildWindowEvent::clone() const
extern "C" Q_DECL_EXPORT
QChildWindowEvent *ritual_ZNK17QChildWindowEvent5cloneEv(
    const QChildWindowEvent *self) {
  return self->clone();
}

//  QChildWindowEvent::~QChildWindowEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QChildWindowEventD1Ev(QChildWindowEvent *self) {
  delete self;
}

//  QChildWindowEvent::QChildWindowEvent(Type type, QWindow *childWindow)
extern "C" Q_DECL_EXPORT
QChildWindowEvent *ritual_ZN17QChildWindowEventC1EN6QEvent4TypeEP7QWindow(
    QEvent::Type type,
    QWindow *childWindow) {
  return new QChildWindowEvent(type, childWindow);
}

//  QWindow *QChildWindowEvent::child() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK17QChildWindowEvent5childEv(
    const QChildWindowEvent *self) {
  return self->child();
}
