//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  A QAbstractAnimationAction that Python can take functions over in. Every QAbstractAnimationAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractAnimationActionCall0)(const void *, int *);
typedef void (*CuteQAbstractAnimationActionCall1)(const void *, const QDebug *, int, int *);
class CuteQAbstractAnimationAction : public QAbstractAnimationAction {
public:
  using QAbstractAnimationAction::QAbstractAnimationAction;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractAnimationAction8doActionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QAbstractAnimationAction11debugActionE6QDebugi")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractAnimationAction::doAction()
  void doAction() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractAnimationActionCall0 call = reinterpret_cast<CuteQAbstractAnimationActionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAnimationAction::debugAction(QDebug a0, int a1) const
  void debugAction(QDebug a0, int a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractAnimationActionCall1 call = reinterpret_cast<CuteQAbstractAnimationActionCall1>(taken[1]);
      call(this, &a0, a1, &handled);
      if (handled) return;
    }
    QAbstractAnimationAction::debugAction(a0, a1);
  }
};

//  QAbstractAnimationAction::~QAbstractAnimationAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractAnimationActionD1Ev(
    QAbstractAnimationAction *self) {
  delete self;
}

//  void QAbstractAnimationAction::doAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractAnimationAction8doActionEv(
    QAbstractAnimationAction *self) {
  self->doAction();
}

//  void QAbstractAnimationAction::debugAction(QDebug a0, int a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QAbstractAnimationAction11debugActionE6QDebugi(
    const QAbstractAnimationAction *self,
    const QDebug *a0,
    int a1) {
  self->debugAction(*a0, a1);
}

//  a Python function taken by a CuteQAbstractAnimationAction, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractAnimationAction(
    QAbstractAnimationAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractAnimationAction *>(self)->take(key, call);
}

//  void QAbstractAnimationAction::debugAction(QDebug a0, int a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK24QAbstractAnimationAction11debugActionE6QDebugi(
    const QAbstractAnimationAction *self,
    const QDebug *a0,
    int a1) {
  self->QAbstractAnimationAction::debugAction(*a0, a1);
}
