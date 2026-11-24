//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlregexpfilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlregexpfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QQmlRegExpFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlRegExpFilter10metaObjectEv(
    const QQmlRegExpFilter *self) {
  return self->metaObject();
}

//  QString QQmlRegExpFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlRegExpFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlRegExpFilter::tr(s, c, n));
}

//  QQmlRegExpFilter::QQmlRegExpFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlRegExpFilter *ritual_ZN16QQmlRegExpFilterC1EP7QObject(QObject *parent) {
  return new QQmlRegExpFilter(parent);
}

//  QRegularExpression QQmlRegExpFilter::regExp() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK16QQmlRegExpFilter6regExpEv(
    const QQmlRegExpFilter *self) {
  return new QRegularExpression(self->regExp());
}

//  void QQmlRegExpFilter::setRegExp(const QRegularExpression &regExp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlRegExpFilter9setRegExpERK18QRegularExpression(
    QQmlRegExpFilter *self,
    const QRegularExpression *regExp) {
  self->setRegExp(*regExp);
}

//  bool QQmlRegExpFilter::filterAcceptsRowInternal(int row, const
//      QModelIndex &sourceParent, const QQmlSortFilterProxyModel
//      *proxyModel) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlRegExpFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlRegExpFilter *self,
    int row,
    const QModelIndex *sourceParent,
    const QQmlSortFilterProxyModel *proxyModel) {
  return self->filterAcceptsRowInternal(row, *sourceParent, proxyModel);
}

//  QQmlRegExpFilterPrivate *QQmlRegExpFilter::d_func()
extern "C" Q_DECL_EXPORT
QQmlRegExpFilterPrivate *ritual_ZN16QQmlRegExpFilter6d_funcEv(
    QQmlRegExpFilter *self) {
  return self->d_func();
}

//  const QQmlRegExpFilterPrivate *QQmlRegExpFilter::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlRegExpFilterPrivate *ritual_ZNK16QQmlRegExpFilter6d_funcEv(
    const QQmlRegExpFilter *self) {
  return self->d_func();
}

//  bool QQmlRegExpFilter::filterAcceptsRowInternal(int row, const
//      QModelIndex &sourceParent, const QQmlSortFilterProxyModel
//      *proxyModel) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QQmlRegExpFilter24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlRegExpFilter *self,
    int row,
    const QModelIndex *sourceParent,
    const QQmlSortFilterProxyModel *proxyModel) {
  return self->QQmlRegExpFilter::filterAcceptsRowInternal(
      row,
      *sourceParent,
      proxyModel);
}
