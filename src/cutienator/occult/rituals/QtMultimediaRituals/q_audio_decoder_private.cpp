//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiodecoder_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/qaudiodecoder.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiodecoder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAudioDecoder *QAudioDecoderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAudioDecoder *ritual_ZN20QAudioDecoderPrivate6q_funcEv(
    QAudioDecoderPrivate *self) {
  return self->q_func();
}

//  const QAudioDecoder *QAudioDecoderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAudioDecoder *ritual_ZNK20QAudioDecoderPrivate6q_funcEv(
    const QAudioDecoderPrivate *self) {
  return self->q_func();
}

//  QAudioDecoderPrivate::~QAudioDecoderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAudioDecoderPrivateD1Ev(QAudioDecoderPrivate *self) {
  delete self;
}
