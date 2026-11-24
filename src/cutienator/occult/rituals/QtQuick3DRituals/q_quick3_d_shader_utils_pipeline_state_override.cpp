//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DShaderUtilsPipelineStateOverride that Python can take functions over in. Every QQuick3DShaderUtilsPipelineStateOverride
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall0)(const void *, int *);
typedef int (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall1)(const void *, int *);
typedef void * (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall2)(const void *, int, int *);
typedef void * (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall3)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall4)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall6)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall7)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsPipelineStateOverrideCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DShaderUtilsPipelineStateOverride : public QQuick3DShaderUtilsPipelineStateOverride {
public:
  using QQuick3DShaderUtilsPipelineStateOverride::QQuick3DShaderUtilsPipelineStateOverride;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN32QQuick3DShaderUtilsRenderCommand12cloneCommandEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QQuick3DShaderUtilsRenderCommand11bufferCountEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QQuick3DShaderUtilsRenderCommand8bufferAtEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGCommand *QQuick3DShaderUtilsPipelineStateOverride::cloneCommand()
  QSSGCommand *cloneCommand() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall0 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSSGCommand *>(given);
    }
    return QQuick3DShaderUtilsPipelineStateOverride::cloneCommand();
  }

  //  int QQuick3DShaderUtilsRenderCommand::bufferCount() const
  int bufferCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall1 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DShaderUtilsRenderCommand::bufferCount();
  }

  //  QQuick3DShaderUtilsBuffer
  //      *QQuick3DShaderUtilsRenderCommand::bufferAt(int idx) const
  QQuick3DShaderUtilsBuffer *bufferAt(int idx) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall2 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall2>(taken[2]);
      void * given = call(this, idx, &handled);
      if (handled) return static_cast<QQuick3DShaderUtilsBuffer *>(given);
    }
    return QQuick3DShaderUtilsRenderCommand::bufferAt(idx);
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall3 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall3>(taken[3]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DObject::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall4 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall5 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall6 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall7 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall8 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall9 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall10 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall11 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall12 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall13 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall14 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsPipelineStateOverrideCall15 call = reinterpret_cast<CuteQQuick3DShaderUtilsPipelineStateOverrideCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DShaderUtilsPipelineStateOverride::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride10metaObjectEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->metaObject();
}

//  QString QQuick3DShaderUtilsPipelineStateOverride::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DShaderUtilsPipelineStateOverride::tr(s, c, n));
}

//  QQuick3DShaderUtilsPipelineStateOverride::QQuick3DShaderUtilsPipelineStat
//      eOverride()
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsPipelineStateOverride *ritual_ZN40QQuick3DShaderUtilsPipelineStateOverrideC1Ev() {
  return new CuteQQuick3DShaderUtilsPipelineStateOverride();
}

//  QQuick3DShaderUtilsPipelineStateOverride::~QQuick3DShaderUtilsPipelineSta
//      teOverride()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverrideD1Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  delete self;
}

//  bool QQuick3DShaderUtilsPipelineStateOverride::depthTestEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride16depthTestEnabledEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->depthTestEnabled();
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setDepthTestEnabled(bool
//      newDepthTestEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19setDepthTestEnabledEb(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    bool newDepthTestEnabled) {
  self->setDepthTestEnabled(newDepthTestEnabled);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetDepthTestEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride21resetDepthTestEnabledEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetDepthTestEnabled();
}

//  bool QQuick3DShaderUtilsPipelineStateOverride::depthWriteEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride17depthWriteEnabledEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->depthWriteEnabled();
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setDepthWriteEnabled(bool
//      newDepthWriteEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride20setDepthWriteEnabledEb(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    bool newDepthWriteEnabled) {
  self->setDepthWriteEnabled(newDepthWriteEnabled);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetDepthWriteEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride22resetDepthWriteEnabledEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetDepthWriteEnabled();
}

//  bool QQuick3DShaderUtilsPipelineStateOverride::blendEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12blendEnabledEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->blendEnabled();
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setBlendEnabled(bool
//      newBlendEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setBlendEnabledEb(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    bool newBlendEnabled) {
  self->setBlendEnabled(newBlendEnabled);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetBlendEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetBlendEnabledEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetBlendEnabled();
}

//  bool QQuick3DShaderUtilsPipelineStateOverride::usesStencilReference()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride20usesStencilReferenceEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->usesStencilReference();
}

//  void
//      QQuick3DShaderUtilsPipelineStateOverride::setUsesStencilReference(boo
//      l newUsesStencilReference)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride23setUsesStencilReferenceEb(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    bool newUsesStencilReference) {
  self->setUsesStencilReference(newUsesStencilReference);
}

//  void
//      QQuick3DShaderUtilsPipelineStateOverride::resetUsesStencilReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride25resetUsesStencilReferenceEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetUsesStencilReference();
}

//  bool QQuick3DShaderUtilsPipelineStateOverride::usesScissor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride11usesScissorEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->usesScissor();
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setUsesScissor(bool
//      newUsesScissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride14setUsesScissorEb(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    bool newUsesScissor) {
  self->setUsesScissor(newUsesScissor);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetUsesScissor()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride16resetUsesScissorEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetUsesScissor();
}

//  CompareOperation
//      QQuick3DShaderUtilsPipelineStateOverride::depthFunction() const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsPipelineStateOverride::CompareOperation ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride13depthFunctionEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->depthFunction();
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setDepthFunction(CompareOp
//      eration newDepthFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride16setDepthFunctionENS_16CompareOperationE(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    QQuick3DShaderUtilsPipelineStateOverride::CompareOperation newDepthFunction) {
  self->setDepthFunction(newDepthFunction);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetDepthFunction()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride18resetDepthFunctionEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetDepthFunction();
}

