//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessbackend_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QNetworkAccessBackendFactory that Python can take functions over in. Every QNetworkAccessBackendFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQNetworkAccessBackendFactoryCall0)(const void *, int, const QNetworkRequest *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessBackendFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessBackendFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessBackendFactory : public QNetworkAccessBackendFactory {
public:
  using QNetworkAccessBackendFactory::QNetworkAccessBackendFactory;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QNetworkAccessBackendFactory6createEN21QNetworkAccessManager9OperationERK15QNetworkRequest")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QNetworkAccessBackend *QNetworkAccessBackendFactory::create(QNetworkA
  //      ccessManager::Operation op, const QNetworkRequest &request) const
  QNetworkAccessBackend *create(
      QNetworkAccessManager::Operation op,
      const QNetworkRequest &request) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall0 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall0>(taken[0]);
      void * given = call(this, static_cast<int>(op), &request, &handled);
      if (handled) return static_cast<QNetworkAccessBackend *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall1 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall2 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall3 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall4 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall5 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall6 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkAccessBackendFactoryCall7 call = reinterpret_cast<CuteQNetworkAccessBackendFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkAccessBackendFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QNetworkAccessBackendFactory10metaObjectEv(
    const QNetworkAccessBackendFactory *self) {
  return self->metaObject();
}

//  void *QNetworkAccessBackendFactory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QNetworkAccessBackendFactory11qt_metacastEPKc(
    QNetworkAccessBackendFactory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkAccessBackendFactory::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QNetworkAccessBackendFactory11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkAccessBackendFactory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNetworkAccessBackendFactory::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QNetworkAccessBackendFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkAccessBackendFactory::tr(s, c, n));
}

//  QNetworkAccessBackendFactory::~QNetworkAccessBackendFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessBackendFactoryD1Ev(
    QNetworkAccessBackendFactory *self) {
  delete self;
}

//  QStringList QNetworkAccessBackendFactory::supportedSchemes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QNetworkAccessBackendFactory16supportedSchemesEv(
    const QNetworkAccessBackendFactory *self) {
  return new QList<QString>(self->supportedSchemes());
}

//  QNetworkAccessBackend
//      *QNetworkAccessBackendFactory::create(QNetworkAccessManager::Operatio
//      n op, const QNetworkRequest &request) const
extern "C" Q_DECL_EXPORT
QNetworkAccessBackend *ritual_ZNK28QNetworkAccessBackendFactory6createEN21QNetworkAccessManager9OperationERK15QNetworkRequest(
    const QNetworkAccessBackendFactory *self,
    QNetworkAccessManager::Operation op,
    const QNetworkRequest *request) {
  return self->create(op, *request);
}

//  a Python function taken by a CuteQNetworkAccessBackendFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessBackendFactory(
    QNetworkAccessBackendFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessBackendFactory *>(self)->take(key, call);
}
