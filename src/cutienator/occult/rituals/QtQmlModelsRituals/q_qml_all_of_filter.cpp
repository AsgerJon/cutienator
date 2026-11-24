//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlalloffilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlalloffilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QQmlAllOfFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlAllOfFilter10metaObjectEv(
    const QQmlAllOfFilter *self) {
  return self->metaObject();
}

//  QString QQmlAllOfFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlAllOfFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAllOfFilter::tr(s, c, n));
}

//  QQmlAllOfFilter::QQmlAllOfFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlAllOfFilter *ritual_ZN15QQmlAllOfFilterC1EP7QObject(QObject *parent) {
  return new QQmlAllOfFilter(parent);
}

//  bool QQmlAllOfFilter::filterAcceptsRowInternal(int a0, const QModelIndex
//      &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlAllOfFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAllOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlAllOfFilter::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlAllOfFilter27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAllOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsColumnInternal(a0, *a1, a2);
}

//  QQmlAllOfFilterPrivate *QQmlAllOfFilter::d_func()
extern "C" Q_DECL_EXPORT
QQmlAllOfFilterPrivate *ritual_ZN15QQmlAllOfFilter6d_funcEv(
    QQmlAllOfFilter *self) {
  return self->d_func();
}

//  const QQmlAllOfFilterPrivate *QQmlAllOfFilter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlAllOfFilterPrivate *ritual_ZNK15QQmlAllOfFilter6d_funcEv(
    const QQmlAllOfFilter *self) {
  return self->d_func();
}

//  bool QQmlAllOfFilter::filterAcceptsRowInternal(int a0, const QModelIndex
//      &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQmlAllOfFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAllOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlAllOfFilter::filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlAllOfFilter::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQmlAllOfFilter27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlAllOfFilter *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlAllOfFilter::filterAcceptsColumnInternal(a0, *a1, a2);
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
