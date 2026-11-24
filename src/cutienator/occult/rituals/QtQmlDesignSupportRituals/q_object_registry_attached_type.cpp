//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistry_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QObjectRegistryAttachedType that Python can take functions over in. Every QObjectRegistryAttachedType
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQObjectRegistryAttachedTypeCall0)(const void *, int *);
typedef void (*CuteQObjectRegistryAttachedTypeCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistryAttachedTypeCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistryAttachedTypeCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryAttachedTypeCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryAttachedTypeCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryAttachedTypeCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryAttachedTypeCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryAttachedTypeCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQObjectRegistryAttachedType : public QObjectRegistryAttachedType {
public:
  using QObjectRegistryAttachedType::QObjectRegistryAttachedType;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QObjectRegistryAttachedType::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall0 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QObjectRegistryAttachedType::classBegin();
  }

  //  void QObjectRegistryAttachedType::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall1 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QObjectRegistryAttachedType::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall2 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall3 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall4 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall5 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall6 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall7 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQObjectRegistryAttachedTypeCall8 call = reinterpret_cast<CuteQObjectRegistryAttachedTypeCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QObjectRegistryAttachedType::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QObjectRegistryAttachedType10metaObjectEv(
    const QObjectRegistryAttachedType *self) {
  return self->metaObject();
}

//  QString QObjectRegistryAttachedType::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QObjectRegistryAttachedType2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QObjectRegistryAttachedType::tr(s, c, n));
}

//  void QObjectRegistryAttachedType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QObjectRegistryAttachedType22qt_qmlMarker_anonymousEv(
    QObjectRegistryAttachedType *self) {
  self->qt_qmlMarker_anonymous();
}

//  QObjectRegistryAttachedType::QObjectRegistryAttachedType(QObject *parent)
extern "C" Q_DECL_EXPORT
QObjectRegistryAttachedType *ritual_ZN27QObjectRegistryAttachedTypeC1EP7QObject(
    QObject *parent) {
  return new CuteQObjectRegistryAttachedType(parent);
}

//  QObjectRegistryAttachedType::~QObjectRegistryAttachedType()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QObjectRegistryAttachedTypeD1Ev(
    QObjectRegistryAttachedType *self) {
  delete self;
}

//  QString QObjectRegistryAttachedType::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QObjectRegistryAttachedType3keyEv(
    const QObjectRegistryAttachedType *self) {
  return new QString(self->key());
}

//  void QObjectRegistryAttachedType::setKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QObjectRegistryAttachedType6setKeyERK7QString(
    QObjectRegistryAttachedType *self,
    const QString *key) {
  self->setKey(*key);
}

//  void QObjectRegistryAttachedType::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QObjectRegistryAttachedType10classBeginEv(
    QObjectRegistryAttachedType *self) {
  self->classBegin();
}

//  void QObjectRegistryAttachedType::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QObjectRegistryAttachedType17componentCompleteEv(
    QObjectRegistryAttachedType *self) {
  self->componentComplete();
}

//  QObjectRegistryAttachedType as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QObjectRegistryAttachedType_QQmlParserStatus(
    QObjectRegistryAttachedType *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQObjectRegistryAttachedType, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QObjectRegistryAttachedType(
    QObjectRegistryAttachedType *self,
    const char *key,
    void *call) {
  return static_cast<CuteQObjectRegistryAttachedType *>(self)->take(key, call);
}

//  void QObjectRegistryAttachedType::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QObjectRegistryAttachedType10classBeginEv(
    QObjectRegistryAttachedType *self) {
  self->QObjectRegistryAttachedType::classBegin();
}

//  void QObjectRegistryAttachedType::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QObjectRegistryAttachedType17componentCompleteEv(
    QObjectRegistryAttachedType *self) {
  self->QObjectRegistryAttachedType::componentComplete();
}
