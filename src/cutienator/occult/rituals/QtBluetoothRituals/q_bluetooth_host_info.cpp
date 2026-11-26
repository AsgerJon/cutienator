//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothhostinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtBluetooth/qbluetoothhostinfo.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QBluetoothHostInfo::QBluetoothHostInfo()
extern "C" Q_DECL_EXPORT
QBluetoothHostInfo *ritual_ZN18QBluetoothHostInfoC1Ev() {
  return new QBluetoothHostInfo();
}

//  QBluetoothHostInfo::QBluetoothHostInfo(const QBluetoothHostInfo &other)
extern "C" Q_DECL_EXPORT
QBluetoothHostInfo *ritual_ZN18QBluetoothHostInfoC1ERKS_(
    const QBluetoothHostInfo *other) {
  return new QBluetoothHostInfo(*other);
}

//  QBluetoothHostInfo::~QBluetoothHostInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBluetoothHostInfoD1Ev(QBluetoothHostInfo *self) {
  delete self;
}

//  QBluetoothHostInfo &QBluetoothHostInfo::operator=(const
//      QBluetoothHostInfo &other)
extern "C" Q_DECL_EXPORT
QBluetoothHostInfo *ritual_ZN18QBluetoothHostInfoaSERKS_(
    QBluetoothHostInfo *self,
    const QBluetoothHostInfo *other) {
  return &(self->operator=(*other));
}

//  bool operator==(const QBluetoothHostInfo &a, const QBluetoothHostInfo &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QBluetoothHostInfoS1_(
    const QBluetoothHostInfo *a,
    const QBluetoothHostInfo *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QBluetoothHostInfo &a, const QBluetoothHostInfo &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QBluetoothHostInfoS1_(
    const QBluetoothHostInfo *a,
    const QBluetoothHostInfo *b) {
  return operator!=(*a, *b);
}

//  QBluetoothAddress QBluetoothHostInfo::address() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK18QBluetoothHostInfo7addressEv(
    const QBluetoothHostInfo *self) {
  return new QBluetoothAddress(self->address());
}

//  void QBluetoothHostInfo::setAddress(const QBluetoothAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBluetoothHostInfo10setAddressERK17QBluetoothAddress(
    QBluetoothHostInfo *self,
    const QBluetoothAddress *address) {
  self->setAddress(*address);
}

//  QString QBluetoothHostInfo::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QBluetoothHostInfo4nameEv(
    const QBluetoothHostInfo *self) {
  return new QString(self->name());
}

//  void QBluetoothHostInfo::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBluetoothHostInfo7setNameERK7QString(
    QBluetoothHostInfo *self,
    const QString *name) {
  self->setName(*name);
}

//  bool QBluetoothHostInfo::equals(const QBluetoothHostInfo &a, const
//      QBluetoothHostInfo &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QBluetoothHostInfo6equalsERKS_S1_(
    const QBluetoothHostInfo *a,
    const QBluetoothHostInfo *b) {
  return QBluetoothHostInfo::equals(*a, *b);
}

//  QBluetoothHostInfoPrivate *QBluetoothHostInfo::d_func()
extern "C" Q_DECL_EXPORT
QBluetoothHostInfoPrivate *ritual_ZN18QBluetoothHostInfo6d_funcEv(
    QBluetoothHostInfo *self) {
  return self->d_func();
}

//  const QBluetoothHostInfoPrivate *QBluetoothHostInfo::d_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothHostInfoPrivate *ritual_ZNK18QBluetoothHostInfo6d_funcEv(
    const QBluetoothHostInfo *self) {
  return self->d_func();
}

//  QList<QBluetoothHostInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QBluetoothHostInfo> *ritual_list_make_QBluetoothHostInfo() {
  return new QList<QBluetoothHostInfo>();
}

//  void QList<QBluetoothHostInfo>::append(const QBluetoothHostInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBluetoothHostInfo(
    QList<QBluetoothHostInfo> *self,
    const QBluetoothHostInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QBluetoothHostInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBluetoothHostInfo(
    const QList<QBluetoothHostInfo> *self) {
  return self->size();
}

//  const QBluetoothHostInfo &QList<QBluetoothHostInfo>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QBluetoothHostInfo *ritual_list_at_QBluetoothHostInfo(
    const QList<QBluetoothHostInfo> *self,
    long long index) {
  return new QBluetoothHostInfo(self->at(index));
}

//  QList<QBluetoothHostInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBluetoothHostInfo(QList<QBluetoothHostInfo> *self) {
  delete self;
}
