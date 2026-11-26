//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
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

//  Only a class built on QQuickUniformAnimator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickUniformAnimator : QQuickUniformAnimator {
  using QQuickUniformAnimator::createJob;
  using QQuickUniformAnimator::propertyName;
};

//  A QQuickUniformAnimator that Python can take functions over in. Every QQuickUniformAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteQQuickUniformAnimatorCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef QString * (*CuteQQuickUniformAnimatorCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef int (*CuteQQuickUniformAnimatorCall2)(const void *, int *);
typedef void (*CuteQQuickUniformAnimatorCall3)(const void *, int *);
typedef void (*CuteQQuickUniformAnimatorCall4)(const void *, int *);
typedef void (*CuteQQuickUniformAnimatorCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickUniformAnimatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickUniformAnimatorCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniformAnimatorCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniformAnimatorCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniformAnimatorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniformAnimatorCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniformAnimatorCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickUniformAnimator : public QQuickUniformAnimator {
public:
  using QQuickUniformAnimator::QQuickUniformAnimator;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK14QQuickAnimator9createJobEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK14QQuickAnimator12propertyNameEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
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

#if QT_CONFIG(quick_shadereffect)
  //  QQuickAnimatorJob *QQuickUniformAnimator::createJob() const
  QQuickAnimatorJob *createJob() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickUniformAnimatorCall0 call = reinterpret_cast<CuteQQuickUniformAnimatorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnimatorJob *>(given);
    }
    return QQuickUniformAnimator::createJob();
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  QString QQuickUniformAnimator::propertyName() const
  QString propertyName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickUniformAnimatorCall1 call = reinterpret_cast<CuteQQuickUniformAnimatorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickUniformAnimator::propertyName();
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  ThreadingModel QQuickAnimator::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickUniformAnimatorCall2 call = reinterpret_cast<CuteQQuickUniformAnimatorCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAnimator::threadingModel();
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickUniformAnimatorCall3 call = reinterpret_cast<CuteQQuickUniformAnimatorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickUniformAnimatorCall4 call = reinterpret_cast<CuteQQuickUniformAnimatorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickUniformAnimatorCall5 call = reinterpret_cast<CuteQQuickUniformAnimatorCall5>(taken[5]);
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
      CuteQQuickUniformAnimatorCall6 call = reinterpret_cast<CuteQQuickUniformAnimatorCall6>(taken[6]);
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
      CuteQQuickUniformAnimatorCall7 call = reinterpret_cast<CuteQQuickUniformAnimatorCall7>(taken[7]);
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
      CuteQQuickUniformAnimatorCall8 call = reinterpret_cast<CuteQQuickUniformAnimatorCall8>(taken[8]);
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
      CuteQQuickUniformAnimatorCall9 call = reinterpret_cast<CuteQQuickUniformAnimatorCall9>(taken[9]);
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
      CuteQQuickUniformAnimatorCall10 call = reinterpret_cast<CuteQQuickUniformAnimatorCall10>(taken[10]);
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
      CuteQQuickUniformAnimatorCall11 call = reinterpret_cast<CuteQQuickUniformAnimatorCall11>(taken[11]);
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
      CuteQQuickUniformAnimatorCall12 call = reinterpret_cast<CuteQQuickUniformAnimatorCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickUniformAnimator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickUniformAnimator10metaObjectEv(
    const QQuickUniformAnimator *self) {
  return self->metaObject();
}

//  void *QQuickUniformAnimator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickUniformAnimator11qt_metacastEPKc(
    QQuickUniformAnimator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickUniformAnimator::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickUniformAnimator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickUniformAnimator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickUniformAnimator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickUniformAnimator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickUniformAnimator::tr(s, c, n));
}

//  QQuickUniformAnimatorPrivate *QQuickUniformAnimator::d_func()
extern "C" Q_DECL_EXPORT
QQuickUniformAnimatorPrivate *ritual_ZN21QQuickUniformAnimator6d_funcEv(
    QQuickUniformAnimator *self) {
  return self->d_func();
}

//  const QQuickUniformAnimatorPrivate *QQuickUniformAnimator::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickUniformAnimatorPrivate *ritual_ZNK21QQuickUniformAnimator6d_funcEv(
    const QQuickUniformAnimator *self) {
  return self->d_func();
}

//  QQuickUniformAnimator::QQuickUniformAnimator(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickUniformAnimator *ritual_ZN21QQuickUniformAnimatorC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickUniformAnimator(parent);
}

//  QString QQuickUniformAnimator::uniform() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickUniformAnimator7uniformEv(
    const QQuickUniformAnimator *self) {
  return new QString(self->uniform());
}

//  void QQuickUniformAnimator::setUniform(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickUniformAnimator10setUniformERK7QString(
    QQuickUniformAnimator *self,
    const QString *a0) {
  self->setUniform(*a0);
}

//  void QQuickUniformAnimator::uniformChanged(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickUniformAnimator14uniformChangedERK7QString(
    QQuickUniformAnimator *self,
    const QString *a0) {
  self->uniformChanged(*a0);
}

//  QQuickAnimatorJob *QQuickUniformAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_ZNK21QQuickUniformAnimator9createJobEv(
    const QQuickUniformAnimator *self) {
  return self->createJob();
}

//  QString QQuickUniformAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickUniformAnimator12propertyNameEv(
    const QQuickUniformAnimator *self) {
  return new QString(self->propertyName());
}

//  a Python function taken by a CuteQQuickUniformAnimator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickUniformAnimator(
    QQuickUniformAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickUniformAnimator *>(self)->take(key, call);
}

//  QQuickAnimatorJob *QQuickUniformAnimator::createJob() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_own_ZNK21QQuickUniformAnimator9createJobEv(
    const QQuickUniformAnimator *self) {
  return static_cast<const OwnQQuickUniformAnimator *>(self)->OwnQQuickUniformAnimator::createJob();
}

//  QString QQuickUniformAnimator::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QQuickUniformAnimator12propertyNameEv(
    const QQuickUniformAnimator *self) {
  return new QString(
      static_cast<const OwnQQuickUniformAnimator *>(self)->OwnQQuickUniformAnimator::propertyName());
}

#endif  // QT_CONFIG(quick_shadereffect)
