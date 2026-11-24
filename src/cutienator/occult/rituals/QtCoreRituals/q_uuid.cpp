//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/quuid.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/quuid.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qcompare.h>

//  QUuid::QUuid(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuidC1EN2Qt14InitializationE(Qt::Initialization a0) {
  return new QUuid(a0);
}

//  QUuid::QUuid()
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuidC1Ev() {
  return new QUuid();
}

//  QUuid::QUuid(uint l, ushort w1, ushort w2, uchar b1, uchar b2, uchar b3,
//      uchar b4, uchar b5, uchar b6, uchar b7, uchar b8)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuidC1Ejtthhhhhhhh(
    uint l,
    ushort w1,
    ushort w2,
    uchar b1,
    uchar b2,
    uchar b3,
    uchar b4,
    uchar b5,
    uchar b6,
    uchar b7,
    uchar b8) {
  return new QUuid(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8);
}

//  QUuid::QUuid(Id128Bytes id128, QSysInfo::Endian order)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuidC1ENS_10Id128BytesEN8QSysInfo6EndianE(
    const QUuid::Id128Bytes *id128,
    QSysInfo::Endian order) {
  return new QUuid(*id128, order);
}

//  QUuid::QUuid(QAnyStringView string)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuidC1E14QAnyStringView(const QString *string) {
  return new QUuid(QAnyStringView(*string));
}

//  QUuid QUuid::fromString(QAnyStringView string)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuid10fromStringE14QAnyStringView(const QString *string) {
  return new QUuid(QUuid::fromString(QAnyStringView(*string)));
}

//  QString QUuid::toString(StringFormat mode) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QUuid8toStringENS_12StringFormatE(
    const QUuid *self,
    QUuid::StringFormat mode) {
  return new QString(self->toString(mode));
}

//  QByteArray QUuid::toByteArray(StringFormat mode) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK5QUuid11toByteArrayENS_12StringFormatE(
    const QUuid *self,
    QUuid::StringFormat mode) {
  return new QByteArray(self->toByteArray(mode));
}

//  Id128Bytes QUuid::toBytes(QSysInfo::Endian order) const
extern "C" Q_DECL_EXPORT
QUuid::Id128Bytes *ritual_ZNK5QUuid7toBytesEN8QSysInfo6EndianE(
    const QUuid *self,
    QSysInfo::Endian order) {
  return new QUuid::Id128Bytes(self->toBytes(order));
}

//  QByteArray QUuid::toRfc4122() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK5QUuid9toRfc4122Ev(const QUuid *self) {
  return new QByteArray(self->toRfc4122());
}

//  QUuid QUuid::fromRfc4122(QByteArrayView a0)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuid11fromRfc4122E14QByteArrayView(
    const QByteArrayView *a0) {
  return new QUuid(QUuid::fromRfc4122(*a0));
}

//  bool QUuid::isNull(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QUuid6isNullEN2Qt15Disambiguated_tE(
    const QUuid *self,
    const Qt::Disambiguated_t *a0) {
  return self->isNull(*a0);
}

//  Qt::strong_ordering QUuid::compareThreeWay_helper(const QUuid &lhs, const
//      QUuid &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN5QUuid22compareThreeWay_helperERKS_S1_(
    const QUuid *lhs,
    const QUuid *rhs) {
  return new Qt::strong_ordering(QUuid::compareThreeWay_helper(*lhs, *rhs));
}

#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator==(const QUuid &lhs, const QUuid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QUuidS1_(const QUuid *lhs, const QUuid *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))

#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator!=(const QUuid &lhs, const QUuid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QUuidS1_(const QUuid *lhs, const QUuid *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))

#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<(const QUuid &lhs, const QUuid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QUuidS1_(const QUuid *lhs, const QUuid *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))

#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>(const QUuid &lhs, const QUuid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QUuidS1_(const QUuid *lhs, const QUuid *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))

#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<=(const QUuid &lhs, const QUuid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QUuidS1_(const QUuid *lhs, const QUuid *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))

#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>=(const QUuid &lhs, const QUuid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QUuidS1_(const QUuid *lhs, const QUuid *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))

//  QUuid QUuid::createUuid()
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuid10createUuidEv() {
  return new QUuid(QUuid::createUuid());
}

//  QUuid QUuid::createUuidV5(QUuid ns, QByteArrayView baseData)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuid12createUuidV5ES_14QByteArrayView(
    const QUuid *ns,
    const QByteArrayView *baseData) {
  return new QUuid(QUuid::createUuidV5(*ns, *baseData));
}

#if !defined(QT_BOOTSTRAPPED)
//  QUuid QUuid::createUuidV3(QUuid ns, QByteArrayView baseData)
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuid12createUuidV3ES_14QByteArrayView(
    const QUuid *ns,
    const QByteArrayView *baseData) {
  return new QUuid(QUuid::createUuidV3(*ns, *baseData));
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  QUuid QUuid::createUuidV7()
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZN5QUuid12createUuidV7Ev() {
  return new QUuid(QUuid::createUuidV7());
}

//  bool QUuid::isKnownVersion(Version v)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QUuid14isKnownVersionENS_7VersionE(QUuid::Version v) {
  return QUuid::isKnownVersion(v);
}

//  Variant QUuid::variant(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
QUuid::Variant ritual_ZNK5QUuid7variantEN2Qt15Disambiguated_tE(
    const QUuid *self,
    const Qt::Disambiguated_t *a0) {
  return self->variant(*a0);
}

//  Version QUuid::version(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
QUuid::Version ritual_ZNK5QUuid7versionEN2Qt15Disambiguated_tE(
    const QUuid *self,
    const Qt::Disambiguated_t *a0) {
  return self->version(*a0);
}

//  QUuid::~QUuid()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QUuidD1Ev(QUuid *self) {
  delete self;
}
