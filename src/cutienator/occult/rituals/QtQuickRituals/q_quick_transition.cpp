//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktransition_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QQuickTransition that Python can take functions over in. Every QQuickTransition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTransitionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTransitionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransitionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransitionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransitionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransitionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTransitionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTransition : public QQuickTransition {
public:
  using QQuickTransition::QQuickTransition;
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
      CuteQQuickTransitionCall0 call = reinterpret_cast<CuteQQuickTransitionCall0>(taken[0]);
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
      CuteQQuickTransitionCall1 call = reinterpret_cast<CuteQQuickTransitionCall1>(taken[1]);
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
      CuteQQuickTransitionCall2 call = reinterpret_cast<CuteQQuickTransitionCall2>(taken[2]);
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
      CuteQQuickTransitionCall3 call = reinterpret_cast<CuteQQuickTransitionCall3>(taken[3]);
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
      CuteQQuickTransitionCall4 call = reinterpret_cast<CuteQQuickTransitionCall4>(taken[4]);
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
      CuteQQuickTransitionCall5 call = reinterpret_cast<CuteQQuickTransitionCall5>(taken[5]);
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
      CuteQQuickTransitionCall6 call = reinterpret_cast<CuteQQuickTransitionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickTransition10metaObjectEv(
    const QQuickTransition *self) {
  return self->metaObject();
}

//  void *QQuickTransition::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickTransition11qt_metacastEPKc(
    QQuickTransition *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTransition::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickTransition11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTransition *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTransition::tr(s, c, n));
}

//  QQuickTransitionPrivate *QQuickTransition::d_func()
extern "C" Q_DECL_EXPORT
QQuickTransitionPrivate *ritual_ZN16QQuickTransition6d_funcEv(
    QQuickTransition *self) {
  return self->d_func();
}

//  const QQuickTransitionPrivate *QQuickTransition::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTransitionPrivate *ritual_ZNK16QQuickTransition6d_funcEv(
    const QQuickTransition *self) {
  return self->d_func();
}

//  QQuickTransition::QQuickTransition(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZN16QQuickTransitionC1EP7QObject(QObject *parent) {
  return new CuteQQuickTransition(parent);
}

//  QQuickTransition::~QQuickTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransitionD1Ev(QQuickTransition *self) {
  delete self;
}

//  QString QQuickTransition::fromState() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickTransition9fromStateEv(
    const QQuickTransition *self) {
  return new QString(self->fromState());
}

//  void QQuickTransition::setFromState(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition12setFromStateERK7QString(
    QQuickTransition *self,
    const QString *a0) {
  self->setFromState(*a0);
}

//  QString QQuickTransition::toState() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickTransition7toStateEv(
    const QQuickTransition *self) {
  return new QString(self->toState());
}

//  void QQuickTransition::setToState(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition10setToStateERK7QString(
    QQuickTransition *self,
    const QString *a0) {
  self->setToState(*a0);
}

//  bool QQuickTransition::reversible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickTransition10reversibleEv(
    const QQuickTransition *self) {
  return self->reversible();
}

//  void QQuickTransition::setReversible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition13setReversibleEb(
    QQuickTransition *self,
    bool a0) {
  self->setReversible(a0);
}

//  bool QQuickTransition::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickTransition7enabledEv(const QQuickTransition *self) {
  return self->enabled();
}

//  void QQuickTransition::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition10setEnabledEb(
    QQuickTransition *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QQuickTransition::running() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickTransition7runningEv(const QQuickTransition *self) {
  return self->running();
}

//  QQmlListProperty<QQuickAbstractAnimation> QQuickTransition::animations()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickAbstractAnimation> *ritual_ZN16QQuickTransition10animationsEv(
    QQuickTransition *self) {
  return new QQmlListProperty<QQuickAbstractAnimation>(self->animations());
}

//  QQuickTransitionInstance
//      *QQuickTransition::prepare(QQuickStateOperation::ActionList &actions,
//      QList<QQmlProperty> &after, QQuickTransitionManager *end, QObject
//      *defaultTarget)
extern "C" Q_DECL_EXPORT
QQuickTransitionInstance *ritual_ZN16QQuickTransition7prepareER5QListI17QQuickStateActionERS0_I12QQmlPropertyEP23QQuickTransitionManagerP7QObject(
    QQuickTransition *self,
    QQuickStateOperation::ActionList *actions,
    QList<QQmlProperty> *after,
    QQuickTransitionManager *end,
    QObject *defaultTarget) {
  return self->prepare(*actions, *after, end, defaultTarget);
}

//  void QQuickTransition::setReversed(bool r)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition11setReversedEb(
    QQuickTransition *self,
    bool r) {
  self->setReversed(r);
}

//  void QQuickTransition::fromChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition11fromChangedEv(QQuickTransition *self) {
  self->fromChanged();
}

//  void QQuickTransition::toChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition9toChangedEv(QQuickTransition *self) {
  self->toChanged();
}

//  void QQuickTransition::reversibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition17reversibleChangedEv(
    QQuickTransition *self) {
  self->reversibleChanged();
}

//  void QQuickTransition::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition14enabledChangedEv(QQuickTransition *self) {
  self->enabledChanged();
}

//  void QQuickTransition::runningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTransition14runningChangedEv(QQuickTransition *self) {
  self->runningChanged();
}

//  a Python function taken by a CuteQQuickTransition, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTransition(
    QQuickTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTransition *>(self)->take(key, call);
}

//  a QQmlListProperty<QQuickAbstractAnimation> a ritual of QQuickTransition
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickTransition__QQmlListProperty_QQuickAbstractAnimation(
    QQmlListProperty<QQuickAbstractAnimation> *self) {
  delete self;
}
