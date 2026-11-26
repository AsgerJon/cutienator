//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebChannel/qwebchannel.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebChannel/qwebchannel.h>
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QBindable>

//  A QWebChannel that Python can take functions over in. Every QWebChannel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebChannelCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebChannelCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebChannelCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebChannel : public QWebChannel {
public:
  using QWebChannel::QWebChannel;
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
      CuteQWebChannelCall0 call = reinterpret_cast<CuteQWebChannelCall0>(taken[0]);
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
      CuteQWebChannelCall1 call = reinterpret_cast<CuteQWebChannelCall1>(taken[1]);
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
      CuteQWebChannelCall2 call = reinterpret_cast<CuteQWebChannelCall2>(taken[2]);
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
      CuteQWebChannelCall3 call = reinterpret_cast<CuteQWebChannelCall3>(taken[3]);
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
      CuteQWebChannelCall4 call = reinterpret_cast<CuteQWebChannelCall4>(taken[4]);
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
      CuteQWebChannelCall5 call = reinterpret_cast<CuteQWebChannelCall5>(taken[5]);
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
      CuteQWebChannelCall6 call = reinterpret_cast<CuteQWebChannelCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebChannel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QWebChannel10metaObjectEv(
    const QWebChannel *self) {
  return self->metaObject();
}

//  void *QWebChannel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QWebChannel11qt_metacastEPKc(
    QWebChannel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebChannel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QWebChannel11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebChannel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebChannel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QWebChannel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebChannel::tr(s, c, n));
}

//  QWebChannel::QWebChannel(QObject *parent)
extern "C" Q_DECL_EXPORT
QWebChannel *ritual_ZN11QWebChannelC1EP7QObject(QObject *parent) {
  return new CuteQWebChannel(parent);
}

//  QWebChannel::~QWebChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannelD1Ev(QWebChannel *self) {
  delete self;
}

//  void QWebChannel::registerObjects(const QHash<QString, QObject *>
//      &objects)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel15registerObjectsERK5QHashI7QStringP7QObjectE(
    QWebChannel *self,
    const QHash<QString, QObject *> *objects) {
  self->registerObjects(*objects);
}

//  QHash<QString, QObject *> QWebChannel::registeredObjects() const
extern "C" Q_DECL_EXPORT
QHash<QString, QObject *> *ritual_ZNK11QWebChannel17registeredObjectsEv(
    const QWebChannel *self) {
  return new QHash<QString, QObject *>(self->registeredObjects());
}

//  void QWebChannel::registerObject(const QString &id, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel14registerObjectERK7QStringP7QObject(
    QWebChannel *self,
    const QString *id,
    QObject *object) {
  self->registerObject(*id, object);
}

//  void QWebChannel::deregisterObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel16deregisterObjectEP7QObject(
    QWebChannel *self,
    QObject *object) {
  self->deregisterObject(object);
}

//  bool QWebChannel::blockUpdates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWebChannel12blockUpdatesEv(const QWebChannel *self) {
  return self->blockUpdates();
}

//  void QWebChannel::setBlockUpdates(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel15setBlockUpdatesEb(
    QWebChannel *self,
    bool block) {
  self->setBlockUpdates(block);
}

//  QBindable<bool> QWebChannel::bindableBlockUpdates()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN11QWebChannel20bindableBlockUpdatesEv(
    QWebChannel *self) {
  return new QBindable<bool>(self->bindableBlockUpdates());
}

//  int QWebChannel::propertyUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWebChannel22propertyUpdateIntervalEv(
    const QWebChannel *self) {
  return self->propertyUpdateInterval();
}

//  void QWebChannel::setPropertyUpdateInterval(int ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel25setPropertyUpdateIntervalEi(
    QWebChannel *self,
    int ms) {
  self->setPropertyUpdateInterval(ms);
}

//  QBindable<int> QWebChannel::bindablePropertyUpdateInterval()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN11QWebChannel30bindablePropertyUpdateIntervalEv(
    QWebChannel *self) {
  return new QBindable<int>(self->bindablePropertyUpdateInterval());
}

//  void QWebChannel::blockUpdatesChanged(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel19blockUpdatesChangedEb(
    QWebChannel *self,
    bool block) {
  self->blockUpdatesChanged(block);
}

//  void QWebChannel::connectTo(QWebChannelAbstractTransport *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel9connectToEP28QWebChannelAbstractTransport(
    QWebChannel *self,
    QWebChannelAbstractTransport *transport) {
  self->connectTo(transport);
}

//  void QWebChannel::disconnectFrom(QWebChannelAbstractTransport *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWebChannel14disconnectFromEP28QWebChannelAbstractTransport(
    QWebChannel *self,
    QWebChannelAbstractTransport *transport) {
  self->disconnectFrom(transport);
}

//  QWebChannelPrivate *QWebChannel::d_func()
extern "C" Q_DECL_EXPORT
QWebChannelPrivate *ritual_ZN11QWebChannel6d_funcEv(QWebChannel *self) {
  return self->d_func();
}

//  const QWebChannelPrivate *QWebChannel::d_func() const
extern "C" Q_DECL_EXPORT
const QWebChannelPrivate *ritual_ZNK11QWebChannel6d_funcEv(
    const QWebChannel *self) {
  return self->d_func();
}

//  QWebChannel::QWebChannel(QWebChannelPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QWebChannel *ritual_ZN11QWebChannelC1ER18QWebChannelPrivateP7QObject(
    QWebChannelPrivate *dd,
    QObject *parent) {
  return new CuteQWebChannel(*dd, parent);
}

//  a Python function taken by a CuteQWebChannel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebChannel(
    QWebChannel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebChannel *>(self)->take(key, call);
}

//  a QBindable<bool> a ritual of QWebChannel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebChannel__QBindable_bool(QBindable<bool> *self) {
  delete self;
}

//  a QBindable<int> a ritual of QWebChannel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebChannel__QBindable_int(QBindable<int> *self) {
  delete self;
}
