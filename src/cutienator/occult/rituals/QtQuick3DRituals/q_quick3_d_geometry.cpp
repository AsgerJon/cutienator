//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3dgeometry.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/qquick3dgeometry.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DGeometry may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DGeometry : QQuick3DGeometry {
  using QQuick3DGeometry::updateSpatialNode;
  using QQuick3DGeometry::markAllDirty;
};

//  A QQuick3DGeometry that Python can take functions over in. Every QQuick3DGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DGeometryCall1)(const void *, int *);
typedef void (*CuteQQuick3DGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DGeometryCall3)(const void *, int *);
typedef void (*CuteQQuick3DGeometryCall4)(const void *, int *);
typedef void (*CuteQQuick3DGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DGeometry : public QQuick3DGeometry {
public:
  using QQuick3DGeometry::QQuick3DGeometry;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DGeometryCall0 call = reinterpret_cast<CuteQQuick3DGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DGeometryCall1 call = reinterpret_cast<CuteQQuick3DGeometryCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DGeometry::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DGeometryCall2 call = reinterpret_cast<CuteQQuick3DGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DGeometryCall3 call = reinterpret_cast<CuteQQuick3DGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DGeometryCall4 call = reinterpret_cast<CuteQQuick3DGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DGeometryCall5 call = reinterpret_cast<CuteQQuick3DGeometryCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DGeometryCall6 call = reinterpret_cast<CuteQQuick3DGeometryCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DGeometryCall7 call = reinterpret_cast<CuteQQuick3DGeometryCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DGeometryCall8 call = reinterpret_cast<CuteQQuick3DGeometryCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DGeometryCall9 call = reinterpret_cast<CuteQQuick3DGeometryCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DGeometryCall10 call = reinterpret_cast<CuteQQuick3DGeometryCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DGeometryCall11 call = reinterpret_cast<CuteQQuick3DGeometryCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DGeometryCall12 call = reinterpret_cast<CuteQQuick3DGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DGeometry10metaObjectEv(
    const QQuick3DGeometry *self) {
  return self->metaObject();
}

//  void *QQuick3DGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuick3DGeometry11qt_metacastEPKc(
    QQuick3DGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DGeometry::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuick3DGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DGeometry::tr(s, c, n));
}

//  QQuick3DGeometryPrivate *QQuick3DGeometry::d_func()
extern "C" Q_DECL_EXPORT
QQuick3DGeometryPrivate *ritual_ZN16QQuick3DGeometry6d_funcEv(
    QQuick3DGeometry *self) {
  return self->d_func();
}

//  const QQuick3DGeometryPrivate *QQuick3DGeometry::d_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DGeometryPrivate *ritual_ZNK16QQuick3DGeometry6d_funcEv(
    const QQuick3DGeometry *self) {
  return self->d_func();
}

//  void QQuick3DGeometry::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry24qt_qmlMarker_uncreatableEv(
    QQuick3DGeometry *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DGeometry::QQuick3DGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DGeometry *ritual_ZN16QQuick3DGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DGeometry(parent);
}

//  QQuick3DGeometry::~QQuick3DGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometryD1Ev(QQuick3DGeometry *self) {
  delete self;
}

//  QByteArray QQuick3DGeometry::vertexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QQuick3DGeometry10vertexDataEv(
    const QQuick3DGeometry *self) {
  return new QByteArray(self->vertexData());
}

//  QByteArray QQuick3DGeometry::indexData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QQuick3DGeometry9indexDataEv(
    const QQuick3DGeometry *self) {
  return new QByteArray(self->indexData());
}

//  int QQuick3DGeometry::attributeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DGeometry14attributeCountEv(
    const QQuick3DGeometry *self) {
  return self->attributeCount();
}

//  Attribute QQuick3DGeometry::attribute(int index) const
extern "C" Q_DECL_EXPORT
QQuick3DGeometry::Attribute *ritual_ZNK16QQuick3DGeometry9attributeEi(
    const QQuick3DGeometry *self,
    int index) {
  return new QQuick3DGeometry::Attribute(self->attribute(index));
}

