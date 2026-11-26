//  Written by dev_tooling.RitualGenerator from the records of QtCore/qurl.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qlist.h>
#include <QtCore/QString>
#include <QtCore/QUrl>
#include <QtCore/QByteArray>
#include <QtCore/QList>

//  QUrl::QUrl()
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrlC1Ev() {
  return new QUrl();
}

//  QUrl::QUrl(const QUrl &copy)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrlC1ERKS_(const QUrl *copy) {
  return new QUrl(*copy);
}

//  QUrl &QUrl::operator=(const QUrl &copy)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrlaSERKS_(QUrl *self, const QUrl *copy) {
  return &(self->operator=(*copy));
}

#if !(defined(QT_NO_URL_CAST_FROM_STRING))
//  QUrl::QUrl(const QString &url, ParsingMode mode)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrlC1ERK7QStringNS_11ParsingModeE(
    const QString *url,
    QUrl::ParsingMode mode) {
  return new QUrl(*url, mode);
}
#endif  // !(defined(QT_NO_URL_CAST_FROM_STRING))

#if !(defined(QT_NO_URL_CAST_FROM_STRING))
//  QUrl &QUrl::operator=(const QString &url)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrlaSERK7QString(QUrl *self, const QString *url) {
  return &(self->operator=(*url));
}
#endif  // !(defined(QT_NO_URL_CAST_FROM_STRING))

//  QUrl::QUrl(QUrl &&other)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrlC1EOS_(QUrl *other) {
  return new QUrl(std::move(*other));
}

//  QUrl &QUrl::operator=(QUrl &&other)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrlaSEOS_(QUrl *self, QUrl *other) {
  return &(self->operator=(std::move(*other)));
}

//  QUrl::~QUrl()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrlD1Ev(QUrl *self) {
  delete self;
}

//  void QUrl::swap(QUrl &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl4swapERS_(QUrl *self, QUrl *other) {
  self->swap(*other);
}

//  void QUrl::setUrl(const QString &url, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl6setUrlERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *url,
    QUrl::ParsingMode mode) {
  self->setUrl(*url, mode);
}

//  QString QUrl::url(FormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl3urlE12QUrlTwoFlagsINS_19UrlFormattingOptionENS_25ComponentFormattingOptionEE(
    const QUrl *self,
    const QUrl::FormattingOptions *options) {
  return new QString(self->url(*options));
}

//  QString QUrl::toString(FormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl8toStringE12QUrlTwoFlagsINS_19UrlFormattingOptionENS_25ComponentFormattingOptionEE(
    const QUrl *self,
    const QUrl::FormattingOptions *options) {
  return new QString(self->toString(*options));
}

//  QString QUrl::toDisplayString(FormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl15toDisplayStringE12QUrlTwoFlagsINS_19UrlFormattingOptionENS_25ComponentFormattingOptionEE(
    const QUrl *self,
    const QUrl::FormattingOptions *options) {
  return new QString(self->toDisplayString(*options));
}

//  QUrl QUrl::adjusted(FormattingOptions options) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK4QUrl8adjustedE12QUrlTwoFlagsINS_19UrlFormattingOptionENS_25ComponentFormattingOptionEE(
    const QUrl *self,
    const QUrl::FormattingOptions *options) {
  return new QUrl(self->adjusted(*options));
}

//  QByteArray QUrl::toEncoded(FormattingOptions options) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK4QUrl9toEncodedE12QUrlTwoFlagsINS_19UrlFormattingOptionENS_25ComponentFormattingOptionEE(
    const QUrl *self,
    const QUrl::FormattingOptions *options) {
  return new QByteArray(self->toEncoded(*options));
}

//  QUrl QUrl::fromEncoded(QByteArrayView input, ParsingMode mode)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrl11fromEncodedE14QByteArrayViewNS_11ParsingModeE(
    const QByteArrayView *input,
    QUrl::ParsingMode mode) {
  return new QUrl(QUrl::fromEncoded(*input, mode));
}

//  QUrl QUrl::fromUserInput(const QString &userInput, const QString
//      &workingDirectory, UserInputResolutionOptions options)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrl13fromUserInputERK7QStringS2_6QFlagsINS_25UserInputResolutionOptionEE(
    const QString *userInput,
    const QString *workingDirectory,
    int options) {
  return new QUrl(
      QUrl::fromUserInput(
          *userInput,
          *workingDirectory,
          QFlags<QUrl::UserInputResolutionOption>::fromInt(options)));
}

//  bool QUrl::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl7isValidEv(const QUrl *self) {
  return self->isValid();
}

//  QString QUrl::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl11errorStringEv(const QUrl *self) {
  return new QString(self->errorString());
}

//  bool QUrl::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl7isEmptyEv(const QUrl *self) {
  return self->isEmpty();
}

