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

//  Only a class built on QQuickOpacityAnimator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickOpacityAnimator : QQuickOpacityAnimator {
  using QQuickOpacityAnimator::createJob;
  using QQuickOpacityAnimator::propertyName;
};

//  A QQuickOpacityAnimator that Python can take functions over in. Every QQuickOpacityAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickOpacityAnimatorCall0)(const void *, int *);
typedef QString * (*CuteQQuickOpacityAnimatorCall1)(const void *, int *);
typedef int (*CuteQQuickOpacityAnimatorCall2)(const void *, int *);
typedef void (*CuteQQuickOpacityAnimatorCall3)(const void *, int *);
typedef void (*CuteQQuickOpacityAnimatorCall4)(const void *, int *);
typedef void (*CuteQQuickOpacityAnimatorCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickOpacityAnimatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickOpacityAnimatorCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOpacityAnimatorCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOpacityAnimatorCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOpacityAnimatorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOpacityAnimatorCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickOpacityAnimatorCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickOpacityAnimator : public QQuickOpacityAnimator {
public:
  using QQuickOpacityAnimator::QQuickOpacityAnimator;
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

  //  QQuickAnimatorJob *QQuickOpacityAnimator::createJob() const
  QQuickAnimatorJob *createJob() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickOpacityAnimatorCall0 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnimatorJob *>(given);
    }
    return QQuickOpacityAnimator::createJob();
  }

  //  QString QQuickOpacityAnimator::propertyName() const
  QString propertyName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickOpacityAnimatorCall1 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickOpacityAnimator::propertyName();
  }

  //  ThreadingModel QQuickAnimator::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickOpacityAnimatorCall2 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAnimator::threadingModel();
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickOpacityAnimatorCall3 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickOpacityAnimatorCall4 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickOpacityAnimatorCall5 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall5>(taken[5]);
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
      CuteQQuickOpacityAnimatorCall6 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall6>(taken[6]);
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
      CuteQQuickOpacityAnimatorCall7 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall7>(taken[7]);
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
      CuteQQuickOpacityAnimatorCall8 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall8>(taken[8]);
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
      CuteQQuickOpacityAnimatorCall9 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall9>(taken[9]);
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
      CuteQQuickOpacityAnimatorCall10 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall10>(taken[10]);
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
      CuteQQuickOpacityAnimatorCall11 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall11>(taken[11]);
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
      CuteQQuickOpacityAnimatorCall12 call = reinterpret_cast<CuteQQuickOpacityAnimatorCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickOpacityAnimator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickOpacityAnimator10metaObjectEv(
    const QQuickOpacityAnimator *self) {
  return self->metaObject();
}

//  QString QQuickOpacityAnimator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickOpacityAnimator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickOpacityAnimator::tr(s, c, n));
}

//  QQuickOpacityAnimator::QQuickOpacityAnimator(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickOpacityAnimator *ritual_ZN21QQuickOpacityAnimatorC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickOpacityAnimator(parent);
}

//  QQuickAnimatorJob *QQuickOpacityAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_ZNK21QQuickOpacityAnimator9createJobEv(
    const QQuickOpacityAnimator *self) {
  return self->createJob();
}

//  QString QQuickOpacityAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickOpacityAnimator12propertyNameEv(
    const QQuickOpacityAnimator *self) {
  return new QString(self->propertyName());
}

//  a Python function taken by a CuteQQuickOpacityAnimator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickOpacityAnimator(
    QQuickOpacityAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickOpacityAnimator *>(self)->take(key, call);
}

//  QQuickAnimatorJob *QQuickOpacityAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_own_ZNK21QQuickOpacityAnimator9createJobEv(
    const QQuickOpacityAnimator *self) {
  return static_cast<const OwnQQuickOpacityAnimator *>(self)->OwnQQuickOpacityAnimator::createJob();
}

//  QString QQuickOpacityAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QQuickOpacityAnimator12propertyNameEv(
    const QQuickOpacityAnimator *self) {
  return new QString(
      static_cast<const OwnQQuickOpacityAnimator *>(self)->OwnQQuickOpacityAnimator::propertyName());
}
