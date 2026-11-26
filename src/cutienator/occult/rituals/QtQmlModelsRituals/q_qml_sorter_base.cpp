//  Written by hand on 2026-11-25 from
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsorterbase_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  QQmlSorterBase is abstract ('compare' is pure virtual), so it gets
//  no constructor and no Cute class: the sorters built on it (as
//  QQmlFunctionSorter) are made with theirs. 'compare' is called
//  through the object. Not written: 'qt_metacast'.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsorterbase_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qcompare.h>

//  const QMetaObject *QQmlSorterBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlSorterBase10metaObjectEv(
    const QQmlSorterBase *self) {
  return self->metaObject();
}

//  QString QQmlSorterBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlSorterBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlSorterBase::tr(s, c, n));
}

//  QQmlSorterBase::~QQmlSorterBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBaseD1Ev(QQmlSorterBase *self) {
  delete self;
}

//  bool QQmlSorterBase::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlSorterBase7enabledEv(const QQmlSorterBase *self) {
  return self->enabled();
}

//  void QQmlSorterBase::setEnabled(const bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase10setEnabledEb(
    QQmlSorterBase *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  Qt::SortOrder QQmlSorterBase::sortOrder() const
extern "C" Q_DECL_EXPORT
Qt::SortOrder ritual_ZNK14QQmlSorterBase9sortOrderEv(
    const QQmlSorterBase *self) {
  return self->sortOrder();
}

//  void QQmlSorterBase::setSortOrder(const Qt::SortOrder sortOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase12setSortOrderEN2Qt9SortOrderE(
    QQmlSorterBase *self,
    Qt::SortOrder sortOrder) {
  self->setSortOrder(sortOrder);
}

//  int QQmlSorterBase::priority() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlSorterBase8priorityEv(const QQmlSorterBase *self) {
  return self->priority();
}

//  void QQmlSorterBase::setPriority(const int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase11setPriorityEi(
    QQmlSorterBase *self,
    int priority) {
  self->setPriority(priority);
}

//  int QQmlSorterBase::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlSorterBase6columnEv(const QQmlSorterBase *self) {
  return self->column();
}

//  void QQmlSorterBase::setColumn(const int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase9setColumnEi(
    QQmlSorterBase *self,
    int column) {
  self->setColumn(column);
}

//  QPartialOrdering QQmlSorterBase::compare(const QModelIndex &a0, const
//      QModelIndex &a1, const QQmlSortFilterProxyModel *a2) const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZNK14QQmlSorterBase7compareERK11QModelIndexS2_PK24QQmlSortFilterProxyModel(
    const QQmlSorterBase *self,
    const QModelIndex *a0,
    const QModelIndex *a1,
    const QQmlSortFilterProxyModel *a2) {
  return new QPartialOrdering(self->compare(*a0, *a1, a2));
}

//  void QQmlSorterBase::update(const QQmlSortFilterProxyModel *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase6updateEPK24QQmlSortFilterProxyModel(
    QQmlSorterBase *self,
    const QQmlSortFilterProxyModel *a0) {
  self->update(a0);
}

//  void QQmlSorterBase::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase14enabledChangedEv(QQmlSorterBase *self) {
  self->enabledChanged();
}

//  void QQmlSorterBase::sortOrderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase16sortOrderChangedEv(QQmlSorterBase *self) {
  self->sortOrderChanged();
}

//  void QQmlSorterBase::priorityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase15priorityChangedEv(QQmlSorterBase *self) {
  self->priorityChanged();
}

//  void QQmlSorterBase::columnChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase13columnChangedEv(QQmlSorterBase *self) {
  self->columnChanged();
}

//  void QQmlSorterBase::invalidateModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase15invalidateModelEv(QQmlSorterBase *self) {
  self->invalidateModel();
}

//  void QQmlSorterBase::invalidateCache(QQmlSorterBase *filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase15invalidateCacheEPS_(
    QQmlSorterBase *self,
    QQmlSorterBase *filter) {
  self->invalidateCache(filter);
}

//  void QQmlSorterBase::invalidate(bool updateCache)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlSorterBase10invalidateEb(
    QQmlSorterBase *self,
    bool updateCache) {
  self->invalidate(updateCache);
}

//  QQmlSorterBasePrivate *QQmlSorterBase::d_func()
extern "C" Q_DECL_EXPORT
QQmlSorterBasePrivate *ritual_ZN14QQmlSorterBase6d_funcEv(
    QQmlSorterBase *self) {
  return self->d_func();
}

//  const QQmlSorterBasePrivate *QQmlSorterBase::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSorterBasePrivate *ritual_ZNK14QQmlSorterBase6d_funcEv(
    const QQmlSorterBase *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
