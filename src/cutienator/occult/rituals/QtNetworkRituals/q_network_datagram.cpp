//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkdatagram.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_UDPSOCKET)
#include <QtNetwork/qnetworkdatagram.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhostaddress.h>

//  QNetworkDatagram::QNetworkDatagram()
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN16QNetworkDatagramC1Ev() {
  return new QNetworkDatagram();
}

//  QNetworkDatagram::QNetworkDatagram(const QByteArray &data, const
//      QHostAddress &destinationAddress, quint16 port)
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN16QNetworkDatagramC1ERK10QByteArrayRK12QHostAddresst(
    const QByteArray *data,
    const QHostAddress *destinationAddress,
    quint16 port) {
  return new QNetworkDatagram(*data, *destinationAddress, port);
}

//  QNetworkDatagram::QNetworkDatagram(const QNetworkDatagram &other)
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN16QNetworkDatagramC1ERKS_(
    const QNetworkDatagram *other) {
  return new QNetworkDatagram(*other);
}

//  QNetworkDatagram &QNetworkDatagram::operator=(const QNetworkDatagram
//      &other)
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN16QNetworkDatagramaSERKS_(
    QNetworkDatagram *self,
    const QNetworkDatagram *other) {
  return &(self->operator=(*other));
}

//  QNetworkDatagram::~QNetworkDatagram()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagramD1Ev(QNetworkDatagram *self) {
  delete self;
}

//  QNetworkDatagram::QNetworkDatagram(QNetworkDatagram &&other)
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN16QNetworkDatagramC1EOS_(
    QNetworkDatagram *other) {
  return new QNetworkDatagram(std::move(*other));
}

//  QNetworkDatagram &QNetworkDatagram::operator=(QNetworkDatagram &&other)
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN16QNetworkDatagramaSEOS_(
    QNetworkDatagram *self,
    QNetworkDatagram *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QNetworkDatagram::swap(QNetworkDatagram &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram4swapERS_(
    QNetworkDatagram *self,
    QNetworkDatagram *other) {
  self->swap(*other);
}

//  void QNetworkDatagram::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram5clearEv(QNetworkDatagram *self) {
  self->clear();
}

//  bool QNetworkDatagram::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QNetworkDatagram7isValidEv(const QNetworkDatagram *self) {
  return self->isValid();
}

//  bool QNetworkDatagram::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QNetworkDatagram6isNullEv(const QNetworkDatagram *self) {
  return self->isNull();
}

//  uint QNetworkDatagram::interfaceIndex() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK16QNetworkDatagram14interfaceIndexEv(
    const QNetworkDatagram *self) {
  return self->interfaceIndex();
}

//  void QNetworkDatagram::setInterfaceIndex(uint index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram17setInterfaceIndexEj(
    QNetworkDatagram *self,
    uint index) {
  self->setInterfaceIndex(index);
}

//  QHostAddress QNetworkDatagram::senderAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK16QNetworkDatagram13senderAddressEv(
    const QNetworkDatagram *self) {
  return new QHostAddress(self->senderAddress());
}

//  QHostAddress QNetworkDatagram::destinationAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK16QNetworkDatagram18destinationAddressEv(
    const QNetworkDatagram *self) {
  return new QHostAddress(self->destinationAddress());
}

//  int QNetworkDatagram::senderPort() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QNetworkDatagram10senderPortEv(
    const QNetworkDatagram *self) {
  return self->senderPort();
}

//  int QNetworkDatagram::destinationPort() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QNetworkDatagram15destinationPortEv(
    const QNetworkDatagram *self) {
  return self->destinationPort();
}

//  void QNetworkDatagram::setSender(const QHostAddress &address, quint16
//      port)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram9setSenderERK12QHostAddresst(
    QNetworkDatagram *self,
    const QHostAddress *address,
    quint16 port) {
  self->setSender(*address, port);
}

//  void QNetworkDatagram::setDestination(const QHostAddress &address,
//      quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram14setDestinationERK12QHostAddresst(
    QNetworkDatagram *self,
    const QHostAddress *address,
    quint16 port) {
  self->setDestination(*address, port);
}

//  int QNetworkDatagram::hopLimit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QNetworkDatagram8hopLimitEv(const QNetworkDatagram *self) {
  return self->hopLimit();
}

//  void QNetworkDatagram::setHopLimit(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram11setHopLimitEi(
    QNetworkDatagram *self,
    int count) {
  self->setHopLimit(count);
}

//  QByteArray QNetworkDatagram::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QNetworkDatagram4dataEv(
    const QNetworkDatagram *self) {
  return new QByteArray(self->data());
}

//  void QNetworkDatagram::setData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram7setDataERK10QByteArray(
    QNetworkDatagram *self,
    const QByteArray *data) {
  self->setData(*data);
}

#if defined(Q_COMPILER_REF_QUALIFIERS) || defined(Q_QDOC)
//  QNetworkDatagram QNetworkDatagram::makeReply(const QByteArray &payload)
//      const
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZNKR16QNetworkDatagram9makeReplyERK10QByteArray(
    const QNetworkDatagram *self,
    const QByteArray *payload) {
  return new QNetworkDatagram(self->makeReply(*payload));
}
#endif  // defined(Q_COMPILER_REF_QUALIFIERS) || defined(Q_QDOC)

//  QNetworkDatagram::QNetworkDatagram(QNetworkDatagramPrivate &dd)
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN16QNetworkDatagramC1ER23QNetworkDatagramPrivate(
    QNetworkDatagramPrivate *dd) {
  return new QNetworkDatagram(*dd);
}

//  QNetworkDatagram QNetworkDatagram::makeReply_helper(const QByteArray
//      &data) const
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZNK16QNetworkDatagram16makeReply_helperERK10QByteArray(
    const QNetworkDatagram *self,
    const QByteArray *data) {
  return new QNetworkDatagram(self->makeReply_helper(*data));
}

//  void QNetworkDatagram::makeReply_helper_inplace(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram24makeReply_helper_inplaceERK10QByteArray(
    QNetworkDatagram *self,
    const QByteArray *data) {
  self->makeReply_helper_inplace(*data);
}

//  void QNetworkDatagram::destroy(QNetworkDatagramPrivate *d)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNetworkDatagram7destroyEP23QNetworkDatagramPrivate(
    QNetworkDatagramPrivate *d) {
  QNetworkDatagram::destroy(d);
}

#endif  // !defined(QT_NO_UDPSOCKET)
