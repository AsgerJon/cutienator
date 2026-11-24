//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickstate_p_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQuick/private/qquickstategroup_p.h>
#include <QtQuick/private/qquickstatechangescript_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 51, as _ZN22QQuickStateActionEvent7executeEv
inline void QQuickStateActionEvent::execute()
{
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 55, as _ZN22QQuickStateActionEvent12isReversableEv
inline bool QQuickStateActionEvent::isReversable()
{
    return false;
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 60, as _ZN22QQuickStateActionEvent7reverseEv
inline void QQuickStateActionEvent::reverse()
{
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 64, as _ZN22QQuickStateActionEvent15changesBindingsEv
inline bool QQuickStateActionEvent::changesBindings()
{
    return false;
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 69, as _ZN22QQuickStateActionEvent13clearBindingsEv
inline void QQuickStateActionEvent::clearBindings()
{
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 73, as _ZN22QQuickStateActionEvent11mayOverrideEPS_
inline bool QQuickStateActionEvent::mayOverride(QQuickStateActionEvent *other)
{
    Q_UNUSED(other);
    return false;
}
//  -----------------------------------------------------------------------

//  A QQuickStateActionEvent that Python can take functions over in. Every QQuickStateActionEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickStateActionEventCall0)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall1)(const void *, int *);
typedef bool (*CuteQQuickStateActionEventCall2)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall3)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall4)(const void *, int *);
typedef bool (*CuteQQuickStateActionEventCall5)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall6)(const void *, QQuickStateActionEvent *, int *);
typedef bool (*CuteQQuickStateActionEventCall7)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall8)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall9)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall10)(const void *, int *);
typedef bool (*CuteQQuickStateActionEventCall11)(const void *, int *);
typedef void (*CuteQQuickStateActionEventCall12)(const void *, int *);
typedef bool (*CuteQQuickStateActionEventCall13)(const void *, QQuickStateActionEvent *, int *);
class CuteQQuickStateActionEvent : public QQuickStateActionEvent {
public:
  using QQuickStateActionEvent::QQuickStateActionEvent;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK22QQuickStateActionEvent4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent7executeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent12isReversableEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent7reverseEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13saveOriginalsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent9needsCopyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13copyOriginalsEPS_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent12isRewindableEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent6rewindEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent17saveCurrentValuesEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent16saveTargetValuesEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent15changesBindingsEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13clearBindingsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent11mayOverrideEPS_")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

  //  EventType QQuickStateActionEvent::type() const
  QQuickStateActionEvent::EventType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStateActionEventCall0 call = reinterpret_cast<CuteQQuickStateActionEventCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickStateActionEvent::EventType>(given);
    }
    return {};
  }

  //  void QQuickStateActionEvent::execute()
  void execute() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStateActionEventCall1 call = reinterpret_cast<CuteQQuickStateActionEventCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::execute();
  }

  //  bool QQuickStateActionEvent::isReversable()
  bool isReversable() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStateActionEventCall2 call = reinterpret_cast<CuteQQuickStateActionEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::isReversable();
  }

  //  void QQuickStateActionEvent::reverse()
  void reverse() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStateActionEventCall3 call = reinterpret_cast<CuteQQuickStateActionEventCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::reverse();
  }

  //  void QQuickStateActionEvent::saveOriginals()
  void saveOriginals() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickStateActionEventCall4 call = reinterpret_cast<CuteQQuickStateActionEventCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::saveOriginals();
  }

  //  bool QQuickStateActionEvent::needsCopy()
  bool needsCopy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickStateActionEventCall5 call = reinterpret_cast<CuteQQuickStateActionEventCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::needsCopy();
  }

  //  void QQuickStateActionEvent::copyOriginals(QQuickStateActionEvent
  //      *a0)
  void copyOriginals(QQuickStateActionEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickStateActionEventCall6 call = reinterpret_cast<CuteQQuickStateActionEventCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::copyOriginals(a0);
  }

  //  bool QQuickStateActionEvent::isRewindable()
  bool isRewindable() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickStateActionEventCall7 call = reinterpret_cast<CuteQQuickStateActionEventCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::isRewindable();
  }

  //  void QQuickStateActionEvent::rewind()
  void rewind() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickStateActionEventCall8 call = reinterpret_cast<CuteQQuickStateActionEventCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::rewind();
  }

  //  void QQuickStateActionEvent::saveCurrentValues()
  void saveCurrentValues() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickStateActionEventCall9 call = reinterpret_cast<CuteQQuickStateActionEventCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::saveCurrentValues();
  }

  //  void QQuickStateActionEvent::saveTargetValues()
  void saveTargetValues() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickStateActionEventCall10 call = reinterpret_cast<CuteQQuickStateActionEventCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::saveTargetValues();
  }

  //  bool QQuickStateActionEvent::changesBindings()
  bool changesBindings() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickStateActionEventCall11 call = reinterpret_cast<CuteQQuickStateActionEventCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::changesBindings();
  }

  //  void QQuickStateActionEvent::clearBindings()
  void clearBindings() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickStateActionEventCall12 call = reinterpret_cast<CuteQQuickStateActionEventCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::clearBindings();
  }

  //  bool QQuickStateActionEvent::mayOverride(QQuickStateActionEvent
  //      *other)
  bool mayOverride(QQuickStateActionEvent *other) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickStateActionEventCall13 call = reinterpret_cast<CuteQQuickStateActionEventCall13>(taken[13]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::mayOverride(other);
  }
};

