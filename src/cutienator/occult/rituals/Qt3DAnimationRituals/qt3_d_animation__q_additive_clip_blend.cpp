//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qadditiveclipblend.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qadditiveclipblend.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::QAdditiveClipBlend that Python can take functions over in. Every Qt3DAnimation::QAdditiveClipBlend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QAdditiveClipBlendCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QAdditiveClipBlendCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAdditiveClipBlendCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAdditiveClipBlendCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAdditiveClipBlendCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAdditiveClipBlendCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QAdditiveClipBlendCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QAdditiveClipBlend : public Qt3DAnimation::QAdditiveClipBlend {
public:
  using Qt3DAnimation::QAdditiveClipBlend::QAdditiveClipBlend;
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
      CuteQt3DAnimation_QAdditiveClipBlendCall0 call = reinterpret_cast<CuteQt3DAnimation_QAdditiveClipBlendCall0>(taken[0]);
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
      CuteQt3DAnimation_QAdditiveClipBlendCall1 call = reinterpret_cast<CuteQt3DAnimation_QAdditiveClipBlendCall1>(taken[1]);
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
      CuteQt3DAnimation_QAdditiveClipBlendCall2 call = reinterpret_cast<CuteQt3DAnimation_QAdditiveClipBlendCall2>(taken[2]);
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
      CuteQt3DAnimation_QAdditiveClipBlendCall3 call = reinterpret_cast<CuteQt3DAnimation_QAdditiveClipBlendCall3>(taken[3]);
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
      CuteQt3DAnimation_QAdditiveClipBlendCall4 call = reinterpret_cast<CuteQt3DAnimation_QAdditiveClipBlendCall4>(taken[4]);
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
      CuteQt3DAnimation_QAdditiveClipBlendCall5 call = reinterpret_cast<CuteQt3DAnimation_QAdditiveClipBlendCall5>(taken[5]);
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
      CuteQt3DAnimation_QAdditiveClipBlendCall6 call = reinterpret_cast<CuteQt3DAnimation_QAdditiveClipBlendCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QAdditiveClipBlend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend10metaObjectEv(
    const Qt3DAnimation::QAdditiveClipBlend *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QAdditiveClipBlend::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation18QAdditiveClipBlend11qt_metacastEPKc(
    Qt3DAnimation::QAdditiveClipBlend *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QAdditiveClipBlend::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation18QAdditiveClipBlend11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QAdditiveClipBlend *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QAdditiveClipBlend::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation18QAdditiveClipBlend2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAdditiveClipBlend::tr(s, c, n));
}

//  Qt3DAnimation::QAdditiveClipBlend::QAdditiveClipBlend(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAdditiveClipBlend *ritual_ZN13Qt3DAnimation18QAdditiveClipBlendC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QAdditiveClipBlend(parent);
}

//  Qt3DAnimation::QAdditiveClipBlend::~QAdditiveClipBlend()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAdditiveClipBlendD1Ev(
    Qt3DAnimation::QAdditiveClipBlend *self) {
  delete self;
}

//  float Qt3DAnimation::QAdditiveClipBlend::additiveFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend14additiveFactorEv(
    const Qt3DAnimation::QAdditiveClipBlend *self) {
  return self->additiveFactor();
}

//  Qt3DAnimation::QAbstractClipBlendNode
//      *Qt3DAnimation::QAdditiveClipBlend::baseClip() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractClipBlendNode *ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend8baseClipEv(
    const Qt3DAnimation::QAdditiveClipBlend *self) {
  return self->baseClip();
}

//  Qt3DAnimation::QAbstractClipBlendNode
//      *Qt3DAnimation::QAdditiveClipBlend::additiveClip() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractClipBlendNode *ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend12additiveClipEv(
    const Qt3DAnimation::QAdditiveClipBlend *self) {
  return self->additiveClip();
}

//  void Qt3DAnimation::QAdditiveClipBlend::setAdditiveFactor(float
//      additiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAdditiveClipBlend17setAdditiveFactorEf(
    Qt3DAnimation::QAdditiveClipBlend *self,
    float additiveFactor) {
  self->setAdditiveFactor(additiveFactor);
}

//  void Qt3DAnimation::QAdditiveClipBlend::setBaseClip(Qt3DAnimation::QAbstr
//      actClipBlendNode *baseClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAdditiveClipBlend11setBaseClipEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QAdditiveClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *baseClip) {
  self->setBaseClip(baseClip);
}

//  void Qt3DAnimation::QAdditiveClipBlend::setAdditiveClip(Qt3DAnimation::QA
//      bstractClipBlendNode *additiveClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAdditiveClipBlend15setAdditiveClipEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QAdditiveClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *additiveClip) {
  self->setAdditiveClip(additiveClip);
}

//  void Qt3DAnimation::QAdditiveClipBlend::additiveFactorChanged(float
//      additiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAdditiveClipBlend21additiveFactorChangedEf(
    Qt3DAnimation::QAdditiveClipBlend *self,
    float additiveFactor) {
  self->additiveFactorChanged(additiveFactor);
}

//  void Qt3DAnimation::QAdditiveClipBlend::baseClipChanged(Qt3DAnimation::QA
//      bstractClipBlendNode *baseClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAdditiveClipBlend15baseClipChangedEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QAdditiveClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *baseClip) {
  self->baseClipChanged(baseClip);
}

//  void Qt3DAnimation::QAdditiveClipBlend::additiveClipChanged(Qt3DAnimation
//      ::QAbstractClipBlendNode *additiveClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAdditiveClipBlend19additiveClipChangedEPNS_22QAbstractClipBlendNodeE(
    Qt3DAnimation::QAdditiveClipBlend *self,
    Qt3DAnimation::QAbstractClipBlendNode *additiveClip) {
  self->additiveClipChanged(additiveClip);
}

//  Qt3DAnimation::QAdditiveClipBlend::QAdditiveClipBlend(QAdditiveClipBlendP
//      rivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAdditiveClipBlend *ritual_ZN13Qt3DAnimation18QAdditiveClipBlendC1ERNS_25QAdditiveClipBlendPrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QAdditiveClipBlendPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QAdditiveClipBlend(*dd, parent);
}

//  QAdditiveClipBlendPrivate *Qt3DAnimation::QAdditiveClipBlend::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAdditiveClipBlendPrivate *ritual_ZN13Qt3DAnimation18QAdditiveClipBlend6d_funcEv(
    Qt3DAnimation::QAdditiveClipBlend *self) {
  return self->d_func();
}

//  const QAdditiveClipBlendPrivate
//      *Qt3DAnimation::QAdditiveClipBlend::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAdditiveClipBlendPrivate *ritual_ZNK13Qt3DAnimation18QAdditiveClipBlend6d_funcEv(
    const Qt3DAnimation::QAdditiveClipBlend *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QAdditiveClipBlend, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAdditiveClipBlend(
    Qt3DAnimation::QAdditiveClipBlend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAdditiveClipBlend *>(self)->take(key, call);
}
