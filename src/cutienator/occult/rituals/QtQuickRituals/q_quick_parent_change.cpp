//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlscriptstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 69, as _ZN22QQuickStateActionEvent13clearBindingsEv
inline void QQuickStateActionEvent::clearBindings()
{
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 64, as _ZN22QQuickStateActionEvent15changesBindingsEv
inline bool QQuickStateActionEvent::changesBindings()
{
    return false;
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 47, as _ZN22QQuickStateActionEventD2Ev
inline QQuickStateActionEvent::~QQuickStateActionEvent()
{
}
//  -----------------------------------------------------------------------

//  A QQuickParentChange that Python can take functions over in. Every QQuickParentChange
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickParentChangeCall0)(const void *, int *);
typedef void (*CuteQQuickParentChangeCall1)(const void *, int *);
typedef bool (*CuteQQuickParentChangeCall2)(const void *, int *);
typedef void (*CuteQQuickParentChangeCall3)(const void *, int *);
typedef int (*CuteQQuickParentChangeCall4)(const void *, int *);
typedef bool (*CuteQQuickParentChangeCall5)(const void *, QQuickStateActionEvent *, int *);
typedef void (*CuteQQuickParentChangeCall6)(const void *, int *);
typedef void (*CuteQQuickParentChangeCall7)(const void *, int *);
typedef bool (*CuteQQuickParentChangeCall8)(const void *, int *);
typedef void (*CuteQQuickParentChangeCall9)(const void *, QQuickStateActionEvent *, int *);
typedef bool (*CuteQQuickParentChangeCall10)(const void *, int *);
typedef void (*CuteQQuickParentChangeCall11)(const void *, int *);
typedef bool (*CuteQQuickParentChangeCall12)(const void *, int *);
typedef void (*CuteQQuickParentChangeCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParentChangeCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParentChangeCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentChangeCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentChangeCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentChangeCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentChangeCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParentChangeCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickParentChange : public QQuickParentChange {
public:
  using QQuickParentChange::QQuickParentChange;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13saveOriginalsEv")) {
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
    if (!std::strcmp(key, "_ZNK22QQuickStateActionEvent4typeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent11mayOverrideEPS_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent6rewindEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent17saveCurrentValuesEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent9needsCopyEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13copyOriginalsEPS_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent12isRewindableEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent16saveTargetValuesEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent15changesBindingsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickStateActionEvent13clearBindingsEv")) {
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

  //  void QQuickParentChange::saveOriginals()
  void saveOriginals() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParentChangeCall0 call = reinterpret_cast<CuteQQuickParentChangeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParentChange::saveOriginals();
  }

  //  void QQuickParentChange::execute()
  void execute() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParentChangeCall1 call = reinterpret_cast<CuteQQuickParentChangeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParentChange::execute();
  }

  //  bool QQuickParentChange::isReversable()
  bool isReversable() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParentChangeCall2 call = reinterpret_cast<CuteQQuickParentChangeCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickParentChange::isReversable();
  }

  //  void QQuickParentChange::reverse()
  void reverse() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParentChangeCall3 call = reinterpret_cast<CuteQQuickParentChangeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParentChange::reverse();
  }

  //  EventType QQuickParentChange::type() const
  QQuickStateActionEvent::EventType type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickParentChangeCall4 call = reinterpret_cast<CuteQQuickParentChangeCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickStateActionEvent::EventType>(given);
    }
    return QQuickParentChange::type();
  }

  //  bool QQuickParentChange::mayOverride(QQuickStateActionEvent *other)
  bool mayOverride(QQuickStateActionEvent *other) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickParentChangeCall5 call = reinterpret_cast<CuteQQuickParentChangeCall5>(taken[5]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QQuickParentChange::mayOverride(other);
  }

  //  void QQuickParentChange::rewind()
  void rewind() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickParentChangeCall6 call = reinterpret_cast<CuteQQuickParentChangeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParentChange::rewind();
  }

  //  void QQuickParentChange::saveCurrentValues()
  void saveCurrentValues() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickParentChangeCall7 call = reinterpret_cast<CuteQQuickParentChangeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParentChange::saveCurrentValues();
  }

  //  bool QQuickStateActionEvent::needsCopy()
  bool needsCopy() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickParentChangeCall8 call = reinterpret_cast<CuteQQuickParentChangeCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::needsCopy();
  }

  //  void QQuickStateActionEvent::copyOriginals(QQuickStateActionEvent
  //      *a0)
  void copyOriginals(QQuickStateActionEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickParentChangeCall9 call = reinterpret_cast<CuteQQuickParentChangeCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::copyOriginals(a0);
  }

  //  bool QQuickStateActionEvent::isRewindable()
  bool isRewindable() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickParentChangeCall10 call = reinterpret_cast<CuteQQuickParentChangeCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::isRewindable();
  }

  //  void QQuickStateActionEvent::saveTargetValues()
  void saveTargetValues() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickParentChangeCall11 call = reinterpret_cast<CuteQQuickParentChangeCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::saveTargetValues();
  }

  //  bool QQuickStateActionEvent::changesBindings()
  bool changesBindings() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickParentChangeCall12 call = reinterpret_cast<CuteQQuickParentChangeCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickStateActionEvent::changesBindings();
  }

  //  void QQuickStateActionEvent::clearBindings()
  void clearBindings() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickParentChangeCall13 call = reinterpret_cast<CuteQQuickParentChangeCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStateActionEvent::clearBindings();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickParentChangeCall14 call = reinterpret_cast<CuteQQuickParentChangeCall14>(taken[14]);
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
      CuteQQuickParentChangeCall15 call = reinterpret_cast<CuteQQuickParentChangeCall15>(taken[15]);
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
      CuteQQuickParentChangeCall16 call = reinterpret_cast<CuteQQuickParentChangeCall16>(taken[16]);
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
      CuteQQuickParentChangeCall17 call = reinterpret_cast<CuteQQuickParentChangeCall17>(taken[17]);
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
      CuteQQuickParentChangeCall18 call = reinterpret_cast<CuteQQuickParentChangeCall18>(taken[18]);
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
      CuteQQuickParentChangeCall19 call = reinterpret_cast<CuteQQuickParentChangeCall19>(taken[19]);
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
      CuteQQuickParentChangeCall20 call = reinterpret_cast<CuteQQuickParentChangeCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickParentChange::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickParentChange10metaObjectEv(
    const QQuickParentChange *self) {
  return self->metaObject();
}

