//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiobuffer.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, instances of templates of the class: 8. Kept as it is when
//  the generator runs again.
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

//  QAudioBuffer &QAudioBuffer::operator=(const QAudioBuffer &other)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN12QAudioBufferaSERKS_(
    QAudioBuffer *self,
    const QAudioBuffer *other) {
  return &(self->operator=(*other));
}

//  QAudioBuffer::QAudioBuffer(QAudioBuffer &&other)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN12QAudioBufferC1EOS_(QAudioBuffer *other) {
  return new QAudioBuffer(std::move(*other));
}

//  QAudioBuffer &QAudioBuffer::operator=(QAudioBuffer &&other)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN12QAudioBufferaSEOS_(
    QAudioBuffer *self,
    QAudioBuffer *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QAudioBuffer::swap(QAudioBuffer &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioBuffer4swapERS_(
    QAudioBuffer *self,
    QAudioBuffer *other) {
  self->swap(*other);
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

//  const void *QAudioBuffer::constData() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK12QAudioBuffer9constDataEv(const QAudioBuffer *self) {
  return self->constData();
}

//  const void *QAudioBuffer::data() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK12QAudioBuffer4dataEv(const QAudioBuffer *self) {
  return self->data();
}

//  void *QAudioBuffer::data()
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QAudioBuffer4dataEv(QAudioBuffer *self) {
  return self->data();
}

//  const T *QAudioBuffer::constData<unsigned char>() const
extern "C" Q_DECL_EXPORT
const unsigned char * ritual_ZNK12QAudioBuffer9constDataIhEEPKT_v(const QAudioBuffer *self) {
  return self->constData<unsigned char>();
}

//  const T *QAudioBuffer::constData<short>() const
extern "C" Q_DECL_EXPORT
const short * ritual_ZNK12QAudioBuffer9constDataIsEEPKT_v(const QAudioBuffer *self) {
  return self->constData<short>();
}

//  const T *QAudioBuffer::constData<int>() const
extern "C" Q_DECL_EXPORT
const int * ritual_ZNK12QAudioBuffer9constDataIiEEPKT_v(const QAudioBuffer *self) {
  return self->constData<int>();
}

//  const T *QAudioBuffer::constData<float>() const
extern "C" Q_DECL_EXPORT
const float * ritual_ZNK12QAudioBuffer9constDataIfEEPKT_v(const QAudioBuffer *self) {
  return self->constData<float>();
}

//  T *QAudioBuffer::data<unsigned char>()
extern "C" Q_DECL_EXPORT
unsigned char * ritual_ZN12QAudioBuffer4dataIhEEPT_v(QAudioBuffer *self) {
  return self->data<unsigned char>();
}

//  T *QAudioBuffer::data<short>()
extern "C" Q_DECL_EXPORT
short * ritual_ZN12QAudioBuffer4dataIsEEPT_v(QAudioBuffer *self) {
  return self->data<short>();
}

//  T *QAudioBuffer::data<int>()
extern "C" Q_DECL_EXPORT
int * ritual_ZN12QAudioBuffer4dataIiEEPT_v(QAudioBuffer *self) {
  return self->data<int>();
}

//  T *QAudioBuffer::data<float>()
extern "C" Q_DECL_EXPORT
float * ritual_ZN12QAudioBuffer4dataIfEEPT_v(QAudioBuffer *self) {
  return self->data<float>();
}
