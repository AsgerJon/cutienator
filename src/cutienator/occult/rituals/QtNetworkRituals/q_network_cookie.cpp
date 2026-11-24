//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkcookie.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qnetworkcookie.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>

//  QNetworkCookie::QNetworkCookie(const QByteArray &name, const QByteArray
//      &value)
extern "C" Q_DECL_EXPORT
QNetworkCookie *ritual_ZN14QNetworkCookieC1ERK10QByteArrayS2_(
    const QByteArray *name,
    const QByteArray *value) {
  return new QNetworkCookie(*name, *value);
}

//  QNetworkCookie::QNetworkCookie(const QNetworkCookie &other)
extern "C" Q_DECL_EXPORT
QNetworkCookie *ritual_ZN14QNetworkCookieC1ERKS_(
    const QNetworkCookie *other) {
  return new QNetworkCookie(*other);
}

//  QNetworkCookie::~QNetworkCookie()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookieD1Ev(QNetworkCookie *self) {
  delete self;
}

//  bool QNetworkCookie::operator==(const QNetworkCookie &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QNetworkCookieeqERKS_(
    const QNetworkCookie *self,
    const QNetworkCookie *other) {
  return self->operator==(*other);
}

//  bool QNetworkCookie::operator!=(const QNetworkCookie &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QNetworkCookieneERKS_(
    const QNetworkCookie *self,
    const QNetworkCookie *other) {
  return self->operator!=(*other);
}

//  bool QNetworkCookie::isSecure() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QNetworkCookie8isSecureEv(const QNetworkCookie *self) {
  return self->isSecure();
}

//  void QNetworkCookie::setSecure(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie9setSecureEb(
    QNetworkCookie *self,
    bool enable) {
  self->setSecure(enable);
}

//  bool QNetworkCookie::isHttpOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QNetworkCookie10isHttpOnlyEv(const QNetworkCookie *self) {
  return self->isHttpOnly();
}

//  void QNetworkCookie::setHttpOnly(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie11setHttpOnlyEb(
    QNetworkCookie *self,
    bool enable) {
  self->setHttpOnly(enable);
}

//  SameSite QNetworkCookie::sameSitePolicy() const
extern "C" Q_DECL_EXPORT
QNetworkCookie::SameSite ritual_ZNK14QNetworkCookie14sameSitePolicyEv(
    const QNetworkCookie *self) {
  return self->sameSitePolicy();
}

//  void QNetworkCookie::setSameSitePolicy(SameSite sameSite)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie17setSameSitePolicyENS_8SameSiteE(
    QNetworkCookie *self,
    QNetworkCookie::SameSite sameSite) {
  self->setSameSitePolicy(sameSite);
}

//  bool QNetworkCookie::isSessionCookie() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QNetworkCookie15isSessionCookieEv(
    const QNetworkCookie *self) {
  return self->isSessionCookie();
}

//  QDateTime QNetworkCookie::expirationDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK14QNetworkCookie14expirationDateEv(
    const QNetworkCookie *self) {
  return new QDateTime(self->expirationDate());
}

//  void QNetworkCookie::setExpirationDate(const QDateTime &date)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie17setExpirationDateERK9QDateTime(
    QNetworkCookie *self,
    const QDateTime *date) {
  self->setExpirationDate(*date);
}

//  QString QNetworkCookie::domain() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QNetworkCookie6domainEv(const QNetworkCookie *self) {
  return new QString(self->domain());
}

//  void QNetworkCookie::setDomain(const QString &domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie9setDomainERK7QString(
    QNetworkCookie *self,
    const QString *domain) {
  self->setDomain(*domain);
}

//  QString QNetworkCookie::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QNetworkCookie4pathEv(const QNetworkCookie *self) {
  return new QString(self->path());
}

//  void QNetworkCookie::setPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie7setPathERK7QString(
    QNetworkCookie *self,
    const QString *path) {
  self->setPath(*path);
}

//  QByteArray QNetworkCookie::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QNetworkCookie4nameEv(const QNetworkCookie *self) {
  return new QByteArray(self->name());
}

//  void QNetworkCookie::setName(const QByteArray &cookieName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie7setNameERK10QByteArray(
    QNetworkCookie *self,
    const QByteArray *cookieName) {
  self->setName(*cookieName);
}

//  QByteArray QNetworkCookie::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QNetworkCookie5valueEv(const QNetworkCookie *self) {
  return new QByteArray(self->value());
}

//  void QNetworkCookie::setValue(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie8setValueERK10QByteArray(
    QNetworkCookie *self,
    const QByteArray *value) {
  self->setValue(*value);
}

//  QByteArray QNetworkCookie::toRawForm(RawForm form) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QNetworkCookie9toRawFormENS_7RawFormE(
    const QNetworkCookie *self,
    QNetworkCookie::RawForm form) {
  return new QByteArray(self->toRawForm(form));
}

//  bool QNetworkCookie::hasSameIdentifier(const QNetworkCookie &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QNetworkCookie17hasSameIdentifierERKS_(
    const QNetworkCookie *self,
    const QNetworkCookie *other) {
  return self->hasSameIdentifier(*other);
}

//  void QNetworkCookie::normalize(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNetworkCookie9normalizeERK4QUrl(
    QNetworkCookie *self,
    const QUrl *url) {
  self->normalize(*url);
}

//  QList<QNetworkCookie> QNetworkCookie::parseCookies(QByteArrayView
//      cookieString)
extern "C" Q_DECL_EXPORT
QList<QNetworkCookie> *ritual_ZN14QNetworkCookie12parseCookiesE14QByteArrayView(
    const QByteArrayView *cookieString) {
  return new QList<QNetworkCookie>(
      QNetworkCookie::parseCookies(
          *cookieString));
}

//  QList<QNetworkCookie>::QList()
extern "C" Q_DECL_EXPORT
QList<QNetworkCookie> *ritual_list_make_QNetworkCookie() {
  return new QList<QNetworkCookie>();
}

//  void QList<QNetworkCookie>::append(const QNetworkCookie &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNetworkCookie(
    QList<QNetworkCookie> *self,
    const QNetworkCookie *element) {
  self->append(*element);
}

//  qsizetype QList<QNetworkCookie>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNetworkCookie(
    const QList<QNetworkCookie> *self) {
  return self->size();
}

//  const QNetworkCookie &QList<QNetworkCookie>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QNetworkCookie *ritual_list_at_QNetworkCookie(
    const QList<QNetworkCookie> *self,
    long long index) {
  return new QNetworkCookie(self->at(index));
}

//  QList<QNetworkCookie>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNetworkCookie(QList<QNetworkCookie> *self) {
  delete self;
}