//  QString QQuickParentChange::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickParentChange2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParentChange::tr(s, c, n));
}

//  QQuickParentChange::QQuickParentChange(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickParentChange *ritual_ZN18QQuickParentChangeC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickParentChange(parent);
}

//  QQuickItem *QQuickParentChange::object() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK18QQuickParentChange6objectEv(
    const QQuickParentChange *self) {
  return self->object();
}

//  void QQuickParentChange::setObject(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange9setObjectEP10QQuickItem(
    QQuickParentChange *self,
    QQuickItem *a0) {
  self->setObject(a0);
}

//  QQuickItem *QQuickParentChange::parent() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK18QQuickParentChange6parentEv(
    const QQuickParentChange *self) {
  return self->parent();
}

//  void QQuickParentChange::setParent(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange9setParentEP10QQuickItem(
    QQuickParentChange *self,
    QQuickItem *a0) {
  self->setParent(a0);
}

//  QQuickItem *QQuickParentChange::originalParent() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK18QQuickParentChange14originalParentEv(
    const QQuickParentChange *self) {
  return self->originalParent();
}

//  QQmlScriptString QQuickParentChange::x() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK18QQuickParentChange1xEv(
    const QQuickParentChange *self) {
  return new QQmlScriptString(self->x());
}

//  void QQuickParentChange::setX(const QQmlScriptString &x)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange4setXERK16QQmlScriptString(
    QQuickParentChange *self,
    const QQmlScriptString *x) {
  self->setX(*x);
}

//  bool QQuickParentChange::xIsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickParentChange6xIsSetEv(
    const QQuickParentChange *self) {
  return self->xIsSet();
}

//  QQmlScriptString QQuickParentChange::y() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK18QQuickParentChange1yEv(
    const QQuickParentChange *self) {
  return new QQmlScriptString(self->y());
}

//  void QQuickParentChange::setY(const QQmlScriptString &y)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange4setYERK16QQmlScriptString(
    QQuickParentChange *self,
    const QQmlScriptString *y) {
  self->setY(*y);
}

//  bool QQuickParentChange::yIsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickParentChange6yIsSetEv(
    const QQuickParentChange *self) {
  return self->yIsSet();
}

//  QQmlScriptString QQuickParentChange::width() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK18QQuickParentChange5widthEv(
    const QQuickParentChange *self) {
  return new QQmlScriptString(self->width());
}

//  void QQuickParentChange::setWidth(const QQmlScriptString &width)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange8setWidthERK16QQmlScriptString(
    QQuickParentChange *self,
    const QQmlScriptString *width) {
  self->setWidth(*width);
}

//  bool QQuickParentChange::widthIsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickParentChange10widthIsSetEv(
    const QQuickParentChange *self) {
  return self->widthIsSet();
}

//  QQmlScriptString QQuickParentChange::height() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK18QQuickParentChange6heightEv(
    const QQuickParentChange *self) {
  return new QQmlScriptString(self->height());
}

//  void QQuickParentChange::setHeight(const QQmlScriptString &height)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange9setHeightERK16QQmlScriptString(
    QQuickParentChange *self,
    const QQmlScriptString *height) {
  self->setHeight(*height);
}

