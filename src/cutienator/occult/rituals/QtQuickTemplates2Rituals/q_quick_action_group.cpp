//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickactiongroup_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickactiongroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickActionGroup that Python can take functions over in. Every QQuickActionGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickActionGroupCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickActionGroupCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionGroupCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionGroupCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionGroupCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionGroupCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickActionGroupCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickActionGroup : public QQuickActionGroup {
public:
  using QQuickActionGroup::QQuickActionGroup;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickActionGroupCall0 call = reinterpret_cast<CuteQQuickActionGroupCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickActionGroupCall1 call = reinterpret_cast<CuteQQuickActionGroupCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickActionGroupCall2 call = reinterpret_cast<CuteQQuickActionGroupCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickActionGroupCall3 call = reinterpret_cast<CuteQQuickActionGroupCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickActionGroupCall4 call = reinterpret_cast<CuteQQuickActionGroupCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickActionGroupCall5 call = reinterpret_cast<CuteQQuickActionGroupCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickActionGroupCall6 call = reinterpret_cast<CuteQQuickActionGroupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickActionGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickActionGroup10metaObjectEv(
    const QQuickActionGroup *self) {
  return self->metaObject();
}

//  QString QQuickActionGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickActionGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickActionGroup::tr(s, c, n));
}

//  void QQuickActionGroup::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickActionGroup21qt_qmlMarker_attachedEv(
    QQuickActionGroup *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickActionGroup::QQuickActionGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickActionGroup *ritual_ZN17QQuickActionGroupC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickActionGroup(parent);
}

//  QQuickActionGroup::~QQuickActionGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickActionGroupD1Ev(QQuickActionGroup *self) {
  delete self;
}

//  QQuickActionGroupAttached
//      *QQuickActionGroup::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickActionGroupAttached *ritual_ZN17QQuickActionGroup21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickActionGroup::qmlAttachedProperties(object);
}

//  QQuickAction *QQuickActionGroup::checkedAction() const
extern "C" Q_DECL_EXPORT
QQuickAction *ritual_ZNK17QQuickActionGroup13checkedActionEv(
    const QQuickActionGroup *self) {
  return self->checkedAction();
}

//  void QQuickActionGroup::setCheckedAction(QQuickAction *checkedAction)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickActionGroup16setCheckedActionEP12QQuickAction(
    QQuickActionGroup *self,
    QQuickAction *checkedAction) {
  self->setCheckedAction(checkedAction);
}

//  bool QQuickActionGroup::isExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickActionGroup11isExclusiveEv(
    const QQuickActionGroup *self) {
  return self->isExclusive();
}

//  void QQuickActionGroup::setExclusive(bool exclusive)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickActionGroup12setExclusiveEb(
    QQuickActionGroup *self,
    bool exclusive) {
  self->setExclusive(exclusive);
}

//  bool QQuickActionGroup::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickActionGroup9isEnabledEv(
    const QQuickActionGroup *self) {
  return self->isEnabled();
}

//  void QQuickActionGroup::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickActionGroup10setEnabledEb(
    QQuickActionGroup *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QQuickActionGroup::addAction(QQuickAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickActionGroup9addActionEP12QQuickAction(
    QQuickActionGroup *self,
    QQuickAction *action) {
  self->addAction(action);
}

//  void QQuickActionGroup::removeAction(QQuickAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickActionGroup12removeActionEP12QQuickAction(
    QQuickActionGroup *self,
    QQuickAction *action) {
  self->removeAction(action);
}

//  a Python function taken by a CuteQQuickActionGroup, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickActionGroup(
    QQuickActionGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickActionGroup *>(self)->take(key, call);
}
