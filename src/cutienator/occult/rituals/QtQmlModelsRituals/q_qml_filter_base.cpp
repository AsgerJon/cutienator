//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfilterbase_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlfilterbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qlist.h>

//  const QMetaObject *QQmlFilterBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlFilterBase10metaObjectEv(
    const QQmlFilterBase *self) {
  return self->metaObject();
}

//  void *QQmlFilterBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQmlFilterBase11qt_metacastEPKc(
    QQmlFilterBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlFilterBase::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQmlFilterBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlFilterBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlFilterBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlFilterBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlFilterBase::tr(s, c, n));
}

//  void QQmlFilterBase::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase24qt_qmlMarker_uncreatableEv(
    QQmlFilterBase *self) {
  self->qt_qmlMarker_uncreatable();
}

//  bool QQmlFilterBase::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlFilterBase7enabledEv(const QQmlFilterBase *self) {
  return self->enabled();
}

//  void QQmlFilterBase::setEnabled(bool bEnable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase10setEnabledEb(
    QQmlFilterBase *self,
    bool bEnable) {
  self->setEnabled(bEnable);
}

//  bool QQmlFilterBase::isInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlFilterBase10isInvertedEv(const QQmlFilterBase *self) {
  return self->isInverted();
}

//  void QQmlFilterBase::setInverted(bool bInvert)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase11setInvertedEb(
    QQmlFilterBase *self,
    bool bInvert) {
  self->setInverted(bInvert);
}

//  int QQmlFilterBase::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlFilterBase6columnEv(const QQmlFilterBase *self) {
  return self->column();
}

//  void QQmlFilterBase::setColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase9setColumnEi(
    QQmlFilterBase *self,
    int column) {
  self->setColumn(column);
}

//  bool QQmlFilterBase::filterAcceptsRowInternal(int a0, const QModelIndex
//      &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterBase *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlFilterBase::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlFilterBase27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterBase *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->filterAcceptsColumnInternal(a0, *a1, a2);
}

//  void QQmlFilterBase::update(const QQmlSortFilterProxyModel *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyModel(
    QQmlFilterBase *self,
    const QQmlSortFilterProxyModel *a0) {
  self->update(a0);
}

//  bool QQmlFilterBase::supportColumnFiltering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlFilterBase22supportColumnFilteringEv(
    const QQmlFilterBase *self) {
  return self->supportColumnFiltering();
}

//  bool QQmlFilterBase::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlFilterBase8isActiveEv(const QQmlFilterBase *self) {
  return self->isActive();
}

//  void QQmlFilterBase::invalidateModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase15invalidateModelEv(QQmlFilterBase *self) {
  self->invalidateModel();
}

//  void QQmlFilterBase::invalidateCache(QQmlFilterBase *filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase15invalidateCacheEPS_(
    QQmlFilterBase *self,
    QQmlFilterBase *filter) {
  self->invalidateCache(filter);
}

//  void QQmlFilterBase::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase14enabledChangedEv(QQmlFilterBase *self) {
  self->enabledChanged();
}

//  void QQmlFilterBase::invertedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase15invertedChangedEv(QQmlFilterBase *self) {
  self->invertedChanged();
}

//  void QQmlFilterBase::columnChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase13columnChangedEv(QQmlFilterBase *self) {
  self->columnChanged();
}

//  QQmlFilterBase::QQmlFilterBase(QQmlFilterBasePrivate *privObj, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlFilterBase *ritual_ZN14QQmlFilterBaseC1EP21QQmlFilterBasePrivateP7QObject(
    QQmlFilterBasePrivate *privObj,
    QObject *parent) {
  return new QQmlFilterBase(privObj, parent);
}

//  void QQmlFilterBase::invalidate(bool updateCache)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlFilterBase10invalidateEb(
    QQmlFilterBase *self,
    bool updateCache) {
  self->invalidate(updateCache);
}

//  QQmlFilterBasePrivate *QQmlFilterBase::d_func()
extern "C" Q_DECL_EXPORT
QQmlFilterBasePrivate *ritual_ZN14QQmlFilterBase6d_funcEv(
    QQmlFilterBase *self) {
  return self->d_func();
}

//  const QQmlFilterBasePrivate *QQmlFilterBase::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlFilterBasePrivate *ritual_ZNK14QQmlFilterBase6d_funcEv(
    const QQmlFilterBase *self) {
  return self->d_func();
}

//  int QQmlFilterBase::column() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QQmlFilterBase6columnEv(const QQmlFilterBase *self) {
  return self->QQmlFilterBase::column();
}

//  void QQmlFilterBase::setColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlFilterBase9setColumnEi(
    QQmlFilterBase *self,
    int column) {
  self->QQmlFilterBase::setColumn(column);
}

//  bool QQmlFilterBase::filterAcceptsRowInternal(int a0, const QModelIndex
//      &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QQmlFilterBase24filterAcceptsRowInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterBase *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlFilterBase::filterAcceptsRowInternal(a0, *a1, a2);
}

//  bool QQmlFilterBase::filterAcceptsColumnInternal(int a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QQmlFilterBase27filterAcceptsColumnInternalEiRK11QModelIndexPK24QQmlSortFilterProxyModel(
    const QQmlFilterBase *self,
    int a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return self->QQmlFilterBase::filterAcceptsColumnInternal(a0, *a1, a2);
}

//  void QQmlFilterBase::update(const QQmlSortFilterProxyModel *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlFilterBase6updateEPK24QQmlSortFilterProxyModel(
    QQmlFilterBase *self,
    const QQmlSortFilterProxyModel *a0) {
  self->QQmlFilterBase::update(a0);
}

//  bool QQmlFilterBase::supportColumnFiltering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QQmlFilterBase22supportColumnFilteringEv(
    const QQmlFilterBase *self) {
  return self->QQmlFilterBase::supportColumnFiltering();
}

//  bool QQmlFilterBase::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QQmlFilterBase8isActiveEv(const QQmlFilterBase *self) {
  return self->QQmlFilterBase::isActive();
}

//  QList<QQmlFilterBase *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlFilterBase *> *ritual_list_make_QQmlFilterBase_ptr() {
  return new QList<QQmlFilterBase *>();
}

//  void QList<QQmlFilterBase *>::append(const QQmlFilterBase * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlFilterBase_ptr(
    QList<QQmlFilterBase *> *self,
    QQmlFilterBase *element) {
  self->append(element);
}

//  qsizetype QList<QQmlFilterBase *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlFilterBase_ptr(
    const QList<QQmlFilterBase *> *self) {
  return self->size();
}

//  const QQmlFilterBase * &QList<QQmlFilterBase *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlFilterBase *ritual_list_at_QQmlFilterBase_ptr(
    const QList<QQmlFilterBase *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQmlFilterBase *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlFilterBase_ptr(QList<QQmlFilterBase *> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
