//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjsengine.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 42. Kept as it is when the
//  generator runs again.
#include <QtQml/QtQml>
#include <QtQml/qjsengine.h>
#include <QtCore/qstring.h>
#include <QtQml/qjsvalue.h>
#include <QtCore/qmetatype.h>
#include <QtQml/qjsprimitivevalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QJSManagedValue>
#include <QtCore/QMetaType>

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

//  void *QJSEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QJSEngine11qt_metacastEPKc(QJSEngine *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QJSEngine::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QJSEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QJSEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QJSValue QJSEngine::evaluate(const QString &program, const QString
//      &fileName, int lineNumber, QStringList *exceptionStackTrace)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine8evaluateERK7QStringS2_iP5QListIS0_E(
    QJSEngine *self,
    const QString *program,
    const QString *fileName,
    int lineNumber,
    QStringList *exceptionStackTrace) {
  return new QJSValue(
      self->evaluate(
          *program,
          *fileName,
          lineNumber,
          exceptionStackTrace));
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

//  void QJSEngine::uiLanguageChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QJSEngine17uiLanguageChangedEv(QJSEngine *self) {
  self->uiLanguageChanged();
}

//  QJSPrimitiveValue QJSEngine::createPrimitive(QMetaType type, const void
//      *ptr)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN9QJSEngine15createPrimitiveE9QMetaTypePKv(
    QJSEngine *self,
    const QMetaType *type,
    const void *ptr) {
  return new QJSPrimitiveValue(self->createPrimitive(*type, ptr));
}

//  QJSManagedValue QJSEngine::createManaged(QMetaType type, const void *ptr)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN9QJSEngine13createManagedE9QMetaTypePKv(
    QJSEngine *self,
    const QMetaType *type,
    const void *ptr) {
  return new QJSManagedValue(self->createManaged(*type, ptr));
}

//  QJSValue QJSEngine::create(QMetaType type, const void *ptr)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN9QJSEngine6createE9QMetaTypePKv(
    QJSEngine *self,
    const QMetaType *type,
    const void *ptr) {
  return new QJSValue(self->create(*type, ptr));
}

//  bool QJSEngine::convertPrimitive(const QJSPrimitiveValue &value,
//      QMetaType type, void *ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine16convertPrimitiveERK17QJSPrimitiveValue9QMetaTypePv(
    const QJSPrimitiveValue *value,
    const QMetaType *type,
    void *ptr) {
  return QJSEngine::convertPrimitive(*value, *type, ptr);
}

//  bool QJSEngine::convertManaged(const QJSManagedValue &value, int type,
//      void *ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine14convertManagedERK15QJSManagedValueiPv(
    const QJSManagedValue *value,
    int type,
    void *ptr) {
  return QJSEngine::convertManaged(*value, type, ptr);
}

//  bool QJSEngine::convertManaged(const QJSManagedValue &value, QMetaType
//      type, void *ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine14convertManagedERK15QJSManagedValue9QMetaTypePv(
    const QJSManagedValue *value,
    const QMetaType *type,
    void *ptr) {
  return QJSEngine::convertManaged(*value, *type, ptr);
}

//  bool QJSEngine::convertV2(const QJSValue &value, QMetaType metaType, void
//      *ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine9convertV2ERK8QJSValue9QMetaTypePv(
    const QJSValue *value,
    const QMetaType *metaType,
    void *ptr) {
  return QJSEngine::convertV2(*value, *metaType, ptr);
}

//  bool QJSEngine::convertString(const QString &string, QMetaType metaType,
//      void *ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine13convertStringERK7QString9QMetaTypePv(
    const QString *string,
    const QMetaType *metaType,
    void *ptr) {
  return QJSEngine::convertString(*string, *metaType, ptr);
}

//  bool QJSEngine::convertVariant(const QVariant &value, QMetaType metaType,
//      void *ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine14convertVariantERK8QVariant9QMetaTypePv(
    QJSEngine *self,
    const QVariant *value,
    const QMetaType *metaType,
    void *ptr) {
  return self->convertVariant(*value, *metaType, ptr);
}

//  bool QJSEngine::convertMetaType(QMetaType fromType, const void *from,
//      QMetaType toType, void *to)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine15convertMetaTypeE9QMetaTypePKvS0_Pv(
    QJSEngine *self,
    const QMetaType *fromType,
    const void *from,
    const QMetaType *toType,
    void *to) {
  return self->convertMetaType(*fromType, from, *toType, to);
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

//  QJSEngine::QJSEngine(QJSEnginePrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZN9QJSEngineC1ER16QJSEnginePrivateP7QObject(
    QJSEnginePrivate *dd,
    QObject *parent) {
  return new CuteQJSEngine(*dd, parent);
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

//  a QJSManagedValue a ritual of QJSEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QJSEngine__QJSManagedValue(QJSManagedValue *self) {
  delete self;
}

