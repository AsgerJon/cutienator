//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickAnima
//  tion/6.12.0/Qt3DQuickAnimation/private/quick3dchannelmapper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/qt3dquickanimation_global_p.h>
#include <Qt3DQuickAnimation/Qt3DQuickAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/quick3dchannelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DAnimation/Qt3DAnimation>

//  A Qt3DAnimation::Animation::Quick::Quick3DChannelMapper that Python can take functions over in. Every Qt3DAnimation::Animation::Quick::Quick3DChannelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapper : public Qt3DAnimation::Animation::Quick::Quick3DChannelMapper {
public:
  using Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::Quick3DChannelMapper;
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
      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall0>(taken[0]);
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
      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall1 call = reinterpret_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall1>(taken[1]);
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
      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall2 call = reinterpret_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall2>(taken[2]);
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
      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall3 call = reinterpret_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall3>(taken[3]);
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
      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall4 call = reinterpret_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall4>(taken[4]);
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
      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall5 call = reinterpret_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall5>(taken[5]);
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
      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall6 call = reinterpret_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation9Animation5Quick20Quick3DChannelMapper10metaObjectEv(
    const Qt3DAnimation::Animation::Quick::Quick3DChannelMapper *self) {
  return self->metaObject();
}

//  void
//      *Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::qt_metacast(c
//      onst char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation9Animation5Quick20Quick3DChannelMapper11qt_metacastEPKc(
    Qt3DAnimation::Animation::Quick::Quick3DChannelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::qt_metacall(QM
//      etaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation9Animation5Quick20Quick3DChannelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::Animation::Quick::Quick3DChannelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::tr(const
//      char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation9Animation5Quick20Quick3DChannelMapper2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::tr(
          s,
          c,
          n));
}

//  Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::Quick3DChannelMapp
//      er(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Quick::Quick3DChannelMapper *ritual_ZN13Qt3DAnimation9Animation5Quick20Quick3DChannelMapperC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapper(parent);
}

//  QChannelMapper
//      *Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::parentMapper(
//      ) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapper *ritual_ZNK13Qt3DAnimation9Animation5Quick20Quick3DChannelMapper12parentMapperEv(
    const Qt3DAnimation::Animation::Quick::Quick3DChannelMapper *self) {
  return self->parentMapper();
}

//  QQmlListProperty<QAbstractChannelMapping>
//      Qt3DAnimation::Animation::Quick::Quick3DChannelMapper::qmlMappings()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DAnimation::QAbstractChannelMapping> *ritual_ZN13Qt3DAnimation9Animation5Quick20Quick3DChannelMapper11qmlMappingsEv(
    Qt3DAnimation::Animation::Quick::Quick3DChannelMapper *self) {
  return new QQmlListProperty<Qt3DAnimation::QAbstractChannelMapping>(
      self->qmlMappings());
}

//  a Python function taken by a
//      CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_Quick_Quick3DChannelMapper(
    Qt3DAnimation::Animation::Quick::Quick3DChannelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_Quick_Quick3DChannelMapper *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DAnimation::QAbstractChannelMapping> a ritual of
//      Qt3DAnimation::Animation::Quick::Quick3DChannelMapper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_Quick_Quick3DChannelMapper__QQmlListProperty_Qt3DAnimation_QAbstractChannelMapping(
    QQmlListProperty<Qt3DAnimation::QAbstractChannelMapping> *self) {
  delete self;
}
