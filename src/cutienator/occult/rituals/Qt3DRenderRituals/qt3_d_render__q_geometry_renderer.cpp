//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qgeometryrenderer.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qgeometryrenderer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QGeometryRenderer that Python can take functions over in. Every Qt3DRender::QGeometryRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGeometryRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGeometryRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QGeometryRenderer : public Qt3DRender::QGeometryRenderer {
public:
  using Qt3DRender::QGeometryRenderer::QGeometryRenderer;
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
      CuteQt3DRender_QGeometryRendererCall0 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererCall0>(taken[0]);
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
      CuteQt3DRender_QGeometryRendererCall1 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererCall1>(taken[1]);
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
      CuteQt3DRender_QGeometryRendererCall2 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererCall2>(taken[2]);
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
      CuteQt3DRender_QGeometryRendererCall3 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererCall3>(taken[3]);
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
      CuteQt3DRender_QGeometryRendererCall4 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererCall4>(taken[4]);
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
      CuteQt3DRender_QGeometryRendererCall5 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererCall5>(taken[5]);
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
      CuteQt3DRender_QGeometryRendererCall6 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QGeometryRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender17QGeometryRenderer10metaObjectEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QGeometryRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender17QGeometryRenderer11qt_metacastEPKc(
    Qt3DRender::QGeometryRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QGeometryRenderer::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender17QGeometryRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QGeometryRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QGeometryRenderer::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender17QGeometryRenderer2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QGeometryRenderer::tr(s, c, n));
}

//  Qt3DRender::QGeometryRenderer::QGeometryRenderer(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRenderer *ritual_ZN10Qt3DRender17QGeometryRendererC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QGeometryRenderer(parent);
}

//  Qt3DRender::QGeometryRenderer::~QGeometryRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRendererD1Ev(
    Qt3DRender::QGeometryRenderer *self) {
  delete self;
}

//  int Qt3DRender::QGeometryRenderer::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer13instanceCountEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->instanceCount();
}

//  int Qt3DRender::QGeometryRenderer::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer11vertexCountEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->vertexCount();
}

//  int Qt3DRender::QGeometryRenderer::indexOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer11indexOffsetEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->indexOffset();
}

//  int Qt3DRender::QGeometryRenderer::firstInstance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer13firstInstanceEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->firstInstance();
}

//  int Qt3DRender::QGeometryRenderer::firstVertex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer11firstVertexEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->firstVertex();
}

//  int Qt3DRender::QGeometryRenderer::indexBufferByteOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer21indexBufferByteOffsetEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->indexBufferByteOffset();
}

//  int Qt3DRender::QGeometryRenderer::restartIndexValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer17restartIndexValueEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->restartIndexValue();
}

//  int Qt3DRender::QGeometryRenderer::verticesPerPatch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QGeometryRenderer16verticesPerPatchEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->verticesPerPatch();
}

//  bool Qt3DRender::QGeometryRenderer::primitiveRestartEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender17QGeometryRenderer23primitiveRestartEnabledEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->primitiveRestartEnabled();
}

//  Qt3DCore::QGeometry *Qt3DRender::QGeometryRenderer::geometry() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZNK10Qt3DRender17QGeometryRenderer8geometryEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->geometry();
}

//  PrimitiveType Qt3DRender::QGeometryRenderer::primitiveType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRenderer::PrimitiveType ritual_ZNK10Qt3DRender17QGeometryRenderer13primitiveTypeEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->primitiveType();
}

//  float Qt3DRender::QGeometryRenderer::sortIndex() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender17QGeometryRenderer9sortIndexEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->sortIndex();
}

//  void Qt3DRender::QGeometryRenderer::setInstanceCount(int instanceCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer16setInstanceCountEi(
    Qt3DRender::QGeometryRenderer *self,
    int instanceCount) {
  self->setInstanceCount(instanceCount);
}

//  void Qt3DRender::QGeometryRenderer::setVertexCount(int vertexCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer14setVertexCountEi(
    Qt3DRender::QGeometryRenderer *self,
    int vertexCount) {
  self->setVertexCount(vertexCount);
}

//  void Qt3DRender::QGeometryRenderer::setIndexOffset(int indexOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer14setIndexOffsetEi(
    Qt3DRender::QGeometryRenderer *self,
    int indexOffset) {
  self->setIndexOffset(indexOffset);
}

//  void Qt3DRender::QGeometryRenderer::setFirstInstance(int firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer16setFirstInstanceEi(
    Qt3DRender::QGeometryRenderer *self,
    int firstInstance) {
  self->setFirstInstance(firstInstance);
}

//  void Qt3DRender::QGeometryRenderer::setFirstVertex(int firstVertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer14setFirstVertexEi(
    Qt3DRender::QGeometryRenderer *self,
    int firstVertex) {
  self->setFirstVertex(firstVertex);
}

//  void Qt3DRender::QGeometryRenderer::setIndexBufferByteOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer24setIndexBufferByteOffsetEi(
    Qt3DRender::QGeometryRenderer *self,
    int offset) {
  self->setIndexBufferByteOffset(offset);
}

//  void Qt3DRender::QGeometryRenderer::setRestartIndexValue(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer20setRestartIndexValueEi(
    Qt3DRender::QGeometryRenderer *self,
    int index) {
  self->setRestartIndexValue(index);
}

