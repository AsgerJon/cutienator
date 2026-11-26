//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qringbuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qringbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QRingBuffer::QRingBuffer(int growth)
extern "C" Q_DECL_EXPORT
QRingBuffer *ritual_ZN11QRingBufferC1Ei(int growth) {
  return new QRingBuffer(growth);
}

//  QRingBuffer::QRingBuffer(QRingBuffer &&a0)
extern "C" Q_DECL_EXPORT
QRingBuffer *ritual_ZN11QRingBufferC1EOS_(QRingBuffer *a0) {
  return new QRingBuffer(std::move(*a0));
}

//  QRingBuffer &QRingBuffer::operator=(QRingBuffer &&a0)
extern "C" Q_DECL_EXPORT
QRingBuffer *ritual_ZN11QRingBufferaSEOS_(
    QRingBuffer *self,
    QRingBuffer *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  void QRingBuffer::setChunkSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer12setChunkSizeEi(QRingBuffer *self, int size) {
  self->setChunkSize(size);
}

//  int QRingBuffer::chunkSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRingBuffer9chunkSizeEv(const QRingBuffer *self) {
  return self->chunkSize();
}

//  qint64 QRingBuffer::nextDataBlockSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QRingBuffer17nextDataBlockSizeEv(
    const QRingBuffer *self) {
  return self->nextDataBlockSize();
}

//  const char *QRingBuffer::readPointer() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK11QRingBuffer11readPointerEv(const QRingBuffer *self) {
  return self->readPointer();
}

//  const char *QRingBuffer::readPointerAtPosition(qint64 pos, qint64
//      &length) const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK11QRingBuffer21readPointerAtPositionExRx(
    const QRingBuffer *self,
    qint64 pos,
    qint64 *length) {
  return self->readPointerAtPosition(pos, *length);
}

//  void QRingBuffer::free(qint64 bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer4freeEx(QRingBuffer *self, qint64 bytes) {
  self->free(bytes);
}

//  char *QRingBuffer::reserve(qint64 bytes)
extern "C" Q_DECL_EXPORT
char *ritual_ZN11QRingBuffer7reserveEx(QRingBuffer *self, qint64 bytes) {
  return self->reserve(bytes);
}

//  char *QRingBuffer::reserveFront(qint64 bytes)
extern "C" Q_DECL_EXPORT
char *ritual_ZN11QRingBuffer12reserveFrontEx(
    QRingBuffer *self,
    qint64 bytes) {
  return self->reserveFront(bytes);
}

//  void QRingBuffer::truncate(qint64 pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer8truncateEx(QRingBuffer *self, qint64 pos) {
  self->truncate(pos);
}

//  void QRingBuffer::chop(qint64 bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer4chopEx(QRingBuffer *self, qint64 bytes) {
  self->chop(bytes);
}

//  bool QRingBuffer::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRingBuffer7isEmptyEv(const QRingBuffer *self) {
  return self->isEmpty();
}

//  int QRingBuffer::getChar()
extern "C" Q_DECL_EXPORT
int ritual_ZN11QRingBuffer7getCharEv(QRingBuffer *self) {
  return self->getChar();
}

//  void QRingBuffer::putChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer7putCharEc(QRingBuffer *self, char c) {
  self->putChar(c);
}

//  void QRingBuffer::ungetChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer9ungetCharEc(QRingBuffer *self, char c) {
  self->ungetChar(c);
}

//  qint64 QRingBuffer::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QRingBuffer4sizeEv(const QRingBuffer *self) {
  return self->size();
}

//  void QRingBuffer::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer5clearEv(QRingBuffer *self) {
  self->clear();
}

//  qint64 QRingBuffer::indexOf(char c) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QRingBuffer7indexOfEc(const QRingBuffer *self, char c) {
  return self->indexOf(c);
}

//  qint64 QRingBuffer::indexOf(char c, qint64 maxLength, qint64 pos) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QRingBuffer7indexOfEcxx(
    const QRingBuffer *self,
    char c,
    qint64 maxLength,
    qint64 pos) {
  return self->indexOf(c, maxLength, pos);
}

//  qint64 QRingBuffer::read(char *data, qint64 maxLength)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QRingBuffer4readEPcx(
    QRingBuffer *self,
    char *data,
    qint64 maxLength) {
  return self->read(data, maxLength);
}

//  QByteArray QRingBuffer::read()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QRingBuffer4readEv(QRingBuffer *self) {
  return new QByteArray(self->read());
}

//  qint64 QRingBuffer::peek(char *data, qint64 maxLength, qint64 pos) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QRingBuffer4peekEPcxx(
    const QRingBuffer *self,
    char *data,
    qint64 maxLength,
    qint64 pos) {
  return self->peek(data, maxLength, pos);
}

//  void QRingBuffer::append(const char *data, qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer6appendEPKcx(
    QRingBuffer *self,
    const char *data,
    qint64 size) {
  self->append(data, size);
}

//  void QRingBuffer::append(const QByteArray &qba)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer6appendERK10QByteArray(
    QRingBuffer *self,
    const QByteArray *qba) {
  self->append(*qba);
}

//  void QRingBuffer::append(QByteArray &&qba)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRingBuffer6appendEO10QByteArray(
    QRingBuffer *self,
    QByteArray *qba) {
  self->append(std::move(*qba));
}

//  qint64 QRingBuffer::skip(qint64 length)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QRingBuffer4skipEx(QRingBuffer *self, qint64 length) {
  return self->skip(length);
}

//  qint64 QRingBuffer::readLineWithoutTerminatingNull(char *data, qint64
//      maxLength)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QRingBuffer30readLineWithoutTerminatingNullEPcx(
    QRingBuffer *self,
    char *data,
    qint64 maxLength) {
  return self->readLineWithoutTerminatingNull(data, maxLength);
}

//  qint64 QRingBuffer::readLine(char *data, qint64 maxLength)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QRingBuffer8readLineEPcx(
    QRingBuffer *self,
    char *data,
    qint64 maxLength) {
  return self->readLine(data, maxLength);
}

//  bool QRingBuffer::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRingBuffer11canReadLineEv(const QRingBuffer *self) {
  return self->canReadLine();
}
