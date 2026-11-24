//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandinputmethodcontrol.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(im)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#include <QtWaylandCompositor/private/qwaylandinputmethodcontrol_p.h>
#include <QtWaylandCompositor/qwaylandcompositor.h>
#include <QtWaylandCompositor/qwaylandseat.h>
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtWaylandCompositor/qwaylandtextinput.h>
#include <QtWaylandCompositor/qwaylandtextinputv3.h>
#include <QtWaylandCompositor/qwaylandqttextinputmethod.h>
#include <QtGui/QInputMethodEvent>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/compositor_api/qwaylandinputmethodcontrol.cpp, line 84, as _ZNK26QWaylandInputMethodControl7enabledEv
inline bool QWaylandInputMethodControl::enabled() const
{
    Q_D(const QWaylandInputMethodControl);

    return d->enabled;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWaylandInputMethodControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWaylandInputMethodControl10metaObjectEv(
    const QWaylandInputMethodControl *self) {
  return self->metaObject();
}

//  QWaylandInputMethodControlPrivate *QWaylandInputMethodControl::d_func()
extern "C" Q_DECL_EXPORT
QWaylandInputMethodControlPrivate *ritual_ZN26QWaylandInputMethodControl6d_funcEv(
    QWaylandInputMethodControl *self) {
  return self->d_func();
}

//  const QWaylandInputMethodControlPrivate
//      *QWaylandInputMethodControl::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandInputMethodControlPrivate *ritual_ZNK26QWaylandInputMethodControl6d_funcEv(
    const QWaylandInputMethodControl *self) {
  return self->d_func();
}

//  bool QWaylandInputMethodControl::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWaylandInputMethodControl7enabledEv(
    const QWaylandInputMethodControl *self) {
  return self->enabled();
}

#endif  // QT_CONFIG(im)
