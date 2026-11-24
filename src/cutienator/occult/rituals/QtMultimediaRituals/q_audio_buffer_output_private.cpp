//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiobufferoutput_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiobufferoutput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudioformat.h>

//  QAudioBufferOutputPrivate::QAudioBufferOutputPrivate(const QAudioFormat
//      &format)
extern "C" Q_DECL_EXPORT
QAudioBufferOutputPrivate *ritual_ZN25QAudioBufferOutputPrivateC1ERK12QAudioFormat(
    const QAudioFormat *format) {
  return new QAudioBufferOutputPrivate(*format);
}