//  QJSValue QJSEngine::toScriptValue<int>(const int &value)
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN9QJSEngine13toScriptValueIiEE8QJSValueRKT_(
    QJSEngine *self,
    int value) {
  return new QJSValue(self->toScriptValue<int>(value));
}

//  QJSValue QJSEngine::toScriptValue<double>(const double &value)
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN9QJSEngine13toScriptValueIdEE8QJSValueRKT_(
    QJSEngine *self,
    double value) {
  return new QJSValue(self->toScriptValue<double>(value));
}

//  QJSValue QJSEngine::toScriptValue<bool>(const bool &value)
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN9QJSEngine13toScriptValueIbEE8QJSValueRKT_(
    QJSEngine *self,
    bool value) {
  return new QJSValue(self->toScriptValue<bool>(value));
}

//  QJSValue QJSEngine::toScriptValue<QString>(const QString &value)
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN9QJSEngine13toScriptValueI7QStringEE8QJSValueRKT_(
    QJSEngine *self,
    const QString *value) {
  return new QJSValue(self->toScriptValue<QString>(*value));
}

//  QJSValue QJSEngine::toScriptValue<QVariant>(const QVariant &value)
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN9QJSEngine13toScriptValueI8QVariantEE8QJSValueRKT_(
    QJSEngine *self,
    const QVariant *value) {
  return new QJSValue(self->toScriptValue<QVariant>(*value));
}

//  QJSManagedValue QJSEngine::toManagedValue<int>(const int &value)
extern "C" Q_DECL_EXPORT
QJSManagedValue * ritual_ZN9QJSEngine14toManagedValueIiEE15QJSManagedValueRKT_(
    QJSEngine *self,
    int value) {
  return new QJSManagedValue(self->toManagedValue<int>(value));
}

//  QJSManagedValue QJSEngine::toManagedValue<double>(const double &value)
extern "C" Q_DECL_EXPORT
QJSManagedValue * ritual_ZN9QJSEngine14toManagedValueIdEE15QJSManagedValueRKT_(
    QJSEngine *self,
    double value) {
  return new QJSManagedValue(self->toManagedValue<double>(value));
}

//  QJSManagedValue QJSEngine::toManagedValue<bool>(const bool &value)
extern "C" Q_DECL_EXPORT
QJSManagedValue * ritual_ZN9QJSEngine14toManagedValueIbEE15QJSManagedValueRKT_(
    QJSEngine *self,
    bool value) {
  return new QJSManagedValue(self->toManagedValue<bool>(value));
}

//  QJSManagedValue QJSEngine::toManagedValue<QString>(const QString &value)
extern "C" Q_DECL_EXPORT
QJSManagedValue * ritual_ZN9QJSEngine14toManagedValueI7QStringEE15QJSManagedValueRKT_(
    QJSEngine *self,
    const QString *value) {
  return new QJSManagedValue(self->toManagedValue<QString>(*value));
}

//  QJSManagedValue QJSEngine::toManagedValue<QVariant>(const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
QJSManagedValue * ritual_ZN9QJSEngine14toManagedValueI8QVariantEE15QJSManagedValueRKT_(
    QJSEngine *self,
    const QVariant *value) {
  return new QJSManagedValue(self->toManagedValue<QVariant>(*value));
}

//  QJSPrimitiveValue QJSEngine::toPrimitiveValue<int>(const int &value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZN9QJSEngine16toPrimitiveValueIiEE17QJSPrimitiveValueRKT_(
    QJSEngine *self,
    int value) {
  return new QJSPrimitiveValue(self->toPrimitiveValue<int>(value));
}

//  QJSPrimitiveValue QJSEngine::toPrimitiveValue<double>(const double
//      &value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZN9QJSEngine16toPrimitiveValueIdEE17QJSPrimitiveValueRKT_(
    QJSEngine *self,
    double value) {
  return new QJSPrimitiveValue(self->toPrimitiveValue<double>(value));
}

