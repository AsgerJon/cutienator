//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qvideowindow_p.h>
#include <QtGui/QPlatformSurfaceEvent>
#include <QtCore/qfile.h>
#include <QtGui/qpainter.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtMultimedia/private/qmemoryvideobuffer_p.h>
#include <QtMultimedia/private/qhwvideobuffer_p.h>
#include <QtMultimedia/private/qmultimediautils_p.h>
#include <QtMultimedia/private/qvideoframe_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 70, as _ZN19QVideoWindowPrivateD1Ev
inline QVideoWindowPrivate::~QVideoWindowPrivate()
{
    QObject::disconnect(m_sink.get(), &QVideoSink::videoFrameChanged,
            q, &QVideoWindow::setVideoFrame);
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 293, as _ZN19QVideoWindowPrivate15resizeSwapChainEv
inline void QVideoWindowPrivate::resizeSwapChain()
{
    m_hasSwapChain = m_swapChain->createOrResize();
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 298, as _ZN19QVideoWindowPrivate16releaseSwapChainEv
inline void QVideoWindowPrivate::releaseSwapChain()
{
    if (m_hasSwapChain) {
        m_hasSwapChain = false;
        m_swapChain->destroy();
    }
}
//  -----------------------------------------------------------------------

//  QVideoWindowPrivate::~QVideoWindowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivateD1Ev(QVideoWindowPrivate *self) {
  delete self;
}

//  bool QVideoWindowPrivate::canRender() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QVideoWindowPrivate9canRenderEv(
    const QVideoWindowPrivate *self) {
  return self->canRender();
}

//  QRhi *QVideoWindowPrivate::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK19QVideoWindowPrivate3rhiEv(
    const QVideoWindowPrivate *self) {
  return self->rhi();
}

//  void QVideoWindowPrivate::resizeSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate15resizeSwapChainEv(
    QVideoWindowPrivate *self) {
  self->resizeSwapChain();
}

//  void QVideoWindowPrivate::releaseSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate16releaseSwapChainEv(
    QVideoWindowPrivate *self) {
  self->releaseSwapChain();
}
