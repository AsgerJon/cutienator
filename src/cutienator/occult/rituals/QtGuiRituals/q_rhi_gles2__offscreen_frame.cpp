//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhigles2_p.h>
#include <QtGui/QOffscreenSurface>
#include <QtGui/QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformopenglcontext.h>
#include <QtCore/qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhigles2.cpp, line 7195, as _ZN19QGles2CommandBufferC1EP18QRhiImplementation
inline QGles2CommandBuffer::QGles2CommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
    resetState();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7201, as _ZN19QGles2CommandBufferD1Ev
inline QGles2CommandBuffer::~QGles2CommandBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7206, as _ZN19QGles2CommandBuffer7destroyEv
inline void QGles2CommandBuffer::destroy()
{
    // nothing to do here
}
//  -----------------------------------------------------------------------

//  QRhiGles2::OffscreenFrame::OffscreenFrame(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QRhiGles2::OffscreenFrame *ritual_ZN9QRhiGles214OffscreenFrameC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QRhiGles2::OffscreenFrame(rhi);
}

#endif  // QT_CONFIG(opengl)
