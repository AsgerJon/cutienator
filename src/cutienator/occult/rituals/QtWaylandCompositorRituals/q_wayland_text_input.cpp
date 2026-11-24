//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandtextinput.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandtextinput.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/qwaylandtextinput.h>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#include <QtGui/QGuiApplication>
#include <QtGui/QInputMethodEvent>
#if QT_CONFIG(xkbcommon)
#include <QtGui/private/qxkbcommon_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/extensions/qwaylandtextinput.cpp, line 518, as _ZN17QWaylandTextInputD1Ev
inline QWaylandTextInput::~QWaylandTextInput()
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWaylandTextInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QWaylandTextInput10metaObjectEv(
    const QWaylandTextInput *self) {
  return self->metaObject();
}

//  QWaylandTextInput::~QWaylandTextInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandTextInputD1Ev(QWaylandTextInput *self) {
  delete self;
}
