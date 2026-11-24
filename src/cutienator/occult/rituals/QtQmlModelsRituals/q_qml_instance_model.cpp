//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlobjectmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlobjectmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQmlInstanceModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlInstanceModel10metaObjectEv(
    const QQmlInstanceModel *self) {
  return self->metaObject();
}

//  QString QQmlInstanceModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlInstanceModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlInstanceModel::tr(s, c, n));
}

//  void QQmlInstanceModel::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlInstanceModel22qt_qmlMarker_anonymousEv(
    QQmlInstanceModel *self) {
  self->qt_qmlMarker_anonymous();
}

//  int QQmlInstanceModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlInstanceModel5countEv(const QQmlInstanceModel *self) {
  return self->count();
}

//  bool QQmlInstanceModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlInstanceModel7isValidEv(const QQmlInstanceModel *self) {
  return self->isValid();
}

//  QObject *QQmlInstanceModel::object(int index,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlInstanceModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlInstanceModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->object(index, incubationMode);
}

//  ReleaseFlags QQmlInstanceModel::release(QObject *object, ReusableFlag
//      reusableFlag)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQmlInstanceModel7releaseEP7QObjectNS_12ReusableFlagE(
    QQmlInstanceModel *self,
    QObject *object,
    QQmlInstanceModel::ReusableFlag reusableFlag) {
  return static_cast<int>(self->release(object, reusableFlag).toInt());
}

//  void QQmlInstanceModel::cancel(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlInstanceModel6cancelEi(QQmlInstanceModel *self, int a0) {
  self->cancel(a0);
}

//  QString QQmlInstanceModel::stringValue(int index, const QString &role)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlInstanceModel11stringValueEiRK7QString(
    QQmlInstanceModel *self,
    int index,
    const QString *role) {
  return new QString(self->stringValue(index, *role));
}

//  QVariant QQmlInstanceModel::variantValue(int a0, const QString &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlInstanceModel12variantValueEiRK7QString(
    QQmlInstanceModel *self,
    int a0,
    const QString *a1) {
  return new QVariant(self->variantValue(a0, *a1));
}

//  void QQmlInstanceModel::setWatchedRoles(const QList<QByteArray> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlInstanceModel15setWatchedRolesERK5QListI10QByteArrayE(
    QQmlInstanceModel *self,
    const QList<QByteArray> *roles) {
  self->setWatchedRoles(*roles);
}

//  QQmlIncubator::Status QQmlInstanceModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZN17QQmlInstanceModel16incubationStatusEi(
    QQmlInstanceModel *self,
    int index) {
  return self->incubationStatus(index);
}

//  void QQmlInstanceModel::drainReusableItemsPool(int maxPoolTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlInstanceModel22drainReusableItemsPoolEi(
    QQmlInstanceModel *self,
    int maxPoolTime) {
  self->drainReusableItemsPool(maxPoolTime);
}

//  int QQmlInstanceModel::poolSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQmlInstanceModel8poolSizeEv(QQmlInstanceModel *self) {
  return self->poolSize();
}

//  int QQmlInstanceModel::indexOf(QObject *object, QObject *objectContext)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlInstanceModel7indexOfEP7QObjectS1_(
    const QQmlInstanceModel *self,
    QObject *object,
    QObject *objectContext) {
  return self->indexOf(object, objectContext);
}

//  const QAbstractItemModel *QQmlInstanceModel::abstractItemModel() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK17QQmlInstanceModel17abstractItemModelEv(
    const QQmlInstanceModel *self) {
  return self->abstractItemModel();
}

//  bool QQmlInstanceModel::setRequiredProperty(int index, const QString
//      &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStringRK8QVariant(
    QQmlInstanceModel *self,
    int index,
    const QString *name,
    const QVariant *value) {
  return self->setRequiredProperty(index, *name, *value);
}

//  void QQmlInstanceModel::cancel(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlInstanceModel6cancelEi(
    QQmlInstanceModel *self,
    int a0) {
  self->QQmlInstanceModel::cancel(a0);
}

//  void QQmlInstanceModel::drainReusableItemsPool(int maxPoolTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlInstanceModel22drainReusableItemsPoolEi(
    QQmlInstanceModel *self,
    int maxPoolTime) {
  self->QQmlInstanceModel::drainReusableItemsPool(maxPoolTime);
}

//  int QQmlInstanceModel::poolSize()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN17QQmlInstanceModel8poolSizeEv(QQmlInstanceModel *self) {
  return self->QQmlInstanceModel::poolSize();
}

//  const QAbstractItemModel *QQmlInstanceModel::abstractItemModel() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_own_ZNK17QQmlInstanceModel17abstractItemModelEv(
    const QQmlInstanceModel *self) {
  return self->QQmlInstanceModel::abstractItemModel();
}

//  bool QQmlInstanceModel::setRequiredProperty(int index, const QString
//      &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStringRK8QVariant(
    QQmlInstanceModel *self,
    int index,
    const QString *name,
    const QVariant *value) {
  return self->QQmlInstanceModel::setRequiredProperty(index, *name, *value);
}

#endif  // QT_CONFIG(qml_object_model)
#endif  // QT_CONFIG(qml_object_model)
