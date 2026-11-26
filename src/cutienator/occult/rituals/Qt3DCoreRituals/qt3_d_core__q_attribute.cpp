//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qattribute.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qattribute.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QAttribute that Python can take functions over in. Every Qt3DCore::QAttribute
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAttributeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAttributeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAttributeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAttributeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAttributeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAttributeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAttributeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QAttribute : public Qt3DCore::QAttribute {
public:
  using Qt3DCore::QAttribute::QAttribute;
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
      CuteQt3DCore_QAttributeCall0 call = reinterpret_cast<CuteQt3DCore_QAttributeCall0>(taken[0]);
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
      CuteQt3DCore_QAttributeCall1 call = reinterpret_cast<CuteQt3DCore_QAttributeCall1>(taken[1]);
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
      CuteQt3DCore_QAttributeCall2 call = reinterpret_cast<CuteQt3DCore_QAttributeCall2>(taken[2]);
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
      CuteQt3DCore_QAttributeCall3 call = reinterpret_cast<CuteQt3DCore_QAttributeCall3>(taken[3]);
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
      CuteQt3DCore_QAttributeCall4 call = reinterpret_cast<CuteQt3DCore_QAttributeCall4>(taken[4]);
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
      CuteQt3DCore_QAttributeCall5 call = reinterpret_cast<CuteQt3DCore_QAttributeCall5>(taken[5]);
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
      CuteQt3DCore_QAttributeCall6 call = reinterpret_cast<CuteQt3DCore_QAttributeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QAttribute::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore10QAttribute10metaObjectEv(
    const Qt3DCore::QAttribute *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QAttribute::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore10QAttribute11qt_metacastEPKc(
    Qt3DCore::QAttribute *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QAttribute::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore10QAttribute11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QAttribute *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QAttribute::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QAttribute::tr(s, c, n));
}

//  Qt3DCore::QAttribute::QAttribute(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZN8Qt3DCore10QAttributeC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QAttribute(parent);
}

//  Qt3DCore::QAttribute::QAttribute(QBuffer *buf, VertexBaseType
//      vertexBaseType, uint vertexSize, uint count, uint offset, uint
//      stride, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZN8Qt3DCore10QAttributeC1EPNS_7QBufferENS0_14VertexBaseTypeEjjjjPNS_5QNodeE(
    Qt3DCore::QBuffer *buf,
    Qt3DCore::QAttribute::VertexBaseType vertexBaseType,
    uint vertexSize,
    uint count,
    uint offset,
    uint stride,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QAttribute(
      buf,
      vertexBaseType,
      vertexSize,
      count,
      offset,
      stride,
      parent);
}

//  Qt3DCore::QAttribute::QAttribute(QBuffer *buf, const QString &name,
//      VertexBaseType vertexBaseType, uint vertexSize, uint count, uint
//      offset, uint stride, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZN8Qt3DCore10QAttributeC1EPNS_7QBufferERK7QStringNS0_14VertexBaseTypeEjjjjPNS_5QNodeE(
    Qt3DCore::QBuffer *buf,
    const QString *name,
    Qt3DCore::QAttribute::VertexBaseType vertexBaseType,
    uint vertexSize,
    uint count,
    uint offset,
    uint stride,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QAttribute(
      buf,
      *name,
      vertexBaseType,
      vertexSize,
      count,
      offset,
      stride,
      parent);
}

//  Qt3DCore::QAttribute::~QAttribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttributeD1Ev(Qt3DCore::QAttribute *self) {
  delete self;
}

//  QBuffer *Qt3DCore::QAttribute::buffer() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBuffer *ritual_ZNK8Qt3DCore10QAttribute6bufferEv(
    const Qt3DCore::QAttribute *self) {
  return self->buffer();
}

//  QString Qt3DCore::QAttribute::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore10QAttribute4nameEv(
    const Qt3DCore::QAttribute *self) {
  return new QString(self->name());
}

//  VertexBaseType Qt3DCore::QAttribute::vertexBaseType() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute::VertexBaseType ritual_ZNK8Qt3DCore10QAttribute14vertexBaseTypeEv(
    const Qt3DCore::QAttribute *self) {
  return self->vertexBaseType();
}

//  uint Qt3DCore::QAttribute::vertexSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8Qt3DCore10QAttribute10vertexSizeEv(
    const Qt3DCore::QAttribute *self) {
  return self->vertexSize();
}

