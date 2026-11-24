//  Written by dev_tooling.RitualGenerator from the records of QtQmlWorkerScr
//  ipt/6.12.0/QtQmlWorkerScript/private/qquickworkerscript_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlWorkerScript/6.12.0/QtQmlWorkerScript/private/qtqmlworkerscriptglobal_p.h>
#include <QtQmlWorkerScript/QtQmlWorkerScript>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlWorkerScript/6.12.0/QtQmlWorkerScript/private/qquickworkerscript_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWorkerScript may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWorkerScript : QQuickWorkerScript {
  using QQuickWorkerScript::classBegin;
  using QQuickWorkerScript::componentComplete;
  using QQuickWorkerScript::event;
};

//  A QQuickWorkerScript that Python can take functions over in. Every QQuickWorkerScript
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWorkerScriptCall0)(const void *, int *);
typedef void (*CuteQQuickWorkerScriptCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWorkerScriptCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWorkerScriptCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWorkerScriptCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWorkerScriptCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWorkerScriptCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWorkerScriptCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWorkerScriptCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWorkerScript : public QQuickWorkerScript {
public:
  using QQuickWorkerScript::QQuickWorkerScript;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  void QQuickWorkerScript::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWorkerScriptCall0 call = reinterpret_cast<CuteQQuickWorkerScriptCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWorkerScript::classBegin();
  }

  //  void QQuickWorkerScript::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWorkerScriptCall1 call = reinterpret_cast<CuteQQuickWorkerScriptCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWorkerScript::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickWorkerScript::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWorkerScriptCall2 call = reinterpret_cast<CuteQQuickWorkerScriptCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickWorkerScript::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWorkerScriptCall3 call = reinterpret_cast<CuteQQuickWorkerScriptCall3>(taken[3]);
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
      CuteQQuickWorkerScriptCall4 call = reinterpret_cast<CuteQQuickWorkerScriptCall4>(taken[4]);
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
      CuteQQuickWorkerScriptCall5 call = reinterpret_cast<CuteQQuickWorkerScriptCall5>(taken[5]);
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
      CuteQQuickWorkerScriptCall6 call = reinterpret_cast<CuteQQuickWorkerScriptCall6>(taken[6]);
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
      CuteQQuickWorkerScriptCall7 call = reinterpret_cast<CuteQQuickWorkerScriptCall7>(taken[7]);
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
      CuteQQuickWorkerScriptCall8 call = reinterpret_cast<CuteQQuickWorkerScriptCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWorkerScript::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickWorkerScript10metaObjectEv(
    const QQuickWorkerScript *self) {
  return self->metaObject();
}

//  QString QQuickWorkerScript::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickWorkerScript2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWorkerScript::tr(s, c, n));
}

//  QQuickWorkerScript::QQuickWorkerScript(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWorkerScript *ritual_ZN18QQuickWorkerScriptC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickWorkerScript(parent);
}

//  QQuickWorkerScript::~QQuickWorkerScript()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWorkerScriptD1Ev(QQuickWorkerScript *self) {
  delete self;
}

//  QUrl QQuickWorkerScript::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickWorkerScript6sourceEv(
    const QQuickWorkerScript *self) {
  return new QUrl(self->source());
}

//  void QQuickWorkerScript::setSource(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWorkerScript9setSourceERK4QUrl(
    QQuickWorkerScript *self,
    const QUrl *a0) {
  self->setSource(*a0);
}

//  bool QQuickWorkerScript::ready() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickWorkerScript5readyEv(const QQuickWorkerScript *self) {
  return self->ready();
}

//  void QQuickWorkerScript::sendMessage(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWorkerScript11sendMessageEP14QQmlV4Function(
    QQuickWorkerScript *self,
    QQmlV4FunctionPtr a0) {
  self->sendMessage(a0);
}

//  void QQuickWorkerScript::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWorkerScript10classBeginEv(QQuickWorkerScript *self) {
  self->classBegin();
}

//  void QQuickWorkerScript::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWorkerScript17componentCompleteEv(
    QQuickWorkerScript *self) {
  self->componentComplete();
}

//  bool QQuickWorkerScript::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickWorkerScript5eventEP6QEvent(
    QQuickWorkerScript *self,
    QEvent *a0) {
  return self->event(a0);
}

//  QQuickWorkerScriptEngine *QQuickWorkerScript::engine()
extern "C" Q_DECL_EXPORT
QQuickWorkerScriptEngine *ritual_ZN18QQuickWorkerScript6engineEv(
    QQuickWorkerScript *self) {
  return self->engine();
}

//  QQuickWorkerScript as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickWorkerScript_QQmlParserStatus(
    QQuickWorkerScript *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickWorkerScript, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWorkerScript(
    QQuickWorkerScript *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWorkerScript *>(self)->take(key, call);
}

//  void QQuickWorkerScript::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickWorkerScript10classBeginEv(
    QQuickWorkerScript *self) {
  static_cast<OwnQQuickWorkerScript *>(self)->OwnQQuickWorkerScript::classBegin();
}

//  void QQuickWorkerScript::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickWorkerScript17componentCompleteEv(
    QQuickWorkerScript *self) {
  static_cast<OwnQQuickWorkerScript *>(self)->OwnQQuickWorkerScript::componentComplete();
}

//  bool QQuickWorkerScript::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickWorkerScript5eventEP6QEvent(
    QQuickWorkerScript *self,
    QEvent *a0) {
  return static_cast<OwnQQuickWorkerScript *>(self)->OwnQQuickWorkerScript::event(
      a0);
}
