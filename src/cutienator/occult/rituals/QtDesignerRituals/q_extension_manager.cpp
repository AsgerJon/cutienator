//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/qextensionmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/qextensionmanager.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QExtensionManager that Python can take functions over in. Every QExtensionManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQExtensionManagerCall0)(const void *, QAbstractExtensionFactory *, const QString *, int *);
typedef void (*CuteQExtensionManagerCall1)(const void *, QAbstractExtensionFactory *, const QString *, int *);
typedef void * (*CuteQExtensionManagerCall2)(const void *, QObject *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQExtensionManagerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQExtensionManagerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQExtensionManagerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQExtensionManagerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQExtensionManagerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQExtensionManagerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQExtensionManagerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQExtensionManager : public QExtensionManager {
public:
  using QExtensionManager::QExtensionManager;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractExtensionManager18registerExtensionsEP25QAbstractExtensionFactoryRK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QAbstractExtensionManager20unregisterExtensionsEP25QAbstractExtensionFactoryRK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAbstractExtensionManager9extensionEP7QObjectRK7QString")) {
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

  //  void QExtensionManager::registerExtensions(QAbstractExtensionFactory
  //      *factory, const QString &iid)
  void registerExtensions(
      QAbstractExtensionFactory *factory,
      const QString &iid) override {
    if (taken[0]) {
      int handled = 0;
      CuteQExtensionManagerCall0 call = reinterpret_cast<CuteQExtensionManagerCall0>(taken[0]);
      call(this, factory, &iid, &handled);
      if (handled) return;
    }
    QExtensionManager::registerExtensions(factory, iid);
  }

  //  void
  //      QExtensionManager::unregisterExtensions(QAbstractExtensionFactory
  //      *factory, const QString &iid)
  void unregisterExtensions(
      QAbstractExtensionFactory *factory,
      const QString &iid) override {
    if (taken[1]) {
      int handled = 0;
      CuteQExtensionManagerCall1 call = reinterpret_cast<CuteQExtensionManagerCall1>(taken[1]);
      call(this, factory, &iid, &handled);
      if (handled) return;
    }
    QExtensionManager::unregisterExtensions(factory, iid);
  }

  //  QObject *QExtensionManager::extension(QObject *object, const QString
  //      &iid) const
  QObject *extension(QObject *object, const QString &iid) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQExtensionManagerCall2 call = reinterpret_cast<CuteQExtensionManagerCall2>(taken[2]);
      void * given = call(this, object, &iid, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QExtensionManager::extension(object, iid);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQExtensionManagerCall3 call = reinterpret_cast<CuteQExtensionManagerCall3>(taken[3]);
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
      CuteQExtensionManagerCall4 call = reinterpret_cast<CuteQExtensionManagerCall4>(taken[4]);
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
      CuteQExtensionManagerCall5 call = reinterpret_cast<CuteQExtensionManagerCall5>(taken[5]);
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
      CuteQExtensionManagerCall6 call = reinterpret_cast<CuteQExtensionManagerCall6>(taken[6]);
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
      CuteQExtensionManagerCall7 call = reinterpret_cast<CuteQExtensionManagerCall7>(taken[7]);
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
      CuteQExtensionManagerCall8 call = reinterpret_cast<CuteQExtensionManagerCall8>(taken[8]);
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
      CuteQExtensionManagerCall9 call = reinterpret_cast<CuteQExtensionManagerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QExtensionManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QExtensionManager10metaObjectEv(
    const QExtensionManager *self) {
  return self->metaObject();
}

//  void *QExtensionManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QExtensionManager11qt_metacastEPKc(
    QExtensionManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QExtensionManager::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QExtensionManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QExtensionManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QExtensionManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QExtensionManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QExtensionManager::tr(s, c, n));
}

//  QExtensionManager::QExtensionManager(QObject *parent)
extern "C" Q_DECL_EXPORT
QExtensionManager *ritual_ZN17QExtensionManagerC1EP7QObject(
    QObject *parent) {
  return new CuteQExtensionManager(parent);
}

//  QExtensionManager::~QExtensionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QExtensionManagerD1Ev(QExtensionManager *self) {
  delete self;
}

//  void QExtensionManager::registerExtensions(QAbstractExtensionFactory
//      *factory, const QString &iid)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QExtensionManager18registerExtensionsEP25QAbstractExtensionFactoryRK7QString(
    QExtensionManager *self,
    QAbstractExtensionFactory *factory,
    const QString *iid) {
  self->registerExtensions(factory, *iid);
}

//  void QExtensionManager::unregisterExtensions(QAbstractExtensionFactory
//      *factory, const QString &iid)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QExtensionManager20unregisterExtensionsEP25QAbstractExtensionFactoryRK7QString(
    QExtensionManager *self,
    QAbstractExtensionFactory *factory,
    const QString *iid) {
  self->unregisterExtensions(factory, *iid);
}

//  QObject *QExtensionManager::extension(QObject *object, const QString
//      &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QExtensionManager9extensionEP7QObjectRK7QString(
    const QExtensionManager *self,
    QObject *object,
    const QString *iid) {
  return self->extension(object, *iid);
}

//  QExtensionManager as the QAbstractExtensionManager it is built on
extern "C" Q_DECL_EXPORT
QAbstractExtensionManager *ritual_cast_QExtensionManager_QAbstractExtensionManager(
    QExtensionManager *self) {
  return static_cast<QAbstractExtensionManager *>(self);
}

//  a Python function taken by a CuteQExtensionManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QExtensionManager(
    QExtensionManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQExtensionManager *>(self)->take(key, call);
}

//  void QExtensionManager::registerExtensions(QAbstractExtensionFactory
//      *factory, const QString &iid)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QExtensionManager18registerExtensionsEP25QAbstractExtensionFactoryRK7QString(
    QExtensionManager *self,
    QAbstractExtensionFactory *factory,
    const QString *iid) {
  self->QExtensionManager::registerExtensions(factory, *iid);
}

//  void QExtensionManager::unregisterExtensions(QAbstractExtensionFactory
//      *factory, const QString &iid)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QExtensionManager20unregisterExtensionsEP25QAbstractExtensionFactoryRK7QString(
    QExtensionManager *self,
    QAbstractExtensionFactory *factory,
    const QString *iid) {
  self->QExtensionManager::unregisterExtensions(factory, *iid);
}

//  QObject *QExtensionManager::extension(QObject *object, const QString
//      &iid) const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK17QExtensionManager9extensionEP7QObjectRK7QString(
    const QExtensionManager *self,
    QObject *object,
    const QString *iid) {
  return self->QExtensionManager::extension(object, *iid);
}
