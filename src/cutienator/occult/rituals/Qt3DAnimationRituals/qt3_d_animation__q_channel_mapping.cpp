//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qchannelmapping.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qchannelmapping.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::QChannelMapping that Python can take functions over in. Every Qt3DAnimation::QChannelMapping
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QChannelMappingCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QChannelMappingCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMappingCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMappingCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMappingCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMappingCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMappingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QChannelMapping : public Qt3DAnimation::QChannelMapping {
public:
  using Qt3DAnimation::QChannelMapping::QChannelMapping;
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
      CuteQt3DAnimation_QChannelMappingCall0 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingCall0>(taken[0]);
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
      CuteQt3DAnimation_QChannelMappingCall1 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingCall1>(taken[1]);
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
      CuteQt3DAnimation_QChannelMappingCall2 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingCall2>(taken[2]);
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
      CuteQt3DAnimation_QChannelMappingCall3 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingCall3>(taken[3]);
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
      CuteQt3DAnimation_QChannelMappingCall4 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingCall4>(taken[4]);
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
      CuteQt3DAnimation_QChannelMappingCall5 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingCall5>(taken[5]);
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
      CuteQt3DAnimation_QChannelMappingCall6 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QChannelMapping::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation15QChannelMapping10metaObjectEv(
    const Qt3DAnimation::QChannelMapping *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QChannelMapping::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation15QChannelMapping11qt_metacastEPKc(
    Qt3DAnimation::QChannelMapping *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QChannelMapping::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation15QChannelMapping11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QChannelMapping *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QChannelMapping::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation15QChannelMapping2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QChannelMapping::tr(s, c, n));
}

//  Qt3DAnimation::QChannelMapping::QChannelMapping(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapping *ritual_ZN13Qt3DAnimation15QChannelMappingC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QChannelMapping(parent);
}

//  Qt3DAnimation::QChannelMapping::~QChannelMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QChannelMappingD1Ev(
    Qt3DAnimation::QChannelMapping *self) {
  delete self;
}

//  QString Qt3DAnimation::QChannelMapping::channelName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation15QChannelMapping11channelNameEv(
    const Qt3DAnimation::QChannelMapping *self) {
  return new QString(self->channelName());
}

//  Qt3DCore::QNode *Qt3DAnimation::QChannelMapping::target() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK13Qt3DAnimation15QChannelMapping6targetEv(
    const Qt3DAnimation::QChannelMapping *self) {
  return self->target();
}

//  QString Qt3DAnimation::QChannelMapping::property() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation15QChannelMapping8propertyEv(
    const Qt3DAnimation::QChannelMapping *self) {
  return new QString(self->property());
}

//  void Qt3DAnimation::QChannelMapping::setChannelName(const QString
//      &channelName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QChannelMapping14setChannelNameERK7QString(
    Qt3DAnimation::QChannelMapping *self,
    const QString *channelName) {
  self->setChannelName(*channelName);
}

//  void Qt3DAnimation::QChannelMapping::setTarget(Qt3DCore::QNode *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QChannelMapping9setTargetEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QChannelMapping *self,
    Qt3DCore::QNode *target) {
  self->setTarget(target);
}

//  void Qt3DAnimation::QChannelMapping::setProperty(const QString &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QChannelMapping11setPropertyERK7QString(
    Qt3DAnimation::QChannelMapping *self,
    const QString *property) {
  self->setProperty(*property);
}

//  void Qt3DAnimation::QChannelMapping::channelNameChanged(QString
//      channelName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QChannelMapping18channelNameChangedE7QString(
    Qt3DAnimation::QChannelMapping *self,
    const QString *channelName) {
  self->channelNameChanged(*channelName);
}

//  void Qt3DAnimation::QChannelMapping::targetChanged(Qt3DCore::QNode
//      *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QChannelMapping13targetChangedEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QChannelMapping *self,
    Qt3DCore::QNode *target) {
  self->targetChanged(target);
}

//  void Qt3DAnimation::QChannelMapping::propertyChanged(QString property)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QChannelMapping15propertyChangedE7QString(
    Qt3DAnimation::QChannelMapping *self,
    const QString *property) {
  self->propertyChanged(*property);
}

//  Qt3DAnimation::QChannelMapping::QChannelMapping(QChannelMappingPrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapping *ritual_ZN13Qt3DAnimation15QChannelMappingC1ERNS_22QChannelMappingPrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QChannelMappingPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QChannelMapping(*dd, parent);
}

//  QChannelMappingPrivate *Qt3DAnimation::QChannelMapping::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMappingPrivate *ritual_ZN13Qt3DAnimation15QChannelMapping6d_funcEv(
    Qt3DAnimation::QChannelMapping *self) {
  return self->d_func();
}

//  const QChannelMappingPrivate *Qt3DAnimation::QChannelMapping::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QChannelMappingPrivate *ritual_ZNK13Qt3DAnimation15QChannelMapping6d_funcEv(
    const Qt3DAnimation::QChannelMapping *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QChannelMapping, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QChannelMapping(
    Qt3DAnimation::QChannelMapping *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QChannelMapping *>(self)->take(key, call);
}
