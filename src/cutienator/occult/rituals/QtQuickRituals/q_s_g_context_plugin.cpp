//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcontextplugin_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcontextplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGContextPlugin that Python can take functions over in. Every QSGContextPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGContextPluginCall0)(const void *, const QImage *, int *);
typedef void * (*CuteQSGContextPluginCall1)(const void *, int *);
typedef void * (*CuteQSGContextPluginCall2)(const void *, const QString *, int *);
typedef int (*CuteQSGContextPluginCall3)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGContextPluginCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGContextPluginCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextPluginCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextPluginCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextPluginCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextPluginCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextPluginCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGContextPlugin : public QSGContextPlugin {
public:
  using QSGContextPlugin::QSGContextPlugin;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QSGContextFactoryInterface29createTextureFactoryFromImageERK6QImage")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QSGContextFactoryInterface19createWindowManagerEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QSGContextFactoryInterface6createERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QSGContextFactoryInterface5flagsERK7QString")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QQuickTextureFactory
  //      *QSGContextPlugin::createTextureFactoryFromImage(const QImage
  //      &a0)
  QQuickTextureFactory *createTextureFactoryFromImage(
      const QImage &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGContextPluginCall0 call = reinterpret_cast<CuteQSGContextPluginCall0>(taken[0]);
      void * given = call(this, &a0, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return QSGContextPlugin::createTextureFactoryFromImage(a0);
  }

  //  QSGRenderLoop *QSGContextPlugin::createWindowManager()
  QSGRenderLoop *createWindowManager() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGContextPluginCall1 call = reinterpret_cast<CuteQSGContextPluginCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRenderLoop *>(given);
    }
    return QSGContextPlugin::createWindowManager();
  }

  //  QSGContext *QSGContextFactoryInterface::create(const QString &key)
  //      const
  QSGContext *create(const QString &key) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGContextPluginCall2 call = reinterpret_cast<CuteQSGContextPluginCall2>(taken[2]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QSGContext *>(given);
    }
    return {};
  }

  //  Flags QSGContextFactoryInterface::flags(const QString &key) const
  QSGContextFactoryInterface::Flags flags(
      const QString &key) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGContextPluginCall3 call = reinterpret_cast<CuteQSGContextPluginCall3>(taken[3]);
      int given = call(this, &key, &handled);
      if (handled) return QFlags<QSGContextFactoryInterface::Flag>::fromInt(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGContextPluginCall4 call = reinterpret_cast<CuteQSGContextPluginCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGContextPluginCall5 call = reinterpret_cast<CuteQSGContextPluginCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGContextPluginCall6 call = reinterpret_cast<CuteQSGContextPluginCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGContextPluginCall7 call = reinterpret_cast<CuteQSGContextPluginCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGContextPluginCall8 call = reinterpret_cast<CuteQSGContextPluginCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGContextPluginCall9 call = reinterpret_cast<CuteQSGContextPluginCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGContextPluginCall10 call = reinterpret_cast<CuteQSGContextPluginCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGContextPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSGContextPlugin10metaObjectEv(
    const QSGContextPlugin *self) {
  return self->metaObject();
}

//  QString QSGContextPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSGContextPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGContextPlugin::tr(s, c, n));
}

//  QSGContextPlugin::~QSGContextPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGContextPluginD1Ev(QSGContextPlugin *self) {
  delete self;
}

//  QQuickTextureFactory
//      *QSGContextPlugin::createTextureFactoryFromImage(const QImage &a0)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN16QSGContextPlugin29createTextureFactoryFromImageERK6QImage(
    QSGContextPlugin *self,
    const QImage *a0) {
  return self->createTextureFactoryFromImage(*a0);
}

//  QSGRenderLoop *QSGContextPlugin::createWindowManager()
extern "C" Q_DECL_EXPORT
QSGRenderLoop *ritual_ZN16QSGContextPlugin19createWindowManagerEv(
    QSGContextPlugin *self) {
  return self->createWindowManager();
}

//  QSGContextPlugin as the QSGContextFactoryInterface it is built on
extern "C" Q_DECL_EXPORT
QSGContextFactoryInterface *ritual_cast_QSGContextPlugin_QSGContextFactoryInterface(
    QSGContextPlugin *self) {
  return static_cast<QSGContextFactoryInterface *>(self);
}

//  a Python function taken by a CuteQSGContextPlugin, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGContextPlugin(
    QSGContextPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGContextPlugin *>(self)->take(key, call);
}

//  QQuickTextureFactory
//      *QSGContextPlugin::createTextureFactoryFromImage(const QImage &a0)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_own_ZN16QSGContextPlugin29createTextureFactoryFromImageERK6QImage(
    QSGContextPlugin *self,
    const QImage *a0) {
  return self->QSGContextPlugin::createTextureFactoryFromImage(*a0);
}

//  QSGRenderLoop *QSGContextPlugin::createWindowManager()
extern "C" Q_DECL_EXPORT
QSGRenderLoop *ritual_own_ZN16QSGContextPlugin19createWindowManagerEv(
    QSGContextPlugin *self) {
  return self->QSGContextPlugin::createWindowManager();
}
