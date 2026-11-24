//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfiltercompositor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlfiltercompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlfilterbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>

//  Only a class built on QQmlFilterCompositor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlFilterCompositor : QQmlFilterCompositor {
  using QQmlFilterCompositor::refreshCache;
};

//  const QMetaObject *QQmlFilterCompositor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlFilterCompositor10metaObjectEv(
    const QQmlFilterCompositor *self) {
  return self->metaObject();
}

//  QString QQmlFilterCompositor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlFilterCompositor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlFilterCompositor::tr(s, c, n));
}

//  void QQmlFilterCompositor::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlFilterCompositor22qt_qmlMarker_anonymousEv(
    QQmlFilterCompositor *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlFilterCompositor::QQmlFilterCompositor(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlFilterCompositor *ritual_ZN20QQmlFilterCompositorC1EP7QObject(
    QObject *parent) {
  return new QQmlFilterCompositor(parent);
}

//  QList<QQmlFilterBase *> QQmlFilterCompositor::filters()
extern "C" Q_DECL_EXPORT
QList<QQmlFilterBase *> *ritual_ZN20QQmlFilterCompositor7filtersEv(
    QQmlFilterCompositor *self) {
  return new QList<QQmlFilterBase *>(self->filters());
}

//  bool QQmlFilterCompositor::filterAcceptsRowInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlFilterCompositor24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterCompositor *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlFilterCompositor::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlFilterCompositor27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterCompositor *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsColumnInternal(a0, *a1, a2);
}

//  void QQmlFilterCompositor::updateFilters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlFilterCompositor13updateFiltersEv(
    QQmlFilterCompositor *self) {
  self->updateFilters();
}

//  void QQmlFilterCompositor::append(QQmlFilterBase *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlFilterCompositor6appendEP14QQmlFilterBase(
    QQmlFilterCompositor *self,
    QQmlFilterBase *a0) {
  self->append(a0);
}

//  qsizetype QQmlFilterCompositor::count()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QQmlFilterCompositor5countEv(
    QQmlFilterCompositor *self) {
  return self->count();
}

//  QQmlFilterBase *QQmlFilterCompositor::at(qsizetype a0)
extern "C" Q_DECL_EXPORT
QQmlFilterBase *ritual_ZN20QQmlFilterCompositor2atEx(
    QQmlFilterCompositor *self,
    qsizetype a0) {
  return self->at(a0);
}

//  void QQmlFilterCompositor::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlFilterCompositor5clearEv(QQmlFilterCompositor *self) {
  self->clear();
}

//  QQmlFilterCompositor::QQmlFilterCompositor(QQmlFilterBasePrivate *priv,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlFilterCompositor *ritual_ZN20QQmlFilterCompositorC1EP21QQmlFilterBasePrivateP7QObject(
    QQmlFilterBasePrivate *priv,
    QObject *parent) {
  return new QQmlFilterCompositor(priv, parent);
}

//  void QQmlFilterCompositor::refreshCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlFilterCompositor12refreshCacheEv(
    QQmlFilterCompositor *self) {
  self->refreshCache();
}

//  QQmlFilterCompositorPrivate *QQmlFilterCompositor::d_func()
extern "C" Q_DECL_EXPORT
QQmlFilterCompositorPrivate *ritual_ZN20QQmlFilterCompositor6d_funcEv(
    QQmlFilterCompositor *self) {
  return self->d_func();
}

//  const QQmlFilterCompositorPrivate *QQmlFilterCompositor::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlFilterCompositorPrivate *ritual_ZNK20QQmlFilterCompositor6d_funcEv(
    const QQmlFilterCompositor *self) {
  return self->d_func();
}

//  bool QQmlFilterCompositor::filterAcceptsRowInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QQmlFilterCompositor24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterCompositor *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlFilterCompositor::filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlFilterCompositor::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QQmlFilterCompositor27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterCompositor *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlFilterCompositor::filterAcceptsColumnInternal(
      a0,
      *a1,
      a2);
}

//  void QQmlFilterCompositor::refreshCache()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlFilterCompositor12refreshCacheEv(
    QQmlFilterCompositor *self) {
  static_cast<OwnQQmlFilterCompositor *>(self)->OwnQQmlFilterCompositor::refreshCache();
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