//  QJSPrimitiveValue QJSEngine::toPrimitiveValue<bool>(const bool &value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZN9QJSEngine16toPrimitiveValueIbEE17QJSPrimitiveValueRKT_(
    QJSEngine *self,
    bool value) {
  return new QJSPrimitiveValue(self->toPrimitiveValue<bool>(value));
}

//  QJSPrimitiveValue QJSEngine::toPrimitiveValue<QString>(const QString
//      &value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZN9QJSEngine16toPrimitiveValueI7QStringEE17QJSPrimitiveValueRKT_(
    QJSEngine *self,
    const QString *value) {
  return new QJSPrimitiveValue(self->toPrimitiveValue<QString>(*value));
}

//  QJSPrimitiveValue QJSEngine::toPrimitiveValue<QVariant>(const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZN9QJSEngine16toPrimitiveValueI8QVariantEE17QJSPrimitiveValueRKT_(
    QJSEngine *self,
    const QVariant *value) {
  return new QJSPrimitiveValue(self->toPrimitiveValue<QVariant>(*value));
}

//  int QJSEngine::fromScriptValue<int>(const QJSValue &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QJSEngine15fromScriptValueIiEET_RK8QJSValue(
    QJSEngine *self,
    const QJSValue *value) {
  return self->fromScriptValue<int>(*value);
}

//  double QJSEngine::fromScriptValue<double>(const QJSValue &value)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QJSEngine15fromScriptValueIdEET_RK8QJSValue(
    QJSEngine *self,
    const QJSValue *value) {
  return self->fromScriptValue<double>(*value);
}

//  bool QJSEngine::fromScriptValue<bool>(const QJSValue &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine15fromScriptValueIbEET_RK8QJSValue(
    QJSEngine *self,
    const QJSValue *value) {
  return self->fromScriptValue<bool>(*value);
}

//  QString QJSEngine::fromScriptValue<QString>(const QJSValue &value)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QJSEngine15fromScriptValueI7QStringEET_RK8QJSValue(
    QJSEngine *self,
    const QJSValue *value) {
  return new QString(self->fromScriptValue<QString>(*value));
}

//  QVariant QJSEngine::fromScriptValue<QVariant>(const QJSValue &value)
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZN9QJSEngine15fromScriptValueI8QVariantEET_RK8QJSValue(
    QJSEngine *self,
    const QJSValue *value) {
  return new QVariant(self->fromScriptValue<QVariant>(*value));
}

//  int QJSEngine::fromManagedValue<int>(const QJSManagedValue &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QJSEngine16fromManagedValueIiEET_RK15QJSManagedValue(
    QJSEngine *self,
    const QJSManagedValue *value) {
  return self->fromManagedValue<int>(*value);
}

//  double QJSEngine::fromManagedValue<double>(const QJSManagedValue &value)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QJSEngine16fromManagedValueIdEET_RK15QJSManagedValue(
    QJSEngine *self,
    const QJSManagedValue *value) {
  return self->fromManagedValue<double>(*value);
}

//  bool QJSEngine::fromManagedValue<bool>(const QJSManagedValue &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine16fromManagedValueIbEET_RK15QJSManagedValue(
    QJSEngine *self,
    const QJSManagedValue *value) {
  return self->fromManagedValue<bool>(*value);
}

//  QString QJSEngine::fromManagedValue<QString>(const QJSManagedValue
//      &value)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QJSEngine16fromManagedValueI7QStringEET_RK15QJSManagedValue(
    QJSEngine *self,
    const QJSManagedValue *value) {
  return new QString(self->fromManagedValue<QString>(*value));
}

//  QVariant QJSEngine::fromManagedValue<QVariant>(const QJSManagedValue
//      &value)
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZN9QJSEngine16fromManagedValueI8QVariantEET_RK15QJSManagedValue(
    QJSEngine *self,
    const QJSManagedValue *value) {
  return new QVariant(self->fromManagedValue<QVariant>(*value));
}

//  int QJSEngine::fromPrimitiveValue<int>(const QJSPrimitiveValue &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QJSEngine18fromPrimitiveValueIiEET_RK17QJSPrimitiveValue(
    QJSEngine *self,
    const QJSPrimitiveValue *value) {
  return self->fromPrimitiveValue<int>(*value);
}

//  double QJSEngine::fromPrimitiveValue<double>(const QJSPrimitiveValue
//      &value)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QJSEngine18fromPrimitiveValueIdEET_RK17QJSPrimitiveValue(
    QJSEngine *self,
    const QJSPrimitiveValue *value) {
  return self->fromPrimitiveValue<double>(*value);
}

