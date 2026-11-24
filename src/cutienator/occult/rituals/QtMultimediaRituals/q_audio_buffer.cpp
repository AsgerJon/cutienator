//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiobuffer.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qaudiobuffer.h>
#include <QtCore/qbytearray.h>
#include <QtMultimedia/qaudioformat.h>

//  QAudioBuffer::QAudioBuffer()
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN12QAudioBufferC1Ev() {
  return new QAudioBuffer();
}

//  QAudioBuffer::QAudioBuffer(const QAudioBuffer &other)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN12QAudioBufferC1ERKS_(const QAudioBuffer *other) {
  return new QAudioBuffer(*other);
}

//  QAudioBuffer::QAudioBuffer(const QByteArray &data, const QAudioFormat
//      &format, qint64 startTime)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN12QAudioBufferC1ERK10QByteArrayRK12QAudioFormatx(
    const QByteArray *data,
    const QAudioFormat *format,
    qint64 startTime) {
  return new QAudioBuffer(*data, *format, startTime);
}

//  QAudioBuffer::QAudioBuffer(int numFrames, const QAudioFormat &format,
//      qint64 startTime)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN12QAudioBufferC1EiRK12QAudioFormatx(
    int numFrames,
    const QAudioFormat *format,
    qint64 startTime) {
  return new QAudioBuffer(numFrames, *format, startTime);
}

//  QAudioBuffer::~QAudioBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioBufferD1Ev(QAudioBuffer *self) {
  delete self;
}

//  bool QAudioBuffer::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioBuffer7isValidEv(const QAudioBuffer *self) {
  return self->isValid();
}

//  void QAudioBuffer::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioBuffer6detachEv(QAudioBuffer *self) {
  self->detach();
}

//  QAudioFormat QAudioBuffer::format() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK12QAudioBuffer6formatEv(const QAudioBuffer *self) {
  return new QAudioFormat(self->format());
}

//  qsizetype QAudioBuffer::frameCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioBuffer10frameCountEv(const QAudioBuffer *self) {
  return self->frameCount();
}

//  qsizetype QAudioBuffer::sampleCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioBuffer11sampleCountEv(const QAudioBuffer *self) {
  return self->sampleCount();
}

//  qsizetype QAudioBuffer::byteCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioBuffer9byteCountEv(const QAudioBuffer *self) {
  return self->byteCount();
}

//  qint64 QAudioBuffer::duration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QAudioBuffer8durationEv(const QAudioBuffer *self) {
  return self->duration();
}

//  qint64 QAudioBuffer::startTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QAudioBuffer9startTimeEv(const QAudioBuffer *self) {
  return self->startTime();
}
