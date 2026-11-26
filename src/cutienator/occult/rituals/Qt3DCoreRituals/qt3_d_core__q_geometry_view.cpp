//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qgeometryview.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qgeometryview.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QGeometryView that Python can take functions over in. Every Qt3DCore::QGeometryView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QGeometryViewCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QGeometryViewCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QGeometryViewCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QGeometryViewCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QGeometryViewCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QGeometryViewCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QGeometryViewCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QGeometryView : public Qt3DCore::QGeometryView {
public:
  using Qt3DCore::QGeometryView::QGeometryView;
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
      CuteQt3DCore_QGeometryViewCall0 call = reinterpret_cast<CuteQt3DCore_QGeometryViewCall0>(taken[0]);
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
      CuteQt3DCore_QGeometryViewCall1 call = reinterpret_cast<CuteQt3DCore_QGeometryViewCall1>(taken[1]);
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
      CuteQt3DCore_QGeometryViewCall2 call = reinterpret_cast<CuteQt3DCore_QGeometryViewCall2>(taken[2]);
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
      CuteQt3DCore_QGeometryViewCall3 call = reinterpret_cast<CuteQt3DCore_QGeometryViewCall3>(taken[3]);
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
      CuteQt3DCore_QGeometryViewCall4 call = reinterpret_cast<CuteQt3DCore_QGeometryViewCall4>(taken[4]);
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
      CuteQt3DCore_QGeometryViewCall5 call = reinterpret_cast<CuteQt3DCore_QGeometryViewCall5>(taken[5]);
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
      CuteQt3DCore_QGeometryViewCall6 call = reinterpret_cast<CuteQt3DCore_QGeometryViewCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QGeometryView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore13QGeometryView10metaObjectEv(
    const Qt3DCore::QGeometryView *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QGeometryView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore13QGeometryView11qt_metacastEPKc(
    Qt3DCore::QGeometryView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QGeometryView::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore13QGeometryView11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QGeometryView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QGeometryView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore13QGeometryView2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QGeometryView::tr(s, c, n));
}

//  Qt3DCore::QGeometryView::QGeometryView(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryView *ritual_ZN8Qt3DCore13QGeometryViewC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QGeometryView(parent);
}

//  Qt3DCore::QGeometryView::~QGeometryView()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryViewD1Ev(Qt3DCore::QGeometryView *self) {
  delete self;
}

//  int Qt3DCore::QGeometryView::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView13instanceCountEv(
    const Qt3DCore::QGeometryView *self) {
  return self->instanceCount();
}

//  int Qt3DCore::QGeometryView::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView11vertexCountEv(
    const Qt3DCore::QGeometryView *self) {
  return self->vertexCount();
}

//  int Qt3DCore::QGeometryView::indexOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView11indexOffsetEv(
    const Qt3DCore::QGeometryView *self) {
  return self->indexOffset();
}

//  int Qt3DCore::QGeometryView::firstInstance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView13firstInstanceEv(
    const Qt3DCore::QGeometryView *self) {
  return self->firstInstance();
}

//  int Qt3DCore::QGeometryView::firstVertex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView11firstVertexEv(
    const Qt3DCore::QGeometryView *self) {
  return self->firstVertex();
}

//  int Qt3DCore::QGeometryView::indexBufferByteOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView21indexBufferByteOffsetEv(
    const Qt3DCore::QGeometryView *self) {
  return self->indexBufferByteOffset();
}

//  int Qt3DCore::QGeometryView::restartIndexValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView17restartIndexValueEv(
    const Qt3DCore::QGeometryView *self) {
  return self->restartIndexValue();
}

//  int Qt3DCore::QGeometryView::verticesPerPatch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore13QGeometryView16verticesPerPatchEv(
    const Qt3DCore::QGeometryView *self) {
  return self->verticesPerPatch();
}

//  bool Qt3DCore::QGeometryView::primitiveRestartEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore13QGeometryView23primitiveRestartEnabledEv(
    const Qt3DCore::QGeometryView *self) {
  return self->primitiveRestartEnabled();
}

//  QGeometry *Qt3DCore::QGeometryView::geometry() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZNK8Qt3DCore13QGeometryView8geometryEv(
    const Qt3DCore::QGeometryView *self) {
  return self->geometry();
}

//  PrimitiveType Qt3DCore::QGeometryView::primitiveType() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryView::PrimitiveType ritual_ZNK8Qt3DCore13QGeometryView13primitiveTypeEv(
    const Qt3DCore::QGeometryView *self) {
  return self->primitiveType();
}

//  void Qt3DCore::QGeometryView::setInstanceCount(int instanceCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView16setInstanceCountEi(
    Qt3DCore::QGeometryView *self,
    int instanceCount) {
  self->setInstanceCount(instanceCount);
}

//  void Qt3DCore::QGeometryView::setVertexCount(int vertexCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView14setVertexCountEi(
    Qt3DCore::QGeometryView *self,
    int vertexCount) {
  self->setVertexCount(vertexCount);
}

//  void Qt3DCore::QGeometryView::setIndexOffset(int indexOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView14setIndexOffsetEi(
    Qt3DCore::QGeometryView *self,
    int indexOffset) {
  self->setIndexOffset(indexOffset);
}

//  void Qt3DCore::QGeometryView::setFirstInstance(int firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView16setFirstInstanceEi(
    Qt3DCore::QGeometryView *self,
    int firstInstance) {
  self->setFirstInstance(firstInstance);
}

//  void Qt3DCore::QGeometryView::setFirstVertex(int firstVertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView14setFirstVertexEi(
    Qt3DCore::QGeometryView *self,
    int firstVertex) {
  self->setFirstVertex(firstVertex);
}

