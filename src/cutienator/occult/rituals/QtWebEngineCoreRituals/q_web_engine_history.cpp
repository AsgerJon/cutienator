//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginehistory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginehistory.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QWebEngineHistory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QWebEngineHistory10metaObjectEv(
    const QWebEngineHistory *self) {
  return self->metaObject();
}

//  void *QWebEngineHistory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QWebEngineHistory11qt_metacastEPKc(
    QWebEngineHistory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineHistory::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QWebEngineHistory11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineHistory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineHistory::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QWebEngineHistory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineHistory::tr(s, c, n));
}

//  void QWebEngineHistory::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineHistory5clearEv(QWebEngineHistory *self) {
  self->clear();
}

//  QList<QWebEngineHistoryItem> QWebEngineHistory::items() const
extern "C" Q_DECL_EXPORT
QList<QWebEngineHistoryItem> *ritual_ZNK17QWebEngineHistory5itemsEv(
    const QWebEngineHistory *self) {
  return new QList<QWebEngineHistoryItem>(self->items());
}

//  QList<QWebEngineHistoryItem> QWebEngineHistory::backItems(int maxItems)
//      const
extern "C" Q_DECL_EXPORT
QList<QWebEngineHistoryItem> *ritual_ZNK17QWebEngineHistory9backItemsEi(
    const QWebEngineHistory *self,
    int maxItems) {
  return new QList<QWebEngineHistoryItem>(self->backItems(maxItems));
}

//  QList<QWebEngineHistoryItem> QWebEngineHistory::forwardItems(int
//      maxItems) const
extern "C" Q_DECL_EXPORT
QList<QWebEngineHistoryItem> *ritual_ZNK17QWebEngineHistory12forwardItemsEi(
    const QWebEngineHistory *self,
    int maxItems) {
  return new QList<QWebEngineHistoryItem>(self->forwardItems(maxItems));
}

//  bool QWebEngineHistory::canGoBack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWebEngineHistory9canGoBackEv(
    const QWebEngineHistory *self) {
  return self->canGoBack();
}

//  bool QWebEngineHistory::canGoForward() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWebEngineHistory12canGoForwardEv(
    const QWebEngineHistory *self) {
  return self->canGoForward();
}

//  void QWebEngineHistory::back()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineHistory4backEv(QWebEngineHistory *self) {
  self->back();
}

//  void QWebEngineHistory::forward()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineHistory7forwardEv(QWebEngineHistory *self) {
  self->forward();
}

//  void QWebEngineHistory::goToItem(const QWebEngineHistoryItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineHistory8goToItemERK21QWebEngineHistoryItem(
    QWebEngineHistory *self,
    const QWebEngineHistoryItem *item) {
  self->goToItem(*item);
}

//  QWebEngineHistoryItem QWebEngineHistory::backItem() const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZNK17QWebEngineHistory8backItemEv(
    const QWebEngineHistory *self) {
  return new QWebEngineHistoryItem(self->backItem());
}

//  QWebEngineHistoryItem QWebEngineHistory::currentItem() const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZNK17QWebEngineHistory11currentItemEv(
    const QWebEngineHistory *self) {
  return new QWebEngineHistoryItem(self->currentItem());
}

//  QWebEngineHistoryItem QWebEngineHistory::forwardItem() const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZNK17QWebEngineHistory11forwardItemEv(
    const QWebEngineHistory *self) {
  return new QWebEngineHistoryItem(self->forwardItem());
}

//  QWebEngineHistoryItem QWebEngineHistory::itemAt(int i) const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryItem *ritual_ZNK17QWebEngineHistory6itemAtEi(
    const QWebEngineHistory *self,
    int i) {
  return new QWebEngineHistoryItem(self->itemAt(i));
}

//  int QWebEngineHistory::currentItemIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QWebEngineHistory16currentItemIndexEv(
    const QWebEngineHistory *self) {
  return self->currentItemIndex();
}

//  int QWebEngineHistory::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QWebEngineHistory5countEv(const QWebEngineHistory *self) {
  return self->count();
}

//  QWebEngineHistoryModel *QWebEngineHistory::itemsModel() const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryModel *ritual_ZNK17QWebEngineHistory10itemsModelEv(
    const QWebEngineHistory *self) {
  return self->itemsModel();
}

//  QWebEngineHistoryModel *QWebEngineHistory::backItemsModel() const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryModel *ritual_ZNK17QWebEngineHistory14backItemsModelEv(
    const QWebEngineHistory *self) {
  return self->backItemsModel();
}

//  QWebEngineHistoryModel *QWebEngineHistory::forwardItemsModel() const
extern "C" Q_DECL_EXPORT
QWebEngineHistoryModel *ritual_ZNK17QWebEngineHistory17forwardItemsModelEv(
    const QWebEngineHistory *self) {
  return self->forwardItemsModel();
}

//  QWebEngineHistory::QWebEngineHistory(QWebEngineHistoryPrivate *d)
extern "C" Q_DECL_EXPORT
QWebEngineHistory *ritual_ZN17QWebEngineHistoryC1EP24QWebEngineHistoryPrivate(
    QWebEngineHistoryPrivate *d) {
  return new QWebEngineHistory(d);
}

//  QWebEngineHistory::~QWebEngineHistory()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineHistoryD1Ev(QWebEngineHistory *self) {
  delete self;
}

//  QWebEngineHistoryPrivate *QWebEngineHistory::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineHistoryPrivate *ritual_ZN17QWebEngineHistory6d_funcEv(
    QWebEngineHistory *self) {
  return self->d_func();
}

//  const QWebEngineHistoryPrivate *QWebEngineHistory::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineHistoryPrivate *ritual_ZNK17QWebEngineHistory6d_funcEv(
    const QWebEngineHistory *self) {
  return self->d_func();
}

//  void QWebEngineHistory::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebEngineHistory5resetEv(QWebEngineHistory *self) {
  self->reset();
}

//  QDataStream &operator>>(QDataStream &a0, QWebEngineHistory &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR17QWebEngineHistory(
    QDataStream *a0,
    QWebEngineHistory *a1) {
  return &(operator>>(*a0, *a1));
}

//  QDataStream &operator<<(QDataStream &a0, const QWebEngineHistory &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK17QWebEngineHistory(
    QDataStream *a0,
    const QWebEngineHistory *a1) {
  return &(operator<<(*a0, *a1));
}
