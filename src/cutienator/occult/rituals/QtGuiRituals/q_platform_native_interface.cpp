//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformnativeinterface.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformnativeinterface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qcursor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QPlatformNativeInterface that Python can take functions over in. Every QPlatformNativeInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformNativeInterfaceCall0)(const void *, const QByteArray *, int *);
typedef void * (*CuteQPlatformNativeInterfaceCall1)(const void *, const QByteArray *, QOpenGLContext *, int *);
typedef void * (*CuteQPlatformNativeInterfaceCall2)(const void *, const QByteArray *, QScreen *, int *);
typedef void * (*CuteQPlatformNativeInterfaceCall3)(const void *, const QByteArray *, QWindow *, int *);
typedef void * (*CuteQPlatformNativeInterfaceCall4)(const void *, const QByteArray *, QBackingStore *, int *);
#if !defined(QT_NO_CURSOR)
typedef void * (*CuteQPlatformNativeInterfaceCall5)(const void *, const QByteArray *, const QCursor *, int *);
#endif  // !defined(QT_NO_CURSOR)
typedef const QVariant * (*CuteQPlatformNativeInterfaceCall6)(const void *, QPlatformWindow *, const QString *, int *);
typedef const QVariant * (*CuteQPlatformNativeInterfaceCall7)(const void *, QPlatformWindow *, const QString *, const QVariant *, int *);
typedef void (*CuteQPlatformNativeInterfaceCall8)(const void *, QPlatformWindow *, const QString *, const QVariant *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformNativeInterfaceCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformNativeInterfaceCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformNativeInterface : public QPlatformNativeInterface {
public:
  using QPlatformNativeInterface::QPlatformNativeInterface;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface28nativeResourceForIntegrationERK10QByteArray")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface24nativeResourceForContextERK10QByteArrayP14QOpenGLContext")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface23nativeResourceForScreenERK10QByteArrayP7QScreen")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface23nativeResourceForWindowERK10QByteArrayP7QWindow")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface29nativeResourceForBackingStoreERK10QByteArrayP13QBackingStore")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface23nativeResourceForCursorERK10QByteArrayRK7QCursor")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QStringRK8QVariant")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatformWindowRK7QStringRK8QVariant")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void *QPlatformNativeInterface::nativeResourceForIntegration(const
  //      QByteArray &resource)
  void *nativeResourceForIntegration(const QByteArray &resource) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall0 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall0>(taken[0]);
      void * given = call(this, &resource, &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QPlatformNativeInterface::nativeResourceForIntegration(resource);
  }

  //  void *QPlatformNativeInterface::nativeResourceForContext(const
  //      QByteArray &resource, QOpenGLContext *context)
  void *nativeResourceForContext(
      const QByteArray &resource,
      QOpenGLContext *context) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall1 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall1>(taken[1]);
      void * given = call(this, &resource, context, &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QPlatformNativeInterface::nativeResourceForContext(resource, context);
  }

  //  void *QPlatformNativeInterface::nativeResourceForScreen(const
  //      QByteArray &resource, QScreen *screen)
  void *nativeResourceForScreen(
      const QByteArray &resource,
      QScreen *screen) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall2 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall2>(taken[2]);
      void * given = call(this, &resource, screen, &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QPlatformNativeInterface::nativeResourceForScreen(resource, screen);
  }

  //  void *QPlatformNativeInterface::nativeResourceForWindow(const
  //      QByteArray &resource, QWindow *window)
  void *nativeResourceForWindow(
      const QByteArray &resource,
      QWindow *window) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall3 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall3>(taken[3]);
      void * given = call(this, &resource, window, &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QPlatformNativeInterface::nativeResourceForWindow(resource, window);
  }

  //  void *QPlatformNativeInterface::nativeResourceForBackingStore(const
  //      QByteArray &resource, QBackingStore *backingStore)
  void *nativeResourceForBackingStore(
      const QByteArray &resource,
      QBackingStore *backingStore) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall4 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall4>(taken[4]);
      void * given = call(this, &resource, backingStore, &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QPlatformNativeInterface::nativeResourceForBackingStore(resource, backingStore);
  }

#if !defined(QT_NO_CURSOR)
  //  void *QPlatformNativeInterface::nativeResourceForCursor(const
  //      QByteArray &resource, const QCursor &cursor)
  void *nativeResourceForCursor(
      const QByteArray &resource,
      const QCursor &cursor) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall5 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall5>(taken[5]);
      void * given = call(this, &resource, &cursor, &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QPlatformNativeInterface::nativeResourceForCursor(resource, cursor);
  }
#endif  // !defined(QT_NO_CURSOR)

  //  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
  //      *window, const QString &name) const
  QVariant windowProperty(
      QPlatformWindow *window,
      const QString &name) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall6 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall6>(taken[6]);
      const QVariant * given = call(this, window, &name, &handled);
      if (handled && given) return *given;
    }
    return QPlatformNativeInterface::windowProperty(window, name);
  }

  //  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
  //      *window, const QString &name, const QVariant &defaultValue) const
  QVariant windowProperty(
      QPlatformWindow *window,
      const QString &name,
      const QVariant &defaultValue) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall7 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall7>(taken[7]);
      const QVariant * given = call(this, window, &name, &defaultValue, &handled);
      if (handled && given) return *given;
    }
    return QPlatformNativeInterface::windowProperty(window, name, defaultValue);
  }

  //  void QPlatformNativeInterface::setWindowProperty(QPlatformWindow
  //      *window, const QString &name, const QVariant &value)
  void setWindowProperty(
      QPlatformWindow *window,
      const QString &name,
      const QVariant &value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall8 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall8>(taken[8]);
      call(this, window, &name, &value, &handled);
      if (handled) return;
    }
    QPlatformNativeInterface::setWindowProperty(window, name, value);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall9 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall10 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall11 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall12 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall13 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall14 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall15 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformNativeInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QPlatformNativeInterface10metaObjectEv(
    const QPlatformNativeInterface *self) {
  return self->metaObject();
}

