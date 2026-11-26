//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_glib_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(glib) && defined(Q_OS_UNIX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_glib_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QEventDispatcherGlibPrivate::QEventDispatcherGlibPrivate(GMainContext
//      *context)
extern "C" Q_DECL_EXPORT
QEventDispatcherGlibPrivate *ritual_ZN27QEventDispatcherGlibPrivateC1EP13_GMainContext(
    GMainContext *context) {
  return new QEventDispatcherGlibPrivate(context);
}

//  QEventDispatcherGlibPrivate::~QEventDispatcherGlibPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QEventDispatcherGlibPrivateD1Ev(
    QEventDispatcherGlibPrivate *self) {
  delete self;
}

//  void QEventDispatcherGlibPrivate::runTimersOnceWithNormalPriority()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QEventDispatcherGlibPrivate31runTimersOnceWithNormalPriorityEv(
    QEventDispatcherGlibPrivate *self) {
  self->runTimersOnceWithNormalPriority();
}

#endif  // QT_CONFIG(glib) && defined(Q_OS_UNIX)
