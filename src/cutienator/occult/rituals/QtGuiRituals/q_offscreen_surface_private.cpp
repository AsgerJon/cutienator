//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qoffscreensurface_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qoffscreensurface.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qoffscreensurface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOffscreenSurface *QOffscreenSurfacePrivate::q_func()
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZN24QOffscreenSurfacePrivate6q_funcEv(
    QOffscreenSurfacePrivate *self) {
  return self->q_func();
}

//  const QOffscreenSurface *QOffscreenSurfacePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOffscreenSurface *ritual_ZNK24QOffscreenSurfacePrivate6q_funcEv(
    const QOffscreenSurfacePrivate *self) {
  return self->q_func();
}

//  QOffscreenSurfacePrivate::QOffscreenSurfacePrivate()
extern "C" Q_DECL_EXPORT
QOffscreenSurfacePrivate *ritual_ZN24QOffscreenSurfacePrivateC1Ev() {
  return new QOffscreenSurfacePrivate();
}

//  QOffscreenSurfacePrivate::~QOffscreenSurfacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOffscreenSurfacePrivateD1Ev(
    QOffscreenSurfacePrivate *self) {
  delete self;
}

//  QOffscreenSurfacePrivate *QOffscreenSurfacePrivate::get(QOffscreenSurface
//      *surface)
extern "C" Q_DECL_EXPORT
QOffscreenSurfacePrivate *ritual_ZN24QOffscreenSurfacePrivate3getEP17QOffscreenSurface(
    QOffscreenSurface *surface) {
  return QOffscreenSurfacePrivate::get(surface);
}
