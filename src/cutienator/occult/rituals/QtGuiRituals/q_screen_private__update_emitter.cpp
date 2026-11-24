//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qscreen_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qscreen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qscreen.h"
#include "qscreen_p.h"
#include "qpixmap.h"
#include "qguiapplication_p.h"
#include <qpa/qplatformscreen.h>
#include <qpa/qplatformscreen_p.h>
#include <QtCore/QDebug>
#include <QtCore/private/qobject_p.h>
#include "qhighdpiscaling_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/kernel/qscreen.cpp, line 813, as _ZN14QScreenPrivate13UpdateEmitterC1EP7QScreen
inline QScreenPrivate::UpdateEmitter::UpdateEmitter(QScreen *screen)
{
    initialState.platformScreen = screen->handle();

    // Use public APIs to read out current state, rather
    // than accessing the QScreenPrivate members, so that
    // we detect any changes to the high-DPI scale factors
    // that may be applied in the getters.

    initialState.logicalDpi = QDpi{
        screen->logicalDotsPerInchX(),
        screen->logicalDotsPerInchY()
    };
    initialState.geometry = screen->geometry();
    initialState.availableGeometry = screen->availableGeometry();
    initialState.primaryOrientation = screen->primaryOrientation();
}

//  from src/gui/kernel/qscreen.cpp, line 831, as _ZN14QScreenPrivate13UpdateEmitterD1Ev
inline QScreenPrivate::UpdateEmitter::~UpdateEmitter()
{
    QScreen *screen = initialState.platformScreen->screen();

    const auto logicalDotsPerInch = QDpi{
        screen->logicalDotsPerInchX(),
        screen->logicalDotsPerInchY()
    };
    if (logicalDotsPerInch != initialState.logicalDpi)
        emit screen->logicalDotsPerInchChanged(screen->logicalDotsPerInch());

    const auto geometry = screen->geometry();
    const auto geometryChanged = geometry != initialState.geometry;
    if (geometryChanged)
        emit screen->geometryChanged(geometry);

    const auto availableGeometry = screen->availableGeometry();
    const auto availableGeometryChanged = availableGeometry != initialState.availableGeometry;
    if (availableGeometryChanged)
        emit screen->availableGeometryChanged(availableGeometry);

    if (geometryChanged || availableGeometryChanged) {
        const auto siblings = screen->virtualSiblings();
        for (QScreen* sibling : siblings)
            emit sibling->virtualGeometryChanged(sibling->virtualGeometry());
    }

    if (geometryChanged) {
        emit screen->physicalDotsPerInchChanged(screen->physicalDotsPerInch());

        const auto primaryOrientation = screen->primaryOrientation();
        if (primaryOrientation != initialState.primaryOrientation)
            emit screen->primaryOrientationChanged(primaryOrientation);
    }
}
//  -----------------------------------------------------------------------

//  QScreenPrivate::UpdateEmitter::UpdateEmitter(QScreen *screen)
extern "C" Q_DECL_EXPORT
QScreenPrivate::UpdateEmitter *ritual_ZN14QScreenPrivate13UpdateEmitterC1EP7QScreen(
    QScreen *screen) {
  return new QScreenPrivate::UpdateEmitter(screen);
}

//  QScreenPrivate::UpdateEmitter::~UpdateEmitter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenPrivate13UpdateEmitterD1Ev(
    QScreenPrivate::UpdateEmitter *self) {
  delete self;
}