//  uint Qt3DCore::QAttribute::count() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8Qt3DCore10QAttribute5countEv(
    const Qt3DCore::QAttribute *self) {
  return self->count();
}

//  uint Qt3DCore::QAttribute::byteStride() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8Qt3DCore10QAttribute10byteStrideEv(
    const Qt3DCore::QAttribute *self) {
  return self->byteStride();
}

//  uint Qt3DCore::QAttribute::byteOffset() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8Qt3DCore10QAttribute10byteOffsetEv(
    const Qt3DCore::QAttribute *self) {
  return self->byteOffset();
}

//  uint Qt3DCore::QAttribute::divisor() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK8Qt3DCore10QAttribute7divisorEv(
    const Qt3DCore::QAttribute *self) {
  return self->divisor();
}

//  AttributeType Qt3DCore::QAttribute::attributeType() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute::AttributeType ritual_ZNK8Qt3DCore10QAttribute13attributeTypeEv(
    const Qt3DCore::QAttribute *self) {
  return self->attributeType();
}

//  QString Qt3DCore::QAttribute::defaultPositionAttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute28defaultPositionAttributeNameEv() {
  return new QString(Qt3DCore::QAttribute::defaultPositionAttributeName());
}

//  QString Qt3DCore::QAttribute::defaultNormalAttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute26defaultNormalAttributeNameEv() {
  return new QString(Qt3DCore::QAttribute::defaultNormalAttributeName());
}

//  QString Qt3DCore::QAttribute::defaultColorAttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute25defaultColorAttributeNameEv() {
  return new QString(Qt3DCore::QAttribute::defaultColorAttributeName());
}

//  QString Qt3DCore::QAttribute::defaultTextureCoordinateAttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute37defaultTextureCoordinateAttributeNameEv() {
  return new QString(
      Qt3DCore::QAttribute::defaultTextureCoordinateAttributeName());
}

//  QString Qt3DCore::QAttribute::defaultTangentAttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute27defaultTangentAttributeNameEv() {
  return new QString(Qt3DCore::QAttribute::defaultTangentAttributeName());
}

//  QString Qt3DCore::QAttribute::defaultJointIndicesAttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute32defaultJointIndicesAttributeNameEv() {
  return new QString(
      Qt3DCore::QAttribute::defaultJointIndicesAttributeName());
}

//  QString Qt3DCore::QAttribute::defaultJointWeightsAttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute32defaultJointWeightsAttributeNameEv() {
  return new QString(
      Qt3DCore::QAttribute::defaultJointWeightsAttributeName());
}

//  QString Qt3DCore::QAttribute::defaultTextureCoordinate1AttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute38defaultTextureCoordinate1AttributeNameEv() {
  return new QString(
      Qt3DCore::QAttribute::defaultTextureCoordinate1AttributeName());
}

//  QString Qt3DCore::QAttribute::defaultTextureCoordinate2AttributeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QAttribute38defaultTextureCoordinate2AttributeNameEv() {
  return new QString(
      Qt3DCore::QAttribute::defaultTextureCoordinate2AttributeName());
}

//  void Qt3DCore::QAttribute::setBuffer(QBuffer *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute9setBufferEPNS_7QBufferE(
    Qt3DCore::QAttribute *self,
    Qt3DCore::QBuffer *buffer) {
  self->setBuffer(buffer);
}

//  void Qt3DCore::QAttribute::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute7setNameERK7QString(
    Qt3DCore::QAttribute *self,
    const QString *name) {
  self->setName(*name);
}

//  void Qt3DCore::QAttribute::setVertexBaseType(VertexBaseType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute17setVertexBaseTypeENS0_14VertexBaseTypeE(
    Qt3DCore::QAttribute *self,
    Qt3DCore::QAttribute::VertexBaseType type) {
  self->setVertexBaseType(type);
}

//  void Qt3DCore::QAttribute::setVertexSize(uint size)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute13setVertexSizeEj(
    Qt3DCore::QAttribute *self,
    uint size) {
  self->setVertexSize(size);
}

//  void Qt3DCore::QAttribute::setCount(uint count)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute8setCountEj(
    Qt3DCore::QAttribute *self,
    uint count) {
  self->setCount(count);
}

