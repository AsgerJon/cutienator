//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlscriptstring.h>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickScriptAction that Python can take functions over in. Every QQuickScriptAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickScriptActionCall0)(const void *, int *);
typedef void (*CuteQQuickScriptActionCall1)(const void *, int *);
typedef int (*CuteQQuickScriptActionCall2)(const void *, int *);
typedef void (*CuteQQuickScriptActionCall3)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScriptActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScriptActionCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScriptActionCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScriptActionCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScriptActionCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScriptActionCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScriptActionCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickScriptAction : public QQuickScriptAction {
public:
  using QQuickScriptAction::QQuickScriptAction;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickScriptActionCall0 call = reinterpret_cast<CuteQQuickScriptActionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickScriptActionCall1 call = reinterpret_cast<CuteQQuickScriptActionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickScriptActionCall2 call = reinterpret_cast<CuteQQuickScriptActionCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickScriptActionCall3 call = reinterpret_cast<CuteQQuickScriptActionCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::setTarget(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickScriptActionCall4 call = reinterpret_cast<CuteQQuickScriptActionCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickScriptActionCall5 call = reinterpret_cast<CuteQQuickScriptActionCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickScriptActionCall6 call = reinterpret_cast<CuteQQuickScriptActionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickScriptActionCall7 call = reinterpret_cast<CuteQQuickScriptActionCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickScriptActionCall8 call = reinterpret_cast<CuteQQuickScriptActionCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickScriptActionCall9 call = reinterpret_cast<CuteQQuickScriptActionCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickScriptActionCall10 call = reinterpret_cast<CuteQQuickScriptActionCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickScriptAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickScriptAction10metaObjectEv(
    const QQuickScriptAction *self) {
  return self->metaObject();
}

//  QString QQuickScriptAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickScriptAction2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScriptAction::tr(s, c, n));
}

//  QQuickScriptActionPrivate *QQuickScriptAction::d_func()
extern "C" Q_DECL_EXPORT
QQuickScriptActionPrivate *ritual_ZN18QQuickScriptAction6d_funcEv(
    QQuickScriptAction *self) {
  return self->d_func();
}

//  const QQuickScriptActionPrivate *QQuickScriptAction::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickScriptActionPrivate *ritual_ZNK18QQuickScriptAction6d_funcEv(
    const QQuickScriptAction *self) {
  return self->d_func();
}

//  QQuickScriptAction::QQuickScriptAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickScriptAction *ritual_ZN18QQuickScriptActionC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickScriptAction(parent);
}

//  QQuickScriptAction::~QQuickScriptAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickScriptActionD1Ev(QQuickScriptAction *self) {
  delete self;
}

//  QQmlScriptString QQuickScriptAction::script() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK18QQuickScriptAction6scriptEv(
    const QQuickScriptAction *self) {
  return new QQmlScriptString(self->script());
}

//  void QQuickScriptAction::setScript(const QQmlScriptString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickScriptAction9setScriptERK16QQmlScriptString(
    QQuickScriptAction *self,
    const QQmlScriptString *a0) {
  self->setScript(*a0);
}

//  QString QQuickScriptAction::stateChangeScriptName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickScriptAction21stateChangeScriptNameEv(
    const QQuickScriptAction *self) {
  return new QString(self->stateChangeScriptName());
}

//  void QQuickScriptAction::setStateChangeScriptName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickScriptAction24setStateChangeScriptNameERK7QString(
    QQuickScriptAction *self,
    const QString *a0) {
  self->setStateChangeScriptName(*a0);
}

//  a Python function taken by a CuteQQuickScriptAction, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScriptAction(
    QQuickScriptAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScriptAction *>(self)->take(key, call);
}
