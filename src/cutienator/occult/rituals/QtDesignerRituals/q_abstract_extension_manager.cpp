//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/extension.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/extension.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAbstractExtensionManager that Python can take functions over in. Every QAbstractExtensionManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractExtensionManagerCall0)(const void *, QAbstractExtensionFactory *, const QString *, int *);
typedef void (*CuteQAbstractExtensionManagerCall1)(const void *, QAbstractExtensionFactory *, const QString *, int *);
typedef void * (*CuteQAbstractExtensionManagerCall2)(const void *, QObject *, const QString *, int *);
class CuteQAbstractExtensionManager : public QAbstractExtensionManager {
public:
  using QAbstractExtensionManager::QAbstractExtensionManager;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractExtensionManager18registerExtensionsEP25QAbstractExtensionFactoryRK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QAbstractExtensionManager20unregisterExtensionsEP25QAbstractExtensionFactoryRK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAbstractExtensionManager9extensionEP7QObjectRK7QString")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractExtensionManager::registerExtensions(QAbstractExtension
  //      Factory *factory, const QString &iid)
  void registerExtensions(
      QAbstractExtensionFactory *factory,
      const QString &iid) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractExtensionManagerCall0 call = reinterpret_cast<CuteQAbstractExtensionManagerCall0>(taken[0]);
      call(this, factory, &iid, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractExtensionManager::unregisterExtensions(QAbstractExtensi
  //      onFactory *factory, const QString &iid)
  void unregisterExtensions(
      QAbstractExtensionFactory *factory,
      const QString &iid) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractExtensionManagerCall1 call = reinterpret_cast<CuteQAbstractExtensionManagerCall1>(taken[1]);
      call(this, factory, &iid, &handled);
      if (handled) return;
    }
  }

  //  QObject *QAbstractExtensionManager::extension(QObject *object, const
  //      QString &iid) const
  QObject *extension(QObject *object, const QString &iid) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractExtensionManagerCall2 call = reinterpret_cast<CuteQAbstractExtensionManagerCall2>(taken[2]);
      void * given = call(this, object, &iid, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }
};

//  QAbstractExtensionManager::~QAbstractExtensionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractExtensionManagerD1Ev(
    QAbstractExtensionManager *self) {
  delete self;
}

//  void
//      QAbstractExtensionManager::registerExtensions(QAbstractExtensionFacto
//      ry *factory, const QString &iid)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractExtensionManager18registerExtensionsEP25QAbstractExtensionFactoryRK7QString(
    QAbstractExtensionManager *self,
    QAbstractExtensionFactory *factory,
    const QString *iid) {
  self->registerExtensions(factory, *iid);
}

//  void
//      QAbstractExtensionManager::unregisterExtensions(QAbstractExtensionFac
//      tory *factory, const QString &iid)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractExtensionManager20unregisterExtensionsEP25QAbstractExtensionFactoryRK7QString(
    QAbstractExtensionManager *self,
    QAbstractExtensionFactory *factory,
    const QString *iid) {
  self->unregisterExtensions(factory, *iid);
}

//  QObject *QAbstractExtensionManager::extension(QObject *object, const
//      QString &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK25QAbstractExtensionManager9extensionEP7QObjectRK7QString(
    const QAbstractExtensionManager *self,
    QObject *object,
    const QString *iid) {
  return self->extension(object, *iid);
}

//  a Python function taken by a CuteQAbstractExtensionManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractExtensionManager(
    QAbstractExtensionManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractExtensionManager *>(self)->take(key, call);
}
