//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbitarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbitarray.h>

//  QBitArray::QBitArray()
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayC1Ev() {
  return new QBitArray();
}

//  QBitArray::QBitArray(qsizetype size, bool val)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayC1Exb(qsizetype size, bool val) {
  return new QBitArray(size, val);
}

//  QBitArray::QBitArray(const QBitArray &other)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayC1ERKS_(const QBitArray *other) {
  return new QBitArray(*other);
}

//  qsizetype QBitArray::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QBitArray4sizeEv(const QBitArray *self) {
  return self->size();
}

//  qsizetype QBitArray::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QBitArray5countEv(const QBitArray *self) {
  return self->count();
}

//  qsizetype QBitArray::count(bool on) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QBitArray5countEb(const QBitArray *self, bool on) {
  return self->count(on);
}

//  bool QBitArray::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QBitArray7isEmptyEv(const QBitArray *self) {
  return self->isEmpty();
}

//  bool QBitArray::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QBitArray6isNullEv(const QBitArray *self) {
  return self->isNull();
}

//  void QBitArray::resize(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray6resizeEx(QBitArray *self, qsizetype size) {
  self->resize(size);
}

//  void QBitArray::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray6detachEv(QBitArray *self) {
  self->detach();
}

//  bool QBitArray::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QBitArray10isDetachedEv(const QBitArray *self) {
  return self->isDetached();
}

//  void QBitArray::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray5clearEv(QBitArray *self) {
  self->clear();
}

//  bool QBitArray::testBit(qsizetype i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QBitArray7testBitEx(const QBitArray *self, qsizetype i) {
  return self->testBit(i);
}

//  void QBitArray::setBit(qsizetype i)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray6setBitEx(QBitArray *self, qsizetype i) {
  self->setBit(i);
}

//  void QBitArray::setBit(qsizetype i, bool val)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray6setBitExb(QBitArray *self, qsizetype i, bool val) {
  self->setBit(i, val);
}

//  void QBitArray::clearBit(qsizetype i)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray8clearBitEx(QBitArray *self, qsizetype i) {
  self->clearBit(i);
}

//  bool QBitArray::toggleBit(qsizetype i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QBitArray9toggleBitEx(QBitArray *self, qsizetype i) {
  return self->toggleBit(i);
}

//  bool QBitArray::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QBitArray2atEx(const QBitArray *self, qsizetype i) {
  return self->at(i);
}

//  QBitRef QBitArray::operator[](qsizetype i)
extern "C" Q_DECL_EXPORT
QBitRef *ritual_ZN9QBitArrayixEx(QBitArray *self, qsizetype i) {
  return new QBitRef(self->operator[](i));
}

//  bool QBitArray::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QBitArrayixEx(const QBitArray *self, qsizetype i) {
  return self->operator[](i);
}

//  bool QBitArray::fill(bool aval, qsizetype asize)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QBitArray4fillEbx(
    QBitArray *self,
    bool aval,
    qsizetype asize) {
  return self->fill(aval, asize);
}

//  void QBitArray::fill(bool val, qsizetype first, qsizetype last)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray4fillEbxx(
    QBitArray *self,
    bool val,
    qsizetype first,
    qsizetype last) {
  self->fill(val, first, last);
}

//  void QBitArray::truncate(qsizetype pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray8truncateEx(QBitArray *self, qsizetype pos) {
  self->truncate(pos);
}

//  const char *QBitArray::bits() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK9QBitArray4bitsEv(const QBitArray *self) {
  return self->bits();
}

//  QBitArray QBitArray::fromBits(const char *data, qsizetype len)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArray8fromBitsEPKcx(
    const char *data,
    qsizetype len) {
  return new QBitArray(QBitArray::fromBits(data, len));
}

//  quint32 QBitArray::toUInt32(QSysInfo::Endian endianness, bool *ok) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK9QBitArray8toUInt32EN8QSysInfo6EndianEPb(
    const QBitArray *self,
    QSysInfo::Endian endianness,
    bool *ok) {
  return self->toUInt32(endianness, ok);
}

//  QBitArray::~QBitArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayD1Ev(QBitArray *self) {
  delete self;
}
