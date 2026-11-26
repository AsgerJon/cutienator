//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkinterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_NETWORKINTERFACE)
#include <QtNetwork/qnetworkinterface.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qlist.h>

//  QNetworkAddressEntry::QNetworkAddressEntry()
extern "C" Q_DECL_EXPORT
QNetworkAddressEntry *ritual_ZN20QNetworkAddressEntryC1Ev() {
  return new QNetworkAddressEntry();
}

//  QNetworkAddressEntry::QNetworkAddressEntry(const QNetworkAddressEntry
//      &other)
extern "C" Q_DECL_EXPORT
QNetworkAddressEntry *ritual_ZN20QNetworkAddressEntryC1ERKS_(
    const QNetworkAddressEntry *other) {
  return new QNetworkAddressEntry(*other);
}

//  QNetworkAddressEntry
//      &QNetworkAddressEntry::operator=(QNetworkAddressEntry &&other)
extern "C" Q_DECL_EXPORT
QNetworkAddressEntry *ritual_ZN20QNetworkAddressEntryaSEOS_(
    QNetworkAddressEntry *self,
    QNetworkAddressEntry *other) {
  return &(self->operator=(std::move(*other)));
}

//  QNetworkAddressEntry &QNetworkAddressEntry::operator=(const
//      QNetworkAddressEntry &other)
extern "C" Q_DECL_EXPORT
QNetworkAddressEntry *ritual_ZN20QNetworkAddressEntryaSERKS_(
    QNetworkAddressEntry *self,
    const QNetworkAddressEntry *other) {
  return &(self->operator=(*other));
}

//  QNetworkAddressEntry::~QNetworkAddressEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntryD1Ev(QNetworkAddressEntry *self) {
  delete self;
}

//  void QNetworkAddressEntry::swap(QNetworkAddressEntry &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry4swapERS_(
    QNetworkAddressEntry *self,
    QNetworkAddressEntry *other) {
  self->swap(*other);
}

//  bool QNetworkAddressEntry::operator==(const QNetworkAddressEntry &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QNetworkAddressEntryeqERKS_(
    const QNetworkAddressEntry *self,
    const QNetworkAddressEntry *other) {
  return self->operator==(*other);
}

//  bool QNetworkAddressEntry::operator!=(const QNetworkAddressEntry &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QNetworkAddressEntryneERKS_(
    const QNetworkAddressEntry *self,
    const QNetworkAddressEntry *other) {
  return self->operator!=(*other);
}

//  DnsEligibilityStatus QNetworkAddressEntry::dnsEligibility() const
extern "C" Q_DECL_EXPORT
QNetworkAddressEntry::DnsEligibilityStatus ritual_ZNK20QNetworkAddressEntry14dnsEligibilityEv(
    const QNetworkAddressEntry *self) {
  return self->dnsEligibility();
}

//  void QNetworkAddressEntry::setDnsEligibility(DnsEligibilityStatus status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry17setDnsEligibilityENS_20DnsEligibilityStatusE(
    QNetworkAddressEntry *self,
    QNetworkAddressEntry::DnsEligibilityStatus status) {
  self->setDnsEligibility(status);
}

//  QHostAddress QNetworkAddressEntry::ip() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK20QNetworkAddressEntry2ipEv(
    const QNetworkAddressEntry *self) {
  return new QHostAddress(self->ip());
}

//  void QNetworkAddressEntry::setIp(const QHostAddress &newIp)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry5setIpERK12QHostAddress(
    QNetworkAddressEntry *self,
    const QHostAddress *newIp) {
  self->setIp(*newIp);
}

//  QHostAddress QNetworkAddressEntry::netmask() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK20QNetworkAddressEntry7netmaskEv(
    const QNetworkAddressEntry *self) {
  return new QHostAddress(self->netmask());
}

