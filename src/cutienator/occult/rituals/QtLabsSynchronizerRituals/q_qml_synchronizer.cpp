//  Written by dev_tooling.RitualGenerator from the records of QtLabsSynchron
//  izer/6.12.0/QtLabsSynchronizer/private/qqmlsynchronizer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsSynchronizer/QtLabsSynchronizer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsSynchronizer/6.12.0/QtLabsSynchronizer/private/qqmlsynchronizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlSynchronizer that Python can take functions over in. Every QQmlSynchronizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSynchronizerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSynchronizerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSynchronizerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSynchronizerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSynchronizerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSynchronizerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSynchronizerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlSynchronizer : public QQmlSynchronizer {
public:
  using QQmlSynchronizer::QQmlSynchronizer;
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
      CuteQQmlSynchronizerCall0 call = reinterpret_cast<CuteQQmlSynchronizerCall0>(taken[0]);
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
      CuteQQmlSynchronizerCall1 call = reinterpret_cast<CuteQQmlSynchronizerCall1>(taken[1]);
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
      CuteQQmlSynchronizerCall2 call = reinterpret_cast<CuteQQmlSynchronizerCall2>(taken[2]);
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
      CuteQQmlSynchronizerCall3 call = reinterpret_cast<CuteQQmlSynchronizerCall3>(taken[3]);
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
      CuteQQmlSynchronizerCall4 call = reinterpret_cast<CuteQQmlSynchronizerCall4>(taken[4]);
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
      CuteQQmlSynchronizerCall5 call = reinterpret_cast<CuteQQmlSynchronizerCall5>(taken[5]);
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
      CuteQQmlSynchronizerCall6 call = reinterpret_cast<CuteQQmlSynchronizerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlSynchronizer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlSynchronizer10metaObjectEv(
    const QQmlSynchronizer *self) {
  return self->metaObject();
}

//  void *QQmlSynchronizer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQmlSynchronizer11qt_metacastEPKc(
    QQmlSynchronizer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlSynchronizer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlSynchronizer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlSynchronizer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlSynchronizer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlSynchronizer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlSynchronizer::tr(s, c, n));
}

//  QQmlSynchronizerPrivate *QQmlSynchronizer::d_func()
extern "C" Q_DECL_EXPORT
QQmlSynchronizerPrivate *ritual_ZN16QQmlSynchronizer6d_funcEv(
    QQmlSynchronizer *self) {
  return self->d_func();
}

//  const QQmlSynchronizerPrivate *QQmlSynchronizer::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSynchronizerPrivate *ritual_ZNK16QQmlSynchronizer6d_funcEv(
    const QQmlSynchronizer *self) {
  return self->d_func();
}

//  QQmlSynchronizer::QQmlSynchronizer(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlSynchronizer *ritual_ZN16QQmlSynchronizerC1EP7QObject(QObject *parent) {
  return new CuteQQmlSynchronizer(parent);
}

//  QObject *QQmlSynchronizer::sourceObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QQmlSynchronizer12sourceObjectEv(
    const QQmlSynchronizer *self) {
  return self->sourceObject();
}

//  void QQmlSynchronizer::setSourceObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer15setSourceObjectEP7QObject(
    QQmlSynchronizer *self,
    QObject *object) {
  self->setSourceObject(object);
}

//  QString QQmlSynchronizer::sourceProperty() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlSynchronizer14sourcePropertyEv(
    const QQmlSynchronizer *self) {
  return new QString(self->sourceProperty());
}

//  void QQmlSynchronizer::setSourceProperty(const QString &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer17setSourcePropertyERK7QString(
    QQmlSynchronizer *self,
    const QString *property) {
  self->setSourceProperty(*property);
}

//  QObject *QQmlSynchronizer::targetObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QQmlSynchronizer12targetObjectEv(
    const QQmlSynchronizer *self) {
  return self->targetObject();
}

//  void QQmlSynchronizer::setTargetObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer15setTargetObjectEP7QObject(
    QQmlSynchronizer *self,
    QObject *object) {
  self->setTargetObject(object);
}

//  QString QQmlSynchronizer::targetProperty() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlSynchronizer14targetPropertyEv(
    const QQmlSynchronizer *self) {
  return new QString(self->targetProperty());
}

//  void QQmlSynchronizer::setTargetProperty(const QString &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer17setTargetPropertyERK7QString(
    QQmlSynchronizer *self,
    const QString *property) {
  self->setTargetProperty(*property);
}

//  void QQmlSynchronizer::sourceObjectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer19sourceObjectChangedEv(
    QQmlSynchronizer *self) {
  self->sourceObjectChanged();
}

//  void QQmlSynchronizer::sourcePropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer21sourcePropertyChangedEv(
    QQmlSynchronizer *self) {
  self->sourcePropertyChanged();
}

//  void QQmlSynchronizer::targetObjectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer19targetObjectChangedEv(
    QQmlSynchronizer *self) {
  self->targetObjectChanged();
}

//  void QQmlSynchronizer::targetPropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer21targetPropertyChangedEv(
    QQmlSynchronizer *self) {
  self->targetPropertyChanged();
}

//  void QQmlSynchronizer::valueBounced(QObject *object, const QString
//      &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer12valueBouncedEP7QObjectRK7QString(
    QQmlSynchronizer *self,
    QObject *object,
    const QString *property) {
  self->valueBounced(object, *property);
}

//  void QQmlSynchronizer::valueIgnored(QObject *object, const QString
//      &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer12valueIgnoredEP7QObjectRK7QString(
    QQmlSynchronizer *self,
    QObject *object,
    const QString *property) {
  self->valueIgnored(object, *property);
}

//  void QQmlSynchronizer::setTarget(const QQmlProperty &target)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer9setTargetERK12QQmlProperty(
    QQmlSynchronizer *self,
    const QQmlProperty *target) {
  self->setTarget(*target);
}

//  void QQmlSynchronizer::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSynchronizer18componentFinalizedEv(
    QQmlSynchronizer *self) {
  self->componentFinalized();
}

//  QQmlSynchronizer as the QQmlPropertyValueSource it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyValueSource *ritual_cast_QQmlSynchronizer_QQmlPropertyValueSource(
    QQmlSynchronizer *self) {
  return static_cast<QQmlPropertyValueSource *>(self);
}

//  QQmlSynchronizer as the QQmlFinalizerHook it is built on
extern "C" Q_DECL_EXPORT
QQmlFinalizerHook *ritual_cast_QQmlSynchronizer_QQmlFinalizerHook(
    QQmlSynchronizer *self) {
  return static_cast<QQmlFinalizerHook *>(self);
}

//  a Python function taken by a CuteQQmlSynchronizer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSynchronizer(
    QQmlSynchronizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSynchronizer *>(self)->take(key, call);
}