//  void *QPlatformNativeInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface11qt_metacastEPKc(
    QPlatformNativeInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformNativeInterface::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QPlatformNativeInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformNativeInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformNativeInterface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QPlatformNativeInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformNativeInterface::tr(s, c, n));
}

//  void *QPlatformNativeInterface::nativeResourceForIntegration(const
//      QByteArray &resource)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface28nativeResourceForIntegrationERK10QByteArray(
    QPlatformNativeInterface *self,
    const QByteArray *resource) {
  return self->nativeResourceForIntegration(*resource);
}

//  void *QPlatformNativeInterface::nativeResourceForContext(const QByteArray
//      &resource, QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface24nativeResourceForContextERK10QByteArrayP14QOpenGLContext(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QOpenGLContext *context) {
  return self->nativeResourceForContext(*resource, context);
}

//  void *QPlatformNativeInterface::nativeResourceForScreen(const QByteArray
//      &resource, QScreen *screen)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface23nativeResourceForScreenERK10QByteArrayP7QScreen(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QScreen *screen) {
  return self->nativeResourceForScreen(*resource, screen);
}

//  void *QPlatformNativeInterface::nativeResourceForWindow(const QByteArray
//      &resource, QWindow *window)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface23nativeResourceForWindowERK10QByteArrayP7QWindow(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QWindow *window) {
  return self->nativeResourceForWindow(*resource, window);
}

//  void *QPlatformNativeInterface::nativeResourceForBackingStore(const
//      QByteArray &resource, QBackingStore *backingStore)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface29nativeResourceForBackingStoreERK10QByteArrayP13QBackingStore(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QBackingStore *backingStore) {
  return self->nativeResourceForBackingStore(*resource, backingStore);
}

#if !defined(QT_NO_CURSOR)
//  void *QPlatformNativeInterface::nativeResourceForCursor(const QByteArray
//      &resource, const QCursor &cursor)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface23nativeResourceForCursorERK10QByteArrayRK7QCursor(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    const QCursor *cursor) {
  return self->nativeResourceForCursor(*resource, *cursor);
}
#endif  // !defined(QT_NO_CURSOR)

//  NativeResourceForIntegrationFunction
//      QPlatformNativeInterface::nativeResourceFunctionForIntegration(const
//      QByteArray &resource)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface36nativeResourceFunctionForIntegrationERK10QByteArray(
    QPlatformNativeInterface *self,
    const QByteArray *resource) {
  return reinterpret_cast<void *>(
      self->nativeResourceFunctionForIntegration(
          *resource));
}

//  NativeResourceForContextFunction
//      QPlatformNativeInterface::nativeResourceFunctionForContext(const
//      QByteArray &resource)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface32nativeResourceFunctionForContextERK10QByteArray(
    QPlatformNativeInterface *self,
    const QByteArray *resource) {
  return reinterpret_cast<void *>(
      self->nativeResourceFunctionForContext(
          *resource));
}

//  NativeResourceForScreenFunction
//      QPlatformNativeInterface::nativeResourceFunctionForScreen(const
//      QByteArray &resource)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface31nativeResourceFunctionForScreenERK10QByteArray(
    QPlatformNativeInterface *self,
    const QByteArray *resource) {
  return reinterpret_cast<void *>(
      self->nativeResourceFunctionForScreen(
          *resource));
}

//  NativeResourceForWindowFunction
//      QPlatformNativeInterface::nativeResourceFunctionForWindow(const
//      QByteArray &resource)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface31nativeResourceFunctionForWindowERK10QByteArray(
    QPlatformNativeInterface *self,
    const QByteArray *resource) {
  return reinterpret_cast<void *>(
      self->nativeResourceFunctionForWindow(
          *resource));
}

