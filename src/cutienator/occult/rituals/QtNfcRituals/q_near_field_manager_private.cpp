//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qnearfieldmanager_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qnearfieldmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNearFieldManagerPrivate that Python can take functions over in. Every QNearFieldManagerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNearFieldManagerPrivateCall0)(const void *, int *);
typedef bool (*CuteQNearFieldManagerPrivateCall1)(const void *, int, int *);
typedef bool (*CuteQNearFieldManagerPrivateCall2)(const void *, int, int *);
typedef void (*CuteQNearFieldManagerPrivateCall3)(const void *, const QString *, int *);
typedef void (*CuteQNearFieldManagerPrivateCall4)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldManagerPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldManagerPrivateCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerPrivateCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerPrivateCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerPrivateCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldManagerPrivateCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNearFieldManagerPrivate : public QNearFieldManagerPrivate {
public:
  using QNearFieldManagerPrivate::QNearFieldManagerPrivate;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK24QNearFieldManagerPrivate9isEnabledEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QNearFieldManagerPrivate11isSupportedEN16QNearFieldTarget12AccessMethodE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QNearFieldManagerPrivate20startTargetDetectionEN16QNearFieldTarget12AccessMethodE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QNearFieldManagerPrivate19stopTargetDetectionERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QNearFieldManagerPrivate18setUserInformationERK7QString")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QNearFieldManagerPrivate::isEnabled() const
  bool isEnabled() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall0 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNearFieldManagerPrivate::isEnabled();
  }

  //  bool
  //      QNearFieldManagerPrivate::isSupported(QNearFieldTarget::AccessMet
  //      hod a0) const
  bool isSupported(QNearFieldTarget::AccessMethod a0) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall1 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall1>(taken[1]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QNearFieldManagerPrivate::isSupported(a0);
  }

  //  bool QNearFieldManagerPrivate::startTargetDetection(QNearFieldTarget:
  //      :AccessMethod a0)
  bool startTargetDetection(QNearFieldTarget::AccessMethod a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall2 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall2>(taken[2]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QNearFieldManagerPrivate::startTargetDetection(a0);
  }

  //  void QNearFieldManagerPrivate::stopTargetDetection(const QString &a0)
  void stopTargetDetection(const QString &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall3 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QNearFieldManagerPrivate::stopTargetDetection(a0);
  }

  //  void QNearFieldManagerPrivate::setUserInformation(const QString &a0)
  void setUserInformation(const QString &a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall4 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall4>(taken[4]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QNearFieldManagerPrivate::setUserInformation(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall5 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall6 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall7 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall8 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall9 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall10 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNearFieldManagerPrivateCall11 call = reinterpret_cast<CuteQNearFieldManagerPrivateCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNearFieldManagerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QNearFieldManagerPrivate10metaObjectEv(
    const QNearFieldManagerPrivate *self) {
  return self->metaObject();
}

//  void *QNearFieldManagerPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QNearFieldManagerPrivate11qt_metacastEPKc(
    QNearFieldManagerPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNearFieldManagerPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QNearFieldManagerPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QNearFieldManagerPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QNearFieldManagerPrivate::~QNearFieldManagerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNearFieldManagerPrivateD1Ev(
    QNearFieldManagerPrivate *self) {
  delete self;
}

//  bool QNearFieldManagerPrivate::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNearFieldManagerPrivate9isEnabledEv(
    const QNearFieldManagerPrivate *self) {
  return self->isEnabled();
}

//  bool QNearFieldManagerPrivate::isSupported(QNearFieldTarget::AccessMethod
//      a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNearFieldManagerPrivate11isSupportedEN16QNearFieldTarget12AccessMethodE(
    const QNearFieldManagerPrivate *self,
    QNearFieldTarget::AccessMethod a0) {
  return self->isSupported(a0);
}

//  bool QNearFieldManagerPrivate::startTargetDetection(QNearFieldTarget::Acc
//      essMethod a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QNearFieldManagerPrivate20startTargetDetectionEN16QNearFieldTarget12AccessMethodE(
    QNearFieldManagerPrivate *self,
    QNearFieldTarget::AccessMethod a0) {
  return self->startTargetDetection(a0);
}

//  void QNearFieldManagerPrivate::stopTargetDetection(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNearFieldManagerPrivate19stopTargetDetectionERK7QString(
    QNearFieldManagerPrivate *self,
    const QString *a0) {
  self->stopTargetDetection(*a0);
}

