//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qeventdispatcher_glib_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(glib) && defined(Q_OS_UNIX)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qeventdispatcher_glib_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPAEventDispatcherGlib *QPAEventDispatcherGlibPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPAEventDispatcherGlib *ritual_ZN29QPAEventDispatcherGlibPrivate6q_funcEv(
    QPAEventDispatcherGlibPrivate *self) {
  return self->q_func();
}

//  const QPAEventDispatcherGlib *QPAEventDispatcherGlibPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QPAEventDispatcherGlib *ritual_ZNK29QPAEventDispatcherGlibPrivate6q_funcEv(
    const QPAEventDispatcherGlibPrivate *self) {
  return self->q_func();
}

//  QPAEventDispatcherGlibPrivate::~QPAEventDispatcherGlibPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QPAEventDispatcherGlibPrivateD1Ev(
    QPAEventDispatcherGlibPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(glib) && defined(Q_OS_UNIX)