//  NativeResourceForBackingStoreFunction
//      QPlatformNativeInterface::nativeResourceFunctionForBackingStore(const
//      QByteArray &resource)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QPlatformNativeInterface37nativeResourceFunctionForBackingStoreERK10QByteArray(
    QPlatformNativeInterface *self,
    const QByteArray *resource) {
  return reinterpret_cast<void *>(
      self->nativeResourceFunctionForBackingStore(
          *resource));
}

//  QFunctionPointer QPlatformNativeInterface::platformFunction(const
//      QByteArray &function) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK24QPlatformNativeInterface16platformFunctionERK10QByteArray(
    const QPlatformNativeInterface *self,
    const QByteArray *function) {
  return reinterpret_cast<void *>(self->platformFunction(*function));
}

//  QVariantMap QPlatformNativeInterface::windowProperties(QPlatformWindow
//      *window) const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK24QPlatformNativeInterface16windowPropertiesEP15QPlatformWindow(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window) {
  return new QMap<QString, QVariant>(self->windowProperties(window));
}

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QString(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name) {
  return new QVariant(self->windowProperty(window, *name));
}

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name, const QVariant &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *defaultValue) {
  return new QVariant(self->windowProperty(window, *name, *defaultValue));
}

//  void QPlatformNativeInterface::setWindowProperty(QPlatformWindow *window,
//      const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *value) {
  self->setWindowProperty(window, *name, *value);
}

//  void QPlatformNativeInterface::windowPropertyChanged(QPlatformWindow
//      *window, const QString &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformNativeInterface21windowPropertyChangedEP15QPlatformWindowRK7QString(
    QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *propertyName) {
  self->windowPropertyChanged(window, *propertyName);
}

//  a Python function taken by a CuteQPlatformNativeInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformNativeInterface(
    QPlatformNativeInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformNativeInterface *>(self)->take(key, call);
}

//  void *QPlatformNativeInterface::nativeResourceForIntegration(const
//      QByteArray &resource)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN24QPlatformNativeInterface28nativeResourceForIntegrationERK10QByteArray(
    QPlatformNativeInterface *self,
    const QByteArray *resource) {
  return self->QPlatformNativeInterface::nativeResourceForIntegration(
      *resource);
}

//  void *QPlatformNativeInterface::nativeResourceForContext(const QByteArray
//      &resource, QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN24QPlatformNativeInterface24nativeResourceForContextERK10QByteArrayP14QOpenGLContext(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QOpenGLContext *context) {
  return self->QPlatformNativeInterface::nativeResourceForContext(
      *resource,
      context);
}

//  void *QPlatformNativeInterface::nativeResourceForScreen(const QByteArray
//      &resource, QScreen *screen)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN24QPlatformNativeInterface23nativeResourceForScreenERK10QByteArrayP7QScreen(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QScreen *screen) {
  return self->QPlatformNativeInterface::nativeResourceForScreen(
      *resource,
      screen);
}

//  void *QPlatformNativeInterface::nativeResourceForWindow(const QByteArray
//      &resource, QWindow *window)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN24QPlatformNativeInterface23nativeResourceForWindowERK10QByteArrayP7QWindow(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QWindow *window) {
  return self->QPlatformNativeInterface::nativeResourceForWindow(
      *resource,
      window);
}

//  void *QPlatformNativeInterface::nativeResourceForBackingStore(const
//      QByteArray &resource, QBackingStore *backingStore)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN24QPlatformNativeInterface29nativeResourceForBackingStoreERK10QByteArrayP13QBackingStore(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    QBackingStore *backingStore) {
  return self->QPlatformNativeInterface::nativeResourceForBackingStore(
      *resource,
      backingStore);
}

#if !defined(QT_NO_CURSOR)
//  void *QPlatformNativeInterface::nativeResourceForCursor(const QByteArray
//      &resource, const QCursor &cursor)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN24QPlatformNativeInterface23nativeResourceForCursorERK10QByteArrayRK7QCursor(
    QPlatformNativeInterface *self,
    const QByteArray *resource,
    const QCursor *cursor) {
  return self->QPlatformNativeInterface::nativeResourceForCursor(
      *resource,
      *cursor);
}
#endif  // !defined(QT_NO_CURSOR)

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QString(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name) {
  return new QVariant(
      self->QPlatformNativeInterface::windowProperty(
          window,
          *name));
}

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name, const QVariant &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *defaultValue) {
  return new QVariant(
      self->QPlatformNativeInterface::windowProperty(
          window,
          *name,
          *defaultValue));
}

//  void QPlatformNativeInterface::setWindowProperty(QPlatformWindow *window,
//      const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *value) {
  self->QPlatformNativeInterface::setWindowProperty(window, *name, *value);
}
