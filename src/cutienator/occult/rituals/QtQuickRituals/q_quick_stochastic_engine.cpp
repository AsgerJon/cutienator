//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QQuickStochasticEngine that Python can take functions over in. Every QQuickStochasticEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQQuickStochasticEngineCall0)(const void *, int, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQQuickStochasticEngineCall1)(const void *, int, int *);
#endif  // QT_CONFIG(quick_sprite)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStochasticEngineCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStochasticEngineCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStochasticEngineCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStochasticEngineCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStochasticEngineCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStochasticEngineCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStochasticEngineCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickStochasticEngine : public QQuickStochasticEngine {
public:
  using QQuickStochasticEngine::QQuickStochasticEngine;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN22QQuickStochasticEngine7restartEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN22QQuickStochasticEngine7advanceEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
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

#if QT_CONFIG(quick_sprite)
  //  void QQuickStochasticEngine::restart(int index)
  void restart(int index) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStochasticEngineCall0 call = reinterpret_cast<CuteQQuickStochasticEngineCall0>(taken[0]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQuickStochasticEngine::restart(index);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QQuickStochasticEngine::advance(int index)
  void advance(int index) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStochasticEngineCall1 call = reinterpret_cast<CuteQQuickStochasticEngineCall1>(taken[1]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQuickStochasticEngine::advance(index);
  }
#endif  // QT_CONFIG(quick_sprite)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStochasticEngineCall2 call = reinterpret_cast<CuteQQuickStochasticEngineCall2>(taken[2]);
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
      CuteQQuickStochasticEngineCall3 call = reinterpret_cast<CuteQQuickStochasticEngineCall3>(taken[3]);
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
      CuteQQuickStochasticEngineCall4 call = reinterpret_cast<CuteQQuickStochasticEngineCall4>(taken[4]);
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
      CuteQQuickStochasticEngineCall5 call = reinterpret_cast<CuteQQuickStochasticEngineCall5>(taken[5]);
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
      CuteQQuickStochasticEngineCall6 call = reinterpret_cast<CuteQQuickStochasticEngineCall6>(taken[6]);
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
      CuteQQuickStochasticEngineCall7 call = reinterpret_cast<CuteQQuickStochasticEngineCall7>(taken[7]);
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
      CuteQQuickStochasticEngineCall8 call = reinterpret_cast<CuteQQuickStochasticEngineCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickStochasticEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickStochasticEngine10metaObjectEv(
    const QQuickStochasticEngine *self) {
  return self->metaObject();
}

//  void *QQuickStochasticEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickStochasticEngine11qt_metacastEPKc(
    QQuickStochasticEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickStochasticEngine::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickStochasticEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickStochasticEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickStochasticEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickStochasticEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStochasticEngine::tr(s, c, n));
}

//  QQuickStochasticEngine::QQuickStochasticEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickStochasticEngine *ritual_ZN22QQuickStochasticEngineC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickStochasticEngine(parent);
}

//  QQuickStochasticEngine::QQuickStochasticEngine(const
//      QList<QQuickStochasticState *> &states, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickStochasticEngine *ritual_ZN22QQuickStochasticEngineC1ERK5QListIP21QQuickStochasticStateEP7QObject(
    const QList<QQuickStochasticState *> *states,
    QObject *parent) {
  return new CuteQQuickStochasticEngine(*states, parent);
}

//  QQuickStochasticEngine::~QQuickStochasticEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngineD1Ev(QQuickStochasticEngine *self) {
  delete self;
}

//  QQmlListProperty<QQuickStochasticState> QQuickStochasticEngine::states()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickStochasticState> *ritual_ZN22QQuickStochasticEngine6statesEv(
    QQuickStochasticEngine *self) {
  return new QQmlListProperty<QQuickStochasticState>(self->states());
}

//  QString QQuickStochasticEngine::globalGoal() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickStochasticEngine10globalGoalEv(
    const QQuickStochasticEngine *self) {
  return new QString(self->globalGoal());
}

//  int QQuickStochasticEngine::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickStochasticEngine5countEv(
    const QQuickStochasticEngine *self) {
  return self->count();
}

//  void QQuickStochasticEngine::setCount(int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine8setCountEi(
    QQuickStochasticEngine *self,
    int c) {
  self->setCount(c);
}

//  void QQuickStochasticEngine::setGoal(int state, int sprite, bool jump)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine7setGoalEiib(
    QQuickStochasticEngine *self,
    int state,
    int sprite,
    bool jump) {
  self->setGoal(state, sprite, jump);
}

