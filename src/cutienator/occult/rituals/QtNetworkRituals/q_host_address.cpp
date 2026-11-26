//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhostaddress.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <utility>
#include <QtNetwork/QHostAddress>
#include <QtCore/QString>

//  QHostAddress::QHostAddress()
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1Ev() {
  return new QHostAddress();
}

//  QHostAddress::QHostAddress(quint32 ip4Addr)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1Ej(quint32 ip4Addr) {
  return new QHostAddress(ip4Addr);
}

//  QHostAddress::QHostAddress(const quint8 *ip6Addr)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1EPKh(const quint8 *ip6Addr) {
  return new QHostAddress(ip6Addr);
}

//  QHostAddress::QHostAddress(const Q_IPV6ADDR &ip6Addr)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1ERK12QIPv6Address(
    const QIPv6Address *ip6Addr) {
  return new QHostAddress(*ip6Addr);
}

//  QHostAddress::QHostAddress(const sockaddr *address)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1EPK8sockaddr(
    const sockaddr *address) {
  return new QHostAddress(address);
}

//  QHostAddress::QHostAddress(const QString &address)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1ERK7QString(const QString *address) {
  return new QHostAddress(*address);
}

//  QHostAddress::QHostAddress(const QHostAddress &copy)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1ERKS_(const QHostAddress *copy) {
  return new QHostAddress(*copy);
}

//  QHostAddress::QHostAddress(QHostAddress &&other)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1EOS_(QHostAddress *other) {
  return new QHostAddress(std::move(*other));
}

//  QHostAddress::QHostAddress(SpecialAddress address)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressC1ENS_14SpecialAddressE(
    QHostAddress::SpecialAddress address) {
  return new QHostAddress(address);
}

//  QHostAddress::~QHostAddress()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddressD1Ev(QHostAddress *self) {
  delete self;
}

//  QHostAddress &QHostAddress::operator=(QHostAddress &&other)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressaSEOS_(
    QHostAddress *self,
    QHostAddress *other) {
  return &(self->operator=(std::move(*other)));
}

//  QHostAddress &QHostAddress::operator=(const QHostAddress &other)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressaSERKS_(
    QHostAddress *self,
    const QHostAddress *other) {
  return &(self->operator=(*other));
}

//  QHostAddress &QHostAddress::operator=(SpecialAddress address)
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZN12QHostAddressaSENS_14SpecialAddressE(
    QHostAddress *self,
    QHostAddress::SpecialAddress address) {
  return &(self->operator=(address));
}

//  void QHostAddress::swap(QHostAddress &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress4swapERS_(
    QHostAddress *self,
    QHostAddress *other) {
  self->swap(*other);
}

//  void QHostAddress::setAddress(quint32 ip4Addr)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress10setAddressEj(
    QHostAddress *self,
    quint32 ip4Addr) {
  self->setAddress(ip4Addr);
}

//  void QHostAddress::setAddress(const quint8 *ip6Addr)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress10setAddressEPKh(
    QHostAddress *self,
    const quint8 *ip6Addr) {
  self->setAddress(ip6Addr);
}

//  void QHostAddress::setAddress(const Q_IPV6ADDR &ip6Addr)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress10setAddressERK12QIPv6Address(
    QHostAddress *self,
    const QIPv6Address *ip6Addr) {
  self->setAddress(*ip6Addr);
}

//  void QHostAddress::setAddress(const sockaddr *address)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress10setAddressEPK8sockaddr(
    QHostAddress *self,
    const sockaddr *address) {
  self->setAddress(address);
}

//  bool QHostAddress::setAddress(const QString &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHostAddress10setAddressERK7QString(
    QHostAddress *self,
    const QString *address) {
  return self->setAddress(*address);
}

//  void QHostAddress::setAddress(SpecialAddress address)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress10setAddressENS_14SpecialAddressE(
    QHostAddress *self,
    QHostAddress::SpecialAddress address) {
  self->setAddress(address);
}

//  NetworkLayerProtocol QHostAddress::protocol() const
extern "C" Q_DECL_EXPORT
QHostAddress::NetworkLayerProtocol ritual_ZNK12QHostAddress8protocolEv(
    const QHostAddress *self) {
  return self->protocol();
}

//  quint32 QHostAddress::toIPv4Address(bool *ok) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK12QHostAddress13toIPv4AddressEPb(
    const QHostAddress *self,
    bool *ok) {
  return self->toIPv4Address(ok);
}

//  Q_IPV6ADDR QHostAddress::toIPv6Address() const
extern "C" Q_DECL_EXPORT
QIPv6Address *ritual_ZNK12QHostAddress13toIPv6AddressEv(
    const QHostAddress *self) {
  return new QIPv6Address(self->toIPv6Address());
}

//  QString QHostAddress::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QHostAddress8toStringEv(const QHostAddress *self) {
  return new QString(self->toString());
}

//  QString QHostAddress::scopeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QHostAddress7scopeIdEv(const QHostAddress *self) {
  return new QString(self->scopeId());
}

//  void QHostAddress::setScopeId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress10setScopeIdERK7QString(
    QHostAddress *self,
    const QString *id) {
  self->setScopeId(*id);
}

