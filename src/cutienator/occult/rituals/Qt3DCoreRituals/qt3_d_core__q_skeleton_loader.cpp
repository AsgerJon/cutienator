//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qskeletonloader.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qskeletonloader.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QSkeletonLoader that Python can take functions over in. Every Qt3DCore::QSkeletonLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QSkeletonLoaderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QSkeletonLoaderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSkeletonLoaderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSkeletonLoaderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSkeletonLoaderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSkeletonLoaderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSkeletonLoaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QSkeletonLoader : public Qt3DCore::QSkeletonLoader {
public:
  using Qt3DCore::QSkeletonLoader::QSkeletonLoader;
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
      CuteQt3DCore_QSkeletonLoaderCall0 call = reinterpret_cast<CuteQt3DCore_QSkeletonLoaderCall0>(taken[0]);
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
      CuteQt3DCore_QSkeletonLoaderCall1 call = reinterpret_cast<CuteQt3DCore_QSkeletonLoaderCall1>(taken[1]);
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
      CuteQt3DCore_QSkeletonLoaderCall2 call = reinterpret_cast<CuteQt3DCore_QSkeletonLoaderCall2>(taken[2]);
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
      CuteQt3DCore_QSkeletonLoaderCall3 call = reinterpret_cast<CuteQt3DCore_QSkeletonLoaderCall3>(taken[3]);
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
      CuteQt3DCore_QSkeletonLoaderCall4 call = reinterpret_cast<CuteQt3DCore_QSkeletonLoaderCall4>(taken[4]);
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
      CuteQt3DCore_QSkeletonLoaderCall5 call = reinterpret_cast<CuteQt3DCore_QSkeletonLoaderCall5>(taken[5]);
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
      CuteQt3DCore_QSkeletonLoaderCall6 call = reinterpret_cast<CuteQt3DCore_QSkeletonLoaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QSkeletonLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore15QSkeletonLoader10metaObjectEv(
    const Qt3DCore::QSkeletonLoader *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QSkeletonLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore15QSkeletonLoader11qt_metacastEPKc(
    Qt3DCore::QSkeletonLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QSkeletonLoader::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore15QSkeletonLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QSkeletonLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QSkeletonLoader::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore15QSkeletonLoader2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QSkeletonLoader::tr(s, c, n));
}

//  Qt3DCore::QSkeletonLoader::QSkeletonLoader(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSkeletonLoader *ritual_ZN8Qt3DCore15QSkeletonLoaderC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QSkeletonLoader(parent);
}

//  Qt3DCore::QSkeletonLoader::QSkeletonLoader(const QUrl &source,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSkeletonLoader *ritual_ZN8Qt3DCore15QSkeletonLoaderC1ERK4QUrlPNS_5QNodeE(
    const QUrl *source,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QSkeletonLoader(*source, parent);
}

//  Qt3DCore::QSkeletonLoader::~QSkeletonLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoaderD1Ev(
    Qt3DCore::QSkeletonLoader *self) {
  delete self;
}

//  QUrl Qt3DCore::QSkeletonLoader::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8Qt3DCore15QSkeletonLoader6sourceEv(
    const Qt3DCore::QSkeletonLoader *self) {
  return new QUrl(self->source());
}

//  Status Qt3DCore::QSkeletonLoader::status() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QSkeletonLoader::Status ritual_ZNK8Qt3DCore15QSkeletonLoader6statusEv(
    const Qt3DCore::QSkeletonLoader *self) {
  return self->status();
}

//  bool Qt3DCore::QSkeletonLoader::isCreateJointsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore15QSkeletonLoader21isCreateJointsEnabledEv(
    const Qt3DCore::QSkeletonLoader *self) {
  return self->isCreateJointsEnabled();
}

//  Qt3DCore::QJoint *Qt3DCore::QSkeletonLoader::rootJoint() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QJoint *ritual_ZNK8Qt3DCore15QSkeletonLoader9rootJointEv(
    const Qt3DCore::QSkeletonLoader *self) {
  return self->rootJoint();
}

//  void Qt3DCore::QSkeletonLoader::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoader9setSourceERK4QUrl(
    Qt3DCore::QSkeletonLoader *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void Qt3DCore::QSkeletonLoader::setCreateJointsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoader22setCreateJointsEnabledEb(
    Qt3DCore::QSkeletonLoader *self,
    bool enabled) {
  self->setCreateJointsEnabled(enabled);
}

//  void Qt3DCore::QSkeletonLoader::sourceChanged(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoader13sourceChangedERK4QUrl(
    Qt3DCore::QSkeletonLoader *self,
    const QUrl *source) {
  self->sourceChanged(*source);
}

//  void Qt3DCore::QSkeletonLoader::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoader13statusChangedENS0_6StatusE(
    Qt3DCore::QSkeletonLoader *self,
    Qt3DCore::QSkeletonLoader::Status status) {
  self->statusChanged(status);
}

//  void Qt3DCore::QSkeletonLoader::createJointsEnabledChanged(bool
//      createJointsEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoader26createJointsEnabledChangedEb(
    Qt3DCore::QSkeletonLoader *self,
    bool createJointsEnabled) {
  self->createJointsEnabledChanged(createJointsEnabled);
}

//  void Qt3DCore::QSkeletonLoader::rootJointChanged(Qt3DCore::QJoint
//      *rootJoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoader16rootJointChangedEPNS_6QJointE(
    Qt3DCore::QSkeletonLoader *self,
    Qt3DCore::QJoint *rootJoint) {
  self->rootJointChanged(rootJoint);
}

//  Qt3DCore::QSkeletonLoader::QSkeletonLoader(QSkeletonLoaderPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSkeletonLoader *ritual_ZN8Qt3DCore15QSkeletonLoaderC1ERNS_22QSkeletonLoaderPrivateEPNS_5QNodeE(
    Qt3DCore::QSkeletonLoaderPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QSkeletonLoader(*dd, parent);
}

//  QSkeletonLoaderPrivate *Qt3DCore::QSkeletonLoader::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QSkeletonLoaderPrivate *ritual_ZN8Qt3DCore15QSkeletonLoader6d_funcEv(
    Qt3DCore::QSkeletonLoader *self) {
  return self->d_func();
}

//  const QSkeletonLoaderPrivate *Qt3DCore::QSkeletonLoader::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QSkeletonLoaderPrivate *ritual_ZNK8Qt3DCore15QSkeletonLoader6d_funcEv(
    const Qt3DCore::QSkeletonLoader *self) {
  return self->d_func();
}

//  void Qt3DCore::QSkeletonLoader::setRootJoint(QJoint *rootJoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore15QSkeletonLoader12setRootJointEPNS_6QJointE(
    Qt3DCore::QSkeletonLoader *self,
    Qt3DCore::QJoint *rootJoint) {
  self->setRootJoint(rootJoint);
}

//  a Python function taken by a CuteQt3DCore_QSkeletonLoader, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QSkeletonLoader(
    Qt3DCore::QSkeletonLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QSkeletonLoader *>(self)->take(key, call);
}
