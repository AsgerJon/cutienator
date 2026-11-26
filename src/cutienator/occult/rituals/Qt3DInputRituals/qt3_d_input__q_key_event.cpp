//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qkeyevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <Qt3DInput/qkeyevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QKeyEvent that Python can take functions over in. Every Qt3DInput::QKeyEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QKeyEventCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QKeyEventCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyEventCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyEventCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyEventCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyEventCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyEventCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QKeyEvent : public Qt3DInput::QKeyEvent {
public:
  using Qt3DInput::QKeyEvent::QKeyEvent;
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
      CuteQt3DInput_QKeyEventCall0 call = reinterpret_cast<CuteQt3DInput_QKeyEventCall0>(taken[0]);
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
      CuteQt3DInput_QKeyEventCall1 call = reinterpret_cast<CuteQt3DInput_QKeyEventCall1>(taken[1]);
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
      CuteQt3DInput_QKeyEventCall2 call = reinterpret_cast<CuteQt3DInput_QKeyEventCall2>(taken[2]);
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
      CuteQt3DInput_QKeyEventCall3 call = reinterpret_cast<CuteQt3DInput_QKeyEventCall3>(taken[3]);
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
      CuteQt3DInput_QKeyEventCall4 call = reinterpret_cast<CuteQt3DInput_QKeyEventCall4>(taken[4]);
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
      CuteQt3DInput_QKeyEventCall5 call = reinterpret_cast<CuteQt3DInput_QKeyEventCall5>(taken[5]);
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
      CuteQt3DInput_QKeyEventCall6 call = reinterpret_cast<CuteQt3DInput_QKeyEventCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QKeyEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput9QKeyEvent10metaObjectEv(
    const Qt3DInput::QKeyEvent *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QKeyEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput9QKeyEvent11qt_metacastEPKc(
    Qt3DInput::QKeyEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QKeyEvent::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput9QKeyEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QKeyEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QKeyEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput9QKeyEvent2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QKeyEvent::tr(s, c, n));
}

//  Qt3DInput::QKeyEvent::QKeyEvent(QEvent::Type type, int key,
//      Qt::KeyboardModifiers modifiers, const QString &text, bool autorep,
//      ushort count)
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyEvent *ritual_ZN9Qt3DInput9QKeyEventC1EN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QEvent::Type type,
    int key,
    int modifiers,
    const QString *text,
    bool autorep,
    ushort count) {
  return new CuteQt3DInput_QKeyEvent(
      type,
      key,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      *text,
      autorep,
      count);
}

//  Qt3DInput::QKeyEvent::~QKeyEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput9QKeyEventD1Ev(Qt3DInput::QKeyEvent *self) {
  delete self;
}

//  int Qt3DInput::QKeyEvent::key() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput9QKeyEvent3keyEv(const Qt3DInput::QKeyEvent *self) {
  return self->key();
}

//  QString Qt3DInput::QKeyEvent::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9Qt3DInput9QKeyEvent4textEv(
    const Qt3DInput::QKeyEvent *self) {
  return new QString(self->text());
}

//  int Qt3DInput::QKeyEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput9QKeyEvent9modifiersEv(
    const Qt3DInput::QKeyEvent *self) {
  return self->modifiers();
}

//  bool Qt3DInput::QKeyEvent::isAutoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput9QKeyEvent12isAutoRepeatEv(
    const Qt3DInput::QKeyEvent *self) {
  return self->isAutoRepeat();
}

//  int Qt3DInput::QKeyEvent::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput9QKeyEvent5countEv(
    const Qt3DInput::QKeyEvent *self) {
  return self->count();
}

//  quint32 Qt3DInput::QKeyEvent::nativeScanCode() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK9Qt3DInput9QKeyEvent14nativeScanCodeEv(
    const Qt3DInput::QKeyEvent *self) {
  return self->nativeScanCode();
}

//  bool Qt3DInput::QKeyEvent::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput9QKeyEvent10isAcceptedEv(
    const Qt3DInput::QKeyEvent *self) {
  return self->isAccepted();
}

//  void Qt3DInput::QKeyEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput9QKeyEvent11setAcceptedEb(
    Qt3DInput::QKeyEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  QEvent::Type Qt3DInput::QKeyEvent::type() const
extern "C" Q_DECL_EXPORT
QEvent::Type ritual_ZNK9Qt3DInput9QKeyEvent4typeEv(
    const Qt3DInput::QKeyEvent *self) {
  return self->type();
}

#if QT_CONFIG(shortcut)
//  bool Qt3DInput::QKeyEvent::matches(QKeySequence::StandardKey key_) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput9QKeyEvent7matchesEN12QKeySequence11StandardKeyE(
    const Qt3DInput::QKeyEvent *self,
    QKeySequence::StandardKey key_) {
  return self->matches(key_);
}
#endif  // QT_CONFIG(shortcut)

//  a Python function taken by a CuteQt3DInput_QKeyEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QKeyEvent(
    Qt3DInput::QKeyEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QKeyEvent *>(self)->take(key, call);
}
