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

//  Only a class built on QQuickYAnimator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickYAnimator : QQuickYAnimator {
  using QQuickYAnimator::createJob;
  using QQuickYAnimator::propertyName;
};

//  A QQuickYAnimator that Python can take functions over in. Every QQuickYAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickYAnimatorCall0)(const void *, int *);
typedef QString * (*CuteQQuickYAnimatorCall1)(const void *, int *);
typedef int (*CuteQQuickYAnimatorCall2)(const void *, int *);
typedef void (*CuteQQuickYAnimatorCall3)(const void *, int *);
typedef void (*CuteQQuickYAnimatorCall4)(const void *, int *);
typedef void (*CuteQQuickYAnimatorCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickYAnimatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickYAnimatorCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickYAnimatorCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickYAnimatorCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickYAnimatorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickYAnimatorCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickYAnimatorCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickYAnimator : public QQuickYAnimator {
public:
  using QQuickYAnimator::QQuickYAnimator;
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

  //  QQuickAnimatorJob *QQuickYAnimator::createJob() const
  QQuickAnimatorJob *createJob() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickYAnimatorCall0 call = reinterpret_cast<CuteQQuickYAnimatorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnimatorJob *>(given);
    }
    return QQuickYAnimator::createJob();
  }

  //  QString QQuickYAnimator::propertyName() const
  QString propertyName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickYAnimatorCall1 call = reinterpret_cast<CuteQQuickYAnimatorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickYAnimator::propertyName();
  }

  //  ThreadingModel QQuickAnimator::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickYAnimatorCall2 call = reinterpret_cast<CuteQQuickYAnimatorCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAnimator::threadingModel();
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickYAnimatorCall3 call = reinterpret_cast<CuteQQuickYAnimatorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickYAnimatorCall4 call = reinterpret_cast<CuteQQuickYAnimatorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickYAnimatorCall5 call = reinterpret_cast<CuteQQuickYAnimatorCall5>(taken[5]);
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
      CuteQQuickYAnimatorCall6 call = reinterpret_cast<CuteQQuickYAnimatorCall6>(taken[6]);
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
      CuteQQuickYAnimatorCall7 call = reinterpret_cast<CuteQQuickYAnimatorCall7>(taken[7]);
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
      CuteQQuickYAnimatorCall8 call = reinterpret_cast<CuteQQuickYAnimatorCall8>(taken[8]);
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
      CuteQQuickYAnimatorCall9 call = reinterpret_cast<CuteQQuickYAnimatorCall9>(taken[9]);
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
      CuteQQuickYAnimatorCall10 call = reinterpret_cast<CuteQQuickYAnimatorCall10>(taken[10]);
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
      CuteQQuickYAnimatorCall11 call = reinterpret_cast<CuteQQuickYAnimatorCall11>(taken[11]);
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
      CuteQQuickYAnimatorCall12 call = reinterpret_cast<CuteQQuickYAnimatorCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickYAnimator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickYAnimator10metaObjectEv(
    const QQuickYAnimator *self) {
  return self->metaObject();
}

//  void *QQuickYAnimator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickYAnimator11qt_metacastEPKc(
    QQuickYAnimator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickYAnimator::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickYAnimator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickYAnimator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickYAnimator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickYAnimator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickYAnimator::tr(s, c, n));
}

//  QQuickYAnimator::QQuickYAnimator(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickYAnimator *ritual_ZN15QQuickYAnimatorC1EP7QObject(QObject *parent) {
  return new CuteQQuickYAnimator(parent);
}

//  QQuickAnimatorJob *QQuickYAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_ZNK15QQuickYAnimator9createJobEv(
    const QQuickYAnimator *self) {
  return self->createJob();
}

//  QString QQuickYAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickYAnimator12propertyNameEv(
    const QQuickYAnimator *self) {
  return new QString(self->propertyName());
}

//  a Python function taken by a CuteQQuickYAnimator, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickYAnimator(
    QQuickYAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickYAnimator *>(self)->take(key, call);
}

//  QQuickAnimatorJob *QQuickYAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_own_ZNK15QQuickYAnimator9createJobEv(
    const QQuickYAnimator *self) {
  return static_cast<const OwnQQuickYAnimator *>(self)->OwnQQuickYAnimator::createJob();
}

//  QString QQuickYAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QQuickYAnimator12propertyNameEv(
    const QQuickYAnimator *self) {
  return new QString(
      static_cast<const OwnQQuickYAnimator *>(self)->OwnQQuickYAnimator::propertyName());
}
