//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktransitionmanager_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktransitionmanager_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickTransitionManager may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTransitionManager : QQuickTransitionManager {
  using QQuickTransitionManager::finished;
};

//  A QQuickTransitionManager that Python can take functions over in. Every QQuickTransitionManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTransitionManagerCall0)(const void *, int *);
class CuteQQuickTransitionManager : public QQuickTransitionManager {
public:
  using QQuickTransitionManager::QQuickTransitionManager;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QQuickTransitionManager8finishedEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuickTransitionManager::finished()
  void finished() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTransitionManagerCall0 call = reinterpret_cast<CuteQQuickTransitionManagerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTransitionManager::finished();
  }
};

//  QQuickTransitionManager::QQuickTransitionManager()
extern "C" Q_DECL_EXPORT
QQuickTransitionManager *ritual_ZN23QQuickTransitionManagerC1Ev() {
  return new CuteQQuickTransitionManager();
}

//  QQuickTransitionManager::~QQuickTransitionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTransitionManagerD1Ev(QQuickTransitionManager *self) {
  delete self;
}

//  bool QQuickTransitionManager::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickTransitionManager9isRunningEv(
    const QQuickTransitionManager *self) {
  return self->isRunning();
}

//  void QQuickTransitionManager::transition(const QList<QQuickStateAction>
//      &a0, QQuickTransition *transition, QObject *defaultTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTransitionManager10transitionERK5QListI17QQuickStateActionEP16QQuickTransitionP7QObject(
    QQuickTransitionManager *self,
    const QList<QQuickStateAction> *a0,
    QQuickTransition *transition,
    QObject *defaultTarget) {
  self->transition(*a0, transition, defaultTarget);
}

//  void QQuickTransitionManager::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTransitionManager6cancelEv(
    QQuickTransitionManager *self) {
  self->cancel();
}

//  void QQuickTransitionManager::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTransitionManager8finishedEv(
    QQuickTransitionManager *self) {
  self->finished();
}

//  void QQuickTransitionManager::complete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTransitionManager8completeEv(
    QQuickTransitionManager *self) {
  self->complete();
}

//  void QQuickTransitionManager::setState(QQuickState *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTransitionManager8setStateEP11QQuickState(
    QQuickTransitionManager *self,
    QQuickState *a0) {
  self->setState(a0);
}

//  a Python function taken by a CuteQQuickTransitionManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTransitionManager(
    QQuickTransitionManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTransitionManager *>(self)->take(key, call);
}

//  void QQuickTransitionManager::finished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickTransitionManager8finishedEv(
    QQuickTransitionManager *self) {
  static_cast<OwnQQuickTransitionManager *>(self)->OwnQQuickTransitionManager::finished();
}
