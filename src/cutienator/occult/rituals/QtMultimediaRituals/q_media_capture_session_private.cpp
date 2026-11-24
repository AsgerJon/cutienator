//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmediacapturesession_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/qmediacapturesession.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmediacapturesession_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmediacapturesession.h"
#include "qmediacapturesession_p.h"
#include <QtMultimedia/qaudiobufferinput.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioinput.h>
#include <QtMultimedia/qaudiooutput.h>
#include <QtMultimedia/qcamera.h>
#include <QtMultimedia/qimagecapture.h>
#include <QtMultimedia/qmediarecorder.h>
#include <QtMultimedia/qscreencapture.h>
#include <QtMultimedia/qvideoframeinput.h>
#include <QtMultimedia/qvideosink.h>
#include <QtMultimedia/qwindowcapture.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtMultimedia/private/qplatformmediacapture_p.h>
#if QT_CONFIG(gstreamer_qt_api)
#  include <QtMultimedia/spi/qgstreamervideosource.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/recording/qmediacapturesession.cpp, line 27, as _ZN27QMediaCaptureSessionPrivate12setVideoSinkEP10QVideoSink
inline void QMediaCaptureSessionPrivate::setVideoSink(QVideoSink *sink)
{
    Q_Q(QMediaCaptureSession);

    if (sink == videoSink)
        return;
    if (videoSink)
        videoSink->setSource(nullptr);
    videoSink = sink;
    if (sink)
        sink->setSource(q);
    if (captureSession)
        captureSession->setVideoPreview(sink);
    emit q->videoOutputChanged();
}
//  -----------------------------------------------------------------------

//  QMediaCaptureSessionPrivate
//      *QMediaCaptureSessionPrivate::get(QMediaCaptureSession *session)
extern "C" Q_DECL_EXPORT
QMediaCaptureSessionPrivate *ritual_ZN27QMediaCaptureSessionPrivate3getEP20QMediaCaptureSession(
    QMediaCaptureSession *session) {
  return QMediaCaptureSessionPrivate::get(session);
}

//  QMediaCaptureSession *QMediaCaptureSessionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZN27QMediaCaptureSessionPrivate6q_funcEv(
    QMediaCaptureSessionPrivate *self) {
  return self->q_func();
}

//  const QMediaCaptureSession *QMediaCaptureSessionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMediaCaptureSession *ritual_ZNK27QMediaCaptureSessionPrivate6q_funcEv(
    const QMediaCaptureSessionPrivate *self) {
  return self->q_func();
}

//  void QMediaCaptureSessionPrivate::setVideoSink(QVideoSink *sink)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QMediaCaptureSessionPrivate12setVideoSinkEP10QVideoSink(
    QMediaCaptureSessionPrivate *self,
    QVideoSink *sink) {
  self->setVideoSink(sink);
}
