//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstatechangescript_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstatechangescript_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qqmlscriptstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickstate_p_p.h"
#include "qquickstate_p.h"
#include "qquickstategroup_p.h"
#include "qquickstatechangescript_p.h"
#include <private/qqmlglobal_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 73, as _ZN22QQuickStateActionEvent11mayOverrideEPS_
inline bool QQuickStateActionEvent::mayOverride(QQuickStateActionEvent *other)
{
    Q_UNUSED(other);
    return false;
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 55, as _ZN22QQuickStateActionEvent12isReversableEv
inline bool QQuickStateActionEvent::isReversable()
{
    return false;
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 69, as _ZN22QQuickStateActionEvent13clearBindingsEv
inline void QQuickStateActionEvent::clearBindings()
{
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 64, as _ZN22QQuickStateActionEvent15changesBindingsEv
inline bool QQuickStateActionEvent::changesBindings()
{
    return false;
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 60, as _ZN22QQuickStateActionEvent7reverseEv
inline void QQuickStateActionEvent::reverse()
{
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 47, as _ZN22QQuickStateActionEventD2Ev
inline QQuickStateActionEvent::~QQuickStateActionEvent()
{
}
//  -----------------------------------------------------------------------

//  A QQuickStateChangeScript that Python can take functions over in. Every QQuickStateChangeScript
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickStateChangeScriptCall0)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall1)(const void *, int *);
typedef bool (*CuteQQuickStateChangeScriptCall2)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall3)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall4)(const void *, int *);
typedef bool (*CuteQQuickStateChangeScriptCall5)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall6)(const void *, QQuickStateActionEvent *, int *);
typedef bool (*CuteQQuickStateChangeScriptCall7)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall8)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall9)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall10)(const void *, int *);
typedef bool (*CuteQQuickStateChangeScriptCall11)(const void *, int *);
typedef void (*CuteQQuickStateChangeScriptCall12)(const void *, int *);
typedef bool (*CuteQQuickStateChangeScriptCall13)(const void *, QQuickStateActionEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStateChangeScriptCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStateChangeScriptCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateChangeScriptCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateChangeScriptCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateChangeScriptCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateChangeScriptCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateChangeScriptCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickStateChangeScript : public QQuickStateChangeScript {
public:
  using QQuickStateChangeScript::QQuickStateChangeScript;
  void *taken[21] = {};

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

  //  EventType QQuickStateChangeScript::type() const
  QQuickStateActionEvent::EventType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall0 call = reinterpret_cast<CuteQQuickStateChangeScriptCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickStateActionEvent::EventType>(given);
    }
    return QQuickStateChangeScript::type();
  }

  //  void QQuickStateChangeScript::execute()
  void execute() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall1 call = reinterpret_cast<CuteQQuickStateChangeScriptCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateChangeScript::execute();
  }

  //  bool QQuickStateActionEvent::isReversable()
  bool isReversable() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall2 call = reinterpret_cast<CuteQQuickStateChangeScriptCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::isReversable();
  }

  //  void QQuickStateActionEvent::reverse()
  void reverse() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall3 call = reinterpret_cast<CuteQQuickStateChangeScriptCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::reverse();
  }

  //  void QQuickStateActionEvent::saveOriginals()
  void saveOriginals() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall4 call = reinterpret_cast<CuteQQuickStateChangeScriptCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::saveOriginals();
  }

  //  bool QQuickStateActionEvent::needsCopy()
  bool needsCopy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall5 call = reinterpret_cast<CuteQQuickStateChangeScriptCall5>(taken[5]);
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
      CuteQQuickStateChangeScriptCall6 call = reinterpret_cast<CuteQQuickStateChangeScriptCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::copyOriginals(a0);
  }

  //  bool QQuickStateActionEvent::isRewindable()
  bool isRewindable() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall7 call = reinterpret_cast<CuteQQuickStateChangeScriptCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::isRewindable();
  }

  //  void QQuickStateActionEvent::rewind()
  void rewind() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall8 call = reinterpret_cast<CuteQQuickStateChangeScriptCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::rewind();
  }

  //  void QQuickStateActionEvent::saveCurrentValues()
  void saveCurrentValues() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall9 call = reinterpret_cast<CuteQQuickStateChangeScriptCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::saveCurrentValues();
  }

  //  void QQuickStateActionEvent::saveTargetValues()
  void saveTargetValues() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall10 call = reinterpret_cast<CuteQQuickStateChangeScriptCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::saveTargetValues();
  }

  //  bool QQuickStateActionEvent::changesBindings()
  bool changesBindings() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall11 call = reinterpret_cast<CuteQQuickStateChangeScriptCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::changesBindings();
  }

  //  void QQuickStateActionEvent::clearBindings()
  void clearBindings() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall12 call = reinterpret_cast<CuteQQuickStateChangeScriptCall12>(taken[12]);
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
      CuteQQuickStateChangeScriptCall13 call = reinterpret_cast<CuteQQuickStateChangeScriptCall13>(taken[13]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::mayOverride(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickStateChangeScriptCall14 call = reinterpret_cast<CuteQQuickStateChangeScriptCall14>(taken[14]);
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
      CuteQQuickStateChangeScriptCall15 call = reinterpret_cast<CuteQQuickStateChangeScriptCall15>(taken[15]);
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
      CuteQQuickStateChangeScriptCall16 call = reinterpret_cast<CuteQQuickStateChangeScriptCall16>(taken[16]);
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
      CuteQQuickStateChangeScriptCall17 call = reinterpret_cast<CuteQQuickStateChangeScriptCall17>(taken[17]);
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
      CuteQQuickStateChangeScriptCall18 call = reinterpret_cast<CuteQQuickStateChangeScriptCall18>(taken[18]);
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
      CuteQQuickStateChangeScriptCall19 call = reinterpret_cast<CuteQQuickStateChangeScriptCall19>(taken[19]);
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
      CuteQQuickStateChangeScriptCall20 call = reinterpret_cast<CuteQQuickStateChangeScriptCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickStateChangeScript::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickStateChangeScript10metaObjectEv(
    const QQuickStateChangeScript *self) {
  return self->metaObject();
}

//  QString QQuickStateChangeScript::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickStateChangeScript2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStateChangeScript::tr(s, c, n));
}

//  QQuickStateChangeScript::QQuickStateChangeScript(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickStateChangeScript *ritual_ZN23QQuickStateChangeScriptC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickStateChangeScript(parent);
}

