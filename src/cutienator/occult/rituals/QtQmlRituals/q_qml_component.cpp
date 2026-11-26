//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlcomponent.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlcomponent.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qanystringview.h>
#include <QtQml/qqmlerror.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlComponent that Python can take functions over in. Every QQmlComponent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQmlComponentCall0)(const void *, QQmlContext *, int *);
typedef void * (*CuteQQmlComponentCall1)(const void *, QQmlContext *, int *);
typedef void (*CuteQQmlComponentCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlComponentCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlComponentCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlComponent : public QQmlComponent {
public:
  using QQmlComponent::QQmlComponent;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QQmlComponent6createEP11QQmlContext")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQmlComponent11beginCreateEP11QQmlContext")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQmlComponent14completeCreateEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QObject *QQmlComponent::create(QQmlContext *context)
  QObject *create(QQmlContext *context) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlComponentCall0 call = reinterpret_cast<CuteQQmlComponentCall0>(taken[0]);
      void * given = call(this, context, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlComponent::create(context);
  }

  //  QObject *QQmlComponent::beginCreate(QQmlContext *a0)
  QObject *beginCreate(QQmlContext *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlComponentCall1 call = reinterpret_cast<CuteQQmlComponentCall1>(taken[1]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlComponent::beginCreate(a0);
  }

  //  void QQmlComponent::completeCreate()
  void completeCreate() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlComponentCall2 call = reinterpret_cast<CuteQQmlComponentCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlComponent::completeCreate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlComponentCall3 call = reinterpret_cast<CuteQQmlComponentCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlComponentCall4 call = reinterpret_cast<CuteQQmlComponentCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlComponentCall5 call = reinterpret_cast<CuteQQmlComponentCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlComponentCall6 call = reinterpret_cast<CuteQQmlComponentCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlComponentCall7 call = reinterpret_cast<CuteQQmlComponentCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlComponentCall8 call = reinterpret_cast<CuteQQmlComponentCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlComponentCall9 call = reinterpret_cast<CuteQQmlComponentCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlComponent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQmlComponent10metaObjectEv(
    const QQmlComponent *self) {
  return self->metaObject();
}

//  void *QQmlComponent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QQmlComponent11qt_metacastEPKc(
    QQmlComponent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlComponent::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQmlComponent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlComponent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlComponent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQmlComponent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlComponent::tr(s, c, n));
}

//  QQmlComponentPrivate *QQmlComponent::d_func()
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate *ritual_ZN13QQmlComponent6d_funcEv(
    QQmlComponent *self) {
  return self->d_func();
}

//  const QQmlComponentPrivate *QQmlComponent::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlComponentPrivate *ritual_ZNK13QQmlComponent6d_funcEv(
    const QQmlComponent *self) {
  return self->d_func();
}

//  QQmlComponent::QQmlComponent(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP7QObject(QObject *parent) {
  return new CuteQQmlComponent(parent);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEngineP7QObject(
    QQmlEngine *a0,
    QObject *parent) {
  return new CuteQQmlComponent(a0, parent);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QString &fileName,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEngineRK7QStringP7QObject(
    QQmlEngine *a0,
    const QString *fileName,
    QObject *parent) {
  return new CuteQQmlComponent(a0, *fileName, parent);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QString &fileName,
//      CompilationMode mode, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEngineRK7QStringNS_15CompilationModeEP7QObject(
    QQmlEngine *a0,
    const QString *fileName,
    QQmlComponent::CompilationMode mode,
    QObject *parent) {
  return new CuteQQmlComponent(a0, *fileName, mode, parent);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QUrl &url, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEngineRK4QUrlP7QObject(
    QQmlEngine *a0,
    const QUrl *url,
    QObject *parent) {
  return new CuteQQmlComponent(a0, *url, parent);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QUrl &url,
//      CompilationMode mode, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEngineRK4QUrlNS_15CompilationModeEP7QObject(
    QQmlEngine *a0,
    const QUrl *url,
    QQmlComponent::CompilationMode mode,
    QObject *parent) {
  return new CuteQQmlComponent(a0, *url, mode, parent);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *engine, QAnyStringView uri,
//      QAnyStringView typeName, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEngine14QAnyStringViewS2_P7QObject(
    QQmlEngine *engine,
    const QString *uri,
    const QString *typeName,
    QObject *parent) {
  return new CuteQQmlComponent(
      engine,
      QAnyStringView(*uri),
      QAnyStringView(*typeName),
      parent);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *engine, QAnyStringView uri,
//      QAnyStringView typeName, CompilationMode mode, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEngine14QAnyStringViewS2_NS_15CompilationModeEP7QObject(
    QQmlEngine *engine,
    const QString *uri,
    const QString *typeName,
    QQmlComponent::CompilationMode mode,
    QObject *parent) {
  return new CuteQQmlComponent(
      engine,
      QAnyStringView(*uri),
      QAnyStringView(*typeName),
      mode,
      parent);
}

//  QQmlComponent::~QQmlComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponentD1Ev(QQmlComponent *self) {
  delete self;
}

//  Status QQmlComponent::status() const
extern "C" Q_DECL_EXPORT
QQmlComponent::Status ritual_ZNK13QQmlComponent6statusEv(
    const QQmlComponent *self) {
  return self->status();
}

//  bool QQmlComponent::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlComponent6isNullEv(const QQmlComponent *self) {
  return self->isNull();
}

