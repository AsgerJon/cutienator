//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 47, as _ZN22QQuickStateActionEventD2Ev
inline QQuickStateActionEvent::~QQuickStateActionEvent()
{
}
//  -----------------------------------------------------------------------

//  A QQuickAnchorChanges that Python can take functions over in. Every QQuickAnchorChanges
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAnchorChangesCall0)(const void *, int *);
typedef bool (*CuteQQuickAnchorChangesCall1)(const void *, int *);
typedef void (*CuteQQuickAnchorChangesCall2)(const void *, int *);
typedef int (*CuteQQuickAnchorChangesCall3)(const void *, int *);
typedef bool (*CuteQQuickAnchorChangesCall4)(const void *, QQuickStateActionEvent *, int *);
typedef bool (*CuteQQuickAnchorChangesCall5)(const void *, int *);
typedef void (*CuteQQuickAnchorChangesCall6)(const void *, int *);
typedef bool (*CuteQQuickAnchorChangesCall7)(const void *, int *);
typedef void (*CuteQQuickAnchorChangesCall8)(const void *, QQuickStateActionEvent *, int *);
typedef void (*CuteQQuickAnchorChangesCall9)(const void *, int *);
typedef void (*CuteQQuickAnchorChangesCall10)(const void *, int *);
typedef void (*CuteQQuickAnchorChangesCall11)(const void *, int *);
typedef void (*CuteQQuickAnchorChangesCall12)(const void *, int *);
typedef bool (*CuteQQuickAnchorChangesCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnchorChangesCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnchorChangesCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorChangesCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorChangesCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorChangesCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorChangesCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorChangesCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnchorChanges : public QQuickAnchorChanges {
public:
  using QQuickAnchorChanges::QQuickAnchorChanges;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent7executeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent12isReversableEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent7reverseEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickStateActionEvent4typeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent11mayOverrideEPS_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent15changesBindingsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13saveOriginalsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent9needsCopyEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13copyOriginalsEPS_")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13clearBindingsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent6rewindEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent17saveCurrentValuesEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent16saveTargetValuesEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent12isRewindableEv")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickAnchorChanges::execute()
  void execute() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall0 call = reinterpret_cast<CuteQQuickAnchorChangesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::execute();
  }

  //  bool QQuickAnchorChanges::isReversable()
  bool isReversable() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall1 call = reinterpret_cast<CuteQQuickAnchorChangesCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnchorChanges::isReversable();
  }

  //  void QQuickAnchorChanges::reverse()
  void reverse() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall2 call = reinterpret_cast<CuteQQuickAnchorChangesCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::reverse();
  }

  //  EventType QQuickAnchorChanges::type() const
  QQuickStateActionEvent::EventType type() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall3 call = reinterpret_cast<CuteQQuickAnchorChangesCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickStateActionEvent::EventType>(given);
    }
    return QQuickAnchorChanges::type();
  }

  //  bool QQuickAnchorChanges::mayOverride(QQuickStateActionEvent *other)
  bool mayOverride(QQuickStateActionEvent *other) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall4 call = reinterpret_cast<CuteQQuickAnchorChangesCall4>(taken[4]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QQuickAnchorChanges::mayOverride(other);
  }

  //  bool QQuickAnchorChanges::changesBindings()
  bool changesBindings() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall5 call = reinterpret_cast<CuteQQuickAnchorChangesCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnchorChanges::changesBindings();
  }

  //  void QQuickAnchorChanges::saveOriginals()
  void saveOriginals() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall6 call = reinterpret_cast<CuteQQuickAnchorChangesCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::saveOriginals();
  }

  //  bool QQuickAnchorChanges::needsCopy()
  bool needsCopy() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall7 call = reinterpret_cast<CuteQQuickAnchorChangesCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnchorChanges::needsCopy();
  }

  //  void QQuickAnchorChanges::copyOriginals(QQuickStateActionEvent *a0)
  void copyOriginals(QQuickStateActionEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall8 call = reinterpret_cast<CuteQQuickAnchorChangesCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::copyOriginals(a0);
  }

  //  void QQuickAnchorChanges::clearBindings()
  void clearBindings() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall9 call = reinterpret_cast<CuteQQuickAnchorChangesCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::clearBindings();
  }

  //  void QQuickAnchorChanges::rewind()
  void rewind() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall10 call = reinterpret_cast<CuteQQuickAnchorChangesCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::rewind();
  }

  //  void QQuickAnchorChanges::saveCurrentValues()
  void saveCurrentValues() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall11 call = reinterpret_cast<CuteQQuickAnchorChangesCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::saveCurrentValues();
  }

  //  void QQuickAnchorChanges::saveTargetValues()
  void saveTargetValues() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall12 call = reinterpret_cast<CuteQQuickAnchorChangesCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnchorChanges::saveTargetValues();
  }

  //  bool QQuickStateActionEvent::isRewindable()
  bool isRewindable() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall13 call = reinterpret_cast<CuteQQuickAnchorChangesCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::isRewindable();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall14 call = reinterpret_cast<CuteQQuickAnchorChangesCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall15 call = reinterpret_cast<CuteQQuickAnchorChangesCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall16 call = reinterpret_cast<CuteQQuickAnchorChangesCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall17 call = reinterpret_cast<CuteQQuickAnchorChangesCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall18 call = reinterpret_cast<CuteQQuickAnchorChangesCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall19 call = reinterpret_cast<CuteQQuickAnchorChangesCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickAnchorChangesCall20 call = reinterpret_cast<CuteQQuickAnchorChangesCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnchorChanges::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickAnchorChanges10metaObjectEv(
    const QQuickAnchorChanges *self) {
  return self->metaObject();
}

