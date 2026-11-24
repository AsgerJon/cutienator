//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/private/qopenglgradientcache_p.h>
#include <QtOpenGL/private/qopengltexturecache_p.h>
#include <QtOpenGL/private/qopenglpaintengine_p.h>
#include <QtOpenGL/private/qopenglpaintdevice_p.h>
#include <string.h> //for memcpy
#include <QtCore/qmath.h>
#include <QtGui/private/qopengl_p.h>
#include <QtGui/private/qopenglcontext_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qpaintengineex_p.h>
#include <QtGui/QPaintEngine>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/private/qdatabuffer_p.h>
#include <QtGui/private/qstatictext_p.h>
#include <QtGui/private/qtriangulator_p.h>
#include <QtOpenGL/private/qopenglengineshadermanager_p.h>
#include <QtOpenGL/private/qopengl2pexvertexarray_p.h>
#include <QtOpenGL/private/qopengltextureglyphcache_p.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopenglpaintengine.cpp, line 2693, as _ZN24QOpenGL2PaintEngineStateC1ERKS_
inline QOpenGL2PaintEngineState::QOpenGL2PaintEngineState(const QOpenGL2PaintEngineState &other)
    : QPainterState(other)
{
    isNew = true;
    needsClipBufferClear = other.needsClipBufferClear;
    clipTestEnabled = other.clipTestEnabled;
    currentClip = other.currentClip;
    canRestoreClip = other.canRestoreClip;
    rectangleClip = other.rectangleClip;
}

//  from src/opengl/qopenglpaintengine.cpp, line 2704, as _ZN24QOpenGL2PaintEngineStateC1Ev
inline QOpenGL2PaintEngineState::QOpenGL2PaintEngineState()
{
    isNew = true;
    needsClipBufferClear = true;
    clipTestEnabled = false;
    canRestoreClip = true;
}

//  from src/opengl/qopenglpaintengine.cpp, line 2712, as _ZN24QOpenGL2PaintEngineStateD1Ev
inline QOpenGL2PaintEngineState::~QOpenGL2PaintEngineState()
{
}
//  -----------------------------------------------------------------------

//  QOpenGL2PaintEngineState::QOpenGL2PaintEngineState(const
//      QOpenGL2PaintEngineState &other)
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineState *ritual_ZN24QOpenGL2PaintEngineStateC1ERKS_(
    const QOpenGL2PaintEngineState *other) {
  return new QOpenGL2PaintEngineState(*other);
}

//  QOpenGL2PaintEngineState::QOpenGL2PaintEngineState()
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineState *ritual_ZN24QOpenGL2PaintEngineStateC1Ev() {
  return new QOpenGL2PaintEngineState();
}

//  QOpenGL2PaintEngineState::~QOpenGL2PaintEngineState()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGL2PaintEngineStateD1Ev(
    QOpenGL2PaintEngineState *self) {
  delete self;
}
