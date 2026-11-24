//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qactiongroup_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(action)
#if QT_CONFIG(action)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qactiongroup.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qactiongroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QActionGroupPrivate that Python can take functions over in. Every QActionGroupPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(action)
typedef void (*CuteQActionGroupPrivateCall0)(const void *, int, QAction *, int *);
#endif  // QT_CONFIG(action)
class CuteQActionGroupPrivate : public QActionGroupPrivate {
public:
  using QActionGroupPrivate::QActionGroupPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN19QActionGroupPrivate10emitSignalENS_6SignalEP7QAction")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
    return false;
  }

#if QT_CONFIG(action)
  //  void QActionGroupPrivate::emitSignal(Signal a0, QAction *a1)
  void emitSignal(QActionGroupPrivate::Signal a0, QAction *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQActionGroupPrivateCall0 call = reinterpret_cast<CuteQActionGroupPrivateCall0>(taken[0]);
      call(this, static_cast<int>(a0), a1, &handled);
      if (handled) return;
    }
    QActionGroupPrivate::emitSignal(a0, a1);
  }
#endif  // QT_CONFIG(action)
};

//  QActionGroup *QActionGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN19QActionGroupPrivate6q_funcEv(
    QActionGroupPrivate *self) {
  return self->q_func();
}

//  const QActionGroup *QActionGroupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QActionGroup *ritual_ZNK19QActionGroupPrivate6q_funcEv(
    const QActionGroupPrivate *self) {
  return self->q_func();
}

//  QActionGroupPrivate::QActionGroupPrivate()
extern "C" Q_DECL_EXPORT
QActionGroupPrivate *ritual_ZN19QActionGroupPrivateC1Ev() {
  return new CuteQActionGroupPrivate();
}

//  QActionGroupPrivate::~QActionGroupPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QActionGroupPrivateD1Ev(QActionGroupPrivate *self) {
  delete self;
}

//  void QActionGroupPrivate::emitSignal(Signal a0, QAction *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QActionGroupPrivate10emitSignalENS_6SignalEP7QAction(
    QActionGroupPrivate *self,
    QActionGroupPrivate::Signal a0,
    QAction *a1) {
  self->emitSignal(a0, a1);
}

//  a Python function taken by a CuteQActionGroupPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QActionGroupPrivate(
    QActionGroupPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQActionGroupPrivate *>(self)->take(key, call);
}

//  void QActionGroupPrivate::emitSignal(Signal a0, QAction *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QActionGroupPrivate10emitSignalENS_6SignalEP7QAction(
    QActionGroupPrivate *self,
    QActionGroupPrivate::Signal a0,
    QAction *a1) {
  self->QActionGroupPrivate::emitSignal(a0, a1);
}

#endif  // QT_CONFIG(action)
#endif  // QT_CONFIG(action)