//  bool QJSEngine::fromPrimitiveValue<bool>(const QJSPrimitiveValue &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine18fromPrimitiveValueIbEET_RK17QJSPrimitiveValue(
    QJSEngine *self,
    const QJSPrimitiveValue *value) {
  return self->fromPrimitiveValue<bool>(*value);
}

//  QString QJSEngine::fromPrimitiveValue<QString>(const QJSPrimitiveValue
//      &value)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QJSEngine18fromPrimitiveValueI7QStringEET_RK17QJSPrimitiveValue(
    QJSEngine *self,
    const QJSPrimitiveValue *value) {
  return new QString(self->fromPrimitiveValue<QString>(*value));
}

//  QVariant QJSEngine::fromPrimitiveValue<QVariant>(const QJSPrimitiveValue
//      &value)
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZN9QJSEngine18fromPrimitiveValueI8QVariantEET_RK17QJSPrimitiveValue(
    QJSEngine *self,
    const QJSPrimitiveValue *value) {
  return new QVariant(self->fromPrimitiveValue<QVariant>(*value));
}

//  int QJSEngine::fromVariant<int>(const QVariant &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QJSEngine11fromVariantIiEET_RK8QVariant(
    QJSEngine *self,
    const QVariant *value) {
  return self->fromVariant<int>(*value);
}

//  double QJSEngine::fromVariant<double>(const QVariant &value)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QJSEngine11fromVariantIdEET_RK8QVariant(
    QJSEngine *self,
    const QVariant *value) {
  return self->fromVariant<double>(*value);
}

//  bool QJSEngine::fromVariant<bool>(const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QJSEngine11fromVariantIbEET_RK8QVariant(
    QJSEngine *self,
    const QVariant *value) {
  return self->fromVariant<bool>(*value);
}

//  QString QJSEngine::fromVariant<QString>(const QVariant &value)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QJSEngine11fromVariantI7QStringEET_RK8QVariant(
    QJSEngine *self,
    const QVariant *value) {
  return new QString(self->fromVariant<QString>(*value));
}

//  QVariant QJSEngine::fromVariant<QVariant>(const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZN9QJSEngine11fromVariantI8QVariantEET_RKS1_(
    QJSEngine *self,
    const QVariant *value) {
  return new QVariant(self->fromVariant<QVariant>(*value));
}

//  QJSValue QJSEngine::newQMetaObject<QObject>()
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN9QJSEngine14newQMetaObjectI7QObjectEE8QJSValuev(
    QJSEngine *self) {
  return new QJSValue(self->newQMetaObject<QObject>());
}

//  QJSValue QJSEngine::newQMetaObject<QJSEngine>()
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN9QJSEngine14newQMetaObjectIS_EE8QJSValuev(
    QJSEngine *self) {
  return new QJSValue(self->newQMetaObject<QJSEngine>());
}

//  QDate QJSEngine::coerceValue<QDateTime, QDate>(const QDateTime &from)
extern "C" Q_DECL_EXPORT
QDate * ritual_ZN9QJSEngine11coerceValueI9QDateTime5QDateEET0_RKT_(
    QJSEngine *self,
    const QDateTime *from) {
  return new QDate(self->coerceValue<QDateTime, QDate>(*from));
}

//  QDateTime QJSEngine::coerceValue<QDate, QDateTime>(const QDate &from)
extern "C" Q_DECL_EXPORT
QDateTime * ritual_ZN9QJSEngine11coerceValueI5QDate9QDateTimeEET0_RKT_(
    QJSEngine *self,
    const QDate *from) {
  return new QDateTime(self->coerceValue<QDate, QDateTime>(*from));
}

//  QString QJSEngine::coerceValue<QDateTime, QString>(const QDateTime &from)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QJSEngine11coerceValueI9QDateTime7QStringEET0_RKT_(
    QJSEngine *self,
    const QDateTime *from) {
  return new QString(self->coerceValue<QDateTime, QString>(*from));
}

//  QString QJSEngine::coerceValue<QDate, QString>(const QDate &from)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QJSEngine11coerceValueI5QDate7QStringEET0_RKT_(
    QJSEngine *self,
    const QDate *from) {
  return new QString(self->coerceValue<QDate, QString>(*from));
}

//  QString QJSEngine::coerceValue<QVariant, QString>(const QVariant &from)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QJSEngine11coerceValueI8QVariant7QStringEET0_RKT_(
    QJSEngine *self,
    const QVariant *from) {
  return new QString(self->coerceValue<QVariant, QString>(*from));
}
