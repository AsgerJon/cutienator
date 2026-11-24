//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebChannelQuick/qqmlwebchannel.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebChannelQuick/QtWebChannelQuick>
#include <QtWebChannelQuick/qqmlwebchannel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlWebChannel that Python can take functions over in. Every QQmlWebChannel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlWebChannelCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlWebChannelCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlWebChannel : public QQmlWebChannel {
public:
  using QQmlWebChannel::QQmlWebChannel;
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
      CuteQQmlWebChannelCall0 call = reinterpret_cast<CuteQQmlWebChannelCall0>(taken[0]);
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
      CuteQQmlWebChannelCall1 call = reinterpret_cast<CuteQQmlWebChannelCall1>(taken[1]);
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
      CuteQQmlWebChannelCall2 call = reinterpret_cast<CuteQQmlWebChannelCall2>(taken[2]);
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
      CuteQQmlWebChannelCall3 call = reinterpret_cast<CuteQQmlWebChannelCall3>(taken[3]);
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
      CuteQQmlWebChannelCall4 call = reinterpret_cast<CuteQQmlWebChannelCall4>(taken[4]);
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
      CuteQQmlWebChannelCall5 call = reinterpret_cast<CuteQQmlWebChannelCall5>(taken[5]);
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
      CuteQQmlWebChannelCall6 call = reinterpret_cast<CuteQQmlWebChannelCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlWebChannel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlWebChannel10metaObjectEv(
    const QQmlWebChannel *self) {
  return self->metaObject();
}

//  QString QQmlWebChannel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlWebChannel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlWebChannel::tr(s, c, n));
}

//  void QQmlWebChannel::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel21qt_qmlMarker_attachedEv(
    QQmlWebChannel *self) {
  self->qt_qmlMarker_attached();
}

//  QQmlWebChannel::QQmlWebChannel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlWebChannel *ritual_ZN14QQmlWebChannelC1EP7QObject(QObject *parent) {
  return new CuteQQmlWebChannel(parent);
}

//  QQmlWebChannel::~QQmlWebChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannelD1Ev(QQmlWebChannel *self) {
  delete self;
}

//  void QQmlWebChannel::registerObjects(const QVariantMap &objects)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel15registerObjectsERK4QMapI7QString8QVariantE(
    QQmlWebChannel *self,
    const QMap<QString, QVariant> *objects) {
  self->registerObjects(*objects);
}

//  QQmlWebChannelAttached *QQmlWebChannel::qmlAttachedProperties(QObject
//      *obj)
extern "C" Q_DECL_EXPORT
QQmlWebChannelAttached *ritual_ZN14QQmlWebChannel21qmlAttachedPropertiesEP7QObject(
    QObject *obj) {
  return QQmlWebChannel::qmlAttachedProperties(obj);
}

//  void QQmlWebChannel::connectTo(QObject *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel9connectToEP7QObject(
    QQmlWebChannel *self,
    QObject *transport) {
  self->connectTo(transport);
}

//  void QQmlWebChannel::disconnectFrom(QObject *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel14disconnectFromEP7QObject(
    QQmlWebChannel *self,
    QObject *transport) {
  self->disconnectFrom(transport);
}

//  a Python function taken by a CuteQQmlWebChannel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlWebChannel(
    QQmlWebChannel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlWebChannel *>(self)->take(key, call);
}