//  void Qt3DCore::QGeometryView::setIndexBufferByteOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView24setIndexBufferByteOffsetEi(
    Qt3DCore::QGeometryView *self,
    int offset) {
  self->setIndexBufferByteOffset(offset);
}

//  void Qt3DCore::QGeometryView::setRestartIndexValue(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView20setRestartIndexValueEi(
    Qt3DCore::QGeometryView *self,
    int index) {
  self->setRestartIndexValue(index);
}

//  void Qt3DCore::QGeometryView::setVerticesPerPatch(int verticesPerPatch)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView19setVerticesPerPatchEi(
    Qt3DCore::QGeometryView *self,
    int verticesPerPatch) {
  self->setVerticesPerPatch(verticesPerPatch);
}

//  void Qt3DCore::QGeometryView::setPrimitiveRestartEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView26setPrimitiveRestartEnabledEb(
    Qt3DCore::QGeometryView *self,
    bool enabled) {
  self->setPrimitiveRestartEnabled(enabled);
}

//  void Qt3DCore::QGeometryView::setGeometry(QGeometry *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView11setGeometryEPNS_9QGeometryE(
    Qt3DCore::QGeometryView *self,
    Qt3DCore::QGeometry *geometry) {
  self->setGeometry(geometry);
}

//  void Qt3DCore::QGeometryView::setPrimitiveType(PrimitiveType
//      primitiveType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView16setPrimitiveTypeENS0_13PrimitiveTypeE(
    Qt3DCore::QGeometryView *self,
    Qt3DCore::QGeometryView::PrimitiveType primitiveType) {
  self->setPrimitiveType(primitiveType);
}

//  void Qt3DCore::QGeometryView::instanceCountChanged(int instanceCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView20instanceCountChangedEi(
    Qt3DCore::QGeometryView *self,
    int instanceCount) {
  self->instanceCountChanged(instanceCount);
}

//  void Qt3DCore::QGeometryView::vertexCountChanged(int vertexCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView18vertexCountChangedEi(
    Qt3DCore::QGeometryView *self,
    int vertexCount) {
  self->vertexCountChanged(vertexCount);
}

//  void Qt3DCore::QGeometryView::indexOffsetChanged(int indexOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView18indexOffsetChangedEi(
    Qt3DCore::QGeometryView *self,
    int indexOffset) {
  self->indexOffsetChanged(indexOffset);
}

//  void Qt3DCore::QGeometryView::firstInstanceChanged(int firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView20firstInstanceChangedEi(
    Qt3DCore::QGeometryView *self,
    int firstInstance) {
  self->firstInstanceChanged(firstInstance);
}

//  void Qt3DCore::QGeometryView::firstVertexChanged(int firstVertex)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView18firstVertexChangedEi(
    Qt3DCore::QGeometryView *self,
    int firstVertex) {
  self->firstVertexChanged(firstVertex);
}

//  void Qt3DCore::QGeometryView::indexBufferByteOffsetChanged(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView28indexBufferByteOffsetChangedEi(
    Qt3DCore::QGeometryView *self,
    int offset) {
  self->indexBufferByteOffsetChanged(offset);
}

//  void Qt3DCore::QGeometryView::restartIndexValueChanged(int
//      restartIndexValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView24restartIndexValueChangedEi(
    Qt3DCore::QGeometryView *self,
    int restartIndexValue) {
  self->restartIndexValueChanged(restartIndexValue);
}

//  void Qt3DCore::QGeometryView::verticesPerPatchChanged(int
//      verticesPerPatch)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView23verticesPerPatchChangedEi(
    Qt3DCore::QGeometryView *self,
    int verticesPerPatch) {
  self->verticesPerPatchChanged(verticesPerPatch);
}

//  void Qt3DCore::QGeometryView::primitiveRestartEnabledChanged(bool
//      primitiveRestartEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView30primitiveRestartEnabledChangedEb(
    Qt3DCore::QGeometryView *self,
    bool primitiveRestartEnabled) {
  self->primitiveRestartEnabledChanged(primitiveRestartEnabled);
}

//  void Qt3DCore::QGeometryView::geometryChanged(QGeometry *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView15geometryChangedEPNS_9QGeometryE(
    Qt3DCore::QGeometryView *self,
    Qt3DCore::QGeometry *geometry) {
  self->geometryChanged(geometry);
}

//  void Qt3DCore::QGeometryView::primitiveTypeChanged(PrimitiveType
//      primitiveType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QGeometryView20primitiveTypeChangedENS0_13PrimitiveTypeE(
    Qt3DCore::QGeometryView *self,
    Qt3DCore::QGeometryView::PrimitiveType primitiveType) {
  self->primitiveTypeChanged(primitiveType);
}

//  Qt3DCore::QGeometryView::QGeometryView(QGeometryViewPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryView *ritual_ZN8Qt3DCore13QGeometryViewC1ERNS_20QGeometryViewPrivateEPNS_5QNodeE(
    Qt3DCore::QGeometryViewPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QGeometryView(*dd, parent);
}

//  QGeometryViewPrivate *Qt3DCore::QGeometryView::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryViewPrivate *ritual_ZN8Qt3DCore13QGeometryView6d_funcEv(
    Qt3DCore::QGeometryView *self) {
  return self->d_func();
}

//  const QGeometryViewPrivate *Qt3DCore::QGeometryView::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QGeometryViewPrivate *ritual_ZNK8Qt3DCore13QGeometryView6d_funcEv(
    const Qt3DCore::QGeometryView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QGeometryView, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QGeometryView(
    Qt3DCore::QGeometryView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QGeometryView *>(self)->take(key, call);
}
