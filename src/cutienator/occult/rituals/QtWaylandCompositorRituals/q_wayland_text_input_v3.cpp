//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandtextinputv3.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the line pulling in Qt's 'qxkbcommon_p.h',
//  copied from Qt's source and used by no code here, stands also under
//  '__has_include(<xkbcommon/xkbcommon.h>)', as that header includes
//  xkbcommon's, which a machine with Qt's kit but without the development
//  headers of xkbcommon lacks. Kept as it is when the generator runs again.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandtextinputv3.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/qwaylandtextinputv3.h>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtGui/QGuiApplication>
#include <QtGui/QInputMethodEvent>
#include <QtGui/qpa/qwindowsysteminterface.h>
#if QT_CONFIG(xkbcommon) && __has_include(<xkbcommon/xkbcommon.h>)
#include <QtGui/private/qxkbcommon_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/extensions/qwaylandtextinputv3.cpp, line 433, as _ZN19QWaylandTextInputV3D1Ev
inline QWaylandTextInputV3::~QWaylandTextInputV3()
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWaylandTextInputV3::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QWaylandTextInputV310metaObjectEv(
    const QWaylandTextInputV3 *self) {
  return self->metaObject();
}

//  QWaylandTextInputV3::~QWaylandTextInputV3()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandTextInputV3D1Ev(QWaylandTextInputV3 *self) {
  delete self;
}