//  QQuickStateActionEvent::~QQuickStateActionEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEventD1Ev(QQuickStateActionEvent *self) {
  delete self;
}

//  EventType QQuickStateActionEvent::type() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent::EventType ritual_ZNK22QQuickStateActionEvent4typeEv(
    const QQuickStateActionEvent *self) {
  return self->type();
}

//  void QQuickStateActionEvent::execute()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent7executeEv(
    QQuickStateActionEvent *self) {
  self->execute();
}

//  bool QQuickStateActionEvent::isReversable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickStateActionEvent12isReversableEv(
    QQuickStateActionEvent *self) {
  return self->isReversable();
}

//  void QQuickStateActionEvent::reverse()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent7reverseEv(
    QQuickStateActionEvent *self) {
  self->reverse();
}

//  void QQuickStateActionEvent::saveOriginals()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent13saveOriginalsEv(
    QQuickStateActionEvent *self) {
  self->saveOriginals();
}

//  bool QQuickStateActionEvent::needsCopy()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickStateActionEvent9needsCopyEv(
    QQuickStateActionEvent *self) {
  return self->needsCopy();
}

//  void QQuickStateActionEvent::copyOriginals(QQuickStateActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent13copyOriginalsEPS_(
    QQuickStateActionEvent *self,
    QQuickStateActionEvent *a0) {
  self->copyOriginals(a0);
}

//  bool QQuickStateActionEvent::isRewindable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickStateActionEvent12isRewindableEv(
    QQuickStateActionEvent *self) {
  return self->isRewindable();
}

//  void QQuickStateActionEvent::rewind()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent6rewindEv(
    QQuickStateActionEvent *self) {
  self->rewind();
}

//  void QQuickStateActionEvent::saveCurrentValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent17saveCurrentValuesEv(
    QQuickStateActionEvent *self) {
  self->saveCurrentValues();
}

//  void QQuickStateActionEvent::saveTargetValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent16saveTargetValuesEv(
    QQuickStateActionEvent *self) {
  self->saveTargetValues();
}

//  bool QQuickStateActionEvent::changesBindings()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickStateActionEvent15changesBindingsEv(
    QQuickStateActionEvent *self) {
  return self->changesBindings();
}

//  void QQuickStateActionEvent::clearBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStateActionEvent13clearBindingsEv(
    QQuickStateActionEvent *self) {
  self->clearBindings();
}

//  bool QQuickStateActionEvent::mayOverride(QQuickStateActionEvent *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickStateActionEvent11mayOverrideEPS_(
    QQuickStateActionEvent *self,
    QQuickStateActionEvent *other) {
  return self->mayOverride(other);
}

//  a Python function taken by a CuteQQuickStateActionEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStateActionEvent(
    QQuickStateActionEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStateActionEvent *>(self)->take(key, call);
}

//  void QQuickStateActionEvent::execute()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent7executeEv(
    QQuickStateActionEvent *self) {
  self->QQuickStateActionEvent::execute();
}

//  bool QQuickStateActionEvent::isReversable()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickStateActionEvent12isReversableEv(
    QQuickStateActionEvent *self) {
  return self->QQuickStateActionEvent::isReversable();
}

//  void QQuickStateActionEvent::reverse()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent7reverseEv(
    QQuickStateActionEvent *self) {
  self->QQuickStateActionEvent::reverse();
}

//  void QQuickStateActionEvent::saveOriginals()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent13saveOriginalsEv(
    QQuickStateActionEvent *self) {
  self->QQuickStateActionEvent::saveOriginals();
}

//  bool QQuickStateActionEvent::needsCopy()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickStateActionEvent9needsCopyEv(
    QQuickStateActionEvent *self) {
  return self->QQuickStateActionEvent::needsCopy();
}

//  void QQuickStateActionEvent::copyOriginals(QQuickStateActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent13copyOriginalsEPS_(
    QQuickStateActionEvent *self,
    QQuickStateActionEvent *a0) {
  self->QQuickStateActionEvent::copyOriginals(a0);
}

//  bool QQuickStateActionEvent::isRewindable()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickStateActionEvent12isRewindableEv(
    QQuickStateActionEvent *self) {
  return self->QQuickStateActionEvent::isRewindable();
}

//  void QQuickStateActionEvent::rewind()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent6rewindEv(
    QQuickStateActionEvent *self) {
  self->QQuickStateActionEvent::rewind();
}

//  void QQuickStateActionEvent::saveCurrentValues()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent17saveCurrentValuesEv(
    QQuickStateActionEvent *self) {
  self->QQuickStateActionEvent::saveCurrentValues();
}

//  void QQuickStateActionEvent::saveTargetValues()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent16saveTargetValuesEv(
    QQuickStateActionEvent *self) {
  self->QQuickStateActionEvent::saveTargetValues();
}

//  bool QQuickStateActionEvent::changesBindings()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickStateActionEvent15changesBindingsEv(
    QQuickStateActionEvent *self) {
  return self->QQuickStateActionEvent::changesBindings();
}

//  void QQuickStateActionEvent::clearBindings()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickStateActionEvent13clearBindingsEv(
    QQuickStateActionEvent *self) {
  self->QQuickStateActionEvent::clearBindings();
}

//  bool QQuickStateActionEvent::mayOverride(QQuickStateActionEvent *other)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickStateActionEvent11mayOverrideEPS_(
    QQuickStateActionEvent *self,
    QQuickStateActionEvent *other) {
  return self->QQuickStateActionEvent::mayOverride(other);
}
