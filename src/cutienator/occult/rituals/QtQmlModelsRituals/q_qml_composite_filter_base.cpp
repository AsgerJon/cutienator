//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlcompositefilterbase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlcompositefilterbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQmlCompositeFilterBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlCompositeFilterBase : QQmlCompositeFilterBase {
  using QQmlCompositeFilterBase::refreshCache;
};

//  const QMetaObject *QQmlCompositeFilterBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQmlCompositeFilterBase10metaObjectEv(
    const QQmlCompositeFilterBase *self) {
  return self->metaObject();
}

//  QString QQmlCompositeFilterBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQmlCompositeFilterBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlCompositeFilterBase::tr(s, c, n));
}

//  void QQmlCompositeFilterBase::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlCompositeFilterBase24qt_qmlMarker_uncreatableEv(
    QQmlCompositeFilterBase *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQmlCompositeFilterBase::QQmlCompositeFilterBase(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlCompositeFilterBase *ritual_ZN23QQmlCompositeFilterBaseC1EP7QObject(
    QObject *parent) {
  return new QQmlCompositeFilterBase(parent);
}

//  void QQmlCompositeFilterBase::update(const QQmlSortFilterProxyModel
//      *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlCompositeFilterBase6updateEPK24QQmlSortFilterProxyModel(
    QQmlCompositeFilterBase *self,
    const QQmlSortFilterProxyModel *model) {
  self->update(model);
}

//  bool QQmlCompositeFilterBase::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlCompositeFilterBase8isActiveEv(
    const QQmlCompositeFilterBase *self) {
  return self->isActive();
}

//  int QQmlCompositeFilterBase::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQmlCompositeFilterBase6columnEv(
    const QQmlCompositeFilterBase *self) {
  return self->column();
}

//  void QQmlCompositeFilterBase::setColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlCompositeFilterBase9setColumnEi(
    QQmlCompositeFilterBase *self,
    int column) {
  self->setColumn(column);
}

//  bool QQmlCompositeFilterBase::supportColumnFiltering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlCompositeFilterBase22supportColumnFilteringEv(
    const QQmlCompositeFilterBase *self) {
  return self->supportColumnFiltering();
}

//  QQmlCompositeFilterBase::QQmlCompositeFilterBase(QQmlFilterCompositorPriv
//      ate *priv, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlCompositeFilterBase *ritual_ZN23QQmlCompositeFilterBaseC1EP27QQmlFilterCompositorPrivateP7QObject(
    QQmlFilterCompositorPrivate *priv,
    QObject *parent) {
  return new QQmlCompositeFilterBase(priv, parent);
}

//  void QQmlCompositeFilterBase::refreshCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlCompositeFilterBase12refreshCacheEv(
    QQmlCompositeFilterBase *self) {
  self->refreshCache();
}

//  QQmlCompositeFilterBasePrivate *QQmlCompositeFilterBase::d_func()
extern "C" Q_DECL_EXPORT
QQmlCompositeFilterBasePrivate *ritual_ZN23QQmlCompositeFilterBase6d_funcEv(
    QQmlCompositeFilterBase *self) {
  return self->d_func();
}

//  const QQmlCompositeFilterBasePrivate *QQmlCompositeFilterBase::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlCompositeFilterBasePrivate *ritual_ZNK23QQmlCompositeFilterBase6d_funcEv(
    const QQmlCompositeFilterBase *self) {
  return self->d_func();
}

//  void QQmlCompositeFilterBase::update(const QQmlSortFilterProxyModel
//      *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQmlCompositeFilterBase6updateEPK24QQmlSortFilterProxyModel(
    QQmlCompositeFilterBase *self,
    const QQmlSortFilterProxyModel *model) {
  self->QQmlCompositeFilterBase::update(model);
}

//  bool QQmlCompositeFilterBase::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QQmlCompositeFilterBase8isActiveEv(
    const QQmlCompositeFilterBase *self) {
  return self->QQmlCompositeFilterBase::isActive();
}

//  int QQmlCompositeFilterBase::column() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QQmlCompositeFilterBase6columnEv(
    const QQmlCompositeFilterBase *self) {
  return self->QQmlCompositeFilterBase::column();
}

//  void QQmlCompositeFilterBase::setColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQmlCompositeFilterBase9setColumnEi(
    QQmlCompositeFilterBase *self,
    int column) {
  self->QQmlCompositeFilterBase::setColumn(column);
}

//  bool QQmlCompositeFilterBase::supportColumnFiltering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QQmlCompositeFilterBase22supportColumnFilteringEv(
    const QQmlCompositeFilterBase *self) {
  return self->QQmlCompositeFilterBase::supportColumnFiltering();
}

//  void QQmlCompositeFilterBase::refreshCache()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQmlCompositeFilterBase12refreshCacheEv(
    QQmlCompositeFilterBase *self) {
  static_cast<OwnQQmlCompositeFilterBase *>(self)->OwnQQmlCompositeFilterBase::refreshCache();
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
