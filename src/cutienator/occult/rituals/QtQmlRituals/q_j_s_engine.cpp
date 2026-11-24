//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjsengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qjsengine.h>
#include <QtCore/qstring.h>
#include <QtQml/qjsvalue.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QJSEngine that Python can take functions over in. Every QJSEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQJSEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQJSEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQJSEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQJSEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQJSEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQJSEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQJSEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQJSEngine : public QJSEngine {
public:
  using QJSEngine::QJSEngine;
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQJSEngineCall0 call = reinterpret_cast<CuteQJSEngineCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQJSEngineCall1 call = reinterpret_cast<CuteQJSEngineCall1>(taken[1]);
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
      CuteQJSEngineCall2 call = reinterpret_cast<CuteQJSEngineCall2>(taken[2]);
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
      CuteQJSEngineCall3 call = reinterpret_cast<CuteQJSEngineCall3>(taken[3]);
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
      CuteQJSEngineCall4 call = reinterpret_cast<CuteQJSEngineCall4>(taken[4]);
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
      CuteQJSEngineCall5 call = reinterpret_cast<CuteQJSEngineCall5>(taken[5]);
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
      CuteQJSEngineCall6 call = reinterpret_cast<CuteQJSEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QJSEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QJSEngine10metaObjectEv(
    const QJSEngine *self) {
  return self->metaObject();
}

//  QString QJSEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QJSEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QJSEngine::tr(s, c, n));
}

//  QJSEngine::QJSEngine()
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZN9QJSEngineC1Ev() {
  return new CuteQJSEngine();
}

//  QJSEngine::QJSEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZN9QJSEngineC1EP7QObject(QObject *parent) {
  return new CuteQJSEngine(parent);
}

//  QJSEngine::~QJSEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngineD1Ev(QJSEngine *self) {
  delete self;
}

//  QJSValue QJSEngine::globalObject() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK9QJSEngine12globalObjectEv(const QJSEngine *self) {
  return new QJSValue(self->globalObject());
}

//  QJSValue QJSEngine::importModule(const QString &fileName)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine12importModuleERK7QString(
    QJSEngine *self,
    const QString *fileName) {
  return new QJSValue(self->importModule(*fileName));
}

//  bool QJSEngine::registerModule(const QString &moduleName, const QJSValue
//      &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine14registerModuleERK7QStringRK8QJSValue(
    QJSEngine *self,
    const QString *moduleName,
    const QJSValue *value) {
  return self->registerModule(*moduleName, *value);
}

//  QJSValue QJSEngine::newObject()
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine9newObjectEv(QJSEngine *self) {
  return new QJSValue(self->newObject());
}

//  QJSValue QJSEngine::newSymbol(const QString &name)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine9newSymbolERK7QString(
    QJSEngine *self,
    const QString *name) {
  return new QJSValue(self->newSymbol(*name));
}

//  QJSValue QJSEngine::newArray(uint length)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine8newArrayEj(QJSEngine *self, uint length) {
  return new QJSValue(self->newArray(length));
}

//  QJSValue QJSEngine::newQObject(QObject *object)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine10newQObjectEP7QObject(
    QJSEngine *self,
    QObject *object) {
  return new QJSValue(self->newQObject(object));
}

//  QJSValue QJSEngine::newQMetaObject(const QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine14newQMetaObjectEPK11QMetaObject(
    QJSEngine *self,
    const QMetaObject *metaObject) {
  return new QJSValue(self->newQMetaObject(metaObject));
}

//  QJSValue QJSEngine::newErrorObject(QJSValue::ErrorType errorType, const
//      QString &message)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine14newErrorObjectEN8QJSValue9ErrorTypeERK7QString(
    QJSEngine *self,
    QJSValue::ErrorType errorType,
    const QString *message) {
  return new QJSValue(self->newErrorObject(errorType, *message));
}

//  void QJSEngine::collectGarbage()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine14collectGarbageEv(QJSEngine *self) {
  self->collectGarbage();
}

//  void QJSEngine::setObjectOwnership(QObject *a0, ObjectOwnership a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine18setObjectOwnershipEP7QObjectNS_15ObjectOwnershipE(
    QObject *a0,
    QJSEngine::ObjectOwnership a1) {
  QJSEngine::setObjectOwnership(a0, a1);
}

