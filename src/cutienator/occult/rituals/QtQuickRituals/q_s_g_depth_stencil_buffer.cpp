//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultrendercontext_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultrendercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtQuick/private/qsgcurveglyphatlas_p.h>
#include <QtGui/QGuiApplication>
#include <QtQuick/private/qsgbatchrenderer_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgrhiatlastexture_p.h>
#include <QtQuick/private/qsgrhidistancefieldglyphcache_p.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#include <QtQuick/private/qsgcompressedtexture_p.h>
#include <QtQuick/qsgrendererinterface.h>
#include <QtQuick/qquickgraphicsconfiguration.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultrendercontext.cpp, line 404, as _ZN21QSGDepthStencilBufferD1Ev
inline QSGDepthStencilBuffer::~QSGDepthStencilBuffer()
{
    if (rc && ds) {
        const auto key = std::pair(ds->pixelSize(), ds->sampleCount());
        rc->m_depthStencilBuffers.remove(key);
    }
    delete ds;
}
//  -----------------------------------------------------------------------

//  QSGDepthStencilBuffer::QSGDepthStencilBuffer()
extern "C" Q_DECL_EXPORT
QSGDepthStencilBuffer *ritual_ZN21QSGDepthStencilBufferC1Ev() {
  return new QSGDepthStencilBuffer();
}

//  QSGDepthStencilBuffer::QSGDepthStencilBuffer(QRhiRenderBuffer *ds)
extern "C" Q_DECL_EXPORT
QSGDepthStencilBuffer *ritual_ZN21QSGDepthStencilBufferC1EP16QRhiRenderBuffer(
    QRhiRenderBuffer *ds) {
  return new QSGDepthStencilBuffer(ds);
}

//  QSGDepthStencilBuffer::~QSGDepthStencilBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDepthStencilBufferD1Ev(QSGDepthStencilBuffer *self) {
  delete self;
}
