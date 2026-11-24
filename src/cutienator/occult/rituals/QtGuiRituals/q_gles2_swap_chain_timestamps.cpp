//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhigles2_p.h"
#include <QOffscreenSurface>
#include <QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <qpa/qplatformopenglcontext.h>
#include <qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhigles2.cpp, line 7326, as _ZN25QGles2SwapChainTimestamps7prepareEP9QRhiGles2
inline void QGles2SwapChainTimestamps::prepare(QRhiGles2 *rhiD)
{
    if (!query[0])
        rhiD->f->glGenQueries(TIMESTAMP_PAIRS * 2, query);
}

//  from src/gui/rhi/qrhigles2.cpp, line 7332, as _ZN25QGles2SwapChainTimestamps7destroyEP9QRhiGles2
inline void QGles2SwapChainTimestamps::destroy(QRhiGles2 *rhiD)
{
    rhiD->f->glDeleteQueries(TIMESTAMP_PAIRS * 2, query);
    memset(active, 0, sizeof(active));
    memset(query, 0, sizeof(query));
}

//  from src/gui/rhi/qrhigles2.cpp, line 7339, as _ZN25QGles2SwapChainTimestamps18tryQueryTimestampsEiP9QRhiGles2Pd
inline bool QGles2SwapChainTimestamps::tryQueryTimestamps(int pairIndex, QRhiGles2 *rhiD, double *elapsedSec)
{
    if (!active[pairIndex])
        return false;

    GLuint tsStart = query[pairIndex * 2];
    GLuint tsEnd = query[pairIndex * 2 + 1];

    GLuint ready = GL_FALSE;
    rhiD->f->glGetQueryObjectuiv(tsEnd, GL_QUERY_RESULT_AVAILABLE, &ready);

    if (!ready)
        return false;

    bool result = false;
    quint64 timestamps[2];
    rhiD->glGetQueryObjectui64v(tsStart, GL_QUERY_RESULT, &timestamps[0]);
    rhiD->glGetQueryObjectui64v(tsEnd, GL_QUERY_RESULT, &timestamps[1]);

    if (timestamps[1] >= timestamps[0]) {
        const quint64 nanoseconds = timestamps[1] - timestamps[0];
        *elapsedSec = nanoseconds / 1000000000.0;
        result = true;
    }

    active[pairIndex] = false;
    return result;
}
//  -----------------------------------------------------------------------

//  void QGles2SwapChainTimestamps::prepare(QRhiGles2 *rhiD)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGles2SwapChainTimestamps7prepareEP9QRhiGles2(
    QGles2SwapChainTimestamps *self,
    QRhiGles2 *rhiD) {
  self->prepare(rhiD);
}

//  void QGles2SwapChainTimestamps::destroy(QRhiGles2 *rhiD)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGles2SwapChainTimestamps7destroyEP9QRhiGles2(
    QGles2SwapChainTimestamps *self,
    QRhiGles2 *rhiD) {
  self->destroy(rhiD);
}

//  bool QGles2SwapChainTimestamps::tryQueryTimestamps(int pairIndex,
//      QRhiGles2 *rhiD, double *elapsedSec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QGles2SwapChainTimestamps18tryQueryTimestampsEiP9QRhiGles2Pd(
    QGles2SwapChainTimestamps *self,
    int pairIndex,
    QRhiGles2 *rhiD,
    double *elapsedSec) {
  return self->tryQueryTimestamps(pairIndex, rhiD, elapsedSec);
}

//  QGles2SwapChainTimestamps::~QGles2SwapChainTimestamps()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGles2SwapChainTimestampsD1Ev(
    QGles2SwapChainTimestamps *self) {
  delete self;
}
