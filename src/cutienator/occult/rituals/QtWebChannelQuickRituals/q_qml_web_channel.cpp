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
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

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

//  void *QQmlWebChannel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQmlWebChannel11qt_metacastEPKc(
    QQmlWebChannel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlWebChannel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQmlWebChannel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlWebChannel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QQmlListProperty<QObject> QQmlWebChannel::registeredObjects()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN14QQmlWebChannel17registeredObjectsEv(
    QQmlWebChannel *self) {
  return new QQmlListProperty<QObject>(self->registeredObjects());
}

//  QQmlListProperty<QObject> QQmlWebChannel::transports()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN14QQmlWebChannel10transportsEv(
    QQmlWebChannel *self) {
  return new QQmlListProperty<QObject>(self->transports());
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

//  QQmlWebChannelPrivate *QQmlWebChannel::d_func()
extern "C" Q_DECL_EXPORT
QQmlWebChannelPrivate *ritual_ZN14QQmlWebChannel6d_funcEv(
    QQmlWebChannel *self) {
  return self->d_func();
}

//  const QQmlWebChannelPrivate *QQmlWebChannel::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlWebChannelPrivate *ritual_ZNK14QQmlWebChannel6d_funcEv(
    const QQmlWebChannel *self) {
  return self->d_func();
}

//  void QQmlWebChannel::registeredObjects_append(QQmlListProperty<QObject>
//      *prop, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel24registeredObjects_appendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *prop,
    QObject *item) {
  QQmlWebChannel::registeredObjects_append(prop, item);
}

//  qsizetype
//      QQmlWebChannel::registeredObjects_count(QQmlListProperty<QObject>
//      *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14QQmlWebChannel23registeredObjects_countEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  return QQmlWebChannel::registeredObjects_count(prop);
}

//  QObject *QQmlWebChannel::registeredObjects_at(QQmlListProperty<QObject>
//      *prop, qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QQmlWebChannel20registeredObjects_atEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *prop,
    qsizetype index) {
  return QQmlWebChannel::registeredObjects_at(prop, index);
}

//  void QQmlWebChannel::registeredObjects_clear(QQmlListProperty<QObject>
//      *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel23registeredObjects_clearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  QQmlWebChannel::registeredObjects_clear(prop);
}

//  void QQmlWebChannel::transports_append(QQmlListProperty<QObject> *prop,
//      QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel17transports_appendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *prop,
    QObject *item) {
  QQmlWebChannel::transports_append(prop, item);
}

//  qsizetype QQmlWebChannel::transports_count(QQmlListProperty<QObject>
//      *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14QQmlWebChannel16transports_countEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  return QQmlWebChannel::transports_count(prop);
}

//  QObject *QQmlWebChannel::transports_at(QQmlListProperty<QObject> *prop,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QQmlWebChannel13transports_atEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *prop,
    qsizetype index) {
  return QQmlWebChannel::transports_at(prop, index);
}

//  void QQmlWebChannel::transports_clear(QQmlListProperty<QObject> *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlWebChannel16transports_clearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  QQmlWebChannel::transports_clear(prop);
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

//  a QQmlListProperty<QObject> a ritual of QQmlWebChannel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlWebChannel__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