//  void QQuickStochasticEngine::start(int index, int state)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine5startEii(
    QQuickStochasticEngine *self,
    int index,
    int state) {
  self->start(index, state);
}

//  void QQuickStochasticEngine::restart(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine7restartEi(
    QQuickStochasticEngine *self,
    int index) {
  self->restart(index);
}

//  void QQuickStochasticEngine::advance(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine7advanceEi(
    QQuickStochasticEngine *self,
    int index) {
  self->advance(index);
}

//  void QQuickStochasticEngine::stop(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine4stopEi(
    QQuickStochasticEngine *self,
    int index) {
  self->stop(index);
}

//  int QQuickStochasticEngine::curState(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickStochasticEngine8curStateEi(
    const QQuickStochasticEngine *self,
    int index) {
  return self->curState(index);
}

//  QQuickStochasticState *QQuickStochasticEngine::state(int idx) const
extern "C" Q_DECL_EXPORT
QQuickStochasticState *ritual_ZNK22QQuickStochasticEngine5stateEi(
    const QQuickStochasticEngine *self,
    int idx) {
  return self->state(idx);
}

//  int QQuickStochasticEngine::stateIndex(QQuickStochasticState *s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickStochasticEngine10stateIndexEP21QQuickStochasticState(
    const QQuickStochasticEngine *self,
    QQuickStochasticState *s) {
  return self->stateIndex(s);
}

//  int QQuickStochasticEngine::stateIndex(const QString &s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickStochasticEngine10stateIndexERK7QString(
    const QQuickStochasticEngine *self,
    const QString *s) {
  return self->stateIndex(*s);
}

//  int QQuickStochasticEngine::stateCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickStochasticEngine10stateCountEv(
    QQuickStochasticEngine *self) {
  return self->stateCount();
}

//  void QQuickStochasticEngine::globalGoalChanged(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine17globalGoalChangedERK7QString(
    QQuickStochasticEngine *self,
    const QString *arg) {
  self->globalGoalChanged(*arg);
}

//  void QQuickStochasticEngine::stateChanged(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine12stateChangedEi(
    QQuickStochasticEngine *self,
    int idx) {
  self->stateChanged(idx);
}

//  void QQuickStochasticEngine::setGlobalGoal(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine13setGlobalGoalERK7QString(
    QQuickStochasticEngine *self,
    const QString *arg) {
  self->setGlobalGoal(*arg);
}

//  uint QQuickStochasticEngine::updateSprites(uint time)
extern "C" Q_DECL_EXPORT
uint ritual_ZN22QQuickStochasticEngine13updateSpritesEj(
    QQuickStochasticEngine *self,
    uint time) {
  return self->updateSprites(time);
}

//  void QQuickStochasticEngine::addToUpdateList(uint t, int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStochasticEngine15addToUpdateListEji(
    QQuickStochasticEngine *self,
    uint t,
    int idx) {
  self->addToUpdateList(t, idx);
}

//  int QQuickStochasticEngine::nextState(int curState, int idx)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickStochasticEngine9nextStateEii(
    QQuickStochasticEngine *self,
    int curState,
    int idx) {
  return self->nextState(curState, idx);
}

//  int QQuickStochasticEngine::goalSeek(int curState, int idx, int dist)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickStochasticEngine8goalSeekEiii(
    QQuickStochasticEngine *self,
    int curState,
    int idx,
    int dist) {
  return self->goalSeek(curState, idx, dist);
}

//  a Python function taken by a CuteQQuickStochasticEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStochasticEngine(
    QQuickStochasticEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStochasticEngine *>(self)->take(key, call);
}

//  void QQuickStochasticEngine::restart(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStochasticEngine7restartEi(
    QQuickStochasticEngine *self,
    int index) {
  self->QQuickStochasticEngine::restart(index);
}

//  void QQuickStochasticEngine::advance(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStochasticEngine7advanceEi(
    QQuickStochasticEngine *self,
    int index) {
  self->QQuickStochasticEngine::advance(index);
}

//  a QQmlListProperty<QQuickStochasticState> a ritual of
//      QQuickStochasticEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickStochasticEngine__QQmlListProperty_QQuickStochasticState(
    QQmlListProperty<QQuickStochasticState> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_sprite)
#endif  // QT_CONFIG(quick_sprite)
