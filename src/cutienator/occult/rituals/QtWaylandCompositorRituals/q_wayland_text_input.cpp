//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandtextinput.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the line pulling in Qt's 'qxkbcommon_p.h',
//  copied from Qt's source and used by no code here, stands also under
//  '__has_include(<xkbcommon/xkbcommon.h>)', as that header includes
//  xkbcommon's, which a machine with Qt's kit but without the development
//  headers of xkbcommon lacks. Kept as it is when the generator runs again.
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
#if QT_CONFIG(xkbcommon) && __has_include(<xkbcommon/xkbcommon.h>)
#include <QtGui/private/qxkbcommon_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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
