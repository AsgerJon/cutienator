//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpsearchresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qhelpsearchresult.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QHelpSearchResult::QHelpSearchResult()
extern "C" Q_DECL_EXPORT
QHelpSearchResult *ritual_ZN17QHelpSearchResultC1Ev() {
  return new QHelpSearchResult();
}

//  QHelpSearchResult::QHelpSearchResult(const QHelpSearchResult &other)
extern "C" Q_DECL_EXPORT
QHelpSearchResult *ritual_ZN17QHelpSearchResultC1ERKS_(
    const QHelpSearchResult *other) {
  return new QHelpSearchResult(*other);
}

//  QHelpSearchResult::QHelpSearchResult(const QUrl &url, const QString
//      &title, const QString &snippet)
extern "C" Q_DECL_EXPORT
QHelpSearchResult *ritual_ZN17QHelpSearchResultC1ERK4QUrlRK7QStringS5_(
    const QUrl *url,
    const QString *title,
    const QString *snippet) {
  return new QHelpSearchResult(*url, *title, *snippet);
}

//  QHelpSearchResult::~QHelpSearchResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchResultD1Ev(QHelpSearchResult *self) {
  delete self;
}

//  QString QHelpSearchResult::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHelpSearchResult5titleEv(
    const QHelpSearchResult *self) {
  return new QString(self->title());
}

//  QUrl QHelpSearchResult::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QHelpSearchResult3urlEv(const QHelpSearchResult *self) {
  return new QUrl(self->url());
}

//  QString QHelpSearchResult::snippet() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHelpSearchResult7snippetEv(
    const QHelpSearchResult *self) {
  return new QString(self->snippet());
}

//  QList<QHelpSearchResult>::QList()
extern "C" Q_DECL_EXPORT
QList<QHelpSearchResult> *ritual_list_make_QHelpSearchResult() {
  return new QList<QHelpSearchResult>();
}

//  void QList<QHelpSearchResult>::append(const QHelpSearchResult &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QHelpSearchResult(
    QList<QHelpSearchResult> *self,
    const QHelpSearchResult *element) {
  self->append(*element);
}

//  qsizetype QList<QHelpSearchResult>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QHelpSearchResult(
    const QList<QHelpSearchResult> *self) {
  return self->size();
}

//  const QHelpSearchResult &QList<QHelpSearchResult>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QHelpSearchResult *ritual_list_at_QHelpSearchResult(
    const QList<QHelpSearchResult> *self,
    long long index) {
  return new QHelpSearchResult(self->at(index));
}

//  QList<QHelpSearchResult>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QHelpSearchResult(QList<QHelpSearchResult> *self) {
  delete self;
}
