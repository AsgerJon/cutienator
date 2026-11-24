//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandqttextinputmethod.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandqttextinputmethod.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qwaylandqttextinputmethod.h"
#include <QtGui/qevent.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/qcolor.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qelapsedtimer.h>
#include <QtWaylandCompositor/qwaylandcompositor.h>
#include <QtWaylandCompositor/qwaylandsurface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/extensions/qwaylandqttextinputmethod.cpp, line 167, as _ZN25QWaylandQtTextInputMethodD1Ev
inline QWaylandQtTextInputMethod::~QWaylandQtTextInputMethod()
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWaylandQtTextInputMethod::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QWaylandQtTextInputMethod10metaObjectEv(
    const QWaylandQtTextInputMethod *self) {
  return self->metaObject();
}

//  QWaylandQtTextInputMethod::~QWaylandQtTextInputMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWaylandQtTextInputMethodD1Ev(
    QWaylandQtTextInputMethod *self) {
  delete self;
}
