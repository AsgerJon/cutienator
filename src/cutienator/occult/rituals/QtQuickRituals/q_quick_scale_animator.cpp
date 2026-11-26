//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickScaleAnimator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickScaleAnimator : QQuickScaleAnimator {
  using QQuickScaleAnimator::createJob;
  using QQuickScaleAnimator::propertyName;
};

//  A QQuickScaleAnimator that Python can take functions over in. Every QQuickScaleAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickScaleAnimatorCall0)(const void *, int *);
typedef QString * (*CuteQQuickScaleAnimatorCall1)(const void *, int *);
typedef int (*CuteQQuickScaleAnimatorCall2)(const void *, int *);
typedef void (*CuteQQuickScaleAnimatorCall3)(const void *, int *);
typedef void (*CuteQQuickScaleAnimatorCall4)(const void *, int *);
typedef void (*CuteQQuickScaleAnimatorCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScaleAnimatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScaleAnimatorCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScaleAnimatorCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScaleAnimatorCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScaleAnimatorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScaleAnimatorCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScaleAnimatorCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickScaleAnimator : public QQuickScaleAnimator {
public:
  using QQuickScaleAnimator::QQuickScaleAnimator;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QQuickAnimator9createJobEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQuickAnimator12propertyNameEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QQuickAnimatorJob *QQuickScaleAnimator::createJob() const
  QQuickAnimatorJob *createJob() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall0 call = reinterpret_cast<CuteQQuickScaleAnimatorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnimatorJob *>(given);
    }
    return QQuickScaleAnimator::createJob();
  }

  //  QString QQuickScaleAnimator::propertyName() const
  QString propertyName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall1 call = reinterpret_cast<CuteQQuickScaleAnimatorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickScaleAnimator::propertyName();
  }

  //  ThreadingModel QQuickAnimator::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall2 call = reinterpret_cast<CuteQQuickScaleAnimatorCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAnimator::threadingModel();
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall3 call = reinterpret_cast<CuteQQuickScaleAnimatorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall4 call = reinterpret_cast<CuteQQuickScaleAnimatorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall5 call = reinterpret_cast<CuteQQuickScaleAnimatorCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::setTarget(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall6 call = reinterpret_cast<CuteQQuickScaleAnimatorCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall7 call = reinterpret_cast<CuteQQuickScaleAnimatorCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall8 call = reinterpret_cast<CuteQQuickScaleAnimatorCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall9 call = reinterpret_cast<CuteQQuickScaleAnimatorCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall10 call = reinterpret_cast<CuteQQuickScaleAnimatorCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall11 call = reinterpret_cast<CuteQQuickScaleAnimatorCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickScaleAnimatorCall12 call = reinterpret_cast<CuteQQuickScaleAnimatorCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickScaleAnimator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickScaleAnimator10metaObjectEv(
    const QQuickScaleAnimator *self) {
  return self->metaObject();
}

//  void *QQuickScaleAnimator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickScaleAnimator11qt_metacastEPKc(
    QQuickScaleAnimator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickScaleAnimator::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickScaleAnimator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickScaleAnimator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickScaleAnimator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickScaleAnimator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScaleAnimator::tr(s, c, n));
}

//  QQuickScaleAnimator::QQuickScaleAnimator(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickScaleAnimator *ritual_ZN19QQuickScaleAnimatorC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickScaleAnimator(parent);
}

//  QQuickAnimatorJob *QQuickScaleAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_ZNK19QQuickScaleAnimator9createJobEv(
    const QQuickScaleAnimator *self) {
  return self->createJob();
}

//  QString QQuickScaleAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickScaleAnimator12propertyNameEv(
    const QQuickScaleAnimator *self) {
  return new QString(self->propertyName());
}

//  a Python function taken by a CuteQQuickScaleAnimator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScaleAnimator(
    QQuickScaleAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScaleAnimator *>(self)->take(key, call);
}

//  QQuickAnimatorJob *QQuickScaleAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_own_ZNK19QQuickScaleAnimator9createJobEv(
    const QQuickScaleAnimator *self) {
  return static_cast<const OwnQQuickScaleAnimator *>(self)->OwnQQuickScaleAnimator::createJob();
}

//  QString QQuickScaleAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QQuickScaleAnimator12propertyNameEv(
    const QQuickScaleAnimator *self) {
  return new QString(
      static_cast<const OwnQQuickScaleAnimator *>(self)->OwnQQuickScaleAnimator::propertyName());
}
