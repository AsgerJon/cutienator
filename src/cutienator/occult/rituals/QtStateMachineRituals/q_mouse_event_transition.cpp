//  Written by hand on 2026-11-25 from QtStateMachine/qmouseeventtransition.h,
//  Qt 6.12.0, the same text on every system. Kept as it is when the
//  generator runs again. Not written: the 'bindable...' functions,
//  which give a template, a 'QBindable'.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(qeventtransition)
#include <QtStateMachine/qmouseeventtransition.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <cstring>

//  Only a class built on QMouseEventTransition may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMouseEventTransition : QMouseEventTransition {
  using QMouseEventTransition::eventTest;
  using QMouseEventTransition::onTransition;
};

//  A QMouseEventTransition that Python can take functions over in. Every
//  QMouseEventTransition Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef bool (*CuteQMouseEventTransitionCall0)(const void *, QEvent *, int *);
typedef void (*CuteQMouseEventTransitionCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMouseEventTransitionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMouseEventTransitionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMouseEventTransitionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMouseEventTransitionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMouseEventTransitionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMouseEventTransitionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMouseEventTransitionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMouseEventTransition : public QMouseEventTransition {
public:
  using QMouseEventTransition::QMouseEventTransition;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAbstractTransition9eventTestEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractTransition12onTransitionEP6QEvent")) {
      taken[1] = call;
      return true;
    }
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

  //  bool QMouseEventTransition::eventTest(QEvent *event)
  bool eventTest(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMouseEventTransitionCall0 call = reinterpret_cast<CuteQMouseEventTransitionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QMouseEventTransition::eventTest(event);
  }

  //  void QMouseEventTransition::onTransition(QEvent *event)
  void onTransition(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMouseEventTransitionCall1 call = reinterpret_cast<CuteQMouseEventTransitionCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMouseEventTransition::onTransition(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QEventTransition::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMouseEventTransitionCall2 call = reinterpret_cast<CuteQMouseEventTransitionCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QEventTransition::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMouseEventTransitionCall3 call = reinterpret_cast<CuteQMouseEventTransitionCall3>(taken[3]);
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
      CuteQMouseEventTransitionCall4 call = reinterpret_cast<CuteQMouseEventTransitionCall4>(taken[4]);
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
      CuteQMouseEventTransitionCall5 call = reinterpret_cast<CuteQMouseEventTransitionCall5>(taken[5]);
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
      CuteQMouseEventTransitionCall6 call = reinterpret_cast<CuteQMouseEventTransitionCall6>(taken[6]);
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
      CuteQMouseEventTransitionCall7 call = reinterpret_cast<CuteQMouseEventTransitionCall7>(taken[7]);
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
      CuteQMouseEventTransitionCall8 call = reinterpret_cast<CuteQMouseEventTransitionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMouseEventTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QMouseEventTransition10metaObjectEv(
    const QMouseEventTransition *self) {
  return self->metaObject();
}

//  QString QMouseEventTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QMouseEventTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMouseEventTransition::tr(s, c, n));
}

//  QMouseEventTransition::QMouseEventTransition(QState *sourceState)
extern "C" Q_DECL_EXPORT
QMouseEventTransition *ritual_ZN21QMouseEventTransitionC1EP6QState(
    QState *sourceState) {
  return new CuteQMouseEventTransition(sourceState);
}

//  QMouseEventTransition::QMouseEventTransition(QObject *object,
//      QEvent::Type type, Qt::MouseButton button, QState *sourceState)
extern "C" Q_DECL_EXPORT
QMouseEventTransition *ritual_ZN21QMouseEventTransitionC1EP7QObjectN6QEvent4TypeEN2Qt11MouseButtonEP6QState(
    QObject *object,
    QEvent::Type type,
    Qt::MouseButton button,
    QState *sourceState) {
  return new CuteQMouseEventTransition(object, type, button, sourceState);
}

//  QMouseEventTransition::~QMouseEventTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMouseEventTransitionD1Ev(QMouseEventTransition *self) {
  delete self;
}

//  Qt::MouseButton QMouseEventTransition::button() const
extern "C" Q_DECL_EXPORT
Qt::MouseButton ritual_ZNK21QMouseEventTransition6buttonEv(
    const QMouseEventTransition *self) {
  return self->button();
}

//  void QMouseEventTransition::setButton(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMouseEventTransition9setButtonEN2Qt11MouseButtonE(
    QMouseEventTransition *self,
    Qt::MouseButton button) {
  self->setButton(button);
}

//  Qt::KeyboardModifiers QMouseEventTransition::modifierMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMouseEventTransition12modifierMaskEv(
    const QMouseEventTransition *self) {
  return static_cast<int>(self->modifierMask().toInt());
}

//  void QMouseEventTransition::setModifierMask(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMouseEventTransition15setModifierMaskE6QFlagsIN2Qt16KeyboardModifierEE(
    QMouseEventTransition *self,
    int modifiers) {
  self->setModifierMask(
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  QPainterPath QMouseEventTransition::hitTestPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK21QMouseEventTransition11hitTestPathEv(
    const QMouseEventTransition *self) {
  return new QPainterPath(self->hitTestPath());
}

//  void QMouseEventTransition::setHitTestPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMouseEventTransition14setHitTestPathERK12QPainterPath(
    QMouseEventTransition *self,
    const QPainterPath *path) {
  self->setHitTestPath(*path);
}

//  bool QMouseEventTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QMouseEventTransition9eventTestEP6QEvent(
    QMouseEventTransition *self,
    QEvent *event) {
  return self->eventTest(event);
}

//  void QMouseEventTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMouseEventTransition12onTransitionEP6QEvent(
    QMouseEventTransition *self,
    QEvent *event) {
  self->onTransition(event);
}

//  a Python function taken by a CuteQMouseEventTransition, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMouseEventTransition(
    QMouseEventTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMouseEventTransition *>(self)->take(key, call);
}

//  bool QMouseEventTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QMouseEventTransition9eventTestEP6QEvent(
    QMouseEventTransition *self,
    QEvent *event) {
  return static_cast<OwnQMouseEventTransition *>(self)->OwnQMouseEventTransition::eventTest(
      event);
}

//  void QMouseEventTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QMouseEventTransition12onTransitionEP6QEvent(
    QMouseEventTransition *self,
    QEvent *event) {
  static_cast<OwnQMouseEventTransition *>(self)->OwnQMouseEventTransition::onTransition(
      event);
}

#endif  // QT_CONFIG(qeventtransition)
