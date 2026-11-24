//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qwaylandview.h"
#include "qwaylandview_p.h"
#include "qwaylandsurface.h"
#include <QtWaylandCompositor/QWaylandSeat>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtCore/QMutex>
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/compositor_api/qwaylandview.cpp, line 112, as _ZN19QWaylandViewPrivate16clearFrontBufferEv
inline void QWaylandViewPrivate::clearFrontBuffer()
{
    if (!bufferLocked) {
        currentBuffer = QWaylandBufferRef();
        currentDamage = QRegion();
    }
}
//  -----------------------------------------------------------------------

//  QWaylandView *QWaylandViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWaylandView *ritual_ZN19QWaylandViewPrivate6q_funcEv(
    QWaylandViewPrivate *self) {
  return self->q_func();
}

//  const QWaylandView *QWaylandViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWaylandView *ritual_ZNK19QWaylandViewPrivate6q_funcEv(
    const QWaylandViewPrivate *self) {
  return self->q_func();
}

//  QWaylandViewPrivate *QWaylandViewPrivate::get(QWaylandView *view)
extern "C" Q_DECL_EXPORT
QWaylandViewPrivate *ritual_ZN19QWaylandViewPrivate3getEP12QWaylandView(
    QWaylandView *view) {
  return QWaylandViewPrivate::get(view);
}

//  QWaylandViewPrivate::QWaylandViewPrivate()
extern "C" Q_DECL_EXPORT
QWaylandViewPrivate *ritual_ZN19QWaylandViewPrivateC1Ev() {
  return new QWaylandViewPrivate();
}

//  void QWaylandViewPrivate::clearFrontBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandViewPrivate16clearFrontBufferEv(
    QWaylandViewPrivate *self) {
  self->clearFrontBuffer();
}
