//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquickkeyframe_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qtquicktimelineglobal_p.h>
#include <QtQuickTimeline/QtQuickTimeline>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquickkeyframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickKeyframe that Python can take functions over in. Every QQuickKeyframe
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQQuickKeyframeCall0)(const void *, QQuickKeyframe *, qreal, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickKeyframeCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickKeyframeCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickKeyframe : public QQuickKeyframe {
public:
  using QQuickKeyframe::QQuickKeyframe;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQuickKeyframe8evaluateEPS_di")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVariant QQuickKeyframe::evaluate(QQuickKeyframe *pre, qreal frame,
  //      int userType) const
  QVariant evaluate(
      QQuickKeyframe *pre,
      qreal frame,
      int userType) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickKeyframeCall0 call = reinterpret_cast<CuteQQuickKeyframeCall0>(taken[0]);
      const QVariant * given = call(this, pre, frame, userType, &handled);
      if (handled && given) return *given;
    }
    return QQuickKeyframe::evaluate(pre, frame, userType);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickKeyframeCall1 call = reinterpret_cast<CuteQQuickKeyframeCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickKeyframeCall2 call = reinterpret_cast<CuteQQuickKeyframeCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickKeyframeCall3 call = reinterpret_cast<CuteQQuickKeyframeCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickKeyframeCall4 call = reinterpret_cast<CuteQQuickKeyframeCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickKeyframeCall5 call = reinterpret_cast<CuteQQuickKeyframeCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickKeyframeCall6 call = reinterpret_cast<CuteQQuickKeyframeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickKeyframeCall7 call = reinterpret_cast<CuteQQuickKeyframeCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickKeyframe::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickKeyframe10metaObjectEv(
    const QQuickKeyframe *self) {
  return self->metaObject();
}

//  void *QQuickKeyframe::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickKeyframe11qt_metacastEPKc(
    QQuickKeyframe *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickKeyframe::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickKeyframe11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickKeyframe *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickKeyframe::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickKeyframe2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickKeyframe::tr(s, c, n));
}

//  QQuickKeyframePrivate *QQuickKeyframe::d_func()
extern "C" Q_DECL_EXPORT
QQuickKeyframePrivate *ritual_ZN14QQuickKeyframe6d_funcEv(
    QQuickKeyframe *self) {
  return self->d_func();
}

//  const QQuickKeyframePrivate *QQuickKeyframe::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickKeyframePrivate *ritual_ZNK14QQuickKeyframe6d_funcEv(
    const QQuickKeyframe *self) {
  return self->d_func();
}

//  QQuickKeyframe::QQuickKeyframe(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickKeyframe *ritual_ZN14QQuickKeyframeC1EP7QObject(QObject *parent) {
  return new CuteQQuickKeyframe(parent);
}

//  qreal QQuickKeyframe::frame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickKeyframe5frameEv(const QQuickKeyframe *self) {
  return self->frame();
}

//  void QQuickKeyframe::setFrame(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyframe8setFrameEd(QQuickKeyframe *self, qreal a0) {
  self->setFrame(a0);
}

//  void QQuickKeyframe::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyframe5resetEv(QQuickKeyframe *self) {
  self->reset();
}

//  QEasingCurve QQuickKeyframe::easing() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK14QQuickKeyframe6easingEv(
    const QQuickKeyframe *self) {
  return new QEasingCurve(self->easing());
}

//  void QQuickKeyframe::setEasing(const QEasingCurve &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyframe9setEasingERK12QEasingCurve(
    QQuickKeyframe *self,
    const QEasingCurve *a0) {
  self->setEasing(*a0);
}

//  QVariant QQuickKeyframe::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickKeyframe5valueEv(const QQuickKeyframe *self) {
  return new QVariant(self->value());
}

//  void QQuickKeyframe::setValue(const QVariant &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyframe8setValueERK8QVariant(
    QQuickKeyframe *self,
    const QVariant *v) {
  self->setValue(*v);
}

//  QVariant QQuickKeyframe::evaluate(QQuickKeyframe *pre, qreal frame, int
//      userType) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickKeyframe8evaluateEPS_di(
    const QQuickKeyframe *self,
    QQuickKeyframe *pre,
    qreal frame,
    int userType) {
  return new QVariant(self->evaluate(pre, frame, userType));
}

//  QQuickKeyframe::QQuickKeyframe(QQuickKeyframePrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickKeyframe *ritual_ZN14QQuickKeyframeC1ER21QQuickKeyframePrivateP7QObject(
    QQuickKeyframePrivate *dd,
    QObject *parent) {
  return new CuteQQuickKeyframe(*dd, parent);
}

//  void QQuickKeyframe::frameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyframe12frameChangedEv(QQuickKeyframe *self) {
  self->frameChanged();
}

//  void QQuickKeyframe::easingCurveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyframe18easingCurveChangedEv(QQuickKeyframe *self) {
  self->easingCurveChanged();
}

//  void QQuickKeyframe::valueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyframe12valueChangedEv(QQuickKeyframe *self) {
  self->valueChanged();
}

//  a Python function taken by a CuteQQuickKeyframe, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickKeyframe(
    QQuickKeyframe *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickKeyframe *>(self)->take(key, call);
}

//  QVariant QQuickKeyframe::evaluate(QQuickKeyframe *pre, qreal frame, int
//      userType) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QQuickKeyframe8evaluateEPS_di(
    const QQuickKeyframe *self,
    QQuickKeyframe *pre,
    qreal frame,
    int userType) {
  return new QVariant(self->QQuickKeyframe::evaluate(pre, frame, userType));
}
