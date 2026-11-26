//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qlerpclipblend.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qlerpclipblend.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::QLerpClipBlend that Python can take functions over in. Every Qt3DAnimation::QLerpClipBlend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QLerpClipBlendCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QLerpClipBlendCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QLerpClipBlendCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QLerpClipBlendCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QLerpClipBlendCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QLerpClipBlendCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QLerpClipBlendCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QLerpClipBlend : public Qt3DAnimation::QLerpClipBlend {
public:
  using Qt3DAnimation::QLerpClipBlend::QLerpClipBlend;
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
      CuteQt3DAnimation_QLerpClipBlendCall0 call = reinterpret_cast<CuteQt3DAnimation_QLerpClipBlendCall0>(taken[0]);
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
      CuteQt3DAnimation_QLerpClipBlendCall1 call = reinterpret_cast<CuteQt3DAnimation_QLerpClipBlendCall1>(taken[1]);
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
      CuteQt3DAnimation_QLerpClipBlendCall2 call = reinterpret_cast<CuteQt3DAnimation_QLerpClipBlendCall2>(taken[2]);
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
      CuteQt3DAnimation_QLerpClipBlendCall3 call = reinterpret_cast<CuteQt3DAnimation_QLerpClipBlendCall3>(taken[3]);
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
      CuteQt3DAnimation_QLerpClipBlendCall4 call = reinterpret_cast<CuteQt3DAnimation_QLerpClipBlendCall4>(taken[4]);
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
      CuteQt3DAnimation_QLerpClipBlendCall5 call = reinterpret_cast<CuteQt3DAnimation_QLerpClipBlendCall5>(taken[5]);
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
      CuteQt3DAnimation_QLerpClipBlendCall6 call = reinterpret_cast<CuteQt3DAnimation_QLerpClipBlendCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QLerpClipBlend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation14QLerpClipBlend10metaObjectEv(
    const Qt3DAnimation::QLerpClipBlend *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QLerpClipBlend::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation14QLerpClipBlend11qt_metacastEPKc(
    Qt3DAnimation::QLerpClipBlend *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QLerpClipBlend::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation14QLerpClipBlend11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QLerpClipBlend *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QLerpClipBlend::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation14QLerpClipBlend2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QLerpClipBlend::tr(s, c, n));
}

//  Qt3DAnimation::QLerpClipBlend::QLerpClipBlend(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QLerpClipBlend *ritual_ZN13Qt3DAnimation14QLerpClipBlendC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QLerpClipBlend(parent);
}

//  Qt3DAnimation::QLerpClipBlend::~QLerpClipBlend()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QLerpClipBlendD1Ev(
    Qt3DAnimation::QLerpClipBlend *self) {
  delete self;
}

//  float Qt3DAnimation::QLerpClipBlend::blendFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation14QLerpClipBlend11blendFactorEv(
    const Qt3DAnimation::QLerpClipBlend *self) {
  return self->blendFactor();
}

//  Qt3DAnimation::QAbstractClipBlendNode
//      *Qt3DAnimation::QLerpClipBlend::startClip() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractClipBlendNode *ritual_ZNK13Qt3DAnimation14QLerpClipBlend9startClipEv(
    const Qt3DAnimation::QLerpClipBlend *self) {
  return self->startClip();
}

//  Qt3DAnimation::QAbstractClipBlendNode
//      *Qt3DAnimation::QLerpClipBlend::endClip() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractClipBlendNode *ritual_ZNK13Qt3DAnimation14QLerpClipBlend7endClipEv(
    const Qt3DAnimation::QLerpClipBlend *self) {
  return self->endClip();
}

//  void Qt3DAnimation::QLerpClipBlend::setBlendFactor(float blendFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QLerpClipBlend14setBlendFactorEf(
    Qt3DAnimation::QLerpClipBlend *self,
    float blendFactor) {
  self->setBlendFactor(blendFactor);
}

//  void Qt3DAnimation::QLerpClipBlend::setStartClip(Qt3DAnimation::QAbstract
//      ClipBlendNode *startClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QLerpClipBlend12setStartClipEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QLerpClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *startClip) {
  self->setStartClip(startClip);
}

//  void Qt3DAnimation::QLerpClipBlend::setEndClip(Qt3DAnimation::QAbstractCl
//      ipBlendNode *endClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QLerpClipBlend10setEndClipEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QLerpClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *endClip) {
  self->setEndClip(endClip);
}

//  void Qt3DAnimation::QLerpClipBlend::blendFactorChanged(float blendFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QLerpClipBlend18blendFactorChangedEf(
    Qt3DAnimation::QLerpClipBlend *self,
    float blendFactor) {
  self->blendFactorChanged(blendFactor);
}

//  void Qt3DAnimation::QLerpClipBlend::startClipChanged(Qt3DAnimation::QAbst
//      ractClipBlendNode *startClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QLerpClipBlend16startClipChangedEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QLerpClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *startClip) {
  self->startClipChanged(startClip);
}

//  void Qt3DAnimation::QLerpClipBlend::endClipChanged(Qt3DAnimation::QAbstra
//      ctClipBlendNode *endClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation14QLerpClipBlend14endClipChangedEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QLerpClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *endClip) {
  self->endClipChanged(endClip);
}

//  Qt3DAnimation::QLerpClipBlend::QLerpClipBlend(QLerpClipBlendPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QLerpClipBlend *ritual_ZN13Qt3DAnimation14QLerpClipBlendC1ERNS_21QLerpClipBlendPrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QLerpClipBlendPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QLerpClipBlend(*dd, parent);
}

//  QLerpClipBlendPrivate *Qt3DAnimation::QLerpClipBlend::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QLerpClipBlendPrivate *ritual_ZN13Qt3DAnimation14QLerpClipBlend6d_funcEv(
    Qt3DAnimation::QLerpClipBlend *self) {
  return self->d_func();
}

//  const QLerpClipBlendPrivate *Qt3DAnimation::QLerpClipBlend::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QLerpClipBlendPrivate *ritual_ZNK13Qt3DAnimation14QLerpClipBlend6d_funcEv(
    const Qt3DAnimation::QLerpClipBlend *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QLerpClipBlend, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QLerpClipBlend(
    Qt3DAnimation::QLerpClipBlend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QLerpClipBlend *>(self)->take(key, call);
}