//  ActionList QQuickStateChangeScript::actions()
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_ZN23QQuickStateChangeScript7actionsEv(
    QQuickStateChangeScript *self) {
  return new QList<QQuickStateAction>(self->actions());
}

//  EventType QQuickStateChangeScript::type() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent::EventType ritual_ZNK23QQuickStateChangeScript4typeEv(
    const QQuickStateChangeScript *self) {
  return self->type();
}

//  QQmlScriptString QQuickStateChangeScript::script() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK23QQuickStateChangeScript6scriptEv(
    const QQuickStateChangeScript *self) {
  return new QQmlScriptString(self->script());
}

//  void QQuickStateChangeScript::setScript(const QQmlScriptString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStateChangeScript9setScriptERK16QQmlScriptString(
    QQuickStateChangeScript *self,
    const QQmlScriptString *a0) {
  self->setScript(*a0);
}

//  QString QQuickStateChangeScript::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickStateChangeScript4nameEv(
    const QQuickStateChangeScript *self) {
  return new QString(self->name());
}

//  void QQuickStateChangeScript::setName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStateChangeScript7setNameERK7QString(
    QQuickStateChangeScript *self,
    const QString *a0) {
  self->setName(*a0);
}

//  void QQuickStateChangeScript::execute()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStateChangeScript7executeEv(
    QQuickStateChangeScript *self) {
  self->execute();
}

//  QQuickStateChangeScript as the QQuickStateActionEvent it is built on
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent *ritual_cast_QQuickStateChangeScript_QQuickStateActionEvent(
    QQuickStateChangeScript *self) {
  return static_cast<QQuickStateActionEvent *>(self);
}

//  a Python function taken by a CuteQQuickStateChangeScript, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStateChangeScript(
    QQuickStateChangeScript *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStateChangeScript *>(self)->take(key, call);
}

//  EventType QQuickStateChangeScript::type() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent::EventType ritual_own_ZNK23QQuickStateChangeScript4typeEv(
    const QQuickStateChangeScript *self) {
  return self->QQuickStateChangeScript::type();
}

//  void QQuickStateChangeScript::execute()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickStateChangeScript7executeEv(
    QQuickStateChangeScript *self) {
  self->QQuickStateChangeScript::execute();
}