//  void *QQuickAnchorChanges::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickAnchorChanges11qt_metacastEPKc(
    QQuickAnchorChanges *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAnchorChanges::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickAnchorChanges11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAnchorChanges *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickAnchorChanges::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickAnchorChanges2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnchorChanges::tr(s, c, n));
}

//  QQuickAnchorChangesPrivate *QQuickAnchorChanges::d_func()
extern "C" Q_DECL_EXPORT
QQuickAnchorChangesPrivate *ritual_ZN19QQuickAnchorChanges6d_funcEv(
    QQuickAnchorChanges *self) {
  return self->d_func();
}

//  const QQuickAnchorChangesPrivate *QQuickAnchorChanges::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnchorChangesPrivate *ritual_ZNK19QQuickAnchorChanges6d_funcEv(
    const QQuickAnchorChanges *self) {
  return self->d_func();
}

//  QQuickAnchorChanges::QQuickAnchorChanges(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAnchorChanges *ritual_ZN19QQuickAnchorChangesC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickAnchorChanges(parent);
}

//  ActionList QQuickAnchorChanges::actions()
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_ZN19QQuickAnchorChanges7actionsEv(
    QQuickAnchorChanges *self) {
  return new QList<QQuickStateAction>(self->actions());
}

//  QQuickAnchorSet *QQuickAnchorChanges::anchors() const
extern "C" Q_DECL_EXPORT
QQuickAnchorSet *ritual_ZNK19QQuickAnchorChanges7anchorsEv(
    const QQuickAnchorChanges *self) {
  return self->anchors();
}

//  QQuickItem *QQuickAnchorChanges::object() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK19QQuickAnchorChanges6objectEv(
    const QQuickAnchorChanges *self) {
  return self->object();
}

//  void QQuickAnchorChanges::setObject(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges9setObjectEP10QQuickItem(
    QQuickAnchorChanges *self,
    QQuickItem *a0) {
  self->setObject(a0);
}

//  void QQuickAnchorChanges::execute()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges7executeEv(QQuickAnchorChanges *self) {
  self->execute();
}

//  bool QQuickAnchorChanges::isReversable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickAnchorChanges12isReversableEv(
    QQuickAnchorChanges *self) {
  return self->isReversable();
}

//  void QQuickAnchorChanges::reverse()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges7reverseEv(QQuickAnchorChanges *self) {
  self->reverse();
}

//  EventType QQuickAnchorChanges::type() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent::EventType ritual_ZNK19QQuickAnchorChanges4typeEv(
    const QQuickAnchorChanges *self) {
  return self->type();
}

//  bool QQuickAnchorChanges::mayOverride(QQuickStateActionEvent *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickAnchorChanges11mayOverrideEP22QQuickStateActionEvent(
    QQuickAnchorChanges *self,
    QQuickStateActionEvent *other) {
  return self->mayOverride(other);
}

//  bool QQuickAnchorChanges::changesBindings()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickAnchorChanges15changesBindingsEv(
    QQuickAnchorChanges *self) {
  return self->changesBindings();
}

//  void QQuickAnchorChanges::saveOriginals()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges13saveOriginalsEv(
    QQuickAnchorChanges *self) {
  self->saveOriginals();
}

//  bool QQuickAnchorChanges::needsCopy()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickAnchorChanges9needsCopyEv(QQuickAnchorChanges *self) {
  return self->needsCopy();
}

