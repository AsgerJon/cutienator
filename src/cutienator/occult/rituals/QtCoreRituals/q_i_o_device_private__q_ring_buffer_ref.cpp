//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qiodevice_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QIODevicePrivate::QRingBufferRef::QRingBufferRef()
extern "C" Q_DECL_EXPORT
QIODevicePrivate::QRingBufferRef *ritual_ZN16QIODevicePrivate14QRingBufferRefC1Ev() {
  return new QIODevicePrivate::QRingBufferRef();
}

//  void QIODevicePrivate::QRingBufferRef::setChunkSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef12setChunkSizeEi(
    QIODevicePrivate::QRingBufferRef *self,
    int size) {
  self->setChunkSize(size);
}

//  int QIODevicePrivate::QRingBufferRef::chunkSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QIODevicePrivate14QRingBufferRef9chunkSizeEv(
    const QIODevicePrivate::QRingBufferRef *self) {
  return self->chunkSize();
}

//  qint64 QIODevicePrivate::QRingBufferRef::nextDataBlockSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QIODevicePrivate14QRingBufferRef17nextDataBlockSizeEv(
    const QIODevicePrivate::QRingBufferRef *self) {
  return self->nextDataBlockSize();
}

//  const char *QIODevicePrivate::QRingBufferRef::readPointer() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK16QIODevicePrivate14QRingBufferRef11readPointerEv(
    const QIODevicePrivate::QRingBufferRef *self) {
  return self->readPointer();
}

//  const char
//      *QIODevicePrivate::QRingBufferRef::readPointerAtPosition(qint64 pos,
//      qint64 &length) const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK16QIODevicePrivate14QRingBufferRef21readPointerAtPositionExRx(
    const QIODevicePrivate::QRingBufferRef *self,
    qint64 pos,
    qint64 *length) {
  return self->readPointerAtPosition(pos, *length);
}

//  void QIODevicePrivate::QRingBufferRef::free(qint64 bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef4freeEx(
    QIODevicePrivate::QRingBufferRef *self,
    qint64 bytes) {
  self->free(bytes);
}

//  void QIODevicePrivate::QRingBufferRef::truncate(qint64 pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef8truncateEx(
    QIODevicePrivate::QRingBufferRef *self,
    qint64 pos) {
  self->truncate(pos);
}

//  void QIODevicePrivate::QRingBufferRef::chop(qint64 bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef4chopEx(
    QIODevicePrivate::QRingBufferRef *self,
    qint64 bytes) {
  self->chop(bytes);
}

//  bool QIODevicePrivate::QRingBufferRef::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QIODevicePrivate14QRingBufferRef7isEmptyEv(
    const QIODevicePrivate::QRingBufferRef *self) {
  return self->isEmpty();
}

//  int QIODevicePrivate::QRingBufferRef::getChar()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QIODevicePrivate14QRingBufferRef7getCharEv(
    QIODevicePrivate::QRingBufferRef *self) {
  return self->getChar();
}

//  void QIODevicePrivate::QRingBufferRef::putChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef7putCharEc(
    QIODevicePrivate::QRingBufferRef *self,
    char c) {
  self->putChar(c);
}

//  void QIODevicePrivate::QRingBufferRef::ungetChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef9ungetCharEc(
    QIODevicePrivate::QRingBufferRef *self,
    char c) {
  self->ungetChar(c);
}

//  qint64 QIODevicePrivate::QRingBufferRef::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QIODevicePrivate14QRingBufferRef4sizeEv(
    const QIODevicePrivate::QRingBufferRef *self) {
  return self->size();
}

//  void QIODevicePrivate::QRingBufferRef::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef5clearEv(
    QIODevicePrivate::QRingBufferRef *self) {
  self->clear();
}

//  qint64 QIODevicePrivate::QRingBufferRef::indexOf(char c) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QIODevicePrivate14QRingBufferRef7indexOfEc(
    const QIODevicePrivate::QRingBufferRef *self,
    char c) {
  return self->indexOf(c);
}

//  qint64 QIODevicePrivate::QRingBufferRef::indexOf(char c, qint64
//      maxLength, qint64 pos) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QIODevicePrivate14QRingBufferRef7indexOfEcxx(
    const QIODevicePrivate::QRingBufferRef *self,
    char c,
    qint64 maxLength,
    qint64 pos) {
  return self->indexOf(c, maxLength, pos);
}

//  QByteArray QIODevicePrivate::QRingBufferRef::read()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN16QIODevicePrivate14QRingBufferRef4readEv(
    QIODevicePrivate::QRingBufferRef *self) {
  return new QByteArray(self->read());
}

//  void QIODevicePrivate::QRingBufferRef::append(const char *data, qint64
//      size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef6appendEPKcx(
    QIODevicePrivate::QRingBufferRef *self,
    const char *data,
    qint64 size) {
  self->append(data, size);
}

//  void QIODevicePrivate::QRingBufferRef::append(const QByteArray &qba)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRef6appendERK10QByteArray(
    QIODevicePrivate::QRingBufferRef *self,
    const QByteArray *qba) {
  self->append(*qba);
}

//  qint64 QIODevicePrivate::QRingBufferRef::skip(qint64 length)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QIODevicePrivate14QRingBufferRef4skipEx(
    QIODevicePrivate::QRingBufferRef *self,
    qint64 length) {
  return self->skip(length);
}

//  bool QIODevicePrivate::QRingBufferRef::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QIODevicePrivate14QRingBufferRef11canReadLineEv(
    const QIODevicePrivate::QRingBufferRef *self) {
  return self->canReadLine();
}

//  QIODevicePrivate::QRingBufferRef::~QRingBufferRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QIODevicePrivate14QRingBufferRefD1Ev(
    QIODevicePrivate::QRingBufferRef *self) {
  delete self;
}
