//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qmouseevent.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qmouseevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QMouseEvent that Python can take functions over in. Every Qt3DInput::QMouseEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QMouseEventCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QMouseEventCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseEventCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseEventCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseEventCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseEventCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseEventCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QMouseEvent : public Qt3DInput::QMouseEvent {
public:
  using Qt3DInput::QMouseEvent::QMouseEvent;
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
      CuteQt3DInput_QMouseEventCall0 call = reinterpret_cast<CuteQt3DInput_QMouseEventCall0>(taken[0]);
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
      CuteQt3DInput_QMouseEventCall1 call = reinterpret_cast<CuteQt3DInput_QMouseEventCall1>(taken[1]);
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
      CuteQt3DInput_QMouseEventCall2 call = reinterpret_cast<CuteQt3DInput_QMouseEventCall2>(taken[2]);
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
      CuteQt3DInput_QMouseEventCall3 call = reinterpret_cast<CuteQt3DInput_QMouseEventCall3>(taken[3]);
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
      CuteQt3DInput_QMouseEventCall4 call = reinterpret_cast<CuteQt3DInput_QMouseEventCall4>(taken[4]);
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
      CuteQt3DInput_QMouseEventCall5 call = reinterpret_cast<CuteQt3DInput_QMouseEventCall5>(taken[5]);
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
      CuteQt3DInput_QMouseEventCall6 call = reinterpret_cast<CuteQt3DInput_QMouseEventCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QMouseEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput11QMouseEvent10metaObjectEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QMouseEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput11QMouseEvent11qt_metacastEPKc(
    Qt3DInput::QMouseEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QMouseEvent::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput11QMouseEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QMouseEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QMouseEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput11QMouseEvent2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QMouseEvent::tr(s, c, n));
}

//  Qt3DInput::QMouseEvent::~QMouseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput11QMouseEventD1Ev(Qt3DInput::QMouseEvent *self) {
  delete self;
}

//  int Qt3DInput::QMouseEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput11QMouseEvent1xEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->x();
}

//  int Qt3DInput::QMouseEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput11QMouseEvent1yEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->y();
}

//  bool Qt3DInput::QMouseEvent::wasHeld() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput11QMouseEvent7wasHeldEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->wasHeld();
}

//  Buttons Qt3DInput::QMouseEvent::button() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseEvent::Buttons ritual_ZNK9Qt3DInput11QMouseEvent6buttonEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->button();
}

//  int Qt3DInput::QMouseEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput11QMouseEvent7buttonsEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->buttons();
}

//  Modifiers Qt3DInput::QMouseEvent::modifiers() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseEvent::Modifiers ritual_ZNK9Qt3DInput11QMouseEvent9modifiersEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->modifiers();
}

//  bool Qt3DInput::QMouseEvent::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput11QMouseEvent10isAcceptedEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->isAccepted();
}

//  void Qt3DInput::QMouseEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput11QMouseEvent11setAcceptedEb(
    Qt3DInput::QMouseEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  QEvent::Type Qt3DInput::QMouseEvent::type() const
extern "C" Q_DECL_EXPORT
QEvent::Type ritual_ZNK9Qt3DInput11QMouseEvent4typeEv(
    const Qt3DInput::QMouseEvent *self) {
  return self->type();
}

//  a Python function taken by a CuteQt3DInput_QMouseEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QMouseEvent(
    Qt3DInput::QMouseEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QMouseEvent *>(self)->take(key, call);
}
