//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhstspolicy.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QHstsPolicy::QHstsPolicy()
extern "C" Q_DECL_EXPORT
QHstsPolicy *ritual_ZN11QHstsPolicyC1Ev() {
  return new QHstsPolicy();
}

//  QHstsPolicy::QHstsPolicy(const QDateTime &expiry, PolicyFlags flags,
//      const QString &host, QUrl::ParsingMode mode)
extern "C" Q_DECL_EXPORT
QHstsPolicy *ritual_ZN11QHstsPolicyC1ERK9QDateTime6QFlagsINS_10PolicyFlagEERK7QStringN4QUrl11ParsingModeE(
    const QDateTime *expiry,
    int flags,
    const QString *host,
    QUrl::ParsingMode mode) {
  return new QHstsPolicy(
      *expiry,
      QFlags<QHstsPolicy::PolicyFlag>::fromInt(flags),
      *host,
      mode);
}

//  QHstsPolicy::QHstsPolicy(const QHstsPolicy &rhs)
extern "C" Q_DECL_EXPORT
QHstsPolicy *ritual_ZN11QHstsPolicyC1ERKS_(const QHstsPolicy *rhs) {
  return new QHstsPolicy(*rhs);
}

//  QHstsPolicy::~QHstsPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHstsPolicyD1Ev(QHstsPolicy *self) {
  delete self;
}

//  void QHstsPolicy::setHost(const QString &host, QUrl::ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHstsPolicy7setHostERK7QStringN4QUrl11ParsingModeE(
    QHstsPolicy *self,
    const QString *host,
    QUrl::ParsingMode mode) {
  self->setHost(*host, mode);
}

//  QString QHstsPolicy::host(QUrl::ComponentFormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QHstsPolicy4hostE6QFlagsIN4QUrl25ComponentFormattingOptionEE(
    const QHstsPolicy *self,
    int options) {
  return new QString(
      self->host(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(options)));
}

//  void QHstsPolicy::setExpiry(const QDateTime &expiry)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHstsPolicy9setExpiryERK9QDateTime(
    QHstsPolicy *self,
    const QDateTime *expiry) {
  self->setExpiry(*expiry);
}

//  QDateTime QHstsPolicy::expiry() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QHstsPolicy6expiryEv(const QHstsPolicy *self) {
  return new QDateTime(self->expiry());
}

//  void QHstsPolicy::setIncludesSubDomains(bool include)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHstsPolicy21setIncludesSubDomainsEb(
    QHstsPolicy *self,
    bool include) {
  self->setIncludesSubDomains(include);
}

//  bool QHstsPolicy::includesSubDomains() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHstsPolicy18includesSubDomainsEv(const QHstsPolicy *self) {
  return self->includesSubDomains();
}

//  bool QHstsPolicy::isExpired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHstsPolicy9isExpiredEv(const QHstsPolicy *self) {
  return self->isExpired();
}

//  bool QHstsPolicy::isEqual(const QHstsPolicy &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHstsPolicy7isEqualERKS_(
    const QHstsPolicy *self,
    const QHstsPolicy *other) {
  return self->isEqual(*other);
}

//  bool operator==(const QHstsPolicy &lhs, const QHstsPolicy &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QHstsPolicyS1_(
    const QHstsPolicy *lhs,
    const QHstsPolicy *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QHstsPolicy &lhs, const QHstsPolicy &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QHstsPolicyS1_(
    const QHstsPolicy *lhs,
    const QHstsPolicy *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QHstsPolicy>::QList()
extern "C" Q_DECL_EXPORT
QList<QHstsPolicy> *ritual_list_make_QHstsPolicy() {
  return new QList<QHstsPolicy>();
}

//  void QList<QHstsPolicy>::append(const QHstsPolicy &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QHstsPolicy(
    QList<QHstsPolicy> *self,
    const QHstsPolicy *element) {
  self->append(*element);
}

//  qsizetype QList<QHstsPolicy>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QHstsPolicy(const QList<QHstsPolicy> *self) {
  return self->size();
}

//  const QHstsPolicy &QList<QHstsPolicy>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QHstsPolicy *ritual_list_at_QHstsPolicy(
    const QList<QHstsPolicy> *self,
    long long index) {
  return new QHstsPolicy(self->at(index));
}

//  QList<QHstsPolicy>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QHstsPolicy(QList<QHstsPolicy> *self) {
  delete self;
}