//  void QNearFieldManagerPrivate::setUserInformation(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNearFieldManagerPrivate18setUserInformationERK7QString(
    QNearFieldManagerPrivate *self,
    const QString *a0) {
  self->setUserInformation(*a0);
}

//  void QNearFieldManagerPrivate::adapterStateChanged(QNearFieldManager::Ada
//      pterState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNearFieldManagerPrivate19adapterStateChangedEN17QNearFieldManager12AdapterStateE(
    QNearFieldManagerPrivate *self,
    QNearFieldManager::AdapterState state) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNearFieldManagerPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "adapterStateChanged(QNearFieldManager::AdapterState)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "adapterStateChanged(QNearFieldManager::AdapterState)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&state)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNearFieldManagerPrivate::targetDetectionStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNearFieldManagerPrivate22targetDetectionStoppedEv(
    QNearFieldManagerPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNearFieldManagerPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetDetectionStopped()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetDetectionStopped()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNearFieldManagerPrivate::targetDetected(QNearFieldTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNearFieldManagerPrivate14targetDetectedEP16QNearFieldTarget(
    QNearFieldManagerPrivate *self,
    QNearFieldTarget *target) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNearFieldManagerPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetDetected(QNearFieldTarget *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetDetected(QNearFieldTarget *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&target)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNearFieldManagerPrivate::targetLost(QNearFieldTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNearFieldManagerPrivate10targetLostEP16QNearFieldTarget(
    QNearFieldManagerPrivate *self,
    QNearFieldTarget *target) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNearFieldManagerPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetLost(QNearFieldTarget *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetLost(QNearFieldTarget *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&target)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQNearFieldManagerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNearFieldManagerPrivate(
    QNearFieldManagerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNearFieldManagerPrivate *>(self)->take(key, call);
}

//  bool QNearFieldManagerPrivate::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QNearFieldManagerPrivate9isEnabledEv(
    const QNearFieldManagerPrivate *self) {
  return self->QNearFieldManagerPrivate::isEnabled();
}

//  bool QNearFieldManagerPrivate::isSupported(QNearFieldTarget::AccessMethod
//      a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QNearFieldManagerPrivate11isSupportedEN16QNearFieldTarget12AccessMethodE(
    const QNearFieldManagerPrivate *self,
    QNearFieldTarget::AccessMethod a0) {
  return self->QNearFieldManagerPrivate::isSupported(a0);
}

//  bool QNearFieldManagerPrivate::startTargetDetection(QNearFieldTarget::Acc
//      essMethod a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QNearFieldManagerPrivate20startTargetDetectionEN16QNearFieldTarget12AccessMethodE(
    QNearFieldManagerPrivate *self,
    QNearFieldTarget::AccessMethod a0) {
  return self->QNearFieldManagerPrivate::startTargetDetection(a0);
}

//  void QNearFieldManagerPrivate::stopTargetDetection(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QNearFieldManagerPrivate19stopTargetDetectionERK7QString(
    QNearFieldManagerPrivate *self,
    const QString *a0) {
  self->QNearFieldManagerPrivate::stopTargetDetection(*a0);
}

//  void QNearFieldManagerPrivate::setUserInformation(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QNearFieldManagerPrivate18setUserInformationERK7QString(
    QNearFieldManagerPrivate *self,
    const QString *a0) {
  self->QNearFieldManagerPrivate::setUserInformation(*a0);
}
