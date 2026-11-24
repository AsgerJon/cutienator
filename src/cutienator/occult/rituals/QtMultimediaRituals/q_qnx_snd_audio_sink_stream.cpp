//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiosink_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(qnx_io_snd)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiosink_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qqnxsndaudiosink_p.h>
#include <QtMultimedia/private/qqnxsndhelpers_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qthread.h>
#include <QtCore/QLoggingCategory>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosink.cpp, line 188, as _ZN22QQnxSndAudioSinkStream16updateStreamIdleEb
inline void QQnxSndAudioSinkStream::updateStreamIdle(bool streamIsIdle)
{
    // Read once into a local: the app thread may null m_parent between the
    // check and the call. The front class joins the worker before clearing
    // m_parent, so a non-null read here is guaranteed to point at a live
    // object for the duration of this call.
    if (auto *parent = m_parent.load(std::memory_order_acquire))
        parent->updateStreamIdle(streamIsIdle);
}
//  -----------------------------------------------------------------------

//  void QQnxSndAudioSinkStream::updateStreamIdle(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQnxSndAudioSinkStream16updateStreamIdleEb(
    QQnxSndAudioSinkStream *self,
    bool a0) {
  self->updateStreamIdle(a0);
}

//  QQnxSndAudioSinkStream as the
//      QtMultimediaPrivate::QPlatformAudioSinkStream it is built on
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QPlatformAudioSinkStream *ritual_cast_QQnxSndAudioSinkStream_QtMultimediaPrivate_QPlatformAudioSinkStream(
    QQnxSndAudioSinkStream *self) {
  return static_cast<QtMultimediaPrivate::QPlatformAudioSinkStream *>(self);
}

#endif  // QT_CONFIG(qnx_io_snd)