//  CullMode QQuick3DShaderUtilsPipelineStateOverride::cullMode() const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsPipelineStateOverride::CullMode ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride8cullModeEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->cullMode();
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setCullMode(CullMode
//      newCullMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride11setCullModeENS_8CullModeE(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    QQuick3DShaderUtilsPipelineStateOverride::CullMode newCullMode) {
  self->setCullMode(newCullMode);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetCullMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride13resetCullModeEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetCullMode();
}

//  PolygonMode QQuick3DShaderUtilsPipelineStateOverride::polygonMode() const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsPipelineStateOverride::PolygonMode ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride11polygonModeEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->polygonMode();
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setPolygonMode(PolygonMode
//      newPolygonMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride14setPolygonModeENS_11PolygonModeE(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    QQuick3DShaderUtilsPipelineStateOverride::PolygonMode newPolygonMode) {
  self->setPolygonMode(newPolygonMode);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetPolygonMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride16resetPolygonModeEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetPolygonMode();
}

//  quint32 QQuick3DShaderUtilsPipelineStateOverride::stencilWriteMask()
//      const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride16stencilWriteMaskEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->stencilWriteMask();
}

//  void
//      QQuick3DShaderUtilsPipelineStateOverride::setStencilWriteMask(quint32
//      newStencilWriteMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19setStencilWriteMaskEj(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    quint32 newStencilWriteMask) {
  self->setStencilWriteMask(newStencilWriteMask);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetStencilWriteMask()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride21resetStencilWriteMaskEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetStencilWriteMask();
}

//  quint32 QQuick3DShaderUtilsPipelineStateOverride::stencilReference()
//      const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride16stencilReferenceEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->stencilReference();
}

//  void
//      QQuick3DShaderUtilsPipelineStateOverride::setStencilReference(quint32
//      newStencilReference)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19setStencilReferenceEj(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    quint32 newStencilReference) {
  self->setStencilReference(newStencilReference);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetStencilReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride21resetStencilReferenceEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetStencilReference();
}

//  QRectF QQuick3DShaderUtilsPipelineStateOverride::viewport() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride8viewportEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QRectF(self->viewport());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setViewport(const QRectF
//      &newViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride11setViewportERK6QRectF(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QRectF *newViewport) {
  self->setViewport(*newViewport);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride13resetViewportEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetViewport();
}

//  QRect QQuick3DShaderUtilsPipelineStateOverride::scissor() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride7scissorEv(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QRect(self->scissor());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setScissor(const QRect
//      &newScissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride10setScissorERK5QRect(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QRect *newScissor) {
  self->setScissor(*newScissor);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetScissor()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride12resetScissorEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetScissor();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend0() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend0Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend0());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend0(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend0)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend0ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend0) {
  self->setTargetBlend0(*newTargetBlend0);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend0()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend0Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend0();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend1() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend1Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend1());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend1(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend1)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend1ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend1) {
  self->setTargetBlend1(*newTargetBlend1);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend1()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend1Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend1();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend2() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend2Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend2());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend2(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend2)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend2ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend2) {
  self->setTargetBlend2(*newTargetBlend2);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend2()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend2Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend2();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend3() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend3Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend3());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend3(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend3)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend3ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend3) {
  self->setTargetBlend3(*newTargetBlend3);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend3()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend3Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend3();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend4() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend4Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend4());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend4(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend4)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend4ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend4) {
  self->setTargetBlend4(*newTargetBlend4);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend4()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend4Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend4();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend5() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend5Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend5());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend5(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend5)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend5ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend5) {
  self->setTargetBlend5(*newTargetBlend5);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend5()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend5Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend5();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend6() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend6Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend6());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend6(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend6)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend6ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend6) {
  self->setTargetBlend6(*newTargetBlend6);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend6()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend6Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend6();
}

//  QQuick3DRenderPassTargetBlend
//      QQuick3DShaderUtilsPipelineStateOverride::targetBlend7() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend7Ev(
    const QQuick3DShaderUtilsPipelineStateOverride *self) {
  return new QQuick3DRenderPassTargetBlend(self->targetBlend7());
}

//  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend7(const
//      QQuick3DRenderPassTargetBlend &newTargetBlend7)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlend7ERK29QQuick3DRenderPassTargetBlend(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const QQuick3DRenderPassTargetBlend *newTargetBlend7) {
  self->setTargetBlend7(*newTargetBlend7);
}

//  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend7()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBlend7Ev(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  self->resetTargetBlend7();
}

//  QSSGCommand *QQuick3DShaderUtilsPipelineStateOverride::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride12cloneCommandEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->cloneCommand();
}

//  a Python function taken by a
//      CuteQQuick3DShaderUtilsPipelineStateOverride, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DShaderUtilsPipelineStateOverride(
    QQuick3DShaderUtilsPipelineStateOverride *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DShaderUtilsPipelineStateOverride *>(self)->take(key, call);
}

//  QSSGCommand *QQuick3DShaderUtilsPipelineStateOverride::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_own_ZN40QQuick3DShaderUtilsPipelineStateOverride12cloneCommandEv(
    QQuick3DShaderUtilsPipelineStateOverride *self) {
  return self->QQuick3DShaderUtilsPipelineStateOverride::cloneCommand();
}
