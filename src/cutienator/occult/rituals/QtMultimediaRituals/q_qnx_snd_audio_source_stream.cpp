//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiosource_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(qnx_io_snd)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qqnxsndaudiosource_p.h>
#include <QtMultimedia/private/qqnxsndhelpers_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qthread.h>
#include <QtCore/QLoggingCategory>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/qnx-iosnd/qqnxsndaudiosource.cpp, line 154, as _ZN24QQnxSndAudioSourceStream16updateStreamIdleEb
inline void QQnxSndAudioSourceStream::updateStreamIdle(bool streamIsIdle)
{
    // See QQnxSndAudioSinkStream::updateStreamIdle — read once into a local
    // to avoid a TOCTOU with stop() nulling m_parent.
    if (auto *parent = m_parent.load(std::memory_order_acquire))
        parent->updateStreamIdle(streamIsIdle);
}
//  -----------------------------------------------------------------------

//  void QQnxSndAudioSourceStream::updateStreamIdle(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQnxSndAudioSourceStream16updateStreamIdleEb(
    QQnxSndAudioSourceStream *self,
    bool a0) {
  self->updateStreamIdle(a0);
}

//  QQnxSndAudioSourceStream as the
//      QtMultimediaPrivate::QPlatformAudioSourceStream it is built on
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QPlatformAudioSourceStream *ritual_cast_QQnxSndAudioSourceStream_QtMultimediaPrivate_QPlatformAudioSourceStream(
    QQnxSndAudioSourceStream *self) {
  return static_cast<QtMultimediaPrivate::QPlatformAudioSourceStream *>(self);
}

#endif  // QT_CONFIG(qnx_io_snd)
