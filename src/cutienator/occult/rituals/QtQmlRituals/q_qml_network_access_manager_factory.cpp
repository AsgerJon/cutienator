//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlnetworkaccessmanagerfactory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/qtqmlglobal.h>
#if QT_CONFIG(qml_network)
#include <QtQml/QtQml>
#include <QtQml/qqmlnetworkaccessmanagerfactory.h>
#include <cstring>

//  A QQmlNetworkAccessManagerFactory that Python can take functions over in. Every QQmlNetworkAccessManagerFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_network)
typedef void * (*CuteQQmlNetworkAccessManagerFactoryCall0)(const void *, QObject *, int *);
#endif  // QT_CONFIG(qml_network)
class CuteQQmlNetworkAccessManagerFactory : public QQmlNetworkAccessManagerFactory {
public:
  using QQmlNetworkAccessManagerFactory::QQmlNetworkAccessManagerFactory;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN31QQmlNetworkAccessManagerFactory6createEP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_network)
    return false;
  }

#if QT_CONFIG(qml_network)
  //  QNetworkAccessManager
  //      *QQmlNetworkAccessManagerFactory::create(QObject *parent)
  QNetworkAccessManager *create(QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlNetworkAccessManagerFactoryCall0 call = reinterpret_cast<CuteQQmlNetworkAccessManagerFactoryCall0>(taken[0]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QNetworkAccessManager *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(qml_network)
};

//  QQmlNetworkAccessManagerFactory::~QQmlNetworkAccessManagerFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlNetworkAccessManagerFactoryD1Ev(
    QQmlNetworkAccessManagerFactory *self) {
  delete self;
}

//  QNetworkAccessManager *QQmlNetworkAccessManagerFactory::create(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZN31QQmlNetworkAccessManagerFactory6createEP7QObject(
    QQmlNetworkAccessManagerFactory *self,
    QObject *parent) {
  return self->create(parent);
}

//  a Python function taken by a CuteQQmlNetworkAccessManagerFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlNetworkAccessManagerFactory(
    QQmlNetworkAccessManagerFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlNetworkAccessManagerFactory *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_network)
