//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qdrawavaudiodecoder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qdrawavaudiodecoder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiobuffer.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdrawavaudiodecoder_p.h"
#include <QtMultimedia/qaudiodecoder.h>
#include <QtMultimedia/qaudiobuffer.h>
#include <QtCore/qdebug.h>
#include <QtCore/qeventloop.h>
#include <QtCore/qfile.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qthreadpool.h>
#if QT_CONFIG(network)
#  include <QtNetwork/qnetworkaccessmanager.h>
#  include <QtNetwork/qnetworkreply.h>
#  include <QtNetwork/qnetworkrequest.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/audio/qdrawavaudiodecoder.cpp, line 197, as _ZN18QDrWavAudioDecoder14setAudioFormatERK12QAudioFormat
inline void QDrWavAudioDecoder::setAudioFormat(const QAudioFormat &format)
{
    if (isDecoding())
        return;
    m_audioFormat = format;
}

//  from ../qtmultimedia/src/multimedia/audio/qdrawavaudiodecoder.cpp, line 250, as _ZN18QDrWavAudioDecoder4readEv
inline QAudioBuffer QDrWavAudioDecoder::read()
{
    if (m_buffer.isValid()) {
        QAudioBuffer buffer = std::exchange(m_buffer, QAudioBuffer());
        positionChanged(duration());
        bufferAvailableChanged(false);
        return buffer;
    }
    return QAudioBuffer();
}
//  -----------------------------------------------------------------------

//  QUrl QDrWavAudioDecoder::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QDrWavAudioDecoder6sourceEv(
    const QDrWavAudioDecoder *self) {
  return new QUrl(self->source());
}

//  QIODevice *QDrWavAudioDecoder::sourceDevice() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK18QDrWavAudioDecoder12sourceDeviceEv(
    const QDrWavAudioDecoder *self) {
  return self->sourceDevice();
}

//  QAudioFormat QDrWavAudioDecoder::audioFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK18QDrWavAudioDecoder11audioFormatEv(
    const QDrWavAudioDecoder *self) {
  return new QAudioFormat(self->audioFormat());
}

//  void QDrWavAudioDecoder::setAudioFormat(const QAudioFormat &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDrWavAudioDecoder14setAudioFormatERK12QAudioFormat(
    QDrWavAudioDecoder *self,
    const QAudioFormat *a0) {
  self->setAudioFormat(*a0);
}

//  QAudioBuffer QDrWavAudioDecoder::read()
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN18QDrWavAudioDecoder4readEv(
    QDrWavAudioDecoder *self) {
  return new QAudioBuffer(self->read());
}

//  bool QDrWavAudioDecoder::canReadQrc() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDrWavAudioDecoder10canReadQrcEv(
    const QDrWavAudioDecoder *self) {
  return self->canReadQrc();
}