//  PrimitiveType QQuick3DGeometry::primitiveType() const
extern "C" Q_DECL_EXPORT
QQuick3DGeometry::PrimitiveType ritual_ZNK16QQuick3DGeometry13primitiveTypeEv(
    const QQuick3DGeometry *self) {
  return self->primitiveType();
}

//  QVector3D QQuick3DGeometry::boundsMin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuick3DGeometry9boundsMinEv(
    const QQuick3DGeometry *self) {
  return new QVector3D(self->boundsMin());
}

//  QVector3D QQuick3DGeometry::boundsMax() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuick3DGeometry9boundsMaxEv(
    const QQuick3DGeometry *self) {
  return new QVector3D(self->boundsMax());
}

//  int QQuick3DGeometry::stride() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DGeometry6strideEv(const QQuick3DGeometry *self) {
  return self->stride();
}

//  void QQuick3DGeometry::setVertexData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry13setVertexDataERK10QByteArray(
    QQuick3DGeometry *self,
    const QByteArray *data) {
  self->setVertexData(*data);
}

//  void QQuick3DGeometry::setVertexData(int offset, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry13setVertexDataEiRK10QByteArray(
    QQuick3DGeometry *self,
    int offset,
    const QByteArray *data) {
  self->setVertexData(offset, *data);
}

//  void QQuick3DGeometry::setIndexData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry12setIndexDataERK10QByteArray(
    QQuick3DGeometry *self,
    const QByteArray *data) {
  self->setIndexData(*data);
}

//  void QQuick3DGeometry::setIndexData(int offset, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry12setIndexDataEiRK10QByteArray(
    QQuick3DGeometry *self,
    int offset,
    const QByteArray *data) {
  self->setIndexData(offset, *data);
}

//  void QQuick3DGeometry::setStride(int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry9setStrideEi(
    QQuick3DGeometry *self,
    int stride) {
  self->setStride(stride);
}

//  void QQuick3DGeometry::setBounds(const QVector3D &min, const QVector3D
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry9setBoundsERK9QVector3DS2_(
    QQuick3DGeometry *self,
    const QVector3D *min,
    const QVector3D *max) {
  self->setBounds(*min, *max);
}

//  void QQuick3DGeometry::setPrimitiveType(PrimitiveType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry16setPrimitiveTypeENS_13PrimitiveTypeE(
    QQuick3DGeometry *self,
    QQuick3DGeometry::PrimitiveType type) {
  self->setPrimitiveType(type);
}

//  void QQuick3DGeometry::addAttribute(Attribute::Semantic semantic, int
//      offset, Attribute::ComponentType componentType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry12addAttributeENS_9Attribute8SemanticEiNS0_13ComponentTypeE(
    QQuick3DGeometry *self,
    QQuick3DGeometry::Attribute::Semantic semantic,
    int offset,
    QQuick3DGeometry::Attribute::ComponentType componentType) {
  self->addAttribute(semantic, offset, componentType);
}

//  void QQuick3DGeometry::addAttribute(const Attribute &att)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry12addAttributeERKNS_9AttributeE(
    QQuick3DGeometry *self,
    const QQuick3DGeometry::Attribute *att) {
  self->addAttribute(*att);
}

//  int QQuick3DGeometry::subsetCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DGeometry11subsetCountEv(
    const QQuick3DGeometry *self) {
  return self->subsetCount();
}

//  QVector3D QQuick3DGeometry::subsetBoundsMin(int subset) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuick3DGeometry15subsetBoundsMinEi(
    const QQuick3DGeometry *self,
    int subset) {
  return new QVector3D(self->subsetBoundsMin(subset));
}

//  QVector3D QQuick3DGeometry::subsetBoundsMax(int subset) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuick3DGeometry15subsetBoundsMaxEi(
    const QQuick3DGeometry *self,
    int subset) {
  return new QVector3D(self->subsetBoundsMax(subset));
}

//  int QQuick3DGeometry::subsetOffset(int subset) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DGeometry12subsetOffsetEi(
    const QQuick3DGeometry *self,
    int subset) {
  return self->subsetOffset(subset);
}

