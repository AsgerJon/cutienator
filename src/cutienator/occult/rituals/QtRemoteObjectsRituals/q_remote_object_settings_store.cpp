//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectsettingsstore.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtRemoteObjects/qremoteobjectsettingsstore.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QRemoteObjectSettingsStore that Python can take functions over in. Every QRemoteObjectSettingsStore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSettingsStoreCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSettingsStoreCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSettingsStoreCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSettingsStoreCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSettingsStoreCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSettingsStoreCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSettingsStoreCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectSettingsStore : public QRemoteObjectSettingsStore {
public:
  using QRemoteObjectSettingsStore::QRemoteObjectSettingsStore;
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
      CuteQRemoteObjectSettingsStoreCall0 call = reinterpret_cast<CuteQRemoteObjectSettingsStoreCall0>(taken[0]);
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
      CuteQRemoteObjectSettingsStoreCall1 call = reinterpret_cast<CuteQRemoteObjectSettingsStoreCall1>(taken[1]);
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
      CuteQRemoteObjectSettingsStoreCall2 call = reinterpret_cast<CuteQRemoteObjectSettingsStoreCall2>(taken[2]);
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
      CuteQRemoteObjectSettingsStoreCall3 call = reinterpret_cast<CuteQRemoteObjectSettingsStoreCall3>(taken[3]);
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
      CuteQRemoteObjectSettingsStoreCall4 call = reinterpret_cast<CuteQRemoteObjectSettingsStoreCall4>(taken[4]);
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
      CuteQRemoteObjectSettingsStoreCall5 call = reinterpret_cast<CuteQRemoteObjectSettingsStoreCall5>(taken[5]);
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
      CuteQRemoteObjectSettingsStoreCall6 call = reinterpret_cast<CuteQRemoteObjectSettingsStoreCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectSettingsStore::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QRemoteObjectSettingsStore10metaObjectEv(
    const QRemoteObjectSettingsStore *self) {
  return self->metaObject();
}

//  void *QRemoteObjectSettingsStore::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QRemoteObjectSettingsStore11qt_metacastEPKc(
    QRemoteObjectSettingsStore *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QRemoteObjectSettingsStore::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QRemoteObjectSettingsStore11qt_metacallEN11QMetaObject4CallEiPPv(
    QRemoteObjectSettingsStore *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QRemoteObjectSettingsStore::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QRemoteObjectSettingsStore2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectSettingsStore::tr(s, c, n));
}

//  QRemoteObjectSettingsStore::QRemoteObjectSettingsStore(QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectSettingsStore *ritual_ZN26QRemoteObjectSettingsStoreC1EP7QObject(
    QObject *parent) {
  return new CuteQRemoteObjectSettingsStore(parent);
}

//  QRemoteObjectSettingsStore::~QRemoteObjectSettingsStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRemoteObjectSettingsStoreD1Ev(
    QRemoteObjectSettingsStore *self) {
  delete self;
}

//  void QRemoteObjectSettingsStore::saveProperties(const QString &repName,
//      const QByteArray &repSig, const QVariantList &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRemoteObjectSettingsStore14savePropertiesERK7QStringRK10QByteArrayRK5QListI8QVariantE(
    QRemoteObjectSettingsStore *self,
    const QString *repName,
    const QByteArray *repSig,
    const QList<QVariant> *values) {
  self->saveProperties(*repName, *repSig, *values);
}

//  QVariantList QRemoteObjectSettingsStore::restoreProperties(const QString
//      &repName, const QByteArray &repSig)
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN26QRemoteObjectSettingsStore17restorePropertiesERK7QStringRK10QByteArray(
    QRemoteObjectSettingsStore *self,
    const QString *repName,
    const QByteArray *repSig) {
  return new QList<QVariant>(self->restoreProperties(*repName, *repSig));
}

//  QRemoteObjectSettingsStorePrivate *QRemoteObjectSettingsStore::d_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectSettingsStorePrivate *ritual_ZN26QRemoteObjectSettingsStore6d_funcEv(
    QRemoteObjectSettingsStore *self) {
  return self->d_func();
}

//  const QRemoteObjectSettingsStorePrivate
//      *QRemoteObjectSettingsStore::d_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectSettingsStorePrivate *ritual_ZNK26QRemoteObjectSettingsStore6d_funcEv(
    const QRemoteObjectSettingsStore *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRemoteObjectSettingsStore, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectSettingsStore(
    QRemoteObjectSettingsStore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectSettingsStore *>(self)->take(key, call);
}
