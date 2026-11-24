//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlanyoffilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlanyoffilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QQmlAnyOfFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlAnyOfFilter10metaObjectEv(
    const QQmlAnyOfFilter *self) {
  return self->metaObject();
}

//  QString QQmlAnyOfFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlAnyOfFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAnyOfFilter::tr(s, c, n));
}

//  QQmlAnyOfFilter::QQmlAnyOfFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlAnyOfFilter *ritual_ZN15QQmlAnyOfFilterC1EP7QObject(QObject *parent) {
  return new QQmlAnyOfFilter(parent);
}

//  bool QQmlAnyOfFilter::filterAcceptsRowInternal(int a0, const QModelIndex
//      &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlAnyOfFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAnyOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlAnyOfFilter::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlAnyOfFilter27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAnyOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsColumnInternal(a0, *a1, a2);
}

//  QQmlAnyOfFilterPrivate *QQmlAnyOfFilter::d_func()
extern "C" Q_DECL_EXPORT
QQmlAnyOfFilterPrivate *ritual_ZN15QQmlAnyOfFilter6d_funcEv(
    QQmlAnyOfFilter *self) {
  return self->d_func();
}

//  const QQmlAnyOfFilterPrivate *QQmlAnyOfFilter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlAnyOfFilterPrivate *ritual_ZNK15QQmlAnyOfFilter6d_funcEv(
    const QQmlAnyOfFilter *self) {
  return self->d_func();
}

//  bool QQmlAnyOfFilter::filterAcceptsRowInternal(int a0, const QModelIndex
//      &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQmlAnyOfFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAnyOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlAnyOfFilter::filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlAnyOfFilter::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQmlAnyOfFilter27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAnyOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlAnyOfFilter::filterAcceptsColumnInternal(a0, *a1, a2);
}