//  int QQuick3DGeometry::subsetCount(int subset) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DGeometry11subsetCountEi(
    const QQuick3DGeometry *self,
    int subset) {
  return self->subsetCount(subset);
}

//  QString QQuick3DGeometry::subsetName(int subset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuick3DGeometry10subsetNameEi(
    const QQuick3DGeometry *self,
    int subset) {
  return new QString(self->subsetName(subset));
}

//  void QQuick3DGeometry::addSubset(int offset, int count, const QVector3D
//      &boundsMin, const QVector3D &boundsMax, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry9addSubsetEiiRK9QVector3DS2_RK7QString(
    QQuick3DGeometry *self,
    int offset,
    int count,
    const QVector3D *boundsMin,
    const QVector3D *boundsMax,
    const QString *name) {
  self->addSubset(offset, count, *boundsMin, *boundsMax, *name);
}

//  QByteArray QQuick3DGeometry::targetData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QQuick3DGeometry10targetDataEv(
    const QQuick3DGeometry *self) {
  return new QByteArray(self->targetData());
}

//  void QQuick3DGeometry::setTargetData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry13setTargetDataERK10QByteArray(
    QQuick3DGeometry *self,
    const QByteArray *data) {
  self->setTargetData(*data);
}

//  void QQuick3DGeometry::setTargetData(int offset, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry13setTargetDataEiRK10QByteArray(
    QQuick3DGeometry *self,
    int offset,
    const QByteArray *data) {
  self->setTargetData(offset, *data);
}

//  TargetAttribute QQuick3DGeometry::targetAttribute(int index) const
extern "C" Q_DECL_EXPORT
QQuick3DGeometry::TargetAttribute *ritual_ZNK16QQuick3DGeometry15targetAttributeEi(
    const QQuick3DGeometry *self,
    int index) {
  return new QQuick3DGeometry::TargetAttribute(self->targetAttribute(index));
}

//  int QQuick3DGeometry::targetAttributeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DGeometry20targetAttributeCountEv(
    const QQuick3DGeometry *self) {
  return self->targetAttributeCount();
}

//  void QQuick3DGeometry::addTargetAttribute(quint32 targetId,
//      Attribute::Semantic semantic, int offset, int stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry18addTargetAttributeEjNS_9Attribute8SemanticEii(
    QQuick3DGeometry *self,
    quint32 targetId,
    QQuick3DGeometry::Attribute::Semantic semantic,
    int offset,
    int stride) {
  self->addTargetAttribute(targetId, semantic, offset, stride);
}

//  void QQuick3DGeometry::addTargetAttribute(const TargetAttribute &att)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry18addTargetAttributeERKNS_15TargetAttributeE(
    QQuick3DGeometry *self,
    const QQuick3DGeometry::TargetAttribute *att) {
  self->addTargetAttribute(*att);
}

//  void QQuick3DGeometry::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry5clearEv(QQuick3DGeometry *self) {
  self->clear();
}

//  void QQuick3DGeometry::geometryNodeDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry17geometryNodeDirtyEv(
    QQuick3DGeometry *self) {
  self->geometryNodeDirty();
}

//  void QQuick3DGeometry::geometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry15geometryChangedEv(QQuick3DGeometry *self) {
  self->geometryChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN16QQuick3DGeometry17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DGeometry *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DGeometry::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DGeometry12markAllDirtyEv(QQuick3DGeometry *self) {
  self->markAllDirty();
}

//  a Python function taken by a CuteQQuick3DGeometry, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DGeometry(
    QQuick3DGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DGeometry *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN16QQuick3DGeometry17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DGeometry *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DGeometry *>(self)->OwnQQuick3DGeometry::updateSpatialNode(
      node);
}

//  void QQuick3DGeometry::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DGeometry12markAllDirtyEv(
    QQuick3DGeometry *self) {
  static_cast<OwnQQuick3DGeometry *>(self)->OwnQQuick3DGeometry::markAllDirty();
}