//  void Qt3DCore::QAttribute::setByteStride(uint byteStride)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute13setByteStrideEj(
    Qt3DCore::QAttribute *self,
    uint byteStride) {
  self->setByteStride(byteStride);
}

//  void Qt3DCore::QAttribute::setByteOffset(uint byteOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute13setByteOffsetEj(
    Qt3DCore::QAttribute *self,
    uint byteOffset) {
  self->setByteOffset(byteOffset);
}

//  void Qt3DCore::QAttribute::setDivisor(uint divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute10setDivisorEj(
    Qt3DCore::QAttribute *self,
    uint divisor) {
  self->setDivisor(divisor);
}

//  void Qt3DCore::QAttribute::setAttributeType(AttributeType attributeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute16setAttributeTypeENS0_13AttributeTypeE(
    Qt3DCore::QAttribute *self,
    Qt3DCore::QAttribute::AttributeType attributeType) {
  self->setAttributeType(attributeType);
}

//  void Qt3DCore::QAttribute::bufferChanged(QBuffer *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute13bufferChangedEPNS_7QBufferE(
    Qt3DCore::QAttribute *self,
    Qt3DCore::QBuffer *buffer) {
  self->bufferChanged(buffer);
}

//  void Qt3DCore::QAttribute::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute11nameChangedERK7QString(
    Qt3DCore::QAttribute *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  void Qt3DCore::QAttribute::vertexBaseTypeChanged(VertexBaseType
//      vertexBaseType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute21vertexBaseTypeChangedENS0_14VertexBaseTypeE(
    Qt3DCore::QAttribute *self,
    Qt3DCore::QAttribute::VertexBaseType vertexBaseType) {
  self->vertexBaseTypeChanged(vertexBaseType);
}

//  void Qt3DCore::QAttribute::vertexSizeChanged(uint vertexSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute17vertexSizeChangedEj(
    Qt3DCore::QAttribute *self,
    uint vertexSize) {
  self->vertexSizeChanged(vertexSize);
}

//  void Qt3DCore::QAttribute::dataTypeChanged(VertexBaseType vertexBaseType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute15dataTypeChangedENS0_14VertexBaseTypeE(
    Qt3DCore::QAttribute *self,
    Qt3DCore::QAttribute::VertexBaseType vertexBaseType) {
  self->dataTypeChanged(vertexBaseType);
}

//  void Qt3DCore::QAttribute::dataSizeChanged(uint vertexSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute15dataSizeChangedEj(
    Qt3DCore::QAttribute *self,
    uint vertexSize) {
  self->dataSizeChanged(vertexSize);
}

//  void Qt3DCore::QAttribute::countChanged(uint count)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute12countChangedEj(
    Qt3DCore::QAttribute *self,
    uint count) {
  self->countChanged(count);
}

//  void Qt3DCore::QAttribute::byteStrideChanged(uint byteStride)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute17byteStrideChangedEj(
    Qt3DCore::QAttribute *self,
    uint byteStride) {
  self->byteStrideChanged(byteStride);
}

//  void Qt3DCore::QAttribute::byteOffsetChanged(uint byteOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute17byteOffsetChangedEj(
    Qt3DCore::QAttribute *self,
    uint byteOffset) {
  self->byteOffsetChanged(byteOffset);
}

//  void Qt3DCore::QAttribute::divisorChanged(uint divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute14divisorChangedEj(
    Qt3DCore::QAttribute *self,
    uint divisor) {
  self->divisorChanged(divisor);
}

//  void Qt3DCore::QAttribute::attributeTypeChanged(AttributeType
//      attributeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAttribute20attributeTypeChangedENS0_13AttributeTypeE(
    Qt3DCore::QAttribute *self,
    Qt3DCore::QAttribute::AttributeType attributeType) {
  self->attributeTypeChanged(attributeType);
}

//  QAttributePrivate *Qt3DCore::QAttribute::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttributePrivate *ritual_ZN8Qt3DCore10QAttribute6d_funcEv(
    Qt3DCore::QAttribute *self) {
  return self->d_func();
}

//  const QAttributePrivate *Qt3DCore::QAttribute::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAttributePrivate *ritual_ZNK8Qt3DCore10QAttribute6d_funcEv(
    const Qt3DCore::QAttribute *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QAttribute, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAttribute(
    Qt3DCore::QAttribute *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAttribute *>(self)->take(key, call);
}
