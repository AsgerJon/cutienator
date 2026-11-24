//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/extension.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/extension.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAbstractExtensionFactory that Python can take functions over in. Every QAbstractExtensionFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAbstractExtensionFactoryCall0)(const void *, QObject *, const QString *, int *);
class CuteQAbstractExtensionFactory : public QAbstractExtensionFactory {
public:
  using QAbstractExtensionFactory::QAbstractExtensionFactory;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QAbstractExtensionFactory9extensionEP7QObjectRK7QString")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QObject *QAbstractExtensionFactory::extension(QObject *object, const
  //      QString &iid) const
  QObject *extension(QObject *object, const QString &iid) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractExtensionFactoryCall0 call = reinterpret_cast<CuteQAbstractExtensionFactoryCall0>(taken[0]);
      void * given = call(this, object, &iid, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }
};

//  QAbstractExtensionFactory::~QAbstractExtensionFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractExtensionFactoryD1Ev(
    QAbstractExtensionFactory *self) {
  delete self;
}

//  QObject *QAbstractExtensionFactory::extension(QObject *object, const
//      QString &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK25QAbstractExtensionFactory9extensionEP7QObjectRK7QString(
    const QAbstractExtensionFactory *self,
    QObject *object,
    const QString *iid) {
  return self->extension(object, *iid);
}

//  a Python function taken by a CuteQAbstractExtensionFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractExtensionFactory(
    QAbstractExtensionFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractExtensionFactory *>(self)->take(key, call);
}
