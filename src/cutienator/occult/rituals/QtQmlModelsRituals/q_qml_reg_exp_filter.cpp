//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlregexpfilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlregexpfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif

//  const QMetaObject *QQmlRegExpFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlRegExpFilter10metaObjectEv(
    const QQmlRegExpFilter *self) {
  return self->metaObject();
}

//  void *QQmlRegExpFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQmlRegExpFilter11qt_metacastEPKc(
    QQmlRegExpFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlRegExpFilter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlRegExpFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlRegExpFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QQmlRegExpFilter::regExpChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlRegExpFilter13regExpChangedEv(QQmlRegExpFilter *self) {
  self->regExpChanged();
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

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
