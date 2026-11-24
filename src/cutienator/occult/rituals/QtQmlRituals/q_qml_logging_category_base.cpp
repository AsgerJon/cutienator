//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlloggingcategorybase_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlloggingcategorybase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQmlLoggingCategoryBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQmlLoggingCategoryBase10metaObjectEv(
    const QQmlLoggingCategoryBase *self) {
  return self->metaObject();
}

//  QString QQmlLoggingCategoryBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQmlLoggingCategoryBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlLoggingCategoryBase::tr(s, c, n));
}

//  void QQmlLoggingCategoryBase::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlLoggingCategoryBase22qt_qmlMarker_anonymousEv(
    QQmlLoggingCategoryBase *self) {
  self->qt_qmlMarker_anonymous();
}

//  const QLoggingCategory *QQmlLoggingCategoryBase::category()
extern "C" Q_DECL_EXPORT
const QLoggingCategory *ritual_ZN23QQmlLoggingCategoryBase8categoryEv(
    QQmlLoggingCategoryBase *self) {
  return self->category();
}

//  void QQmlLoggingCategoryBase::setCategory(const char *name, QtMsgType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlLoggingCategoryBase11setCategoryEPKc9QtMsgType(
    QQmlLoggingCategoryBase *self,
    const char *name,
    QtMsgType type) {
  self->setCategory(name, type);
}

//  void QQmlLoggingCategoryBase::forceCompletion()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlLoggingCategoryBase15forceCompletionEv(
    QQmlLoggingCategoryBase *self) {
  self->forceCompletion();
}