//  ObjectOwnership QJSEngine::objectOwnership(QObject *a0)
extern "C" Q_DECL_EXPORT
QJSEngine::ObjectOwnership ritual_ZN9QJSEngine15objectOwnershipEP7QObject(
    QObject *a0) {
  return QJSEngine::objectOwnership(a0);
}

//  void QJSEngine::installExtensions(Extensions extensions, const QJSValue
//      &object)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine17installExtensionsE6QFlagsINS_9ExtensionEERK8QJSValue(
    QJSEngine *self,
    int extensions,
    const QJSValue *object) {
  self->installExtensions(
      QFlags<QJSEngine::Extension>::fromInt(extensions),
      *object);
}

//  void QJSEngine::setInterrupted(bool interrupted)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine14setInterruptedEb(
    QJSEngine *self,
    bool interrupted) {
  self->setInterrupted(interrupted);
}

//  bool QJSEngine::isInterrupted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QJSEngine13isInterruptedEv(const QJSEngine *self) {
  return self->isInterrupted();
}

//  QV4::ExecutionEngine *QJSEngine::handle() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK9QJSEngine6handleEv(const QJSEngine *self) {
  return self->handle();
}

//  void QJSEngine::throwError(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine10throwErrorERK7QString(
    QJSEngine *self,
    const QString *message) {
  self->throwError(*message);
}

//  void QJSEngine::throwError(QJSValue::ErrorType errorType, const QString
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine10throwErrorEN8QJSValue9ErrorTypeERK7QString(
    QJSEngine *self,
    QJSValue::ErrorType errorType,
    const QString *message) {
  self->throwError(errorType, *message);
}

//  void QJSEngine::throwError(const QJSValue &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine10throwErrorERK8QJSValue(
    QJSEngine *self,
    const QJSValue *error) {
  self->throwError(*error);
}

//  bool QJSEngine::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QJSEngine8hasErrorEv(const QJSEngine *self) {
  return self->hasError();
}

//  QJSValue QJSEngine::catchError()
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine10catchErrorEv(QJSEngine *self) {
  return new QJSValue(self->catchError());
}

//  QString QJSEngine::uiLanguage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QJSEngine10uiLanguageEv(const QJSEngine *self) {
  return new QString(self->uiLanguage());
}

//  void QJSEngine::setUiLanguage(const QString &language)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine13setUiLanguageERK7QString(
    QJSEngine *self,
    const QString *language) {
  self->setUiLanguage(*language);
}

//  QString QJSEngine::convertQObjectToString(QObject *object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QJSEngine22convertQObjectToStringEP7QObject(
    QJSEngine *self,
    QObject *object) {
  return new QString(self->convertQObjectToString(object));
}

//  QString QJSEngine::convertDateTimeToString(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QJSEngine23convertDateTimeToStringERK9QDateTime(
    QJSEngine *self,
    const QDateTime *dateTime) {
  return new QString(self->convertDateTimeToString(*dateTime));
}

//  double QJSEngine::convertDateTimeToNumber(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QJSEngine23convertDateTimeToNumberERK9QDateTime(
    QJSEngine *self,
    const QDateTime *dateTime) {
  return self->convertDateTimeToNumber(*dateTime);
}

//  QDate QJSEngine::convertDateTimeToDate(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN9QJSEngine21convertDateTimeToDateERK9QDateTime(
    const QDateTime *dateTime) {
  return new QDate(QJSEngine::convertDateTimeToDate(*dateTime));
}

//  QJSEnginePrivate *QJSEngine::d_func()
extern "C" Q_DECL_EXPORT
QJSEnginePrivate *ritual_ZN9QJSEngine6d_funcEv(QJSEngine *self) {
  return self->d_func();
}

//  const QJSEnginePrivate *QJSEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QJSEnginePrivate *ritual_ZNK9QJSEngine6d_funcEv(
    const QJSEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQJSEngine, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QJSEngine(QJSEngine *self, const char *key, void *call) {
  return static_cast<CuteQJSEngine *>(self)->take(key, call);
}