//  bool QQuickParentChange::heightIsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickParentChange11heightIsSetEv(
    const QQuickParentChange *self) {
  return self->heightIsSet();
}

//  QQmlScriptString QQuickParentChange::scale() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK18QQuickParentChange5scaleEv(
    const QQuickParentChange *self) {
  return new QQmlScriptString(self->scale());
}

//  void QQuickParentChange::setScale(const QQmlScriptString &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange8setScaleERK16QQmlScriptString(
    QQuickParentChange *self,
    const QQmlScriptString *scale) {
  self->setScale(*scale);
}

//  bool QQuickParentChange::scaleIsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickParentChange10scaleIsSetEv(
    const QQuickParentChange *self) {
  return self->scaleIsSet();
}

//  QQmlScriptString QQuickParentChange::rotation() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK18QQuickParentChange8rotationEv(
    const QQuickParentChange *self) {
  return new QQmlScriptString(self->rotation());
}

//  void QQuickParentChange::setRotation(const QQmlScriptString &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange11setRotationERK16QQmlScriptString(
    QQuickParentChange *self,
    const QQmlScriptString *rotation) {
  self->setRotation(*rotation);
}

//  bool QQuickParentChange::rotationIsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickParentChange13rotationIsSetEv(
    const QQuickParentChange *self) {
  return self->rotationIsSet();
}

//  ActionList QQuickParentChange::actions()
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_ZN18QQuickParentChange7actionsEv(
    QQuickParentChange *self) {
  return new QList<QQuickStateAction>(self->actions());
}

//  void QQuickParentChange::saveOriginals()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange13saveOriginalsEv(
    QQuickParentChange *self) {
  self->saveOriginals();
}

//  void QQuickParentChange::execute()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange7executeEv(QQuickParentChange *self) {
  self->execute();
}

//  bool QQuickParentChange::isReversable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickParentChange12isReversableEv(
    QQuickParentChange *self) {
  return self->isReversable();
}

//  void QQuickParentChange::reverse()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange7reverseEv(QQuickParentChange *self) {
  self->reverse();
}

//  EventType QQuickParentChange::type() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent::EventType ritual_ZNK18QQuickParentChange4typeEv(
    const QQuickParentChange *self) {
  return self->type();
}

//  bool QQuickParentChange::mayOverride(QQuickStateActionEvent *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickParentChange11mayOverrideEP22QQuickStateActionEvent(
    QQuickParentChange *self,
    QQuickStateActionEvent *other) {
  return self->mayOverride(other);
}

//  void QQuickParentChange::rewind()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange6rewindEv(QQuickParentChange *self) {
  self->rewind();
}

//  void QQuickParentChange::saveCurrentValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickParentChange17saveCurrentValuesEv(
    QQuickParentChange *self) {
  self->saveCurrentValues();
}

//  QQuickParentChange as the QQuickStateActionEvent it is built on
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent *ritual_cast_QQuickParentChange_QQuickStateActionEvent(
    QQuickParentChange *self) {
  return static_cast<QQuickStateActionEvent *>(self);
}

//  a Python function taken by a CuteQQuickParentChange, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParentChange(
    QQuickParentChange *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParentChange *>(self)->take(key, call);
}

//  void QQuickParentChange::saveOriginals()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickParentChange13saveOriginalsEv(
    QQuickParentChange *self) {
  self->QQuickParentChange::saveOriginals();
}

//  void QQuickParentChange::execute()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickParentChange7executeEv(QQuickParentChange *self) {
  self->QQuickParentChange::execute();
}

//  bool QQuickParentChange::isReversable()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickParentChange12isReversableEv(
    QQuickParentChange *self) {
  return self->QQuickParentChange::isReversable();
}

//  void QQuickParentChange::reverse()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickParentChange7reverseEv(QQuickParentChange *self) {
  self->QQuickParentChange::reverse();
}

//  EventType QQuickParentChange::type() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent::EventType ritual_own_ZNK18QQuickParentChange4typeEv(
    const QQuickParentChange *self) {
  return self->QQuickParentChange::type();
}

//  bool QQuickParentChange::mayOverride(QQuickStateActionEvent *other)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickParentChange11mayOverrideEP22QQuickStateActionEvent(
    QQuickParentChange *self,
    QQuickStateActionEvent *other) {
  return self->QQuickParentChange::mayOverride(other);
}

//  void QQuickParentChange::rewind()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickParentChange6rewindEv(QQuickParentChange *self) {
  self->QQuickParentChange::rewind();
}

//  void QQuickParentChange::saveCurrentValues()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickParentChange17saveCurrentValuesEv(
    QQuickParentChange *self) {
  self->QQuickParentChange::saveCurrentValues();
}
