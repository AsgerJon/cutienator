//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsocketnotifier.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSocketNotifier may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSocketNotifier : QSocketNotifier {
  using QSocketNotifier::event;
};

//  A QSocketNotifier that Python can take functions over in. Every QSocketNotifier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSocketNotifierCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQSocketNotifierCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQSocketNotifierCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQSocketNotifierCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQSocketNotifierCall4)(const void *, QEvent *, int *);
typedef void (*CuteQSocketNotifierCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQSocketNotifierCall6)(const void *, const QMetaMethod *, int *);
class CuteQSocketNotifier : public QSocketNotifier {
public:
  using QSocketNotifier::QSocketNotifier;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QSocketNotifier::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSocketNotifierCall0 call = reinterpret_cast<CuteQSocketNotifierCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSocketNotifier::event(a0);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSocketNotifierCall1 call = reinterpret_cast<CuteQSocketNotifierCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSocketNotifierCall2 call = reinterpret_cast<CuteQSocketNotifierCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSocketNotifierCall3 call = reinterpret_cast<CuteQSocketNotifierCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSocketNotifierCall4 call = reinterpret_cast<CuteQSocketNotifierCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSocketNotifierCall5 call = reinterpret_cast<CuteQSocketNotifierCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSocketNotifierCall6 call = reinterpret_cast<CuteQSocketNotifierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QSocketNotifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSocketNotifier10metaObjectEv(
    const QSocketNotifier *self) {
  return self->metaObject();
}

//  QString QSocketNotifier::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSocketNotifier2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSocketNotifier::tr(s, c, n));
}

//  QSocketNotifier::QSocketNotifier(Type a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QSocketNotifier *ritual_ZN15QSocketNotifierC1ENS_4TypeEP7QObject(
    QSocketNotifier::Type a0,
    QObject *parent) {
  return new CuteQSocketNotifier(a0, parent);
}

//  QSocketNotifier::QSocketNotifier(qintptr socket, Type a1, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSocketNotifier *ritual_ZN15QSocketNotifierC1ExNS_4TypeEP7QObject(
    qintptr socket,
    QSocketNotifier::Type a1,
    QObject *parent) {
  return new CuteQSocketNotifier(socket, a1, parent);
}

//  QSocketNotifier::~QSocketNotifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSocketNotifierD1Ev(QSocketNotifier *self) {
  delete self;
}

//  void QSocketNotifier::setSocket(qintptr socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSocketNotifier9setSocketEx(
    QSocketNotifier *self,
    qintptr socket) {
  self->setSocket(socket);
}

//  qintptr QSocketNotifier::socket() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK15QSocketNotifier6socketEv(const QSocketNotifier *self) {
  return self->socket();
}

//  Type QSocketNotifier::type() const
extern "C" Q_DECL_EXPORT
QSocketNotifier::Type ritual_ZNK15QSocketNotifier4typeEv(
    const QSocketNotifier *self) {
  return self->type();
}

//  bool QSocketNotifier::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSocketNotifier7isValidEv(const QSocketNotifier *self) {
  return self->isValid();
}

//  bool QSocketNotifier::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSocketNotifier9isEnabledEv(const QSocketNotifier *self) {
  return self->isEnabled();
}

//  void QSocketNotifier::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSocketNotifier10setEnabledEb(
    QSocketNotifier *self,
    bool a0) {
  self->setEnabled(a0);
}

//  bool QSocketNotifier::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSocketNotifier5eventEP6QEvent(
    QSocketNotifier *self,
    QEvent *a0) {
  return self->event(a0);
}

//  a Python function taken by a CuteQSocketNotifier, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSocketNotifier(
    QSocketNotifier *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSocketNotifier *>(self)->take(key, call);
}

//  bool QSocketNotifier::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QSocketNotifier5eventEP6QEvent(
    QSocketNotifier *self,
    QEvent *a0) {
  return static_cast<OwnQSocketNotifier *>(self)->OwnQSocketNotifier::event(
      a0);
}