//  void QNetworkAddressEntry::setNetmask(const QHostAddress &newNetmask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry10setNetmaskERK12QHostAddress(
    QNetworkAddressEntry *self,
    const QHostAddress *newNetmask) {
  self->setNetmask(*newNetmask);
}

//  int QNetworkAddressEntry::prefixLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QNetworkAddressEntry12prefixLengthEv(
    const QNetworkAddressEntry *self) {
  return self->prefixLength();
}

//  void QNetworkAddressEntry::setPrefixLength(int length)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry15setPrefixLengthEi(
    QNetworkAddressEntry *self,
    int length) {
  self->setPrefixLength(length);
}

//  QHostAddress QNetworkAddressEntry::broadcast() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK20QNetworkAddressEntry9broadcastEv(
    const QNetworkAddressEntry *self) {
  return new QHostAddress(self->broadcast());
}

//  void QNetworkAddressEntry::setBroadcast(const QHostAddress &newBroadcast)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry12setBroadcastERK12QHostAddress(
    QNetworkAddressEntry *self,
    const QHostAddress *newBroadcast) {
  self->setBroadcast(*newBroadcast);
}

//  bool QNetworkAddressEntry::isLifetimeKnown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QNetworkAddressEntry15isLifetimeKnownEv(
    const QNetworkAddressEntry *self) {
  return self->isLifetimeKnown();
}

//  QDeadlineTimer QNetworkAddressEntry::preferredLifetime() const
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZNK20QNetworkAddressEntry17preferredLifetimeEv(
    const QNetworkAddressEntry *self) {
  return new QDeadlineTimer(self->preferredLifetime());
}

//  QDeadlineTimer QNetworkAddressEntry::validityLifetime() const
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZNK20QNetworkAddressEntry16validityLifetimeEv(
    const QNetworkAddressEntry *self) {
  return new QDeadlineTimer(self->validityLifetime());
}

//  void QNetworkAddressEntry::setAddressLifetime(QDeadlineTimer preferred,
//      QDeadlineTimer validity)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry18setAddressLifetimeE14QDeadlineTimerS0_(
    QNetworkAddressEntry *self,
    const QDeadlineTimer *preferred,
    const QDeadlineTimer *validity) {
  self->setAddressLifetime(*preferred, *validity);
}

//  void QNetworkAddressEntry::clearAddressLifetime()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkAddressEntry20clearAddressLifetimeEv(
    QNetworkAddressEntry *self) {
  self->clearAddressLifetime();
}

//  bool QNetworkAddressEntry::isPermanent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QNetworkAddressEntry11isPermanentEv(
    const QNetworkAddressEntry *self) {
  return self->isPermanent();
}

//  bool QNetworkAddressEntry::isTemporary() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QNetworkAddressEntry11isTemporaryEv(
    const QNetworkAddressEntry *self) {
  return self->isTemporary();
}

//  QList<QNetworkAddressEntry>::QList()
extern "C" Q_DECL_EXPORT
QList<QNetworkAddressEntry> *ritual_list_make_QNetworkAddressEntry() {
  return new QList<QNetworkAddressEntry>();
}

//  void QList<QNetworkAddressEntry>::append(const QNetworkAddressEntry
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNetworkAddressEntry(
    QList<QNetworkAddressEntry> *self,
    const QNetworkAddressEntry *element) {
  self->append(*element);
}

//  qsizetype QList<QNetworkAddressEntry>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNetworkAddressEntry(
    const QList<QNetworkAddressEntry> *self) {
  return self->size();
}

//  const QNetworkAddressEntry &QList<QNetworkAddressEntry>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QNetworkAddressEntry *ritual_list_at_QNetworkAddressEntry(
    const QList<QNetworkAddressEntry> *self,
    long long index) {
  return new QNetworkAddressEntry(self->at(index));
}

//  QList<QNetworkAddressEntry>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNetworkAddressEntry(
    QList<QNetworkAddressEntry> *self) {
  delete self;
}

#endif  // !defined(QT_NO_NETWORKINTERFACE)
