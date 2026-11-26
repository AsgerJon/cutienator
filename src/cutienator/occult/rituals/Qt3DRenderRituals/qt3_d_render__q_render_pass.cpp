//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrenderpass.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrenderpass.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QRenderPass that Python can take functions over in. Every Qt3DRender::QRenderPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderPassCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderPassCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderPassCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderPassCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderPassCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderPassCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderPassCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderPass : public Qt3DRender::QRenderPass {
public:
  using Qt3DRender::QRenderPass::QRenderPass;
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
      CuteQt3DRender_QRenderPassCall0 call = reinterpret_cast<CuteQt3DRender_QRenderPassCall0>(taken[0]);
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
      CuteQt3DRender_QRenderPassCall1 call = reinterpret_cast<CuteQt3DRender_QRenderPassCall1>(taken[1]);
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
      CuteQt3DRender_QRenderPassCall2 call = reinterpret_cast<CuteQt3DRender_QRenderPassCall2>(taken[2]);
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
      CuteQt3DRender_QRenderPassCall3 call = reinterpret_cast<CuteQt3DRender_QRenderPassCall3>(taken[3]);
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
      CuteQt3DRender_QRenderPassCall4 call = reinterpret_cast<CuteQt3DRender_QRenderPassCall4>(taken[4]);
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
      CuteQt3DRender_QRenderPassCall5 call = reinterpret_cast<CuteQt3DRender_QRenderPassCall5>(taken[5]);
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
      CuteQt3DRender_QRenderPassCall6 call = reinterpret_cast<CuteQt3DRender_QRenderPassCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderPass::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender11QRenderPass10metaObjectEv(
    const Qt3DRender::QRenderPass *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderPass::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender11QRenderPass11qt_metacastEPKc(
    Qt3DRender::QRenderPass *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderPass::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender11QRenderPass11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderPass *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRenderPass::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender11QRenderPass2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderPass::tr(s, c, n));
}

//  Qt3DRender::QRenderPass::QRenderPass(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderPass *ritual_ZN10Qt3DRender11QRenderPassC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderPass(parent);
}

//  Qt3DRender::QRenderPass::~QRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPassD1Ev(Qt3DRender::QRenderPass *self) {
  delete self;
}

//  QShaderProgram *Qt3DRender::QRenderPass::shaderProgram() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram *ritual_ZNK10Qt3DRender11QRenderPass13shaderProgramEv(
    const Qt3DRender::QRenderPass *self) {
  return self->shaderProgram();
}

//  void Qt3DRender::QRenderPass::addFilterKey(QFilterKey *filterKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass12addFilterKeyEPNS_10QFilterKeyE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QFilterKey *filterKey) {
  self->addFilterKey(filterKey);
}

//  void Qt3DRender::QRenderPass::removeFilterKey(QFilterKey *filterKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass15removeFilterKeyEPNS_10QFilterKeyE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QFilterKey *filterKey) {
  self->removeFilterKey(filterKey);
}

//  QList<QFilterKey *> Qt3DRender::QRenderPass::filterKeys() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QFilterKey *> *ritual_ZNK10Qt3DRender11QRenderPass10filterKeysEv(
    const Qt3DRender::QRenderPass *self) {
  return new QList<Qt3DRender::QFilterKey *>(self->filterKeys());
}

//  void Qt3DRender::QRenderPass::addRenderState(QRenderState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass14addRenderStateEPNS_12QRenderStateE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QRenderState *state) {
  self->addRenderState(state);
}

//  void Qt3DRender::QRenderPass::removeRenderState(QRenderState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass17removeRenderStateEPNS_12QRenderStateE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QRenderState *state) {
  self->removeRenderState(state);
}

//  QList<QRenderState *> Qt3DRender::QRenderPass::renderStates() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QRenderState *> *ritual_ZNK10Qt3DRender11QRenderPass12renderStatesEv(
    const Qt3DRender::QRenderPass *self) {
  return new QList<Qt3DRender::QRenderState *>(self->renderStates());
}

//  void Qt3DRender::QRenderPass::addParameter(QParameter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass12addParameterEPNS_10QParameterE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QParameter *p) {
  self->addParameter(p);
}

//  void Qt3DRender::QRenderPass::removeParameter(QParameter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass15removeParameterEPNS_10QParameterE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QParameter *p) {
  self->removeParameter(p);
}

//  QList<QParameter *> Qt3DRender::QRenderPass::parameters() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QParameter *> *ritual_ZNK10Qt3DRender11QRenderPass10parametersEv(
    const Qt3DRender::QRenderPass *self) {
  return new QList<Qt3DRender::QParameter *>(self->parameters());
}

//  void Qt3DRender::QRenderPass::setShaderProgram(QShaderProgram
//      *shaderProgram)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass16setShaderProgramEPNS_14QShaderProgramE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QShaderProgram *shaderProgram) {
  self->setShaderProgram(shaderProgram);
}

//  void Qt3DRender::QRenderPass::shaderProgramChanged(QShaderProgram
//      *shaderProgram)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QRenderPass20shaderProgramChangedEPNS_14QShaderProgramE(
    Qt3DRender::QRenderPass *self,
    Qt3DRender::QShaderProgram *shaderProgram) {
  self->shaderProgramChanged(shaderProgram);
}

//  Qt3DRender::QRenderPass::QRenderPass(QRenderPassPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderPass *ritual_ZN10Qt3DRender11QRenderPassC1ERNS_18QRenderPassPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QRenderPassPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderPass(*dd, parent);
}

//  QRenderPassPrivate *Qt3DRender::QRenderPass::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderPassPrivate *ritual_ZN10Qt3DRender11QRenderPass6d_funcEv(
    Qt3DRender::QRenderPass *self) {
  return self->d_func();
}

//  const QRenderPassPrivate *Qt3DRender::QRenderPass::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderPassPrivate *ritual_ZNK10Qt3DRender11QRenderPass6d_funcEv(
    const Qt3DRender::QRenderPass *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderPass, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderPass(
    Qt3DRender::QRenderPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderPass *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QFilterKey *> a ritual of Qt3DRender::QRenderPass
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QRenderPass__QList_Qt3DRender_QFilterKey(
    QList<Qt3DRender::QFilterKey *> *self) {
  delete self;
}

//  a QList<Qt3DRender::QRenderState *> a ritual of Qt3DRender::QRenderPass
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QRenderPass__QList_Qt3DRender_QRenderState(
    QList<Qt3DRender::QRenderState *> *self) {
  delete self;
}

//  a QList<Qt3DRender::QParameter *> a ritual of Qt3DRender::QRenderPass
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QRenderPass__QList_Qt3DRender_QParameter(
    QList<Qt3DRender::QParameter *> *self) {
  delete self;
}