//  void QUrl::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl5clearEv(QUrl *self) {
  self->clear();
}

//  void QUrl::setScheme(const QString &scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl9setSchemeERK7QString(QUrl *self, const QString *scheme) {
  self->setScheme(*scheme);
}

//  QString QUrl::scheme() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl6schemeEv(const QUrl *self) {
  return new QString(self->scheme());
}

//  void QUrl::setAuthority(const QString &authority, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl12setAuthorityERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *authority,
    QUrl::ParsingMode mode) {
  self->setAuthority(*authority, mode);
}

//  QString QUrl::authority(ComponentFormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl9authorityE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int options) {
  return new QString(
      self->authority(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(options)));
}

//  void QUrl::setUserInfo(const QString &userInfo, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl11setUserInfoERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *userInfo,
    QUrl::ParsingMode mode) {
  self->setUserInfo(*userInfo, mode);
}

//  QString QUrl::userInfo(ComponentFormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl8userInfoE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int options) {
  return new QString(
      self->userInfo(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(options)));
}

//  void QUrl::setUserName(const QString &userName, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl11setUserNameERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *userName,
    QUrl::ParsingMode mode) {
  self->setUserName(*userName, mode);
}

//  QString QUrl::userName(ComponentFormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl8userNameE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int options) {
  return new QString(
      self->userName(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(options)));
}

//  void QUrl::setPassword(const QString &password, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl11setPasswordERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *password,
    QUrl::ParsingMode mode) {
  self->setPassword(*password, mode);
}

//  QString QUrl::password(ComponentFormattingOptions a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl8passwordE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int a0) {
  return new QString(
      self->password(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(a0)));
}

//  void QUrl::setHost(const QString &host, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl7setHostERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *host,
    QUrl::ParsingMode mode) {
  self->setHost(*host, mode);
}

//  QString QUrl::host(ComponentFormattingOptions a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl4hostE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int a0) {
  return new QString(
      self->host(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(a0)));
}

//  void QUrl::setPort(int port)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl7setPortEi(QUrl *self, int port) {
  self->setPort(port);
}

//  int QUrl::port(int defaultPort) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QUrl4portEi(const QUrl *self, int defaultPort) {
  return self->port(defaultPort);
}

//  void QUrl::setPath(const QString &path, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl7setPathERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *path,
    QUrl::ParsingMode mode) {
  self->setPath(*path, mode);
}

//  QString QUrl::path(ComponentFormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl4pathE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int options) {
  return new QString(
      self->path(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(options)));
}

//  QString QUrl::fileName(ComponentFormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl8fileNameE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int options) {
  return new QString(
      self->fileName(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(options)));
}

//  bool QUrl::hasQuery() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl8hasQueryEv(const QUrl *self) {
  return self->hasQuery();
}

//  void QUrl::setQuery(const QString &query, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl8setQueryERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *query,
    QUrl::ParsingMode mode) {
  self->setQuery(*query, mode);
}

//  void QUrl::setQuery(const QUrlQuery &query)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl8setQueryERK9QUrlQuery(
    QUrl *self,
    const QUrlQuery *query) {
  self->setQuery(*query);
}

//  QString QUrl::query(ComponentFormattingOptions a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl5queryE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int a0) {
  return new QString(
      self->query(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(a0)));
}

//  bool QUrl::hasFragment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl11hasFragmentEv(const QUrl *self) {
  return self->hasFragment();
}

//  QString QUrl::fragment(ComponentFormattingOptions options) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl8fragmentE6QFlagsINS_25ComponentFormattingOptionEE(
    const QUrl *self,
    int options) {
  return new QString(
      self->fragment(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(options)));
}

//  void QUrl::setFragment(const QString &fragment, ParsingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl11setFragmentERK7QStringNS_11ParsingModeE(
    QUrl *self,
    const QString *fragment,
    QUrl::ParsingMode mode) {
  self->setFragment(*fragment, mode);
}

//  QUrl QUrl::resolved(const QUrl &relative) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK4QUrl8resolvedERKS_(const QUrl *self, const QUrl *relative) {
  return new QUrl(self->resolved(*relative));
}

//  bool QUrl::isRelative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl10isRelativeEv(const QUrl *self) {
  return self->isRelative();
}

//  bool QUrl::isParentOf(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl10isParentOfERKS_(const QUrl *self, const QUrl *url) {
  return self->isParentOf(*url);
}

//  bool QUrl::isLocalFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl11isLocalFileEv(const QUrl *self) {
  return self->isLocalFile();
}

//  QUrl QUrl::fromLocalFile(const QString &localfile)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN4QUrl13fromLocalFileERK7QString(const QString *localfile) {
  return new QUrl(QUrl::fromLocalFile(*localfile));
}

//  QString QUrl::toLocalFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QUrl11toLocalFileEv(const QUrl *self) {
  return new QString(self->toLocalFile());
}

