//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlcontext.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlcontext.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qobject.h>
#include <QtCore/qurl.h>
#include <QtQml/qjsvalue.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlContext that Python can take functions over in. Every QQmlContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlContextCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlContextCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContextCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContextCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContextCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContextCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContextCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlContext : public QQmlContext {
public:
  using QQmlContext::QQmlContext;
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
      CuteQQmlContextCall0 call = reinterpret_cast<CuteQQmlContextCall0>(taken[0]);
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
      CuteQQmlContextCall1 call = reinterpret_cast<CuteQQmlContextCall1>(taken[1]);
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
      CuteQQmlContextCall2 call = reinterpret_cast<CuteQQmlContextCall2>(taken[2]);
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
      CuteQQmlContextCall3 call = reinterpret_cast<CuteQQmlContextCall3>(taken[3]);
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
      CuteQQmlContextCall4 call = reinterpret_cast<CuteQQmlContextCall4>(taken[4]);
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
      CuteQQmlContextCall5 call = reinterpret_cast<CuteQQmlContextCall5>(taken[5]);
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
      CuteQQmlContextCall6 call = reinterpret_cast<CuteQQmlContextCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQmlContext10metaObjectEv(
    const QQmlContext *self) {
  return self->metaObject();
}

//  QString QQmlContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlContext::tr(s, c, n));
}

//  QQmlContextPrivate *QQmlContext::d_func()
extern "C" Q_DECL_EXPORT
QQmlContextPrivate *ritual_ZN11QQmlContext6d_funcEv(QQmlContext *self) {
  return self->d_func();
}

//  const QQmlContextPrivate *QQmlContext::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlContextPrivate *ritual_ZNK11QQmlContext6d_funcEv(
    const QQmlContext *self) {
  return self->d_func();
}

//  QQmlContext::QQmlContext(QQmlEngine *parent, QObject *objParent)
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZN11QQmlContextC1EP10QQmlEngineP7QObject(
    QQmlEngine *parent,
    QObject *objParent) {
  return new CuteQQmlContext(parent, objParent);
}

//  QQmlContext::QQmlContext(QQmlContext *parent, QObject *objParent)
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZN11QQmlContextC1EPS_P7QObject(
    QQmlContext *parent,
    QObject *objParent) {
  return new CuteQQmlContext(parent, objParent);
}

//  QQmlContext::~QQmlContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlContextD1Ev(QQmlContext *self) {
  delete self;
}

//  bool QQmlContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlContext7isValidEv(const QQmlContext *self) {
  return self->isValid();
}

//  QQmlEngine *QQmlContext::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK11QQmlContext6engineEv(const QQmlContext *self) {
  return self->engine();
}

//  QQmlContext *QQmlContext::parentContext() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK11QQmlContext13parentContextEv(
    const QQmlContext *self) {
  return self->parentContext();
}

//  QList<QQmlContext *> QQmlContext::childContexts() const
extern "C" Q_DECL_EXPORT
QList<QQmlContext *> *ritual_ZNK11QQmlContext13childContextsEv(
    const QQmlContext *self) {
  return new QList<QQmlContext *>(self->childContexts());
}

//  QObject *QQmlContext::contextObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QQmlContext13contextObjectEv(const QQmlContext *self) {
  return self->contextObject();
}

//  void QQmlContext::setContextObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlContext16setContextObjectEP7QObject(
    QQmlContext *self,
    QObject *a0) {
  self->setContextObject(a0);
}

//  QVariant QQmlContext::contextProperty(const QString &a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QQmlContext15contextPropertyERK7QString(
    const QQmlContext *self,
    const QString *a0) {
  return new QVariant(self->contextProperty(*a0));
}

//  void QQmlContext::setContextProperty(const QString &a0, QObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlContext18setContextPropertyERK7QStringP7QObject(
    QQmlContext *self,
    const QString *a0,
    QObject *a1) {
  self->setContextProperty(*a0, a1);
}

//  void QQmlContext::setContextProperty(const QString &a0, const QVariant
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlContext18setContextPropertyERK7QStringRK8QVariant(
    QQmlContext *self,
    const QString *a0,
    const QVariant *a1) {
  self->setContextProperty(*a0, *a1);
}

//  QString QQmlContext::nameForObject(const QObject *a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlContext13nameForObjectEPK7QObject(
    const QQmlContext *self,
    const QObject *a0) {
  return new QString(self->nameForObject(a0));
}

//  QObject *QQmlContext::objectForName(const QString &a0) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QQmlContext13objectForNameERK7QString(
    const QQmlContext *self,
    const QString *a0) {
  return self->objectForName(*a0);
}

//  QObject *QQmlContext::findObjectRecursively(const QString &id) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QQmlContext21findObjectRecursivelyERK7QString(
    const QQmlContext *self,
    const QString *id) {
  return self->findObjectRecursively(*id);
}

//  QList<QObject *> QQmlContext::findObjectsRecursively(const QString &id)
//      const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK11QQmlContext22findObjectsRecursivelyERK7QString(
    const QQmlContext *self,
    const QString *id) {
  return new QList<QObject *>(self->findObjectsRecursively(*id));
}

//  QUrl QQmlContext::resolvedUrl(const QUrl &a0) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK11QQmlContext11resolvedUrlERK4QUrl(
    const QQmlContext *self,
    const QUrl *a0) {
  return new QUrl(self->resolvedUrl(*a0));
}

//  void QQmlContext::setBaseUrl(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlContext10setBaseUrlERK4QUrl(
    QQmlContext *self,
    const QUrl *a0) {
  self->setBaseUrl(*a0);
}

//  QUrl QQmlContext::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK11QQmlContext7baseUrlEv(const QQmlContext *self) {
  return new QUrl(self->baseUrl());
}

//  QJSValue QQmlContext::importedScript(const QString &name) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK11QQmlContext14importedScriptERK7QString(
    const QQmlContext *self,
    const QString *name) {
  return new QJSValue(self->importedScript(*name));
}

//  QQmlContext::QQmlContext(QQmlEngine *a0, bool a1)
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZN11QQmlContextC1EP10QQmlEngineb(
    QQmlEngine *a0,
    bool a1) {
  return new CuteQQmlContext(a0, a1);
}

//  a Python function taken by a CuteQQmlContext, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlContext(
    QQmlContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlContext *>(self)->take(key, call);
}

//  QList<QQmlContext *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlContext *> *ritual_list_make_QQmlContext_ptr() {
  return new QList<QQmlContext *>();
}

//  void QList<QQmlContext *>::append(const QQmlContext * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlContext_ptr(
    QList<QQmlContext *> *self,
    QQmlContext *element) {
  self->append(element);
}

//  qsizetype QList<QQmlContext *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlContext_ptr(
    const QList<QQmlContext *> *self) {
  return self->size();
}

//  const QQmlContext * &QList<QQmlContext *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_list_at_QQmlContext_ptr(
    const QList<QQmlContext *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQmlContext *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlContext_ptr(QList<QQmlContext *> *self) {
  delete self;
}
