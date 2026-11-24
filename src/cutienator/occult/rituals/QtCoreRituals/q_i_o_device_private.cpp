//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qiodevice_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qiodevice.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QIODevicePrivate that Python can take functions over in. Every QIODevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQIODevicePrivateCall0)(const void *, char, int *);
typedef const QByteArray * (*CuteQIODevicePrivateCall1)(const void *, qint64, int *);
class CuteQIODevicePrivate : public QIODevicePrivate {
public:
  using QIODevicePrivate::QIODevicePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQIODevicePrivateCall0 call = reinterpret_cast<CuteQIODevicePrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIODevicePrivateCall1 call = reinterpret_cast<CuteQIODevicePrivateCall1>(taken[1]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QIODevice *QIODevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN16QIODevicePrivate6q_funcEv(QIODevicePrivate *self) {
  return self->q_func();
}

//  const QIODevice *QIODevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QIODevice *ritual_ZNK16QIODevicePrivate6q_funcEv(
    const QIODevicePrivate *self) {
  return self->q_func();
}

//  QIODevicePrivate::QIODevicePrivate(decltype(QObjectPrivateVersion)
//      version)
extern "C" Q_DECL_EXPORT
QIODevicePrivate *ritual_ZN16QIODevicePrivateC1E16QtPrivate_6_12_0(
    decltype(QObjectPrivateVersion) version) {
  return new CuteQIODevicePrivate(version);
}

//  QIODevicePrivate::~QIODevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivateD1Ev(QIODevicePrivate *self) {
  delete self;
}

//  bool QIODevicePrivate::putCharHelper(char c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QIODevicePrivate13putCharHelperEc(
    QIODevicePrivate *self,
    char c) {
  return self->putCharHelper(c);
}

//  bool QIODevicePrivate::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QIODevicePrivate12isSequentialEv(
    const QIODevicePrivate *self) {
  return self->isSequential();
}

//  bool QIODevicePrivate::isBufferEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QIODevicePrivate13isBufferEmptyEv(
    const QIODevicePrivate *self) {
  return self->isBufferEmpty();
}

//  bool QIODevicePrivate::allWriteBuffersEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QIODevicePrivate20allWriteBuffersEmptyEv(
    const QIODevicePrivate *self) {
  return self->allWriteBuffersEmpty();
}

//  void QIODevicePrivate::seekBuffer(qint64 newPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate10seekBufferEx(
    QIODevicePrivate *self,
    qint64 newPos) {
  self->seekBuffer(newPos);
}

//  void QIODevicePrivate::setCurrentReadChannel(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate21setCurrentReadChannelEi(
    QIODevicePrivate *self,
    int channel) {
  self->setCurrentReadChannel(channel);
}

//  void QIODevicePrivate::setCurrentWriteChannel(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate22setCurrentWriteChannelEi(
    QIODevicePrivate *self,
    int channel) {
  self->setCurrentWriteChannel(channel);
}

//  void QIODevicePrivate::setReadChannelCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate19setReadChannelCountEi(
    QIODevicePrivate *self,
    int count) {
  self->setReadChannelCount(count);
}

//  void QIODevicePrivate::setWriteChannelCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate20setWriteChannelCountEi(
    QIODevicePrivate *self,
    int count) {
  self->setWriteChannelCount(count);
}

//  QByteArray QIODevicePrivate::peek(qint64 maxSize)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN16QIODevicePrivate4peekEx(
    QIODevicePrivate *self,
    qint64 maxSize) {
  return new QByteArray(self->peek(maxSize));
}

//  qint64 QIODevicePrivate::skipByReading(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QIODevicePrivate13skipByReadingEx(
    QIODevicePrivate *self,
    qint64 maxSize) {
  return self->skipByReading(maxSize);
}

//  qint64 QIODevicePrivate::skipLine()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QIODevicePrivate8skipLineEv(QIODevicePrivate *self) {
  return self->skipLine();
}

//  void QIODevicePrivate::write(const char *data, qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate5writeEPKcx(
    QIODevicePrivate *self,
    const char *data,
    qint64 size) {
  self->write(data, size);
}

//  bool QIODevicePrivate::isWriteChunkCached(const char *data, qint64 size)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QIODevicePrivate18isWriteChunkCachedEPKcx(
    const QIODevicePrivate *self,
    const char *data,
    qint64 size) {
  return self->isWriteChunkCached(data, size);
}

//  a Python function taken by a CuteQIODevicePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIODevicePrivate(
    QIODevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIODevicePrivate *>(self)->take(key, call);
}

//  bool QIODevicePrivate::putCharHelper(char c)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QIODevicePrivate13putCharHelperEc(
    QIODevicePrivate *self,
    char c) {
  return self->QIODevicePrivate::putCharHelper(c);
}

//  QByteArray QIODevicePrivate::peek(qint64 maxSize)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZN16QIODevicePrivate4peekEx(
    QIODevicePrivate *self,
    qint64 maxSize) {
  return new QByteArray(self->QIODevicePrivate::peek(maxSize));
}
