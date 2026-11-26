//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbitarray.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, rituals for functions the generator leaves out: 1. Kept as it is
//  when the generator runs again.
#include <QtCore/qbitarray.h>

//  QBitArray operator&(const QBitArray &a1, const QBitArray &a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZanRK9QBitArrayS1_(
    const QBitArray *a1,
    const QBitArray *a2) {
  return new QBitArray(operator&(*a1, *a2));
}

//  QBitArray operator&(QBitArray &&a1, const QBitArray &a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZanO9QBitArrayRKS_(QBitArray *a1, const QBitArray *a2) {
  return new QBitArray(operator&(std::move(*a1), *a2));
}

//  QBitArray operator&(const QBitArray &a1, QBitArray &&a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZanRK9QBitArrayOS_(const QBitArray *a1, QBitArray *a2) {
  return new QBitArray(operator&(*a1, std::move(*a2)));
}

//  QBitArray operator&(QBitArray &&a1, QBitArray &&a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZanO9QBitArrayS0_(QBitArray *a1, QBitArray *a2) {
  return new QBitArray(operator&(std::move(*a1), std::move(*a2)));
}

//  QBitArray operator|(const QBitArray &a1, const QBitArray &a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZorRK9QBitArrayS1_(
    const QBitArray *a1,
    const QBitArray *a2) {
  return new QBitArray(operator|(*a1, *a2));
}

//  QBitArray operator|(QBitArray &&a1, const QBitArray &a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZorO9QBitArrayRKS_(QBitArray *a1, const QBitArray *a2) {
  return new QBitArray(operator|(std::move(*a1), *a2));
}

//  QBitArray operator|(const QBitArray &a1, QBitArray &&a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZorRK9QBitArrayOS_(const QBitArray *a1, QBitArray *a2) {
  return new QBitArray(operator|(*a1, std::move(*a2)));
}

//  QBitArray operator|(QBitArray &&a1, QBitArray &&a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZorO9QBitArrayS0_(QBitArray *a1, QBitArray *a2) {
  return new QBitArray(operator|(std::move(*a1), std::move(*a2)));
}

//  QBitArray operator^(const QBitArray &a1, const QBitArray &a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZeoRK9QBitArrayS1_(
    const QBitArray *a1,
    const QBitArray *a2) {
  return new QBitArray(operator^(*a1, *a2));
}

//  QBitArray operator^(QBitArray &&a1, const QBitArray &a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZeoO9QBitArrayRKS_(QBitArray *a1, const QBitArray *a2) {
  return new QBitArray(operator^(std::move(*a1), *a2));
}

//  QBitArray operator^(const QBitArray &a1, QBitArray &&a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZeoRK9QBitArrayOS_(const QBitArray *a1, QBitArray *a2) {
  return new QBitArray(operator^(*a1, std::move(*a2)));
}

//  QBitArray operator^(QBitArray &&a1, QBitArray &&a2)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZeoO9QBitArrayS0_(QBitArray *a1, QBitArray *a2) {
  return new QBitArray(operator^(std::move(*a1), std::move(*a2)));
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QBitArray &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK9QBitArray(
    QDataStream *a0,
    const QBitArray *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QBitArray &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR9QBitArray(
    QDataStream *a0,
    QBitArray *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QBitArray operator~(QBitArray a)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_Zco9QBitArray(const QBitArray *a) {
  return new QBitArray(operator~(*a));
}

//  QBitArray::QBitArray(QByteArrayData &&dd)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayC1EO17QArrayDataPointerIcE(
    QByteArrayData *dd) {
  return new QBitArray(std::move(*dd));
}

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

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBitArray::QBitArray(const QBitArray &other)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayC1ERKS_(const QBitArray *other) {
  return new QBitArray(*other);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBitArray &QBitArray::operator=(const QBitArray &other)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayaSERKS_(
    QBitArray *self,
    const QBitArray *other) {
  return &(self->operator=(*other));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBitArray::QBitArray(QBitArray &&other)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayC1EOS_(QBitArray *other) {
  return new QBitArray(std::move(*other));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBitArray &QBitArray::operator=(QBitArray &&other)
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZN9QBitArrayaSEOS_(QBitArray *self, QBitArray *other) {
  return &(self->operator=(std::move(*other)));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QBitArray::swap(QBitArray &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArray4swapERS_(QBitArray *self, QBitArray *other) {
  self->swap(*other);
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

//  QBitArray &QBitArray::operator&=(QBitArray &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayaNEOS_(QBitArray *self, QBitArray *a0) {
  self->operator&=(std::move(*a0));
}

//  QBitArray &QBitArray::operator|=(QBitArray &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayoREOS_(QBitArray *self, QBitArray *a0) {
  self->operator|=(std::move(*a0));
}

//  QBitArray &QBitArray::operator^=(QBitArray &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayeOEOS_(QBitArray *self, QBitArray *a0) {
  self->operator^=(std::move(*a0));
}

//  QBitArray &QBitArray::operator&=(const QBitArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayaNERKS_(QBitArray *self, const QBitArray *a0) {
  self->operator&=(*a0);
}

//  QBitArray &QBitArray::operator|=(const QBitArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayoRERKS_(QBitArray *self, const QBitArray *a0) {
  self->operator|=(*a0);
}

//  QBitArray &QBitArray::operator^=(const QBitArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayeOERKS_(QBitArray *self, const QBitArray *a0) {
  self->operator^=(*a0);
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

//  DataPtr &QBitArray::data_ptr()
extern "C" Q_DECL_EXPORT
QBitArray::DataPtr *ritual_ZN9QBitArray8data_ptrEv(QBitArray *self) {
  return &(self->data_ptr());
}

//  const DataPtr &QBitArray::data_ptr() const
extern "C" Q_DECL_EXPORT
const QBitArray::DataPtr *ritual_ZNK9QBitArray8data_ptrEv(
    const QBitArray *self) {
  return &(self->data_ptr());
}

//  bool operator==(const QBitArray &lhs, const QBitArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QBitArrayS1_(const QBitArray *lhs, const QBitArray *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QBitArray &lhs, const QBitArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QBitArrayS1_(const QBitArray *lhs, const QBitArray *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QBitArray::~QBitArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QBitArrayD1Ev(QBitArray *self) {
  delete self;
}

//  QBitArray QBitArray::inverted_inplace() &&
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZNO9QBitArray16inverted_inplaceEv(
    QBitArray *self) {
  return new QBitArray(std::move(*self).inverted_inplace());
}
