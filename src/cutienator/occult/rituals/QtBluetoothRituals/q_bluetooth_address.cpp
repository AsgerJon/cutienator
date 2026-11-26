//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothaddress.h, Qt 6.12.0. Changes made here are lost.
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QBluetoothAddress::QBluetoothAddress()
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZN17QBluetoothAddressC1Ev() {
  return new QBluetoothAddress();
}

//  QBluetoothAddress::QBluetoothAddress(quint64 address)
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZN17QBluetoothAddressC1Ey(quint64 address) {
  return new QBluetoothAddress(address);
}

//  QBluetoothAddress::QBluetoothAddress(const QString &address)
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZN17QBluetoothAddressC1ERK7QString(
    const QString *address) {
  return new QBluetoothAddress(*address);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBluetoothAddress::QBluetoothAddress(const QBluetoothAddress &other)
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZN17QBluetoothAddressC1ERKS_(
    const QBluetoothAddress *other) {
  return new QBluetoothAddress(*other);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBluetoothAddress::~QBluetoothAddress()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QBluetoothAddressD1Ev(QBluetoothAddress *self) {
  delete self;
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBluetoothAddress &QBluetoothAddress::operator=(const QBluetoothAddress
//      &other)
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZN17QBluetoothAddressaSERKS_(
    QBluetoothAddress *self,
    const QBluetoothAddress *other) {
  return &(self->operator=(*other));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBluetoothAddress::QBluetoothAddress(QBluetoothAddress &&a0)
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZN17QBluetoothAddressC1EOS_(
    QBluetoothAddress *a0) {
  return new QBluetoothAddress(std::move(*a0));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QBluetoothAddress &QBluetoothAddress::operator=(QBluetoothAddress &&a0)
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZN17QBluetoothAddressaSEOS_(
    QBluetoothAddress *self,
    QBluetoothAddress *a0) {
  return &(self->operator=(std::move(*a0)));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  bool QBluetoothAddress::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QBluetoothAddress6isNullEv(const QBluetoothAddress *self) {
  return self->isNull();
}

//  void QBluetoothAddress::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QBluetoothAddress5clearEv(QBluetoothAddress *self) {
  self->clear();
}

//  bool operator<(const QBluetoothAddress &a, const QBluetoothAddress &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK17QBluetoothAddressS1_(
    const QBluetoothAddress *a,
    const QBluetoothAddress *b) {
  return operator<(*a, *b);
}

//  bool operator==(const QBluetoothAddress &a, const QBluetoothAddress &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK17QBluetoothAddressS1_(
    const QBluetoothAddress *a,
    const QBluetoothAddress *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QBluetoothAddress &a, const QBluetoothAddress &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK17QBluetoothAddressS1_(
    const QBluetoothAddress *a,
    const QBluetoothAddress *b) {
  return operator!=(*a, *b);
}

//  quint64 QBluetoothAddress::toUInt64() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QBluetoothAddress8toUInt64Ev(
    const QBluetoothAddress *self) {
  return self->toUInt64();
}

//  QString QBluetoothAddress::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QBluetoothAddress8toStringEv(
    const QBluetoothAddress *self) {
  return new QString(self->toString());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug d, const QBluetoothAddress &a)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK17QBluetoothAddress(
    const QDebug *d,
    const QBluetoothAddress *a) {
  return new QDebug(operator<<(*d, *a));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QBluetoothAddress::streamingOperator(QDebug a0, const
//      QBluetoothAddress &address)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN17QBluetoothAddress17streamingOperatorE6QDebugRKS_(
    const QDebug *a0,
    const QBluetoothAddress *address) {
  return new QDebug(QBluetoothAddress::streamingOperator(*a0, *address));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QBluetoothAddress>::QList()
extern "C" Q_DECL_EXPORT
QList<QBluetoothAddress> *ritual_list_make_QBluetoothAddress() {
  return new QList<QBluetoothAddress>();
}

//  void QList<QBluetoothAddress>::append(const QBluetoothAddress &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBluetoothAddress(
    QList<QBluetoothAddress> *self,
    const QBluetoothAddress *element) {
  self->append(*element);
}

//  qsizetype QList<QBluetoothAddress>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBluetoothAddress(
    const QList<QBluetoothAddress> *self) {
  return self->size();
}

//  const QBluetoothAddress &QList<QBluetoothAddress>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_list_at_QBluetoothAddress(
    const QList<QBluetoothAddress> *self,
    long long index) {
  return new QBluetoothAddress(self->at(index));
}

//  QList<QBluetoothAddress>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBluetoothAddress(QList<QBluetoothAddress> *self) {
  delete self;
}
