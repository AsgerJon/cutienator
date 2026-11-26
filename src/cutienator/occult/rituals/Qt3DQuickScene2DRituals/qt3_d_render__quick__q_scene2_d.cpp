//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/qscene2d.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#include <Qt3DQuickScene2D/qscene2d.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Quick::QScene2D that Python can take functions over in. Every Qt3DRender::Quick::QScene2D
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Quick_QScene2DCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Quick_QScene2DCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_QScene2DCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_QScene2DCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_QScene2DCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_QScene2DCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_QScene2DCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Quick_QScene2D : public Qt3DRender::Quick::QScene2D {
public:
  using Qt3DRender::Quick::QScene2D::QScene2D;
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
      CuteQt3DRender_Quick_QScene2DCall0 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DCall0>(taken[0]);
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
      CuteQt3DRender_Quick_QScene2DCall1 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DCall1>(taken[1]);
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
      CuteQt3DRender_Quick_QScene2DCall2 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DCall2>(taken[2]);
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
      CuteQt3DRender_Quick_QScene2DCall3 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DCall3>(taken[3]);
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
      CuteQt3DRender_Quick_QScene2DCall4 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DCall4>(taken[4]);
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
      CuteQt3DRender_Quick_QScene2DCall5 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DCall5>(taken[5]);
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
      CuteQt3DRender_Quick_QScene2DCall6 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::Quick::QScene2D::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender5Quick8QScene2D10metaObjectEv(
    const Qt3DRender::Quick::QScene2D *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Quick::QScene2D::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender5Quick8QScene2D11qt_metacastEPKc(
    Qt3DRender::Quick::QScene2D *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Quick::QScene2D::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender5Quick8QScene2D11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Quick::QScene2D *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Quick::QScene2D::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender5Quick8QScene2D2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::Quick::QScene2D::tr(s, c, n));
}

//  Qt3DRender::Quick::QScene2D::QScene2D(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::QScene2D *ritual_ZN10Qt3DRender5Quick8QScene2DC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_Quick_QScene2D(parent);
}

//  Qt3DRender::QRenderTargetOutput *Qt3DRender::Quick::QScene2D::output()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput *ritual_ZNK10Qt3DRender5Quick8QScene2D6outputEv(
    const Qt3DRender::Quick::QScene2D *self) {
  return self->output();
}

//  QScene2D::RenderPolicy Qt3DRender::Quick::QScene2D::renderPolicy() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::QScene2D::RenderPolicy ritual_ZNK10Qt3DRender5Quick8QScene2D12renderPolicyEv(
    const Qt3DRender::Quick::QScene2D *self) {
  return self->renderPolicy();
}

//  QQuickItem *Qt3DRender::Quick::QScene2D::item() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10Qt3DRender5Quick8QScene2D4itemEv(
    const Qt3DRender::Quick::QScene2D *self) {
  return self->item();
}

//  bool Qt3DRender::Quick::QScene2D::isMouseEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender5Quick8QScene2D14isMouseEnabledEv(
    const Qt3DRender::Quick::QScene2D *self) {
  return self->isMouseEnabled();
}

//  QList<Qt3DCore::QEntity *> Qt3DRender::Quick::QScene2D::entities() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QEntity *> *ritual_ZNK10Qt3DRender5Quick8QScene2D8entitiesEv(
    const Qt3DRender::Quick::QScene2D *self) {
  return new QList<Qt3DCore::QEntity *>(self->entities());
}

//  void Qt3DRender::Quick::QScene2D::addEntity(Qt3DCore::QEntity *entity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D9addEntityEPN8Qt3DCore7QEntityE(
    Qt3DRender::Quick::QScene2D *self,
    Qt3DCore::QEntity *entity) {
  self->addEntity(entity);
}

//  void Qt3DRender::Quick::QScene2D::removeEntity(Qt3DCore::QEntity *entity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D12removeEntityEPN8Qt3DCore7QEntityE(
    Qt3DRender::Quick::QScene2D *self,
    Qt3DCore::QEntity *entity) {
  self->removeEntity(entity);
}

//  void
//      Qt3DRender::Quick::QScene2D::setOutput(Qt3DRender::QRenderTargetOutpu
//      t *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D9setOutputEPNS_19QRenderTargetOutputE(
    Qt3DRender::Quick::QScene2D *self,
    Qt3DRender::QRenderTargetOutput *output) {
  self->setOutput(output);
}

//  void Qt3DRender::Quick::QScene2D::setRenderPolicy(QScene2D::RenderPolicy
//      policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D15setRenderPolicyENS1_12RenderPolicyE(
    Qt3DRender::Quick::QScene2D *self,
    Qt3DRender::Quick::QScene2D::RenderPolicy policy) {
  self->setRenderPolicy(policy);
}

//  void Qt3DRender::Quick::QScene2D::setItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D7setItemEP10QQuickItem(
    Qt3DRender::Quick::QScene2D *self,
    QQuickItem *item) {
  self->setItem(item);
}

//  void Qt3DRender::Quick::QScene2D::setMouseEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D15setMouseEnabledEb(
    Qt3DRender::Quick::QScene2D *self,
    bool enabled) {
  self->setMouseEnabled(enabled);
}

//  void Qt3DRender::Quick::QScene2D::outputChanged(Qt3DRender::QRenderTarget
//      Output *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D13outputChangedEPNS_19QRenderTargetOutputE(
    Qt3DRender::Quick::QScene2D *self,
    Qt3DRender::QRenderTargetOutput *output) {
  self->outputChanged(output);
}

//  void
//      Qt3DRender::Quick::QScene2D::renderPolicyChanged(QScene2D::RenderPoli
//      cy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D19renderPolicyChangedENS1_12RenderPolicyE(
    Qt3DRender::Quick::QScene2D *self,
    Qt3DRender::Quick::QScene2D::RenderPolicy policy) {
  self->renderPolicyChanged(policy);
}

//  void Qt3DRender::Quick::QScene2D::itemChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D11itemChangedEP10QQuickItem(
    Qt3DRender::Quick::QScene2D *self,
    QQuickItem *item) {
  self->itemChanged(item);
}

//  void Qt3DRender::Quick::QScene2D::mouseEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick8QScene2D19mouseEnabledChangedEb(
    Qt3DRender::Quick::QScene2D *self,
    bool enabled) {
  self->mouseEnabledChanged(enabled);
}

//  QScene2DPrivate *Qt3DRender::Quick::QScene2D::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::QScene2DPrivate *ritual_ZN10Qt3DRender5Quick8QScene2D6d_funcEv(
    Qt3DRender::Quick::QScene2D *self) {
  return self->d_func();
}

//  const QScene2DPrivate *Qt3DRender::Quick::QScene2D::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Quick::QScene2DPrivate *ritual_ZNK10Qt3DRender5Quick8QScene2D6d_funcEv(
    const Qt3DRender::Quick::QScene2D *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_Quick_QScene2D, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Quick_QScene2D(
    Qt3DRender::Quick::QScene2D *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Quick_QScene2D *>(self)->take(key, call);
}

//  a QList<Qt3DCore::QEntity *> a ritual of Qt3DRender::Quick::QScene2D gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Quick_QScene2D__QList_Qt3DCore_QEntity(
    QList<Qt3DCore::QEntity *> *self) {
  delete self;
}