//  void Qt3DRender::QGeometryRenderer::setVerticesPerPatch(int
//      verticesPerPatch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer19setVerticesPerPatchEi(
    Qt3DRender::QGeometryRenderer *self,
    int verticesPerPatch) {
  self->setVerticesPerPatch(verticesPerPatch);
}

//  void Qt3DRender::QGeometryRenderer::setPrimitiveRestartEnabled(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer26setPrimitiveRestartEnabledEb(
    Qt3DRender::QGeometryRenderer *self,
    bool enabled) {
  self->setPrimitiveRestartEnabled(enabled);
}

//  void Qt3DRender::QGeometryRenderer::setGeometry(Qt3DCore::QGeometry
//      *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer11setGeometryEPN8Qt3DCore9QGeometryE(
    Qt3DRender::QGeometryRenderer *self,
    Qt3DCore::QGeometry *geometry) {
  self->setGeometry(geometry);
}

//  void Qt3DRender::QGeometryRenderer::setPrimitiveType(PrimitiveType
//      primitiveType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer16setPrimitiveTypeENS0_13PrimitiveTypeE(
    Qt3DRender::QGeometryRenderer *self,
    Qt3DRender::QGeometryRenderer::PrimitiveType primitiveType) {
  self->setPrimitiveType(primitiveType);
}

//  void Qt3DRender::QGeometryRenderer::setSortIndex(float sortIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer12setSortIndexEf(
    Qt3DRender::QGeometryRenderer *self,
    float sortIndex) {
  self->setSortIndex(sortIndex);
}

//  void Qt3DRender::QGeometryRenderer::instanceCountChanged(int
//      instanceCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer20instanceCountChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int instanceCount) {
  self->instanceCountChanged(instanceCount);
}

//  void Qt3DRender::QGeometryRenderer::vertexCountChanged(int vertexCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer18vertexCountChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int vertexCount) {
  self->vertexCountChanged(vertexCount);
}

//  void Qt3DRender::QGeometryRenderer::indexOffsetChanged(int indexOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer18indexOffsetChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int indexOffset) {
  self->indexOffsetChanged(indexOffset);
}

//  void Qt3DRender::QGeometryRenderer::firstInstanceChanged(int
//      firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer20firstInstanceChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int firstInstance) {
  self->firstInstanceChanged(firstInstance);
}

//  void Qt3DRender::QGeometryRenderer::firstVertexChanged(int firstVertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer18firstVertexChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int firstVertex) {
  self->firstVertexChanged(firstVertex);
}

//  void Qt3DRender::QGeometryRenderer::indexBufferByteOffsetChanged(int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer28indexBufferByteOffsetChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int offset) {
  self->indexBufferByteOffsetChanged(offset);
}

//  void Qt3DRender::QGeometryRenderer::restartIndexValueChanged(int
//      restartIndexValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer24restartIndexValueChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int restartIndexValue) {
  self->restartIndexValueChanged(restartIndexValue);
}

//  void Qt3DRender::QGeometryRenderer::verticesPerPatchChanged(int
//      verticesPerPatch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer23verticesPerPatchChangedEi(
    Qt3DRender::QGeometryRenderer *self,
    int verticesPerPatch) {
  self->verticesPerPatchChanged(verticesPerPatch);
}

//  void Qt3DRender::QGeometryRenderer::primitiveRestartEnabledChanged(bool
//      primitiveRestartEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer30primitiveRestartEnabledChangedEb(
    Qt3DRender::QGeometryRenderer *self,
    bool primitiveRestartEnabled) {
  self->primitiveRestartEnabledChanged(primitiveRestartEnabled);
}

//  void Qt3DRender::QGeometryRenderer::geometryChanged(Qt3DCore::QGeometry
//      *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer15geometryChangedEPN8Qt3DCore9QGeometryE(
    Qt3DRender::QGeometryRenderer *self,
    Qt3DCore::QGeometry *geometry) {
  self->geometryChanged(geometry);
}

//  void Qt3DRender::QGeometryRenderer::primitiveTypeChanged(PrimitiveType
//      primitiveType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer20primitiveTypeChangedENS0_13PrimitiveTypeE(
    Qt3DRender::QGeometryRenderer *self,
    Qt3DRender::QGeometryRenderer::PrimitiveType primitiveType) {
  self->primitiveTypeChanged(primitiveType);
}

//  void Qt3DRender::QGeometryRenderer::sortIndexChanged(float sortIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QGeometryRenderer16sortIndexChangedEf(
    Qt3DRender::QGeometryRenderer *self,
    float sortIndex) {
  self->sortIndexChanged(sortIndex);
}

//  Qt3DRender::QGeometryRenderer::QGeometryRenderer(QGeometryRendererPrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRenderer *ritual_ZN10Qt3DRender17QGeometryRendererC1ERNS_24QGeometryRendererPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QGeometryRendererPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QGeometryRenderer(*dd, parent);
}

//  QGeometryRendererPrivate *Qt3DRender::QGeometryRenderer::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRendererPrivate *ritual_ZN10Qt3DRender17QGeometryRenderer6d_funcEv(
    Qt3DRender::QGeometryRenderer *self) {
  return self->d_func();
}

//  const QGeometryRendererPrivate *Qt3DRender::QGeometryRenderer::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QGeometryRendererPrivate *ritual_ZNK10Qt3DRender17QGeometryRenderer6d_funcEv(
    const Qt3DRender::QGeometryRenderer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QGeometryRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QGeometryRenderer(
    Qt3DRender::QGeometryRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QGeometryRenderer *>(self)->take(key, call);
}
