//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrendercapture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrendercapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qrendercapture.h>
#include <Qt3DRender/private/qrendercapture_p.h>
#include <QtCore/QPointer>
#include <QtCore/QMutexLocker>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/qrendercapture.cpp, line 117, as _ZN10Qt3DRender26QRenderCaptureReplyPrivateC1Ev
namespace Qt3DRender {
inline QRenderCaptureReplyPrivate::QRenderCaptureReplyPrivate()
    : QObjectPrivate()
    , m_captureId(0)
    , m_complete(false)
{

}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  Qt3DRender::QRenderCaptureReplyPrivate::QRenderCaptureReplyPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReplyPrivate *ritual_ZN10Qt3DRender26QRenderCaptureReplyPrivateC1Ev() {
  return new Qt3DRender::QRenderCaptureReplyPrivate();
}

//  QRenderCaptureReply *Qt3DRender::QRenderCaptureReplyPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReply *ritual_ZN10Qt3DRender26QRenderCaptureReplyPrivate6q_funcEv(
    Qt3DRender::QRenderCaptureReplyPrivate *self) {
  return self->q_func();
}

//  const QRenderCaptureReply
//      *Qt3DRender::QRenderCaptureReplyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderCaptureReply *ritual_ZNK10Qt3DRender26QRenderCaptureReplyPrivate6q_funcEv(
    const Qt3DRender::QRenderCaptureReplyPrivate *self) {
  return self->q_func();
}
