//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qbytedatabuffer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qbytedatabuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>

//  void QByteDataBuffer::squeezeFirst()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QByteDataBuffer12squeezeFirstEv(QByteDataBuffer *self) {
  self->squeezeFirst();
}

//  void QByteDataBuffer::append(const QByteDataBuffer &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QByteDataBuffer6appendERKS_(
    QByteDataBuffer *self,
    const QByteDataBuffer *other) {
  self->append(*other);
}

//  void QByteDataBuffer::append(const QByteArray &bd)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QByteDataBuffer6appendERK10QByteArray(
    QByteDataBuffer *self,
    const QByteArray *bd) {
  self->append(*bd);
}

//  void QByteDataBuffer::prepend(const QByteArray &bd)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QByteDataBuffer7prependERK10QByteArray(
    QByteDataBuffer *self,
    const QByteArray *bd) {
  self->prepend(*bd);
}

//  QByteArray QByteDataBuffer::read()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QByteDataBuffer4readEv(QByteDataBuffer *self) {
  return new QByteArray(self->read());
}

//  QByteArray QByteDataBuffer::readAll()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QByteDataBuffer7readAllEv(QByteDataBuffer *self) {
  return new QByteArray(self->readAll());
}

//  QByteArray QByteDataBuffer::read(qint64 amount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QByteDataBuffer4readEx(
    QByteDataBuffer *self,
    qint64 amount) {
  return new QByteArray(self->read(amount));
}

//  QByteArrayView QByteDataBuffer::readPointer() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK15QByteDataBuffer11readPointerEv(
    const QByteDataBuffer *self) {
  return new QByteArrayView(self->readPointer());
}

//  void QByteDataBuffer::advanceReadPointer(qint64 distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QByteDataBuffer18advanceReadPointerEx(
    QByteDataBuffer *self,
    qint64 distance) {
  self->advanceReadPointer(distance);
}

//  char QByteDataBuffer::getChar()
extern "C" Q_DECL_EXPORT
char ritual_ZN15QByteDataBuffer7getCharEv(QByteDataBuffer *self) {
  return self->getChar();
}

//  void QByteDataBuffer::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QByteDataBuffer5clearEv(QByteDataBuffer *self) {
  self->clear();
}

//  qint64 QByteDataBuffer::byteAmount() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QByteDataBuffer10byteAmountEv(
    const QByteDataBuffer *self) {
  return self->byteAmount();
}

//  qsizetype QByteDataBuffer::bufferCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QByteDataBuffer11bufferCountEv(
    const QByteDataBuffer *self) {
  return self->bufferCount();
}

//  bool QByteDataBuffer::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QByteDataBuffer7isEmptyEv(const QByteDataBuffer *self) {
  return self->isEmpty();
}

//  qint64 QByteDataBuffer::sizeNextBlock() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QByteDataBuffer13sizeNextBlockEv(
    const QByteDataBuffer *self) {
  return self->sizeNextBlock();
}

//  bool QByteDataBuffer::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QByteDataBuffer11canReadLineEv(
    const QByteDataBuffer *self) {
  return self->canReadLine();
}

//  const QByteArray &QByteDataBuffer::last() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QByteDataBuffer4lastEv(const QByteDataBuffer *self) {
  return new QByteArray(self->last());
}

//  QByteDataBuffer::~QByteDataBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QByteDataBufferD1Ev(QByteDataBuffer *self) {
  delete self;
}
