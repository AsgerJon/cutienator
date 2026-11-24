//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstategroup_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstategroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickStateGroup that Python can take functions over in. Every QQuickStateGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickStateGroupCall0)(const void *, int *);
typedef void (*CuteQQuickStateGroupCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStateGroupCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStateGroupCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateGroupCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateGroupCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateGroupCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateGroupCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateGroupCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickStateGroup : public QQuickStateGroup {
public:
  using QQuickStateGroup::QQuickStateGroup;
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

  //  void QQuickStateGroup::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStateGroupCall0 call = reinterpret_cast<CuteQQuickStateGroupCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateGroup::classBegin();
  }

  //  void QQuickStateGroup::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStateGroupCall1 call = reinterpret_cast<CuteQQuickStateGroupCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateGroup::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStateGroupCall2 call = reinterpret_cast<CuteQQuickStateGroupCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStateGroupCall3 call = reinterpret_cast<CuteQQuickStateGroupCall3>(taken[3]);
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
      CuteQQuickStateGroupCall4 call = reinterpret_cast<CuteQQuickStateGroupCall4>(taken[4]);
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
      CuteQQuickStateGroupCall5 call = reinterpret_cast<CuteQQuickStateGroupCall5>(taken[5]);
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
      CuteQQuickStateGroupCall6 call = reinterpret_cast<CuteQQuickStateGroupCall6>(taken[6]);
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
      CuteQQuickStateGroupCall7 call = reinterpret_cast<CuteQQuickStateGroupCall7>(taken[7]);
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
      CuteQQuickStateGroupCall8 call = reinterpret_cast<CuteQQuickStateGroupCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickStateGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickStateGroup10metaObjectEv(
    const QQuickStateGroup *self) {
  return self->metaObject();
}

//  QString QQuickStateGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickStateGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStateGroup::tr(s, c, n));
}

//  QQuickStateGroup::QQuickStateGroup(QObject *a0)
extern "C" Q_DECL_EXPORT
QQuickStateGroup *ritual_ZN16QQuickStateGroupC1EP7QObject(QObject *a0) {
  return new CuteQQuickStateGroup(a0);
}

//  QQuickStateGroup::~QQuickStateGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStateGroupD1Ev(QQuickStateGroup *self) {
  delete self;
}

//  QString QQuickStateGroup::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickStateGroup5stateEv(const QQuickStateGroup *self) {
  return new QString(self->state());
}

//  void QQuickStateGroup::setState(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStateGroup8setStateERK7QString(
    QQuickStateGroup *self,
    const QString *a0) {
  self->setState(*a0);
}

//  QList<QQuickState *> QQuickStateGroup::states() const
extern "C" Q_DECL_EXPORT
QList<QQuickState *> *ritual_ZNK16QQuickStateGroup6statesEv(
    const QQuickStateGroup *self) {
  return new QList<QQuickState *>(self->states());
}

//  QQuickState *QQuickStateGroup::findState(const QString &name) const
extern "C" Q_DECL_EXPORT
QQuickState *ritual_ZNK16QQuickStateGroup9findStateERK7QString(
    const QQuickStateGroup *self,
    const QString *name) {
  return self->findState(*name);
}

//  void QQuickStateGroup::removeState(QQuickState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStateGroup11removeStateEP11QQuickState(
    QQuickStateGroup *self,
    QQuickState *state) {
  self->removeState(state);
}

//  void QQuickStateGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStateGroup10classBeginEv(QQuickStateGroup *self) {
  self->classBegin();
}

//  void QQuickStateGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStateGroup17componentCompleteEv(
    QQuickStateGroup *self) {
  self->componentComplete();
}

//  bool QQuickStateGroup::updateAutoState()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickStateGroup15updateAutoStateEv(QQuickStateGroup *self) {
  return self->updateAutoState();
}

//  void QQuickStateGroup::stateAboutToComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStateGroup20stateAboutToCompleteEv(
    QQuickStateGroup *self) {
  self->stateAboutToComplete();
}

//  QQuickStateGroup as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickStateGroup_QQmlParserStatus(
    QQuickStateGroup *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickStateGroup, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStateGroup(
    QQuickStateGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStateGroup *>(self)->take(key, call);
}

//  void QQuickStateGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickStateGroup10classBeginEv(QQuickStateGroup *self) {
  self->QQuickStateGroup::classBegin();
}

//  void QQuickStateGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickStateGroup17componentCompleteEv(
    QQuickStateGroup *self) {
  self->QQuickStateGroup::componentComplete();
}
