//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlapplicationengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlapplicationengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qobject.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlApplicationEngine that Python can take functions over in. Every QQmlApplicationEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlApplicationEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlApplicationEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlApplicationEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlApplicationEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlApplicationEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlApplicationEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlApplicationEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlApplicationEngine : public QQmlApplicationEngine {
public:
  using QQmlApplicationEngine::QQmlApplicationEngine;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQmlEngine::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlApplicationEngineCall0 call = reinterpret_cast<CuteQQmlApplicationEngineCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlEngine::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlApplicationEngineCall1 call = reinterpret_cast<CuteQQmlApplicationEngineCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlApplicationEngineCall2 call = reinterpret_cast<CuteQQmlApplicationEngineCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlApplicationEngineCall3 call = reinterpret_cast<CuteQQmlApplicationEngineCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlApplicationEngineCall4 call = reinterpret_cast<CuteQQmlApplicationEngineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlApplicationEngineCall5 call = reinterpret_cast<CuteQQmlApplicationEngineCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlApplicationEngineCall6 call = reinterpret_cast<CuteQQmlApplicationEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlApplicationEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQmlApplicationEngine10metaObjectEv(
    const QQmlApplicationEngine *self) {
  return self->metaObject();
}

//  void *QQmlApplicationEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQmlApplicationEngine11qt_metacastEPKc(
    QQmlApplicationEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlApplicationEngine::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQmlApplicationEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlApplicationEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlApplicationEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQmlApplicationEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlApplicationEngine::tr(s, c, n));
}

//  QQmlApplicationEngine::QQmlApplicationEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlApplicationEngine *ritual_ZN21QQmlApplicationEngineC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlApplicationEngine(parent);
}

//  QQmlApplicationEngine::QQmlApplicationEngine(const QUrl &url, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlApplicationEngine *ritual_ZN21QQmlApplicationEngineC1ERK4QUrlP7QObject(
    const QUrl *url,
    QObject *parent) {
  return new CuteQQmlApplicationEngine(*url, parent);
}

//  QQmlApplicationEngine::QQmlApplicationEngine(QAnyStringView uri,
//      QAnyStringView typeName, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlApplicationEngine *ritual_ZN21QQmlApplicationEngineC1E14QAnyStringViewS0_P7QObject(
    const QString *uri,
    const QString *typeName,
    QObject *parent) {
  return new CuteQQmlApplicationEngine(
      QAnyStringView(*uri),
      QAnyStringView(*typeName),
      parent);
}

//  QQmlApplicationEngine::QQmlApplicationEngine(const QString &filePath,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlApplicationEngine *ritual_ZN21QQmlApplicationEngineC1ERK7QStringP7QObject(
    const QString *filePath,
    QObject *parent) {
  return new CuteQQmlApplicationEngine(*filePath, parent);
}

//  QQmlApplicationEngine::~QQmlApplicationEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngineD1Ev(QQmlApplicationEngine *self) {
  delete self;
}

//  QList<QObject *> QQmlApplicationEngine::rootObjects() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK21QQmlApplicationEngine11rootObjectsEv(
    const QQmlApplicationEngine *self) {
  return new QList<QObject *>(self->rootObjects());
}

//  void QQmlApplicationEngine::load(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine4loadERK4QUrl(
    QQmlApplicationEngine *self,
    const QUrl *url) {
  self->load(*url);
}

//  void QQmlApplicationEngine::load(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine4loadERK7QString(
    QQmlApplicationEngine *self,
    const QString *filePath) {
  self->load(*filePath);
}

//  void QQmlApplicationEngine::loadFromModule(QAnyStringView uri,
//      QAnyStringView typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine14loadFromModuleE14QAnyStringViewS0_(
    QQmlApplicationEngine *self,
    const QString *uri,
    const QString *typeName) {
  self->loadFromModule(QAnyStringView(*uri), QAnyStringView(*typeName));
}

//  void QQmlApplicationEngine::setInitialProperties(const QVariantMap
//      &initialProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine20setInitialPropertiesERK4QMapI7QString8QVariantE(
    QQmlApplicationEngine *self,
    const QMap<QString, QVariant> *initialProperties) {
  self->setInitialProperties(*initialProperties);
}

//  void QQmlApplicationEngine::setExtraFileSelectors(const QStringList
//      &extraFileSelectors)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine21setExtraFileSelectorsERK5QListI7QStringE(
    QQmlApplicationEngine *self,
    const QList<QString> *extraFileSelectors) {
  self->setExtraFileSelectors(*extraFileSelectors);
}

//  void QQmlApplicationEngine::loadData(const QByteArray &data, const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine8loadDataERK10QByteArrayRK4QUrl(
    QQmlApplicationEngine *self,
    const QByteArray *data,
    const QUrl *url) {
  self->loadData(*data, *url);
}

//  void QQmlApplicationEngine::objectCreated(QObject *object, const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine13objectCreatedEP7QObjectRK4QUrl(
    QQmlApplicationEngine *self,
    QObject *object,
    const QUrl *url) {
  self->objectCreated(object, *url);
}

//  void QQmlApplicationEngine::objectCreationFailed(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlApplicationEngine20objectCreationFailedERK4QUrl(
    QQmlApplicationEngine *self,
    const QUrl *url) {
  self->objectCreationFailed(*url);
}

//  QQmlApplicationEnginePrivate *QQmlApplicationEngine::d_func()
extern "C" Q_DECL_EXPORT
QQmlApplicationEnginePrivate *ritual_ZN21QQmlApplicationEngine6d_funcEv(
    QQmlApplicationEngine *self) {
  return self->d_func();
}

//  const QQmlApplicationEnginePrivate *QQmlApplicationEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlApplicationEnginePrivate *ritual_ZNK21QQmlApplicationEngine6d_funcEv(
    const QQmlApplicationEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlApplicationEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlApplicationEngine(
    QQmlApplicationEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlApplicationEngine *>(self)->take(key, call);
}
