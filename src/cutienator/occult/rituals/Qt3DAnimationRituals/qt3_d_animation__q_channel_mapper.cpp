//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qchannelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qchannelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DAnimation/Qt3DAnimation>

//  A Qt3DAnimation::QChannelMapper that Python can take functions over in. Every Qt3DAnimation::QChannelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QChannelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QChannelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QChannelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QChannelMapper : public Qt3DAnimation::QChannelMapper {
public:
  using Qt3DAnimation::QChannelMapper::QChannelMapper;
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
      CuteQt3DAnimation_QChannelMapperCall0 call = reinterpret_cast<CuteQt3DAnimation_QChannelMapperCall0>(taken[0]);
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
      CuteQt3DAnimation_QChannelMapperCall1 call = reinterpret_cast<CuteQt3DAnimation_QChannelMapperCall1>(taken[1]);
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
      CuteQt3DAnimation_QChannelMapperCall2 call = reinterpret_cast<CuteQt3DAnimation_QChannelMapperCall2>(taken[2]);
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
      CuteQt3DAnimation_QChannelMapperCall3 call = reinterpret_cast<CuteQt3DAnimation_QChannelMapperCall3>(taken[3]);
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
      CuteQt3DAnimation_QChannelMapperCall4 call = reinterpret_cast<CuteQt3DAnimation_QChannelMapperCall4>(taken[4]);
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
      CuteQt3DAnimation_QChannelMapperCall5 call = reinterpret_cast<CuteQt3DAnimation_QChannelMapperCall5>(taken[5]);
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
      CuteQt3DAnimation_QChannelMapperCall6 call = reinterpret_cast<CuteQt3DAnimation_QChannelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QChannelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation14QChannelMapper10metaObjectEv(
    const Qt3DAnimation::QChannelMapper *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QChannelMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation14QChannelMapper11qt_metacastEPKc(
    Qt3DAnimation::QChannelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QChannelMapper::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation14QChannelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QChannelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QChannelMapper::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation14QChannelMapper2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QChannelMapper::tr(s, c, n));
}

//  Qt3DAnimation::QChannelMapper::QChannelMapper(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapper *ritual_ZN13Qt3DAnimation14QChannelMapperC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QChannelMapper(parent);
}

//  Qt3DAnimation::QChannelMapper::~QChannelMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QChannelMapperD1Ev(
    Qt3DAnimation::QChannelMapper *self) {
  delete self;
}

//  void Qt3DAnimation::QChannelMapper::addMapping(QAbstractChannelMapping
//      *mapping)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QChannelMapper10addMappingEPNS_23QAbstractChannelMappingE(
    Qt3DAnimation::QChannelMapper *self,
    Qt3DAnimation::QAbstractChannelMapping *mapping) {
  self->addMapping(mapping);
}

//  void Qt3DAnimation::QChannelMapper::removeMapping(QAbstractChannelMapping
//      *mapping)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QChannelMapper13removeMappingEPNS_23QAbstractChannelMappingE(
    Qt3DAnimation::QChannelMapper *self,
    Qt3DAnimation::QAbstractChannelMapping *mapping) {
  self->removeMapping(mapping);
}

//  QList<QAbstractChannelMapping *>
//      Qt3DAnimation::QChannelMapper::mappings() const
extern "C" Q_DECL_EXPORT
QList<Qt3DAnimation::QAbstractChannelMapping *> *ritual_ZNK13Qt3DAnimation14QChannelMapper8mappingsEv(
    const Qt3DAnimation::QChannelMapper *self) {
  return new QList<Qt3DAnimation::QAbstractChannelMapping *>(
      self->mappings());
}

//  Qt3DAnimation::QChannelMapper::QChannelMapper(QChannelMapperPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapper *ritual_ZN13Qt3DAnimation14QChannelMapperC1ERNS_21QChannelMapperPrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QChannelMapperPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QChannelMapper(*dd, parent);
}

//  QChannelMapperPrivate *Qt3DAnimation::QChannelMapper::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapperPrivate *ritual_ZN13Qt3DAnimation14QChannelMapper6d_funcEv(
    Qt3DAnimation::QChannelMapper *self) {
  return self->d_func();
}

//  const QChannelMapperPrivate *Qt3DAnimation::QChannelMapper::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QChannelMapperPrivate *ritual_ZNK13Qt3DAnimation14QChannelMapper6d_funcEv(
    const Qt3DAnimation::QChannelMapper *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QChannelMapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QChannelMapper(
    Qt3DAnimation::QChannelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QChannelMapper *>(self)->take(key, call);
}

//  a QList<Qt3DAnimation::QAbstractChannelMapping *> a ritual of
//      Qt3DAnimation::QChannelMapper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QChannelMapper__QList_Qt3DAnimation_QAbstractChannelMapping(
    QList<Qt3DAnimation::QAbstractChannelMapping *> *self) {
  delete self;
}