//  void QUrl::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl6detachEv(QUrl *self) {
  self->detach();
}

//  bool QUrl::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl10isDetachedEv(const QUrl *self) {
  return self->isDetached();
}

//  bool QUrl::matches(const QUrl &url, FormattingOptions options) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QUrl7matchesERKS_12QUrlTwoFlagsINS_19UrlFormattingOptionENS_25ComponentFormattingOptionEE(
    const QUrl *self,
    const QUrl *url,
    const QUrl::FormattingOptions *options) {
  return self->matches(*url, *options);
}

//  QString QUrl::fromPercentEncoding(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QUrl19fromPercentEncodingERK10QByteArray(
    const QByteArray *a0) {
  return new QString(QUrl::fromPercentEncoding(*a0));
}

//  QByteArray QUrl::toPercentEncoding(const QString &a0, const QByteArray
//      &exclude, const QByteArray &include)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN4QUrl17toPercentEncodingERK7QStringRK10QByteArrayS5_(
    const QString *a0,
    const QByteArray *exclude,
    const QByteArray *include) {
  return new QByteArray(QUrl::toPercentEncoding(*a0, *exclude, *include));
}

//  QString QUrl::fromAce(const QByteArray &domain, AceProcessingOptions
//      options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QUrl7fromAceERK10QByteArray6QFlagsINS_19AceProcessingOptionEE(
    const QByteArray *domain,
    int options) {
  return new QString(
      QUrl::fromAce(
          *domain,
          QFlags<QUrl::AceProcessingOption>::fromInt(options)));
}

//  QByteArray QUrl::toAce(const QString &domain, AceProcessingOptions
//      options)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN4QUrl5toAceERK7QString6QFlagsINS_19AceProcessingOptionEE(
    const QString *domain,
    int options) {
  return new QByteArray(
      QUrl::toAce(
          *domain,
          QFlags<QUrl::AceProcessingOption>::fromInt(options)));
}

//  QStringList QUrl::idnWhitelist()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN4QUrl12idnWhitelistEv() {
  return new QList<QString>(QUrl::idnWhitelist());
}

//  QStringList QUrl::toStringList(const QList<QUrl> &uris, FormattingOptions
//      options)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN4QUrl12toStringListERK5QListIS_E12QUrlTwoFlagsINS_19UrlFormattingOptionENS_25ComponentFormattingOptionEE(
    const QList<QUrl> *uris,
    const QUrl::FormattingOptions *options) {
  return new QList<QString>(QUrl::toStringList(*uris, *options));
}

//  QList<QUrl> QUrl::fromStringList(const QStringList &uris, ParsingMode
//      mode)
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZN4QUrl14fromStringListERK5QListI7QStringENS_11ParsingModeE(
    const QList<QString> *uris,
    QUrl::ParsingMode mode) {
  return new QList<QUrl>(QUrl::fromStringList(*uris, mode));
}

//  void QUrl::setIdnWhitelist(const QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl15setIdnWhitelistERK5QListI7QStringE(
    const QList<QString> *a0) {
  QUrl::setIdnWhitelist(*a0);
}

//  bool operator==(const QUrl &lhs, const QUrl &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK4QUrlS1_(const QUrl *lhs, const QUrl *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QUrl &lhs, const QUrl &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK4QUrlS1_(const QUrl *lhs, const QUrl *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QUrl &lhs, const QUrl &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK4QUrlS1_(const QUrl *lhs, const QUrl *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QUrl &lhs, const QUrl &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK4QUrlS1_(const QUrl *lhs, const QUrl *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QUrl &lhs, const QUrl &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK4QUrlS1_(const QUrl *lhs, const QUrl *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QUrl &lhs, const QUrl &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK4QUrlS1_(const QUrl *lhs, const QUrl *rhs) {
  return operator>=(*lhs, *rhs);
}

//  void QUrl::detachToClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QUrl13detachToClearEv(QUrl *self) {
  self->detachToClear();
}

//  DataPtr &QUrl::data_ptr()
extern "C" Q_DECL_EXPORT
QUrl::DataPtr *ritual_ZN4QUrl8data_ptrEv(QUrl *self) {
  return &(self->data_ptr());
}

//  QList<QUrl>::QList()
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_list_make_QUrl() {
  return new QList<QUrl>();
}

//  void QList<QUrl>::append(const QUrl &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QUrl(QList<QUrl> *self, const QUrl *element) {
  self->append(*element);
}

//  qsizetype QList<QUrl>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QUrl(const QList<QUrl> *self) {
  return self->size();
}

//  const QUrl &QList<QUrl>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_list_at_QUrl(const QList<QUrl> *self, long long index) {
  return new QUrl(self->at(index));
}

//  QList<QUrl>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QUrl(QList<QUrl> *self) {
  delete self;
}
