//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcoreevent_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, rituals for functions the generator leaves
//  out: 1. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcoreevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcoreevent.h>
#include <QtCore/private/qcoreevent_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/qbasicatomic.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qcoreevent.cpp, line 681, as _ZN20QDeferredDeleteEventD2Ev
inline QDeferredDeleteEvent::~QDeferredDeleteEvent() = default;

//  from src/corelib/kernel/qcoreevent.cpp, line 681, as _ZNK20QDeferredDeleteEvent5cloneEv
inline QDeferredDeleteEvent* QDeferredDeleteEvent::clone() const { auto c = new QDeferredDeleteEvent(*this); [[maybe_unused]] QEvent *e = c; Q_ASSERT(reinterpret_cast<quintptr>(c) == reinterpret_cast<quintptr>(e)); return c; }

//  from src/corelib/kernel/qcoreevent.cpp, line 681, as _ZN20QDeferredDeleteEventC1ERKS_
inline QDeferredDeleteEvent::QDeferredDeleteEvent(const QDeferredDeleteEvent &) = default;
//  -----------------------------------------------------------------------

//  A QDeferredDeleteEvent that Python can take functions over in. Every QDeferredDeleteEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDeferredDeleteEventCall0)(const void *, int *);
typedef void (*CuteQDeferredDeleteEventCall1)(const void *, bool, int *);
class CuteQDeferredDeleteEvent : public QDeferredDeleteEvent {
public:
  using QDeferredDeleteEvent::QDeferredDeleteEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QDeferredDeleteEvent *QDeferredDeleteEvent::clone() const
  QDeferredDeleteEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeferredDeleteEventCall0 call = reinterpret_cast<CuteQDeferredDeleteEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDeferredDeleteEvent *>(given);
    }
    return QDeferredDeleteEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeferredDeleteEventCall1 call = reinterpret_cast<CuteQDeferredDeleteEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QDeferredDeleteEvent &QDeferredDeleteEvent::operator=(const
//      QDeferredDeleteEvent &other)
extern "C" Q_DECL_EXPORT
QDeferredDeleteEvent *ritual_ZN20QDeferredDeleteEventaSERKS_(
    QDeferredDeleteEvent *self,
    const QDeferredDeleteEvent *other) {
  return &(self->operator=(*other));
}

//  QDeferredDeleteEvent *QDeferredDeleteEvent::clone() const
extern "C" Q_DECL_EXPORT
QDeferredDeleteEvent *ritual_ZNK20QDeferredDeleteEvent5cloneEv(
    const QDeferredDeleteEvent *self) {
  return self->clone();
}

//  QDeferredDeleteEvent::~QDeferredDeleteEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeferredDeleteEventD1Ev(QDeferredDeleteEvent *self) {
  delete self;
}

//  int QDeferredDeleteEvent::loopLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDeferredDeleteEvent9loopLevelEv(
    const QDeferredDeleteEvent *self) {
  return self->loopLevel();
}

//  int QDeferredDeleteEvent::scopeLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDeferredDeleteEvent10scopeLevelEv(
    const QDeferredDeleteEvent *self) {
  return self->scopeLevel();
}

//  a Python function taken by a CuteQDeferredDeleteEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeferredDeleteEvent(
    QDeferredDeleteEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeferredDeleteEvent *>(self)->take(key, call);
}

//  QDeferredDeleteEvent *QDeferredDeleteEvent::clone() const
extern "C" Q_DECL_EXPORT
QDeferredDeleteEvent *ritual_own_ZNK20QDeferredDeleteEvent5cloneEv(
    const QDeferredDeleteEvent *self) {
  return self->QDeferredDeleteEvent::clone();
}

//  QDeferredDeleteEvent::QDeferredDeleteEvent(const QDeferredDeleteEvent
//      &a0)
extern "C" Q_DECL_EXPORT
QDeferredDeleteEvent *ritual_ZN20QDeferredDeleteEventC2ERKS_(
    const QDeferredDeleteEvent *a0) {
  return new QDeferredDeleteEvent(*a0);
}