//  bool QQmlComponent::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlComponent7isReadyEv(const QQmlComponent *self) {
  return self->isReady();
}

//  bool QQmlComponent::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlComponent7isErrorEv(const QQmlComponent *self) {
  return self->isError();
}

//  bool QQmlComponent::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlComponent9isLoadingEv(const QQmlComponent *self) {
  return self->isLoading();
}

//  bool QQmlComponent::isBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlComponent7isBoundEv(const QQmlComponent *self) {
  return self->isBound();
}

//  QList<QQmlError> QQmlComponent::errors() const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK13QQmlComponent6errorsEv(
    const QQmlComponent *self) {
  return new QList<QQmlError>(self->errors());
}

//  QString QQmlComponent::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQmlComponent11errorStringEv(
    const QQmlComponent *self) {
  return new QString(self->errorString());
}

//  qreal QQmlComponent::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQmlComponent8progressEv(const QQmlComponent *self) {
  return self->progress();
}

//  QUrl QQmlComponent::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QQmlComponent3urlEv(const QQmlComponent *self) {
  return new QUrl(self->url());
}

//  QObject *QQmlComponent::create(QQmlContext *context)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN13QQmlComponent6createEP11QQmlContext(
    QQmlComponent *self,
    QQmlContext *context) {
  return self->create(context);
}

//  QObject *QQmlComponent::createWithInitialProperties(const QVariantMap
//      &initialProperties, QQmlContext *context)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN13QQmlComponent27createWithInitialPropertiesERK4QMapI7QString8QVariantEP11QQmlContext(
    QQmlComponent *self,
    const QMap<QString, QVariant> *initialProperties,
    QQmlContext *context) {
  return self->createWithInitialProperties(*initialProperties, context);
}

//  void QQmlComponent::setInitialProperties(QObject *component, const
//      QVariantMap &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent20setInitialPropertiesEP7QObjectRK4QMapI7QString8QVariantE(
    QQmlComponent *self,
    QObject *component,
    const QMap<QString, QVariant> *properties) {
  self->setInitialProperties(component, *properties);
}

//  QObject *QQmlComponent::beginCreate(QQmlContext *a0)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN13QQmlComponent11beginCreateEP11QQmlContext(
    QQmlComponent *self,
    QQmlContext *a0) {
  return self->beginCreate(a0);
}

//  void QQmlComponent::completeCreate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent14completeCreateEv(QQmlComponent *self) {
  self->completeCreate();
}

//  void QQmlComponent::create(QQmlIncubator &a0, QQmlContext *context,
//      QQmlContext *forContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent6createER13QQmlIncubatorP11QQmlContextS3_(
    QQmlComponent *self,
    QQmlIncubator *a0,
    QQmlContext *context,
    QQmlContext *forContext) {
  self->create(*a0, context, forContext);
}

//  QQmlContext *QQmlComponent::creationContext() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK13QQmlComponent15creationContextEv(
    const QQmlComponent *self) {
  return self->creationContext();
}

//  QQmlEngine *QQmlComponent::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK13QQmlComponent6engineEv(const QQmlComponent *self) {
  return self->engine();
}

