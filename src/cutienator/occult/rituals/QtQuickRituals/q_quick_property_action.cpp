//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A QQuickPropertyAction that Python can take functions over in. Every QQuickPropertyAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPropertyActionCall0)(const void *, int *);
typedef void (*CuteQQuickPropertyActionCall1)(const void *, int *);
typedef int (*CuteQQuickPropertyActionCall2)(const void *, int *);
typedef void (*CuteQQuickPropertyActionCall3)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPropertyActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPropertyActionCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyActionCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyActionCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyActionCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyActionCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyActionCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPropertyAction : public QQuickPropertyAction {
public:
  using QQuickPropertyAction::QQuickPropertyAction;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPropertyActionCall0 call = reinterpret_cast<CuteQQuickPropertyActionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPropertyActionCall1 call = reinterpret_cast<CuteQQuickPropertyActionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPropertyActionCall2 call = reinterpret_cast<CuteQQuickPropertyActionCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPropertyActionCall3 call = reinterpret_cast<CuteQQuickPropertyActionCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::setTarget(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPropertyActionCall4 call = reinterpret_cast<CuteQQuickPropertyActionCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPropertyActionCall5 call = reinterpret_cast<CuteQQuickPropertyActionCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPropertyActionCall6 call = reinterpret_cast<CuteQQuickPropertyActionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPropertyActionCall7 call = reinterpret_cast<CuteQQuickPropertyActionCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPropertyActionCall8 call = reinterpret_cast<CuteQQuickPropertyActionCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPropertyActionCall9 call = reinterpret_cast<CuteQQuickPropertyActionCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPropertyActionCall10 call = reinterpret_cast<CuteQQuickPropertyActionCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPropertyAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickPropertyAction10metaObjectEv(
    const QQuickPropertyAction *self) {
  return self->metaObject();
}

//  void *QQuickPropertyAction::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickPropertyAction11qt_metacastEPKc(
    QQuickPropertyAction *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPropertyAction::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickPropertyAction11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPropertyAction *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPropertyAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickPropertyAction2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPropertyAction::tr(s, c, n));
}

//  QQuickPropertyActionPrivate *QQuickPropertyAction::d_func()
extern "C" Q_DECL_EXPORT
QQuickPropertyActionPrivate *ritual_ZN20QQuickPropertyAction6d_funcEv(
    QQuickPropertyAction *self) {
  return self->d_func();
}

//  const QQuickPropertyActionPrivate *QQuickPropertyAction::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPropertyActionPrivate *ritual_ZNK20QQuickPropertyAction6d_funcEv(
    const QQuickPropertyAction *self) {
  return self->d_func();
}

//  QQuickPropertyAction::QQuickPropertyAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPropertyAction *ritual_ZN20QQuickPropertyActionC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPropertyAction(parent);
}

//  QQuickPropertyAction::~QQuickPropertyAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyActionD1Ev(QQuickPropertyAction *self) {
  delete self;
}

//  QObject *QQuickPropertyAction::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QQuickPropertyAction6targetEv(
    const QQuickPropertyAction *self) {
  return self->target();
}

//  void QQuickPropertyAction::setTargetObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction15setTargetObjectEP7QObject(
    QQuickPropertyAction *self,
    QObject *a0) {
  self->setTargetObject(a0);
}

//  QString QQuickPropertyAction::property() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickPropertyAction8propertyEv(
    const QQuickPropertyAction *self) {
  return new QString(self->property());
}

//  void QQuickPropertyAction::setProperty(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction11setPropertyERK7QString(
    QQuickPropertyAction *self,
    const QString *a0) {
  self->setProperty(*a0);
}

//  QString QQuickPropertyAction::properties() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickPropertyAction10propertiesEv(
    const QQuickPropertyAction *self) {
  return new QString(self->properties());
}

//  void QQuickPropertyAction::setProperties(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction13setPropertiesERK7QString(
    QQuickPropertyAction *self,
    const QString *a0) {
  self->setProperties(*a0);
}

//  QQmlListProperty<QObject> QQuickPropertyAction::targets()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN20QQuickPropertyAction7targetsEv(
    QQuickPropertyAction *self) {
  return new QQmlListProperty<QObject>(self->targets());
}

//  QQmlListProperty<QObject> QQuickPropertyAction::exclude()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN20QQuickPropertyAction7excludeEv(
    QQuickPropertyAction *self) {
  return new QQmlListProperty<QObject>(self->exclude());
}

//  QVariant QQuickPropertyAction::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQuickPropertyAction5valueEv(
    const QQuickPropertyAction *self) {
  return new QVariant(self->value());
}

//  void QQuickPropertyAction::setValue(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction8setValueERK8QVariant(
    QQuickPropertyAction *self,
    const QVariant *a0) {
  self->setValue(*a0);
}

//  void QQuickPropertyAction::valueChanged(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction12valueChangedERK8QVariant(
    QQuickPropertyAction *self,
    const QVariant *a0) {
  self->valueChanged(*a0);
}

//  void QQuickPropertyAction::propertiesChanged(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction17propertiesChangedERK7QString(
    QQuickPropertyAction *self,
    const QString *a0) {
  self->propertiesChanged(*a0);
}

//  void QQuickPropertyAction::targetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction13targetChangedEv(
    QQuickPropertyAction *self) {
  self->targetChanged();
}

//  void QQuickPropertyAction::propertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPropertyAction15propertyChangedEv(
    QQuickPropertyAction *self) {
  self->propertyChanged();
}

//  QAbstractAnimationJob
//      *QQuickPropertyAction::transition(QQuickStateActions &actions,
//      QQmlProperties &modified, TransitionDirection direction, QObject
//      *defaultTarget)
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN20QQuickPropertyAction10transitionER5QListI17QQuickStateActionERS0_I12QQmlPropertyEN23QQuickAbstractAnimation19TransitionDirectionEP7QObject(
    QQuickPropertyAction *self,
    QQuickStateActions *actions,
    QQmlProperties *modified,
    QQuickAbstractAnimation::TransitionDirection direction,
    QObject *defaultTarget) {
  return self->transition(*actions, *modified, direction, defaultTarget);
}

//  a Python function taken by a CuteQQuickPropertyAction, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPropertyAction(
    QQuickPropertyAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPropertyAction *>(self)->take(key, call);
}

//  a QQmlListProperty<QObject> a ritual of QQuickPropertyAction gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickPropertyAction__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
