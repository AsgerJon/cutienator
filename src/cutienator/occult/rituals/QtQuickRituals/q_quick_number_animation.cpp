//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickNumberAnimation that Python can take functions over in. Every QQuickNumberAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickNumberAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickNumberAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickNumberAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickNumberAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickNumberAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickNumberAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickNumberAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickNumberAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNumberAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNumberAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNumberAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNumberAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickNumberAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickNumberAnimation : public QQuickNumberAnimation {
public:
  using QQuickNumberAnimation::QQuickNumberAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQuickPropertyAnimation11setDurationEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
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

  //  int QQuickPropertyAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickNumberAnimationCall0 call = reinterpret_cast<CuteQQuickNumberAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickNumberAnimationCall1 call = reinterpret_cast<CuteQQuickNumberAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickNumberAnimationCall2 call = reinterpret_cast<CuteQQuickNumberAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickNumberAnimationCall3 call = reinterpret_cast<CuteQQuickNumberAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickNumberAnimationCall4 call = reinterpret_cast<CuteQQuickNumberAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickNumberAnimationCall5 call = reinterpret_cast<CuteQQuickNumberAnimationCall5>(taken[5]);
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
      CuteQQuickNumberAnimationCall6 call = reinterpret_cast<CuteQQuickNumberAnimationCall6>(taken[6]);
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
      CuteQQuickNumberAnimationCall7 call = reinterpret_cast<CuteQQuickNumberAnimationCall7>(taken[7]);
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
      CuteQQuickNumberAnimationCall8 call = reinterpret_cast<CuteQQuickNumberAnimationCall8>(taken[8]);
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
      CuteQQuickNumberAnimationCall9 call = reinterpret_cast<CuteQQuickNumberAnimationCall9>(taken[9]);
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
      CuteQQuickNumberAnimationCall10 call = reinterpret_cast<CuteQQuickNumberAnimationCall10>(taken[10]);
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
      CuteQQuickNumberAnimationCall11 call = reinterpret_cast<CuteQQuickNumberAnimationCall11>(taken[11]);
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
      CuteQQuickNumberAnimationCall12 call = reinterpret_cast<CuteQQuickNumberAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickNumberAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickNumberAnimation10metaObjectEv(
    const QQuickNumberAnimation *self) {
  return self->metaObject();
}

//  void *QQuickNumberAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickNumberAnimation11qt_metacastEPKc(
    QQuickNumberAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickNumberAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickNumberAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickNumberAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickNumberAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickNumberAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickNumberAnimation::tr(s, c, n));
}

//  QQuickPropertyAnimationPrivate *QQuickNumberAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickPropertyAnimationPrivate *ritual_ZN21QQuickNumberAnimation6d_funcEv(
    QQuickNumberAnimation *self) {
  return self->d_func();
}

//  const QQuickPropertyAnimationPrivate *QQuickNumberAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickPropertyAnimationPrivate *ritual_ZNK21QQuickNumberAnimation6d_funcEv(
    const QQuickNumberAnimation *self) {
  return self->d_func();
}

//  QQuickNumberAnimation::QQuickNumberAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickNumberAnimation *ritual_ZN21QQuickNumberAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickNumberAnimation(parent);
}

//  QQuickNumberAnimation::~QQuickNumberAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickNumberAnimationD1Ev(QQuickNumberAnimation *self) {
  delete self;
}

//  qreal QQuickNumberAnimation::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickNumberAnimation4fromEv(
    const QQuickNumberAnimation *self) {
  return self->from();
}

//  void QQuickNumberAnimation::setFrom(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickNumberAnimation7setFromEd(
    QQuickNumberAnimation *self,
    qreal a0) {
  self->setFrom(a0);
}

//  qreal QQuickNumberAnimation::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickNumberAnimation2toEv(
    const QQuickNumberAnimation *self) {
  return self->to();
}

//  void QQuickNumberAnimation::setTo(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickNumberAnimation5setToEd(
    QQuickNumberAnimation *self,
    qreal a0) {
  self->setTo(a0);
}

//  QQuickNumberAnimation::QQuickNumberAnimation(QQuickPropertyAnimationPriva
//      te &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickNumberAnimation *ritual_ZN21QQuickNumberAnimationC1ER30QQuickPropertyAnimationPrivateP7QObject(
    QQuickPropertyAnimationPrivate *dd,
    QObject *parent) {
  return new CuteQQuickNumberAnimation(*dd, parent);
}

//  void QQuickNumberAnimation::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickNumberAnimation4initEv(QQuickNumberAnimation *self) {
  self->init();
}

//  a Python function taken by a CuteQQuickNumberAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickNumberAnimation(
    QQuickNumberAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickNumberAnimation *>(self)->take(key, call);
}
