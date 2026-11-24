//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(menu)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QMenuPrivate::DelayState::DelayState()
extern "C" Q_DECL_EXPORT
QMenuPrivate::DelayState *ritual_ZN12QMenuPrivate10DelayStateC1Ev() {
  return new QMenuPrivate::DelayState();
}

//  void QMenuPrivate::DelayState::initialize(QMenu *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate10DelayState10initializeEP5QMenu(
    QMenuPrivate::DelayState *self,
    QMenu *parent) {
  self->initialize(parent);
}

//  void QMenuPrivate::DelayState::start(int timeout, QAction *toStartAction)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate10DelayState5startEiP7QAction(
    QMenuPrivate::DelayState *self,
    int timeout,
    QAction *toStartAction) {
  self->start(timeout, toStartAction);
}

//  void QMenuPrivate::DelayState::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate10DelayState4stopEv(
    QMenuPrivate::DelayState *self) {
  self->stop();
}

#endif  // QT_CONFIG(menu)