//  void QQuickAnchorChanges::copyOriginals(QQuickStateActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges13copyOriginalsEP22QQuickStateActionEvent(
    QQuickAnchorChanges *self,
    QQuickStateActionEvent *a0) {
  self->copyOriginals(a0);
}

//  void QQuickAnchorChanges::clearBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges13clearBindingsEv(
    QQuickAnchorChanges *self) {
  self->clearBindings();
}

//  void QQuickAnchorChanges::rewind()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges6rewindEv(QQuickAnchorChanges *self) {
  self->rewind();
}

//  void QQuickAnchorChanges::saveCurrentValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges17saveCurrentValuesEv(
    QQuickAnchorChanges *self) {
  self->saveCurrentValues();
}

//  QList<QQuickStateAction> QQuickAnchorChanges::additionalActions() const
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_ZNK19QQuickAnchorChanges17additionalActionsEv(
    const QQuickAnchorChanges *self) {
  return new QList<QQuickStateAction>(self->additionalActions());
}

//  void QQuickAnchorChanges::saveTargetValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickAnchorChanges16saveTargetValuesEv(
    QQuickAnchorChanges *self) {
  self->saveTargetValues();
}

//  QQuickAnchorChanges as the QQuickStateActionEvent it is built on
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent *ritual_cast_QQuickAnchorChanges_QQuickStateActionEvent(
    QQuickAnchorChanges *self) {
  return static_cast<QQuickStateActionEvent *>(self);
}

//  a Python function taken by a CuteQQuickAnchorChanges, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnchorChanges(
    QQuickAnchorChanges *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnchorChanges *>(self)->take(key, call);
}

//  void QQuickAnchorChanges::execute()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges7executeEv(
    QQuickAnchorChanges *self) {
  self->QQuickAnchorChanges::execute();
}

//  bool QQuickAnchorChanges::isReversable()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickAnchorChanges12isReversableEv(
    QQuickAnchorChanges *self) {
  return self->QQuickAnchorChanges::isReversable();
}

//  void QQuickAnchorChanges::reverse()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges7reverseEv(
    QQuickAnchorChanges *self) {
  self->QQuickAnchorChanges::reverse();
}

//  EventType QQuickAnchorChanges::type() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent::EventType ritual_own_ZNK19QQuickAnchorChanges4typeEv(
    const QQuickAnchorChanges *self) {
  return self->QQuickAnchorChanges::type();
}

//  bool QQuickAnchorChanges::mayOverride(QQuickStateActionEvent *other)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickAnchorChanges11mayOverrideEP22QQuickStateActionEvent(
    QQuickAnchorChanges *self,
    QQuickStateActionEvent *other) {
  return self->QQuickAnchorChanges::mayOverride(other);
}

//  bool QQuickAnchorChanges::changesBindings()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickAnchorChanges15changesBindingsEv(
    QQuickAnchorChanges *self) {
  return self->QQuickAnchorChanges::changesBindings();
}

//  void QQuickAnchorChanges::saveOriginals()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges13saveOriginalsEv(
    QQuickAnchorChanges *self) {
  self->QQuickAnchorChanges::saveOriginals();
}

//  bool QQuickAnchorChanges::needsCopy()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickAnchorChanges9needsCopyEv(
    QQuickAnchorChanges *self) {
  return self->QQuickAnchorChanges::needsCopy();
}

//  void QQuickAnchorChanges::copyOriginals(QQuickStateActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges13copyOriginalsEP22QQuickStateActionEvent(
    QQuickAnchorChanges *self,
    QQuickStateActionEvent *a0) {
  self->QQuickAnchorChanges::copyOriginals(a0);
}

//  void QQuickAnchorChanges::clearBindings()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges13clearBindingsEv(
    QQuickAnchorChanges *self) {
  self->QQuickAnchorChanges::clearBindings();
}

//  void QQuickAnchorChanges::rewind()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges6rewindEv(QQuickAnchorChanges *self) {
  self->QQuickAnchorChanges::rewind();
}

//  void QQuickAnchorChanges::saveCurrentValues()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges17saveCurrentValuesEv(
    QQuickAnchorChanges *self) {
  self->QQuickAnchorChanges::saveCurrentValues();
}

//  void QQuickAnchorChanges::saveTargetValues()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickAnchorChanges16saveTargetValuesEv(
    QQuickAnchorChanges *self) {
  self->QQuickAnchorChanges::saveTargetValues();
}