//  bool QHostAddress::isEqual(const QHostAddress &address, ConversionMode
//      mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress7isEqualERKS_6QFlagsINS_18ConversionModeFlagEE(
    const QHostAddress *self,
    const QHostAddress *address,
    int mode) {
  return self->isEqual(
      *address,
      QFlags<QHostAddress::ConversionModeFlag>::fromInt(mode));
}

//  bool QHostAddress::operator==(const QHostAddress &address) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddresseqERKS_(
    const QHostAddress *self,
    const QHostAddress *address) {
  return self->operator==(*address);
}

//  bool QHostAddress::operator==(SpecialAddress address) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddresseqENS_14SpecialAddressE(
    const QHostAddress *self,
    QHostAddress::SpecialAddress address) {
  return self->operator==(address);
}

//  bool QHostAddress::operator!=(const QHostAddress &address) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddressneERKS_(
    const QHostAddress *self,
    const QHostAddress *address) {
  return self->operator!=(*address);
}

//  bool QHostAddress::operator!=(SpecialAddress address) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddressneENS_14SpecialAddressE(
    const QHostAddress *self,
    QHostAddress::SpecialAddress address) {
  return self->operator!=(address);
}

//  bool QHostAddress::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress6isNullEv(const QHostAddress *self) {
  return self->isNull();
}

//  void QHostAddress::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHostAddress5clearEv(QHostAddress *self) {
  self->clear();
}

//  bool QHostAddress::isInSubnet(const QHostAddress &subnet, int netmask)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress10isInSubnetERKS_i(
    const QHostAddress *self,
    const QHostAddress *subnet,
    int netmask) {
  return self->isInSubnet(*subnet, netmask);
}

//  bool QHostAddress::isInSubnet(const std::pair<QHostAddress, int> &subnet)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress10isInSubnetERKSt4pairIS_iE(
    const QHostAddress *self,
    const std::pair<QHostAddress, int> *subnet) {
  return self->isInSubnet(*subnet);
}

//  bool QHostAddress::isLoopback() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress10isLoopbackEv(const QHostAddress *self) {
  return self->isLoopback();
}

//  bool QHostAddress::isGlobal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress8isGlobalEv(const QHostAddress *self) {
  return self->isGlobal();
}

//  bool QHostAddress::isLinkLocal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress11isLinkLocalEv(const QHostAddress *self) {
  return self->isLinkLocal();
}

//  bool QHostAddress::isSiteLocal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress11isSiteLocalEv(const QHostAddress *self) {
  return self->isSiteLocal();
}

//  bool QHostAddress::isUniqueLocalUnicast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress20isUniqueLocalUnicastEv(
    const QHostAddress *self) {
  return self->isUniqueLocalUnicast();
}

//  bool QHostAddress::isMulticast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress11isMulticastEv(const QHostAddress *self) {
  return self->isMulticast();
}

//  bool QHostAddress::isBroadcast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress11isBroadcastEv(const QHostAddress *self) {
  return self->isBroadcast();
}

//  bool QHostAddress::isPrivateUse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHostAddress12isPrivateUseEv(const QHostAddress *self) {
  return self->isPrivateUse();
}

//  std::pair<QHostAddress, int> QHostAddress::parseSubnet(const QString
//      &subnet)
extern "C" Q_DECL_EXPORT
std::pair<QHostAddress, int> *ritual_ZN12QHostAddress11parseSubnetERK7QString(
    const QString *subnet) {
  return new std::pair<QHostAddress, int>(
      QHostAddress::parseSubnet(
          *subnet));
}

//  bool operator==(QHostAddress::SpecialAddress lhs, const QHostAddress
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN12QHostAddress14SpecialAddressERKS_(
    QHostAddress::SpecialAddress lhs,
    const QHostAddress *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(QHostAddress::SpecialAddress lhs, const QHostAddress
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneN12QHostAddress14SpecialAddressERKS_(
    QHostAddress::SpecialAddress lhs,
    const QHostAddress *rhs) {
  return operator!=(lhs, *rhs);
}

//  QList<QHostAddress>::QList()
extern "C" Q_DECL_EXPORT
QList<QHostAddress> *ritual_list_make_QHostAddress() {
  return new QList<QHostAddress>();
}

//  void QList<QHostAddress>::append(const QHostAddress &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QHostAddress(
    QList<QHostAddress> *self,
    const QHostAddress *element) {
  self->append(*element);
}

//  qsizetype QList<QHostAddress>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QHostAddress(const QList<QHostAddress> *self) {
  return self->size();
}

//  const QHostAddress &QList<QHostAddress>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_list_at_QHostAddress(
    const QList<QHostAddress> *self,
    long long index) {
  return new QHostAddress(self->at(index));
}

//  QList<QHostAddress>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QHostAddress(QList<QHostAddress> *self) {
  delete self;
}

//  a std::pair<QHostAddress, int> a ritual of QHostAddress gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHostAddress__std_pair_QHostAddress_int(
    std::pair<QHostAddress, int> *self) {
  delete self;
}