//  QQmlComponentAttached *QQmlComponent::qmlAttachedProperties(QObject *a0)
extern "C" Q_DECL_EXPORT
QQmlComponentAttached *ritual_ZN13QQmlComponent21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQmlComponent::qmlAttachedProperties(a0);
}

//  void QQmlComponent::loadUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent7loadUrlERK4QUrl(
    QQmlComponent *self,
    const QUrl *url) {
  self->loadUrl(*url);
}

//  void QQmlComponent::loadUrl(const QUrl &url, CompilationMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent7loadUrlERK4QUrlNS_15CompilationModeE(
    QQmlComponent *self,
    const QUrl *url,
    QQmlComponent::CompilationMode mode) {
  self->loadUrl(*url, mode);
}

//  void QQmlComponent::loadFromModule(QAnyStringView uri, QAnyStringView
//      typeName, QQmlComponent::CompilationMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent14loadFromModuleE14QAnyStringViewS0_NS_15CompilationModeE(
    QQmlComponent *self,
    const QString *uri,
    const QString *typeName,
    QQmlComponent::CompilationMode mode) {
  self->loadFromModule(
      QAnyStringView(*uri),
      QAnyStringView(*typeName),
      mode);
}

//  void QQmlComponent::setData(const QByteArray &data, const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent7setDataERK10QByteArrayRK4QUrl(
    QQmlComponent *self,
    const QByteArray *data,
    const QUrl *baseUrl) {
  self->setData(*data, *baseUrl);
}

//  void QQmlComponent::statusChanged(QQmlComponent::Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent13statusChangedENS_6StatusE(
    QQmlComponent *self,
    QQmlComponent::Status a0) {
  self->statusChanged(a0);
}

//  void QQmlComponent::progressChanged(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent15progressChangedEd(
    QQmlComponent *self,
    qreal a0) {
  self->progressChanged(a0);
}

//  QQmlComponent::QQmlComponent(QQmlComponentPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1ER20QQmlComponentPrivateP7QObject(
    QQmlComponentPrivate *dd,
    QObject *parent) {
  return new CuteQQmlComponent(*dd, parent);
}

#if QT_DEPRECATED_SINCE(6, 3)
//  void QQmlComponent::createObject(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent12createObjectEP14QQmlV4Function(
    QQmlComponent *self,
    QQmlV4FunctionPtr a0) {
  self->createObject(a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 3)

//  QObject *QQmlComponent::createObject(QObject *parent, const QVariantMap
//      &properties)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN13QQmlComponent12createObjectEP7QObjectRK4QMapI7QString8QVariantE(
    QQmlComponent *self,
    QObject *parent,
    const QMap<QString, QVariant> *properties) {
  return self->createObject(parent, *properties);
}

//  void QQmlComponent::incubateObject(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlComponent14incubateObjectEP14QQmlV4Function(
    QQmlComponent *self,
    QQmlV4FunctionPtr a0) {
  self->incubateObject(a0);
}

//  QQmlComponent::QQmlComponent(QQmlEngine *a0,
//      QV4::ExecutableCompilationUnit *compilationUnit, int a2, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN13QQmlComponentC1EP10QQmlEnginePN3QV425ExecutableCompilationUnitEiP7QObject(
    QQmlEngine *a0,
    QV4::ExecutableCompilationUnit *compilationUnit,
    int a2,
    QObject *parent) {
  return new CuteQQmlComponent(a0, compilationUnit, a2, parent);
}

//  a Python function taken by a CuteQQmlComponent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlComponent(
    QQmlComponent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlComponent *>(self)->take(key, call);
}

//  QObject *QQmlComponent::create(QQmlContext *context)
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN13QQmlComponent6createEP11QQmlContext(
    QQmlComponent *self,
    QQmlContext *context) {
  return self->QQmlComponent::create(context);
}

//  QObject *QQmlComponent::beginCreate(QQmlContext *a0)
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN13QQmlComponent11beginCreateEP11QQmlContext(
    QQmlComponent *self,
    QQmlContext *a0) {
  return self->QQmlComponent::beginCreate(a0);
}

//  void QQmlComponent::completeCreate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQmlComponent14completeCreateEv(QQmlComponent *self) {
  self->QQmlComponent::completeCreate();
}
