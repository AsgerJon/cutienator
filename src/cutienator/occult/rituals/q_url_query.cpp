//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qurlquery.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qurlquery.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>

//  QUrlQuery::QUrlQuery()
extern "C" Q_DECL_EXPORT
QUrlQuery *ritual_ZN9QUrlQueryC1Ev() {
  return new QUrlQuery();
}

//  QUrlQuery::QUrlQuery(const QUrl &url)
extern "C" Q_DECL_EXPORT
QUrlQuery *ritual_ZN9QUrlQueryC1ERK4QUrl(const QUrl *url) {
  return new QUrlQuery(*url);
}

//  QUrlQuery::QUrlQuery(const QString &queryString)
extern "C" Q_DECL_EXPORT
QUrlQuery *ritual_ZN9QUrlQueryC1ERK7QString(const QString *queryString) {
  return new QUrlQuery(*queryString);
}

//  QUrlQuery::QUrlQuery(const QUrlQuery &other)
extern "C" Q_DECL_EXPORT
QUrlQuery *ritual_ZN9QUrlQueryC1ERKS_(const QUrlQuery *other) {
  return new QUrlQuery(*other);
}

//  QUrlQuery::~QUrlQuery()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlQueryD1Ev(QUrlQuery *self) {
  delete self;
}

//  bool QUrlQuery::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QUrlQuery7isEmptyEv(const QUrlQuery *self) {
  return self->isEmpty();
}

//  bool QUrlQuery::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QUrlQuery10isDetachedEv(const QUrlQuery *self) {
  return self->isDetached();
}

//  void QUrlQuery::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlQuery5clearEv(QUrlQuery *self) {
  self->clear();
}

//  QString QUrlQuery::query(QUrl::ComponentFormattingOptions encoding) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QUrlQuery5queryE6QFlagsIN4QUrl25ComponentFormattingOptionEE(
    const QUrlQuery *self,
    int encoding) {
  return new QString(
      self->query(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(encoding)));
}

//  void QUrlQuery::setQuery(const QString &queryString)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlQuery8setQueryERK7QString(
    QUrlQuery *self,
    const QString *queryString) {
  self->setQuery(*queryString);
}

//  QString QUrlQuery::toString(QUrl::ComponentFormattingOptions encoding)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QUrlQuery8toStringE6QFlagsIN4QUrl25ComponentFormattingOptionEE(
    const QUrlQuery *self,
    int encoding) {
  return new QString(
      self->toString(
          QFlags<QUrl::ComponentFormattingOption>::fromInt(encoding)));
}

//  void QUrlQuery::setQueryDelimiters(QChar valueDelimiter, QChar
//      pairDelimiter)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlQuery18setQueryDelimitersE5QCharS0_(
    QUrlQuery *self,
    const QChar *valueDelimiter,
    const QChar *pairDelimiter) {
  self->setQueryDelimiters(*valueDelimiter, *pairDelimiter);
}

//  QChar QUrlQuery::queryValueDelimiter() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK9QUrlQuery19queryValueDelimiterEv(const QUrlQuery *self) {
  return new QChar(self->queryValueDelimiter());
}

//  QChar QUrlQuery::queryPairDelimiter() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK9QUrlQuery18queryPairDelimiterEv(const QUrlQuery *self) {
  return new QChar(self->queryPairDelimiter());
}

//  bool QUrlQuery::hasQueryItem(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QUrlQuery12hasQueryItemERK7QString(
    const QUrlQuery *self,
    const QString *key) {
  return self->hasQueryItem(*key);
}

//  void QUrlQuery::addQueryItem(const QString &key, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlQuery12addQueryItemERK7QStringS2_(
    QUrlQuery *self,
    const QString *key,
    const QString *value) {
  self->addQueryItem(*key, *value);
}

//  void QUrlQuery::removeQueryItem(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlQuery15removeQueryItemERK7QString(
    QUrlQuery *self,
    const QString *key) {
  self->removeQueryItem(*key);
}

//  QString QUrlQuery::queryItemValue(const QString &key,
//      QUrl::ComponentFormattingOptions encoding) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QUrlQuery14queryItemValueERK7QString6QFlagsIN4QUrl25ComponentFormattingOptionEE(
    const QUrlQuery *self,
    const QString *key,
    int encoding) {
  return new QString(
      self->queryItemValue(
          *key,
          QFlags<QUrl::ComponentFormattingOption>::fromInt(encoding)));
}

//  void QUrlQuery::removeAllQueryItems(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUrlQuery19removeAllQueryItemsERK7QString(
    QUrlQuery *self,
    const QString *key) {
  self->removeAllQueryItems(*key);
}
