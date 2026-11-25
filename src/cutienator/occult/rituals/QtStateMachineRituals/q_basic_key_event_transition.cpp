//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qbasickeyeventtransition_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructors, 'tr' and the functions that are
//  not virtual, which Qt's library offers not.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(qeventtransition)
#include <QtStateMachine/6.12.0/QtStateMachine/private/qbasickeyeventtransition_p.h>

//  const QMetaObject *QBasicKeyEventTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QBasicKeyEventTransition10metaObjectEv(
    const QBasicKeyEventTransition *self) {
  return self->metaObject();
}

//  QBasicKeyEventTransition::~QBasicKeyEventTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBasicKeyEventTransitionD1Ev(
    QBasicKeyEventTransition *self) {
  delete self;
}

//  bool QBasicKeyEventTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QBasicKeyEventTransition9eventTestEP6QEvent(
    QBasicKeyEventTransition *self,
    QEvent *event) {
  return self->eventTest(event);
}

//  void QBasicKeyEventTransition::onTransition(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBasicKeyEventTransition12onTransitionEP6QEvent(
    QBasicKeyEventTransition *self,
    QEvent *a0) {
  self->onTransition(a0);
}

#endif  // QT_CONFIG(qeventtransition)
