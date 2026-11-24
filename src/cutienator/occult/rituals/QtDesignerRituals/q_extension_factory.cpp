//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/default_extensionfactory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/QtDesigner>
#include <QtDesigner/default_extensionfactory.h>
#include <QtCore/qstring.h>

//  Only a class built on QExtensionFactory may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQExtensionFactory : QExtensionFactory {
  using QExtensionFactory::createExtension;
};

//  const QMetaObject *QExtensionFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QExtensionFactory10metaObjectEv(
    const QExtensionFactory *self) {
  return self->metaObject();
}

//  QString QExtensionFactory::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QExtensionFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QExtensionFactory::tr(s, c, n));
}

//  QExtensionFactory::QExtensionFactory(QExtensionManager *parent)
extern "C" Q_DECL_EXPORT
QExtensionFactory *ritual_ZN17QExtensionFactoryC1EP17QExtensionManager(
    QExtensionManager *parent) {
  return new QExtensionFactory(parent);
}

//  QObject *QExtensionFactory::extension(QObject *object, const QString
//      &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QExtensionFactory9extensionEP7QObjectRK7QString(
    const QExtensionFactory *self,
    QObject *object,
    const QString *iid) {
  return self->extension(object, *iid);
}

//  QExtensionManager *QExtensionFactory::extensionManager() const
extern "C" Q_DECL_EXPORT
QExtensionManager *ritual_ZNK17QExtensionFactory16extensionManagerEv(
    const QExtensionFactory *self) {
  return self->extensionManager();
}

//  void QExtensionFactory::objectDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QExtensionFactory15objectDestroyedEP7QObject(
    QExtensionFactory *self,
    QObject *object) {
  self->objectDestroyed(object);
}

//  QObject *QExtensionFactory::createExtension(QObject *object, const
//      QString &iid, QObject *parent) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QExtensionFactory15createExtensionEP7QObjectRK7QStringS1_(
    const QExtensionFactory *self,
    QObject *object,
    const QString *iid,
    QObject *parent) {
  return self->createExtension(object, *iid, parent);
}

//  QExtensionFactory as the QAbstractExtensionFactory it is built on
extern "C" Q_DECL_EXPORT
QAbstractExtensionFactory *ritual_cast_QExtensionFactory_QAbstractExtensionFactory(
    QExtensionFactory *self) {
  return static_cast<QAbstractExtensionFactory *>(self);
}

//  QObject *QExtensionFactory::extension(QObject *object, const QString
//      &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK17QExtensionFactory9extensionEP7QObjectRK7QString(
    const QExtensionFactory *self,
    QObject *object,
    const QString *iid) {
  return self->QExtensionFactory::extension(object, *iid);
}

//  QObject *QExtensionFactory::createExtension(QObject *object, const
//      QString &iid, QObject *parent) const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK17QExtensionFactory15createExtensionEP7QObjectRK7QStringS1_(
    const QExtensionFactory *self,
    QObject *object,
    const QString *iid,
    QObject *parent) {
  return static_cast<const OwnQExtensionFactory *>(self)->OwnQExtensionFactory::createExtension(
      object,
      *iid,
      parent);
}
