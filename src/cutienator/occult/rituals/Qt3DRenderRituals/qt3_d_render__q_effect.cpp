//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qeffect.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qeffect.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QEffect that Python can take functions over in. Every Qt3DRender::QEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QEffectCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QEffectCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEffectCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEffectCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEffectCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEffectCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QEffectCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QEffect : public Qt3DRender::QEffect {
public:
  using Qt3DRender::QEffect::QEffect;
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
      CuteQt3DRender_QEffectCall0 call = reinterpret_cast<CuteQt3DRender_QEffectCall0>(taken[0]);
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
      CuteQt3DRender_QEffectCall1 call = reinterpret_cast<CuteQt3DRender_QEffectCall1>(taken[1]);
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
      CuteQt3DRender_QEffectCall2 call = reinterpret_cast<CuteQt3DRender_QEffectCall2>(taken[2]);
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
      CuteQt3DRender_QEffectCall3 call = reinterpret_cast<CuteQt3DRender_QEffectCall3>(taken[3]);
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
      CuteQt3DRender_QEffectCall4 call = reinterpret_cast<CuteQt3DRender_QEffectCall4>(taken[4]);
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
      CuteQt3DRender_QEffectCall5 call = reinterpret_cast<CuteQt3DRender_QEffectCall5>(taken[5]);
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
      CuteQt3DRender_QEffectCall6 call = reinterpret_cast<CuteQt3DRender_QEffectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender7QEffect10metaObjectEv(
    const Qt3DRender::QEffect *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QEffect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender7QEffect11qt_metacastEPKc(
    Qt3DRender::QEffect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QEffect::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender7QEffect11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QEffect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender7QEffect2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QEffect::tr(s, c, n));
}

//  Qt3DRender::QEffect::QEffect(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QEffect *ritual_ZN10Qt3DRender7QEffectC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QEffect(parent);
}

//  Qt3DRender::QEffect::~QEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QEffectD1Ev(Qt3DRender::QEffect *self) {
  delete self;
}

//  void Qt3DRender::QEffect::addParameter(QParameter *parameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QEffect12addParameterEPNS_10QParameterE(
    Qt3DRender::QEffect *self,
    Qt3DRender::QParameter *parameter) {
  self->addParameter(parameter);
}

//  void Qt3DRender::QEffect::removeParameter(QParameter *parameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QEffect15removeParameterEPNS_10QParameterE(
    Qt3DRender::QEffect *self,
    Qt3DRender::QParameter *parameter) {
  self->removeParameter(parameter);
}

//  QList<QParameter *> Qt3DRender::QEffect::parameters() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QParameter *> *ritual_ZNK10Qt3DRender7QEffect10parametersEv(
    const Qt3DRender::QEffect *self) {
  return new QList<Qt3DRender::QParameter *>(self->parameters());
}

//  void Qt3DRender::QEffect::addTechnique(QTechnique *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QEffect12addTechniqueEPNS_10QTechniqueE(
    Qt3DRender::QEffect *self,
    Qt3DRender::QTechnique *t) {
  self->addTechnique(t);
}

//  void Qt3DRender::QEffect::removeTechnique(QTechnique *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QEffect15removeTechniqueEPNS_10QTechniqueE(
    Qt3DRender::QEffect *self,
    Qt3DRender::QTechnique *t) {
  self->removeTechnique(t);
}

//  QList<QTechnique *> Qt3DRender::QEffect::techniques() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QTechnique *> *ritual_ZNK10Qt3DRender7QEffect10techniquesEv(
    const Qt3DRender::QEffect *self) {
  return new QList<Qt3DRender::QTechnique *>(self->techniques());
}

//  Qt3DRender::QEffect::QEffect(QEffectPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QEffect *ritual_ZN10Qt3DRender7QEffectC1ERNS_14QEffectPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QEffectPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QEffect(*dd, parent);
}

//  QEffectPrivate *Qt3DRender::QEffect::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QEffectPrivate *ritual_ZN10Qt3DRender7QEffect6d_funcEv(
    Qt3DRender::QEffect *self) {
  return self->d_func();
}

//  const QEffectPrivate *Qt3DRender::QEffect::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QEffectPrivate *ritual_ZNK10Qt3DRender7QEffect6d_funcEv(
    const Qt3DRender::QEffect *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QEffect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QEffect(
    Qt3DRender::QEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QEffect *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QParameter *> a ritual of Qt3DRender::QEffect gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QEffect__QList_Qt3DRender_QParameter(
    QList<Qt3DRender::QParameter *> *self) {
  delete self;
}

//  a QList<Qt3DRender::QTechnique *> a ritual of Qt3DRender::QEffect gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QEffect__QList_Qt3DRender_QTechnique(
    QList<Qt3DRender::QTechnique *> *self) {
  delete self;
}
