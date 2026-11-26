//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsamplecache_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the constructor 'QSample()' is taken
//  out, with its row. Qt declares it, private, and defines it nowhere,
//  so the library offers no such function and linking refused it.
//  Kept as it is when the generator runs again.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsamplecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qurl.h>

//  QSample::~QSample()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSampleD1Ev(QSample *self) {
  delete self;
}

//  State QSample::state() const
extern "C" Q_DECL_EXPORT
QSample::State ritual_ZNK7QSample5stateEv(const QSample *self) {
  return self->state();
}

//  const QByteArray &QSample::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QSample4dataEv(const QSample *self) {
  return new QByteArray(self->data());
}

//  const QAudioFormat &QSample::format() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK7QSample6formatEv(const QSample *self) {
  return new QAudioFormat(self->format());
}

//  qsizetype QSample::frameCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QSample10frameCountEv(const QSample *self) {
  return self->frameCount();
}

//  void QSample::setError()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSample8setErrorEv(QSample *self) {
  self->setError();
}

//  void QSample::setData(QByteArray a0, QAudioFormat a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSample7setDataE10QByteArray12QAudioFormat(
    QSample *self,
    const QByteArray *a0,
    const QAudioFormat *a1) {
  self->setData(*a0, *a1);
}

//  QSample::QSample(QUrl url, QSampleCache *parent)
extern "C" Q_DECL_EXPORT
QSample *ritual_ZN7QSampleC1E4QUrlP12QSampleCache(
    const QUrl *url,
    QSampleCache *parent) {
  return new QSample(*url, parent);
}

//  QSample::QSample(QByteArray data, QAudioFormat format)
extern "C" Q_DECL_EXPORT
QSample *ritual_ZN7QSampleC1E10QByteArray12QAudioFormat(
    const QByteArray *data,
    const QAudioFormat *format) {
  return new QSample(*data, *format);
}

//  void QSample::clearParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSample11clearParentEv(QSample *self) {
  self->clearParent();
}
