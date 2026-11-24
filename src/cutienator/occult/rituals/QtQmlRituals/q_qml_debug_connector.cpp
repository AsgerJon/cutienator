//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugconnector_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugconnector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlDebugConnector that Python can take functions over in. Every QQmlDebugConnector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugConnectorCall0)(const void *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void * (*CuteQQmlDebugConnectorCall1)(const void *, const QString *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlDebugConnectorCall2)(const void *, QJSEngine *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlDebugConnectorCall3)(const void *, QJSEngine *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugConnectorCall4)(const void *, QJSEngine *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugConnectorCall5)(const void *, const QString *, QQmlDebugService *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugConnectorCall6)(const void *, const QString *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugConnectorCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugConnectorCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDebugConnector : public QQmlDebugConnector {
public:
  using QQmlDebugConnector::QQmlDebugConnector;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZNK18QQmlDebugConnector12blockingModeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZNK18QQmlDebugConnector7serviceERK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector9addEngineEP9QJSEngine")) {
      taken[2] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector12removeEngineEP9QJSEngine")) {
      taken[3] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZNK18QQmlDebugConnector9hasEngineEP9QJSEngine")) {
      taken[4] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector10addServiceERK7QStringP16QQmlDebugService")) {
      taken[5] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector13removeServiceERK7QString")) {
      taken[6] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::blockingMode() const
  bool blockingMode() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall0 call = reinterpret_cast<CuteQQmlDebugConnectorCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  QQmlDebugService *QQmlDebugConnector::service(const QString &name)
  //      const
  QQmlDebugService *service(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall1 call = reinterpret_cast<CuteQQmlDebugConnectorCall1>(taken[1]);
      void * given = call(this, &name, &handled);
      if (handled) return static_cast<QQmlDebugService *>(given);
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlDebugConnector::addEngine(QJSEngine *engine)
  void addEngine(QJSEngine *engine) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall2 call = reinterpret_cast<CuteQQmlDebugConnectorCall2>(taken[2]);
      call(this, engine, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlDebugConnector::removeEngine(QJSEngine *engine)
  void removeEngine(QJSEngine *engine) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall3 call = reinterpret_cast<CuteQQmlDebugConnectorCall3>(taken[3]);
      call(this, engine, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::hasEngine(QJSEngine *engine) const
  bool hasEngine(QJSEngine *engine) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall4 call = reinterpret_cast<CuteQQmlDebugConnectorCall4>(taken[4]);
      bool given = call(this, engine, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::addService(const QString &name,
  //      QQmlDebugService *service)
  bool addService(const QString &name, QQmlDebugService *service) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall5 call = reinterpret_cast<CuteQQmlDebugConnectorCall5>(taken[5]);
      bool given = call(this, &name, service, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::removeService(const QString &name)
  bool removeService(const QString &name) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall6 call = reinterpret_cast<CuteQQmlDebugConnectorCall6>(taken[6]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall7 call = reinterpret_cast<CuteQQmlDebugConnectorCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall8 call = reinterpret_cast<CuteQQmlDebugConnectorCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall9 call = reinterpret_cast<CuteQQmlDebugConnectorCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall10 call = reinterpret_cast<CuteQQmlDebugConnectorCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall11 call = reinterpret_cast<CuteQQmlDebugConnectorCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall12 call = reinterpret_cast<CuteQQmlDebugConnectorCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlDebugConnectorCall13 call = reinterpret_cast<CuteQQmlDebugConnectorCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDebugConnector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQmlDebugConnector10metaObjectEv(
    const QQmlDebugConnector *self) {
  return self->metaObject();
}

//  QString QQmlDebugConnector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlDebugConnector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDebugConnector::tr(s, c, n));
}

//  void QQmlDebugConnector::setPluginKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDebugConnector12setPluginKeyERK7QString(
    const QString *key) {
  QQmlDebugConnector::setPluginKey(*key);
}

//  void QQmlDebugConnector::setServices(const QStringList &services)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDebugConnector11setServicesERK5QListI7QStringE(
    const QList<QString> *services) {
  QQmlDebugConnector::setServices(*services);
}

//  QQmlDebugConnector *QQmlDebugConnector::instance()
extern "C" Q_DECL_EXPORT
QQmlDebugConnector *ritual_ZN18QQmlDebugConnector8instanceEv() {
  return QQmlDebugConnector::instance();
}

//  int QQmlDebugConnector::dataStreamVersion()
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQmlDebugConnector17dataStreamVersionEv() {
  return QQmlDebugConnector::dataStreamVersion();
}

//  bool QQmlDebugConnector::blockingMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlDebugConnector12blockingModeEv(
    const QQmlDebugConnector *self) {
  return self->blockingMode();
}

//  QQmlDebugService *QQmlDebugConnector::service(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlDebugService *ritual_ZNK18QQmlDebugConnector7serviceERK7QString(
    const QQmlDebugConnector *self,
    const QString *name) {
  return self->service(*name);
}

//  void QQmlDebugConnector::addEngine(QJSEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDebugConnector9addEngineEP9QJSEngine(
    QQmlDebugConnector *self,
    QJSEngine *engine) {
  self->addEngine(engine);
}

//  void QQmlDebugConnector::removeEngine(QJSEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDebugConnector12removeEngineEP9QJSEngine(
    QQmlDebugConnector *self,
    QJSEngine *engine) {
  self->removeEngine(engine);
}

//  bool QQmlDebugConnector::hasEngine(QJSEngine *engine) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlDebugConnector9hasEngineEP9QJSEngine(
    const QQmlDebugConnector *self,
    QJSEngine *engine) {
  return self->hasEngine(engine);
}

//  bool QQmlDebugConnector::addService(const QString &name, QQmlDebugService
//      *service)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlDebugConnector10addServiceERK7QStringP16QQmlDebugService(
    QQmlDebugConnector *self,
    const QString *name,
    QQmlDebugService *service) {
  return self->addService(*name, service);
}

//  bool QQmlDebugConnector::removeService(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlDebugConnector13removeServiceERK7QString(
    QQmlDebugConnector *self,
    const QString *name) {
  return self->removeService(*name);
}

//  bool QQmlDebugConnector::open(const QVariantHash &configuration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlDebugConnector4openERK5QHashI7QString8QVariantE(
    QQmlDebugConnector *self,
    const QHash<QString, QVariant> *configuration) {
  return self->open(*configuration);
}

//  QString QQmlDebugConnector::commandLineArguments()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlDebugConnector20commandLineArgumentsEv() {
  return new QString(QQmlDebugConnector::commandLineArguments());
}

//  a Python function taken by a CuteQQmlDebugConnector, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDebugConnector(
    QQmlDebugConnector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDebugConnector *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
