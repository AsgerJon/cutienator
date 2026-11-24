//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_IMAGEFORMATPLUGIN)
#include <QtGui/qimageiohandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QImageIOPlugin that Python can take functions over in. Every QImageIOPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_IMAGEFORMATPLUGIN)
typedef int (*CuteQImageIOPluginCall0)(const void *, QIODevice *, const QByteArray *, int *);
#endif  // !defined(QT_NO_IMAGEFORMATPLUGIN)
#if !defined(QT_NO_IMAGEFORMATPLUGIN)
typedef void * (*CuteQImageIOPluginCall1)(const void *, QIODevice *, const QByteArray *, int *);
#endif  // !defined(QT_NO_IMAGEFORMATPLUGIN)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQImageIOPluginCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQImageIOPluginCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageIOPluginCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageIOPluginCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageIOPluginCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageIOPluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQImageIOPluginCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQImageIOPlugin : public QImageIOPlugin {
public:
  using QImageIOPlugin::QImageIOPlugin;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_IMAGEFORMATPLUGIN)
    if (!std::strcmp(key, "_ZNK14QImageIOPlugin12capabilitiesEP9QIODeviceRK10QByteArray")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMATPLUGIN)
#if !defined(QT_NO_IMAGEFORMATPLUGIN)
    if (!std::strcmp(key, "_ZNK14QImageIOPlugin6createEP9QIODeviceRK10QByteArray")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_IMAGEFORMATPLUGIN)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_IMAGEFORMATPLUGIN)
  //  Capabilities QImageIOPlugin::capabilities(QIODevice *device, const
  //      QByteArray &format) const
  QImageIOPlugin::Capabilities capabilities(
      QIODevice *device,
      const QByteArray &format) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQImageIOPluginCall0 call = reinterpret_cast<CuteQImageIOPluginCall0>(taken[0]);
      int given = call(this, device, &format, &handled);
      if (handled) return QFlags<QImageIOPlugin::Capability>::fromInt(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_IMAGEFORMATPLUGIN)

#if !defined(QT_NO_IMAGEFORMATPLUGIN)
  //  QImageIOHandler *QImageIOPlugin::create(QIODevice *device, const
  //      QByteArray &format) const
  QImageIOHandler *create(
      QIODevice *device,
      const QByteArray &format) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQImageIOPluginCall1 call = reinterpret_cast<CuteQImageIOPluginCall1>(taken[1]);
      void * given = call(this, device, &format, &handled);
      if (handled) return static_cast<QImageIOHandler *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_IMAGEFORMATPLUGIN)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQImageIOPluginCall2 call = reinterpret_cast<CuteQImageIOPluginCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQImageIOPluginCall3 call = reinterpret_cast<CuteQImageIOPluginCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQImageIOPluginCall4 call = reinterpret_cast<CuteQImageIOPluginCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQImageIOPluginCall5 call = reinterpret_cast<CuteQImageIOPluginCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQImageIOPluginCall6 call = reinterpret_cast<CuteQImageIOPluginCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQImageIOPluginCall7 call = reinterpret_cast<CuteQImageIOPluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQImageIOPluginCall8 call = reinterpret_cast<CuteQImageIOPluginCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QImageIOPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QImageIOPlugin10metaObjectEv(
    const QImageIOPlugin *self) {
  return self->metaObject();
}

//  QString QImageIOPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QImageIOPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QImageIOPlugin::tr(s, c, n));
}

//  QImageIOPlugin::~QImageIOPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QImageIOPluginD1Ev(QImageIOPlugin *self) {
  delete self;
}

//  Capabilities QImageIOPlugin::capabilities(QIODevice *device, const
//      QByteArray &format) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QImageIOPlugin12capabilitiesEP9QIODeviceRK10QByteArray(
    const QImageIOPlugin *self,
    QIODevice *device,
    const QByteArray *format) {
  return static_cast<int>(self->capabilities(device, *format).toInt());
}

//  QImageIOHandler *QImageIOPlugin::create(QIODevice *device, const
//      QByteArray &format) const
extern "C" Q_DECL_EXPORT
QImageIOHandler *ritual_ZNK14QImageIOPlugin6createEP9QIODeviceRK10QByteArray(
    const QImageIOPlugin *self,
    QIODevice *device,
    const QByteArray *format) {
  return self->create(device, *format);
}

//  a Python function taken by a CuteQImageIOPlugin, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QImageIOPlugin(
    QImageIOPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQImageIOPlugin *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_IMAGEFORMATPLUGIN)
