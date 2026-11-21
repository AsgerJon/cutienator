//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QActionEvent *QActionEvent::clone() const
extern "C" Q_DECL_EXPORT
QActionEvent *ritual_ZNK12QActionEvent5cloneEv(const QActionEvent *self) {
  return self->clone();
}

//  QActionEvent::~QActionEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionEventD1Ev(QActionEvent *self) {
  delete self;
}

//  QActionEvent::QActionEvent(int type, QAction *action, QAction *before)
extern "C" Q_DECL_EXPORT
QActionEvent *ritual_ZN12QActionEventC1EiP7QActionS1_(
    int type,
    QAction *action,
    QAction *before) {
  return new QActionEvent(type, action, before);
}

//  QAction *QActionEvent::action() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QActionEvent6actionEv(const QActionEvent *self) {
  return self->action();
}

//  QAction *QActionEvent::before() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QActionEvent6beforeEv(const QActionEvent *self) {
  return self->before();
}
