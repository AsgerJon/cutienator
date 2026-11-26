//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothuuid.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  the ritual of toUInt128(QSysInfo::Endian) is taken out, as Qt declares it
//  but its library does not define it where Qt has QT_SUPPORTS_INT128. Kept
//  as it is when the generator runs again. Also added by hand on 2026-11-25,
//  instances of templates of the class: 2.
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/quuid.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QBluetoothUuid::QBluetoothUuid()
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1Ev() {
  return new QBluetoothUuid();
}

//  QBluetoothUuid::QBluetoothUuid(ProtocolUuid uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1ENS_12ProtocolUuidE(
    QBluetoothUuid::ProtocolUuid uuid) {
  return new QBluetoothUuid(uuid);
}

//  QBluetoothUuid::QBluetoothUuid(ServiceClassUuid uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1ENS_16ServiceClassUuidE(
    QBluetoothUuid::ServiceClassUuid uuid) {
  return new QBluetoothUuid(uuid);
}

//  QBluetoothUuid::QBluetoothUuid(CharacteristicType uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1ENS_18CharacteristicTypeE(
    QBluetoothUuid::CharacteristicType uuid) {
  return new QBluetoothUuid(uuid);
}

//  QBluetoothUuid::QBluetoothUuid(DescriptorType uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1ENS_14DescriptorTypeE(
    QBluetoothUuid::DescriptorType uuid) {
  return new QBluetoothUuid(uuid);
}

//  QBluetoothUuid::QBluetoothUuid(quint16 uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1Et(quint16 uuid) {
  return new QBluetoothUuid(uuid);
}

//  QBluetoothUuid::QBluetoothUuid(quint32 uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1Ej(quint32 uuid) {
  return new QBluetoothUuid(uuid);
}

//  QBluetoothUuid::QBluetoothUuid(const QBluetoothUuid &uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1ERKS_(
    const QBluetoothUuid *uuid) {
  return new QBluetoothUuid(*uuid);
}

//  QBluetoothUuid::QBluetoothUuid(const QUuid &uuid)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidC1ERK5QUuid(const QUuid *uuid) {
  return new QBluetoothUuid(*uuid);
}

//  QBluetoothUuid::~QBluetoothUuid()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBluetoothUuidD1Ev(QBluetoothUuid *self) {
  delete self;
}

//  QBluetoothUuid &QBluetoothUuid::operator=(const QBluetoothUuid &other)
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZN14QBluetoothUuidaSERKS_(
    QBluetoothUuid *self,
    const QBluetoothUuid *other) {
  return &(self->operator=(*other));
}

//  bool operator==(const QBluetoothUuid &a, const QBluetoothUuid &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QBluetoothUuidS1_(
    const QBluetoothUuid *a,
    const QBluetoothUuid *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QBluetoothUuid &a, const QBluetoothUuid &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QBluetoothUuidS1_(
    const QBluetoothUuid *a,
    const QBluetoothUuid *b) {
  return operator!=(*a, *b);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QBluetoothUuid &uuid)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK14QBluetoothUuid(
    const QDebug *debug,
    const QBluetoothUuid *uuid) {
  return new QDebug(operator<<(*debug, *uuid));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  int QBluetoothUuid::minimumSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QBluetoothUuid11minimumSizeEv(const QBluetoothUuid *self) {
  return self->minimumSize();
}

//  quint16 QBluetoothUuid::toUInt16(bool *ok) const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK14QBluetoothUuid8toUInt16EPb(
    const QBluetoothUuid *self,
    bool *ok) {
  return self->toUInt16(ok);
}

//  quint32 QBluetoothUuid::toUInt32(bool *ok) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK14QBluetoothUuid8toUInt32EPb(
    const QBluetoothUuid *self,
    bool *ok) {
  return self->toUInt32(ok);
}

//  QString QBluetoothUuid::serviceClassToString(ServiceClassUuid uuid)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBluetoothUuid20serviceClassToStringENS_16ServiceClassUuidE(
    QBluetoothUuid::ServiceClassUuid uuid) {
  return new QString(QBluetoothUuid::serviceClassToString(uuid));
}

//  QString QBluetoothUuid::protocolToString(ProtocolUuid uuid)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBluetoothUuid16protocolToStringENS_12ProtocolUuidE(
    QBluetoothUuid::ProtocolUuid uuid) {
  return new QString(QBluetoothUuid::protocolToString(uuid));
}

//  QString QBluetoothUuid::characteristicToString(CharacteristicType uuid)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBluetoothUuid22characteristicToStringENS_18CharacteristicTypeE(
    QBluetoothUuid::CharacteristicType uuid) {
  return new QString(QBluetoothUuid::characteristicToString(uuid));
}

//  QString QBluetoothUuid::descriptorToString(DescriptorType uuid)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBluetoothUuid18descriptorToStringENS_14DescriptorTypeE(
    QBluetoothUuid::DescriptorType uuid) {
  return new QString(QBluetoothUuid::descriptorToString(uuid));
}

//  QList<QBluetoothUuid>::QList()
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_list_make_QBluetoothUuid() {
  return new QList<QBluetoothUuid>();
}

//  void QList<QBluetoothUuid>::append(const QBluetoothUuid &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBluetoothUuid(
    QList<QBluetoothUuid> *self,
    const QBluetoothUuid *element) {
  self->append(*element);
}

//  qsizetype QList<QBluetoothUuid>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBluetoothUuid(
    const QList<QBluetoothUuid> *self) {
  return self->size();
}

//  const QBluetoothUuid &QList<QBluetoothUuid>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_list_at_QBluetoothUuid(
    const QList<QBluetoothUuid> *self,
    long long index) {
  return new QBluetoothUuid(self->at(index));
}

//  QList<QBluetoothUuid>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBluetoothUuid(QList<QBluetoothUuid> *self) {
  delete self;
}

//  QBluetoothUuid::QBluetoothUuid(QAnyStringView string)
extern "C" Q_DECL_EXPORT
QBluetoothUuid * ritual_ZN14QBluetoothUuidCI25QUuidE14QAnyStringView(
    const QString *string) {
  return new QBluetoothUuid(QAnyStringView(*string));
}

//  QBluetoothUuid::QBluetoothUuid(uint l, ushort w1, ushort w2, uchar b1,
//      uchar b2, uchar b3, uchar b4, uchar b5, uchar b6, uchar b7, uchar b8)
extern "C" Q_DECL_EXPORT
QBluetoothUuid * ritual_ZN14QBluetoothUuidCI25QUuidEjtthhhhhhhh(
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
  return new QBluetoothUuid(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8);
}
