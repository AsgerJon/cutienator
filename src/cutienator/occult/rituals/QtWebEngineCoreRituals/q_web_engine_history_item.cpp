//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginehistory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginehistory.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>

//  QWebEngineHistoryItem::QWebEngineHistoryItem(const QWebEngineHistoryItem
//      &other)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZN21QWebEngineHistoryItemC1ERKS_(
    const QWebEngineHistoryItem *other) {
  return new QWebEngineHistoryItem(*other);
}

//  QWebEngineHistoryItem::QWebEngineHistoryItem(QWebEngineHistoryItem
//      &&other)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZN21QWebEngineHistoryItemC1EOS_(
    QWebEngineHistoryItem *other) {
  return new QWebEngineHistoryItem(std::move(*other));
}

//  QWebEngineHistoryItem &QWebEngineHistoryItem::operator=(const
//      QWebEngineHistoryItem &other)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZN21QWebEngineHistoryItemaSERKS_(
    QWebEngineHistoryItem *self,
    const QWebEngineHistoryItem *other) {
  return &(self->operator=(*other));
}

//  QWebEngineHistoryItem
//      &QWebEngineHistoryItem::operator=(QWebEngineHistoryItem &&other)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZN21QWebEngineHistoryItemaSEOS_(
    QWebEngineHistoryItem *self,
    QWebEngineHistoryItem *other) {
  return &(self->operator=(std::move(*other)));
}

//  QWebEngineHistoryItem::~QWebEngineHistoryItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHistoryItemD1Ev(QWebEngineHistoryItem *self) {
  delete self;
}

//  QUrl QWebEngineHistoryItem::originalUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QWebEngineHistoryItem11originalUrlEv(
    const QWebEngineHistoryItem *self) {
  return new QUrl(self->originalUrl());
}

//  QUrl QWebEngineHistoryItem::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QWebEngineHistoryItem3urlEv(
    const QWebEngineHistoryItem *self) {
  return new QUrl(self->url());
}

//  QString QWebEngineHistoryItem::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineHistoryItem5titleEv(
    const QWebEngineHistoryItem *self) {
  return new QString(self->title());
}

//  QDateTime QWebEngineHistoryItem::lastVisited() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK21QWebEngineHistoryItem11lastVisitedEv(
    const QWebEngineHistoryItem *self) {
  return new QDateTime(self->lastVisited());
}

//  QUrl QWebEngineHistoryItem::iconUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QWebEngineHistoryItem7iconUrlEv(
    const QWebEngineHistoryItem *self) {
  return new QUrl(self->iconUrl());
}

//  bool QWebEngineHistoryItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineHistoryItem7isValidEv(
    const QWebEngineHistoryItem *self) {
  return self->isValid();
}

//  void QWebEngineHistoryItem::swap(QWebEngineHistoryItem &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHistoryItem4swapERS_(
    QWebEngineHistoryItem *self,
    QWebEngineHistoryItem *other) {
  self->swap(*other);
}

//  QWebEngineHistoryItem::QWebEngineHistoryItem(QWebEngineHistoryItemPrivate
//      *priv)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZN21QWebEngineHistoryItemC1EP28QWebEngineHistoryItemPrivate(
    QWebEngineHistoryItemPrivate *priv) {
  return new QWebEngineHistoryItem(priv);
}

//  QWebEngineHistoryItemPrivate *QWebEngineHistoryItem::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItemPrivate *ritual_ZN21QWebEngineHistoryItem6d_funcEv(
    QWebEngineHistoryItem *self) {
  return self->d_func();
}

//  const QWebEngineHistoryItemPrivate *QWebEngineHistoryItem::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineHistoryItemPrivate *ritual_ZNK21QWebEngineHistoryItem6d_funcEv(
    const QWebEngineHistoryItem *self) {
  return self->d_func();
}

//  QList<QWebEngineHistoryItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QWebEngineHistoryItem> *ritual_list_make_QWebEngineHistoryItem() {
  return new QList<QWebEngineHistoryItem>();
}

//  void QList<QWebEngineHistoryItem>::append(const QWebEngineHistoryItem
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWebEngineHistoryItem(
    QList<QWebEngineHistoryItem> *self,
    const QWebEngineHistoryItem *element) {
  self->append(*element);
}

//  qsizetype QList<QWebEngineHistoryItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWebEngineHistoryItem(
    const QList<QWebEngineHistoryItem> *self) {
  return self->size();
}

//  const QWebEngineHistoryItem &QList<QWebEngineHistoryItem>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_list_at_QWebEngineHistoryItem(
    const QList<QWebEngineHistoryItem> *self,
    long long index) {
  return new QWebEngineHistoryItem(self->at(index));
}

//  QList<QWebEngineHistoryItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWebEngineHistoryItem(
    QList<QWebEngineHistoryItem> *self) {
  delete self;
}
