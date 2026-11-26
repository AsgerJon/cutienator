//  Written by hand on 2026-11-25 from
//  QtBluetooth/6.12.0/QtBluetooth/private/qprivatelinearbuffer_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its inline
//  functions are called. The header leaves the buffer size to the file
//  that includes it, as Qt's own sockets do, so it is given here the
//  16384 they give it.
//  Not written: the constructor and the private makeSpace.
//  The class header stands under '#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER',
//  so it stays with this file and the define before it, out of the part's
//  shared header.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtCore/qbytearray.h>
#include <algorithm>
#include <cstring>
#ifndef QPRIVATELINEARBUFFER_BUFFERSIZE
#define QPRIVATELINEARBUFFER_BUFFERSIZE Q_INT64_C(16384)
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qprivatelinearbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPrivateLinearBuffer::~QPrivateLinearBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPrivateLinearBufferD1Ev(
    QPrivateLinearBuffer *self) {
  delete self;
}

//  void QPrivateLinearBuffer::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPrivateLinearBuffer5clearEv(
    QPrivateLinearBuffer *self) {
  self->clear();
}

//  qsizetype QPrivateLinearBuffer::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK20QPrivateLinearBuffer4sizeEv(
    const QPrivateLinearBuffer *self) {
  return self->size();
}

//  bool QPrivateLinearBuffer::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPrivateLinearBuffer7isEmptyEv(
    const QPrivateLinearBuffer *self) {
  return self->isEmpty();
}

//  void QPrivateLinearBuffer::skip(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPrivateLinearBuffer4skipEx(
    QPrivateLinearBuffer *self,
    qsizetype n) {
  self->skip(n);
}

//  int QPrivateLinearBuffer::getChar()
extern "C" Q_DECL_EXPORT
int ritual_ZN20QPrivateLinearBuffer7getCharEv(
    QPrivateLinearBuffer *self) {
  return self->getChar();
}

//  qsizetype QPrivateLinearBuffer::read(char *target, qsizetype size)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QPrivateLinearBuffer4readEPcx(
    QPrivateLinearBuffer *self,
    char *target,
    qsizetype size) {
  return self->read(target, size);
}

//  char *QPrivateLinearBuffer::reserve(qsizetype size)
extern "C" Q_DECL_EXPORT
char *ritual_ZN20QPrivateLinearBuffer7reserveEx(
    QPrivateLinearBuffer *self,
    qsizetype size) {
  return self->reserve(size);
}

//  void QPrivateLinearBuffer::chop(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPrivateLinearBuffer4chopEx(
    QPrivateLinearBuffer *self,
    qsizetype size) {
  self->chop(size);
}

//  QByteArray QPrivateLinearBuffer::readAll()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN20QPrivateLinearBuffer7readAllEv(
    QPrivateLinearBuffer *self) {
  return new QByteArray(self->readAll());
}

//  qsizetype QPrivateLinearBuffer::readLine(char *target, qsizetype size)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QPrivateLinearBuffer8readLineEPcx(
    QPrivateLinearBuffer *self,
    char *target,
    qsizetype size) {
  return self->readLine(target, size);
}

//  bool QPrivateLinearBuffer::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPrivateLinearBuffer11canReadLineEv(
    const QPrivateLinearBuffer *self) {
  return self->canReadLine();
}

//  void QPrivateLinearBuffer::ungetChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPrivateLinearBuffer9ungetCharEc(
    QPrivateLinearBuffer *self,
    char c) {
  self->ungetChar(c);
}

//  void QPrivateLinearBuffer::ungetBlock(const char *block, qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPrivateLinearBuffer10ungetBlockEPKcx(
    QPrivateLinearBuffer *self,
    const char *block,
    qsizetype size) {
  self->ungetBlock(block, size);
}
