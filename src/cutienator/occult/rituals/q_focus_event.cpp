//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QFocusEvent *QFocusEvent::clone() const
extern "C" Q_DECL_EXPORT
QFocusEvent *ritual_ZNK11QFocusEvent5cloneEv(const QFocusEvent *self) {
  return self->clone();
}

//  QFocusEvent::~QFocusEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFocusEventD1Ev(QFocusEvent *self) {
  delete self;
}

//  QFocusEvent::QFocusEvent(Type type, Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
QFocusEvent *ritual_ZN11QFocusEventC1EN6QEvent4TypeEN2Qt11FocusReasonE(
    QEvent::Type type,
    Qt::FocusReason reason) {
  return new QFocusEvent(type, reason);
}

//  bool QFocusEvent::gotFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFocusEvent8gotFocusEv(const QFocusEvent *self) {
  return self->gotFocus();
}

//  bool QFocusEvent::lostFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFocusEvent9lostFocusEv(const QFocusEvent *self) {
  return self->lostFocus();
}

//  Qt::FocusReason QFocusEvent::reason() const
extern "C" Q_DECL_EXPORT
Qt::FocusReason ritual_ZNK11QFocusEvent6reasonEv(const QFocusEvent *self) {
  return self->reason();
}
