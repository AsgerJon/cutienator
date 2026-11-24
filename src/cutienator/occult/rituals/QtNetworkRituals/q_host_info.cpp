//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhostinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhostinfo.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qlist.h>

//  QHostInfo::QHostInfo(int lookupId)
extern "C" Q_DECL_EXPORT
QHostInfo *ritual_ZN9QHostInfoC1Ei(int lookupId) {
  return new QHostInfo(lookupId);
}

//  QHostInfo::QHostInfo(const QHostInfo &d)
extern "C" Q_DECL_EXPORT
QHostInfo *ritual_ZN9QHostInfoC1ERKS_(const QHostInfo *d) {
  return new QHostInfo(*d);
}

//  QHostInfo::~QHostInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfoD1Ev(QHostInfo *self) {
  delete self;
}

//  QString QHostInfo::hostName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QHostInfo8hostNameEv(const QHostInfo *self) {
  return new QString(self->hostName());
}

//  void QHostInfo::setHostName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfo11setHostNameERK7QString(
    QHostInfo *self,
    const QString *name) {
  self->setHostName(*name);
}

//  QList<QHostAddress> QHostInfo::addresses() const
extern "C" Q_DECL_EXPORT
QList<QHostAddress> *ritual_ZNK9QHostInfo9addressesEv(
    const QHostInfo *self) {
  return new QList<QHostAddress>(self->addresses());
}

//  void QHostInfo::setAddresses(const QList<QHostAddress> &addresses)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfo12setAddressesERK5QListI12QHostAddressE(
    QHostInfo *self,
    const QList<QHostAddress> *addresses) {
  self->setAddresses(*addresses);
}

//  HostInfoError QHostInfo::error() const
extern "C" Q_DECL_EXPORT
QHostInfo::HostInfoError ritual_ZNK9QHostInfo5errorEv(
    const QHostInfo *self) {
  return self->error();
}

//  void QHostInfo::setError(HostInfoError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfo8setErrorENS_13HostInfoErrorE(
    QHostInfo *self,
    QHostInfo::HostInfoError error) {
  self->setError(error);
}

//  QString QHostInfo::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QHostInfo11errorStringEv(const QHostInfo *self) {
  return new QString(self->errorString());
}

//  void QHostInfo::setErrorString(const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfo14setErrorStringERK7QString(
    QHostInfo *self,
    const QString *errorString) {
  self->setErrorString(*errorString);
}

//  void QHostInfo::setLookupId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfo11setLookupIdEi(QHostInfo *self, int id) {
  self->setLookupId(id);
}

//  int QHostInfo::lookupId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QHostInfo8lookupIdEv(const QHostInfo *self) {
  return self->lookupId();
}

//  int QHostInfo::lookupHost(const QString &name, const QObject *receiver,
//      const char *member)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QHostInfo10lookupHostERK7QStringPK7QObjectPKc(
    const QString *name,
    const QObject *receiver,
    const char *member) {
  return QHostInfo::lookupHost(*name, receiver, member);
}

//  void QHostInfo::abortHostLookup(int lookupId)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfo15abortHostLookupEi(int lookupId) {
  QHostInfo::abortHostLookup(lookupId);
}

//  QHostInfo QHostInfo::fromName(const QString &name)
extern "C" Q_DECL_EXPORT
QHostInfo *ritual_ZN9QHostInfo8fromNameERK7QString(const QString *name) {
  return new QHostInfo(QHostInfo::fromName(*name));
}

//  QString QHostInfo::localHostName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QHostInfo13localHostNameEv() {
  return new QString(QHostInfo::localHostName());
}

//  QString QHostInfo::localDomainName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QHostInfo15localDomainNameEv() {
  return new QString(QHostInfo::localDomainName());
}

//  void QHostInfo::clearCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHostInfo10clearCacheEv() {
  QHostInfo::clearCache();
}

//  QHostInfoPrivate *QHostInfo::d_func()
extern "C" Q_DECL_EXPORT
QHostInfoPrivate *ritual_ZN9QHostInfo6d_funcEv(QHostInfo *self) {
  return self->d_func();
}

//  const QHostInfoPrivate *QHostInfo::d_func() const
extern "C" Q_DECL_EXPORT
const QHostInfoPrivate *ritual_ZNK9QHostInfo6d_funcEv(
    const QHostInfo *self) {
  return self->d_func();
}

//  int QHostInfo::lookupHostImpl(const QString &name, const QObject
//      *receiver, QtPrivate::QSlotObjectBase *slotObj, const char *member)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QHostInfo14lookupHostImplERK7QStringPK7QObjectPN9QtPrivate15QSlotObjectBaseEPKc(
    const QString *name,
    const QObject *receiver,
    QtPrivate::QSlotObjectBase *slotObj,
    const char *member) {
  return QHostInfo::lookupHostImpl(*name, receiver, slotObj, member);
}
