//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpchttp2channel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpcQuick/QtGrpcQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpchttp2channel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <memory>
#include <QtGrpc/QAbstractGrpcChannel>

//  A QQmlGrpcHttp2Channel that Python can take functions over in. Every QQmlGrpcHttp2Channel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcHttp2ChannelCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcHttp2ChannelCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcHttp2ChannelCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcHttp2ChannelCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcHttp2ChannelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcHttp2ChannelCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcHttp2ChannelCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlGrpcHttp2Channel : public QQmlGrpcHttp2Channel {
public:
  using QQmlGrpcHttp2Channel::QQmlGrpcHttp2Channel;
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
      CuteQQmlGrpcHttp2ChannelCall0 call = reinterpret_cast<CuteQQmlGrpcHttp2ChannelCall0>(taken[0]);
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
      CuteQQmlGrpcHttp2ChannelCall1 call = reinterpret_cast<CuteQQmlGrpcHttp2ChannelCall1>(taken[1]);
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
      CuteQQmlGrpcHttp2ChannelCall2 call = reinterpret_cast<CuteQQmlGrpcHttp2ChannelCall2>(taken[2]);
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
      CuteQQmlGrpcHttp2ChannelCall3 call = reinterpret_cast<CuteQQmlGrpcHttp2ChannelCall3>(taken[3]);
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
      CuteQQmlGrpcHttp2ChannelCall4 call = reinterpret_cast<CuteQQmlGrpcHttp2ChannelCall4>(taken[4]);
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
      CuteQQmlGrpcHttp2ChannelCall5 call = reinterpret_cast<CuteQQmlGrpcHttp2ChannelCall5>(taken[5]);
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
      CuteQQmlGrpcHttp2ChannelCall6 call = reinterpret_cast<CuteQQmlGrpcHttp2ChannelCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlGrpcHttp2Channel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlGrpcHttp2Channel10metaObjectEv(
    const QQmlGrpcHttp2Channel *self) {
  return self->metaObject();
}

//  void *QQmlGrpcHttp2Channel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQmlGrpcHttp2Channel11qt_metacastEPKc(
    QQmlGrpcHttp2Channel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlGrpcHttp2Channel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQmlGrpcHttp2Channel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlGrpcHttp2Channel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlGrpcHttp2Channel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlGrpcHttp2Channel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlGrpcHttp2Channel::tr(s, c, n));
}

//  QQmlGrpcHttp2Channel::QQmlGrpcHttp2Channel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlGrpcHttp2Channel *ritual_ZN20QQmlGrpcHttp2ChannelC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlGrpcHttp2Channel(parent);
}

//  QQmlGrpcHttp2Channel::~QQmlGrpcHttp2Channel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGrpcHttp2ChannelD1Ev(QQmlGrpcHttp2Channel *self) {
  delete self;
}

//  std::shared_ptr<QAbstractGrpcChannel> QQmlGrpcHttp2Channel::channel()
//      const
extern "C" Q_DECL_EXPORT
std::shared_ptr<QAbstractGrpcChannel> *ritual_ZNK20QQmlGrpcHttp2Channel7channelEv(
    const QQmlGrpcHttp2Channel *self) {
  return new std::shared_ptr<QAbstractGrpcChannel>(self->channel());
}

//  QQmlGrpcChannelOptions *QQmlGrpcHttp2Channel::options() const
extern "C" Q_DECL_EXPORT
QQmlGrpcChannelOptions *ritual_ZNK20QQmlGrpcHttp2Channel7optionsEv(
    const QQmlGrpcHttp2Channel *self) {
  return self->options();
}

//  void QQmlGrpcHttp2Channel::setOptions(QQmlGrpcChannelOptions *options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGrpcHttp2Channel10setOptionsEP22QQmlGrpcChannelOptions(
    QQmlGrpcHttp2Channel *self,
    QQmlGrpcChannelOptions *options) {
  self->setOptions(options);
}

//  QUrl QQmlGrpcHttp2Channel::hostUri() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQmlGrpcHttp2Channel7hostUriEv(
    const QQmlGrpcHttp2Channel *self) {
  return new QUrl(self->hostUri());
}

//  void QQmlGrpcHttp2Channel::setHostUri(const QUrl &hostUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGrpcHttp2Channel10setHostUriERK4QUrl(
    QQmlGrpcHttp2Channel *self,
    const QUrl *hostUri) {
  self->setHostUri(*hostUri);
}

//  void QQmlGrpcHttp2Channel::optionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGrpcHttp2Channel14optionsChangedEv(
    QQmlGrpcHttp2Channel *self) {
  self->optionsChanged();
}

//  void QQmlGrpcHttp2Channel::channelUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGrpcHttp2Channel14channelUpdatedEv(
    QQmlGrpcHttp2Channel *self) {
  self->channelUpdated();
}

//  void QQmlGrpcHttp2Channel::hostUriChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGrpcHttp2Channel14hostUriChangedEv(
    QQmlGrpcHttp2Channel *self) {
  self->hostUriChanged();
}

//  void QQmlGrpcHttp2Channel::updateChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGrpcHttp2Channel13updateChannelEv(
    QQmlGrpcHttp2Channel *self) {
  self->updateChannel();
}

//  QQmlGrpcHttp2ChannelPrivate *QQmlGrpcHttp2Channel::d_func()
extern "C" Q_DECL_EXPORT
QQmlGrpcHttp2ChannelPrivate *ritual_ZN20QQmlGrpcHttp2Channel6d_funcEv(
    QQmlGrpcHttp2Channel *self) {
  return self->d_func();
}

//  const QQmlGrpcHttp2ChannelPrivate *QQmlGrpcHttp2Channel::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlGrpcHttp2ChannelPrivate *ritual_ZNK20QQmlGrpcHttp2Channel6d_funcEv(
    const QQmlGrpcHttp2Channel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlGrpcHttp2Channel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlGrpcHttp2Channel(
    QQmlGrpcHttp2Channel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlGrpcHttp2Channel *>(self)->take(key, call);
}

//  a std::shared_ptr<QAbstractGrpcChannel> a ritual of QQmlGrpcHttp2Channel
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlGrpcHttp2Channel__std_shared_ptr_QAbstractGrpcChannel(
    std::shared_ptr<QAbstractGrpcChannel> *self) {
  delete self;
}
