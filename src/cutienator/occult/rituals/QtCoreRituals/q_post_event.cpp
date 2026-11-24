//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qthread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPostEvent::QPostEvent()
extern "C" Q_DECL_EXPORT
QPostEvent *ritual_ZN10QPostEventC1Ev() {
  return new QPostEvent();
}

//  QPostEvent::QPostEvent(QObject *r, QEvent *e, int p)
extern "C" Q_DECL_EXPORT
QPostEvent *ritual_ZN10QPostEventC1EP7QObjectP6QEventi(
    QObject *r,
    QEvent *e,
    int p) {
  return new QPostEvent(r, e, p);
}

//  QPostEvent::~QPostEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPostEventD1Ev(QPostEvent *self) {
  delete self;
}
