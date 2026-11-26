//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/uniform_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: Qt's 'Vector3D', 'Vector4D' and 'Matrix4x4' are the
//  SSE classes of Qt3DCore where __SSE2__ is defined, and QVector3D,
//  QVector4D and QMatrix4x4 elsewhere; each constructor is written for both,
//  under that #if (the compiler refused a QVector3D for the SSE class). The
//  constructor taking a QList is taken out (Qt's lists are not written).
//  Kept as it is when the generator runs again. Also added by hand on
//  2026-11-25, instances of templates of the class: 6.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/uniform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <Qt3DCore/qnodeid.h>

//  Qt3DRender::Render::UniformValue::UniformValue()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1Ev() {
  return new Qt3DRender::Render::UniformValue();
}

//  Qt3DRender::Render::UniformValue::UniformValue(int i)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1Ei(
    int i) {
  return new Qt3DRender::Render::UniformValue(i);
}

//  Qt3DRender::Render::UniformValue::UniformValue(uint i)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1Ej(
    uint i) {
  return new Qt3DRender::Render::UniformValue(i);
}

//  Qt3DRender::Render::UniformValue::UniformValue(float f)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1Ef(
    float f) {
  return new Qt3DRender::Render::UniformValue(f);
}

//  Qt3DRender::Render::UniformValue::UniformValue(double d)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1Ed(
    double d) {
  return new Qt3DRender::Render::UniformValue(d);
}

//  Qt3DRender::Render::UniformValue::UniformValue(bool b)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1Eb(
    bool b) {
  return new Qt3DRender::Render::UniformValue(b);
}

//  Qt3DRender::Render::UniformValue::UniformValue(const QVector2D &vec2)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERK9QVector2D(
    const QVector2D *vec2) {
  return new Qt3DRender::Render::UniformValue(*vec2);
}

#if defined(__SSE2__)
//  Qt3DRender::Render::UniformValue::UniformValue(const Vector3D &vec3)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERKN8Qt3DCore12Vector3D_SSEE(
    const Qt3DCore::Vector3D_SSE *vec3) {
  return new Qt3DRender::Render::UniformValue(*vec3);
}
#else
//  Qt3DRender::Render::UniformValue::UniformValue(const Vector3D &vec3)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERK9QVector3D(
    const QVector3D *vec3) {
  return new Qt3DRender::Render::UniformValue(*vec3);
}
#endif  // defined(__SSE2__)

#if defined(__SSE2__)
//  Qt3DRender::Render::UniformValue::UniformValue(const Vector4D &vec4)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERKN8Qt3DCore12Vector4D_SSEE(
    const Qt3DCore::Vector4D_SSE *vec4) {
  return new Qt3DRender::Render::UniformValue(*vec4);
}
#else
//  Qt3DRender::Render::UniformValue::UniformValue(const Vector4D &vec4)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERK9QVector4D(
    const QVector4D *vec4) {
  return new Qt3DRender::Render::UniformValue(*vec4);
}
#endif  // defined(__SSE2__)

//  Qt3DRender::Render::UniformValue::UniformValue(const QMatrix3x3 &mat33)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERK14QGenericMatrixILi3ELi3EfE(
    const QMatrix3x3 *mat33) {
  return new Qt3DRender::Render::UniformValue(*mat33);
}

#if defined(__SSE2__)
//  Qt3DRender::Render::UniformValue::UniformValue(const Matrix4x4 &mat44)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERKN8Qt3DCore13Matrix4x4_SSEE(
    const Qt3DCore::Matrix4x4_SSE *mat44) {
  return new Qt3DRender::Render::UniformValue(*mat44);
}
#else
//  Qt3DRender::Render::UniformValue::UniformValue(const QMatrix4x4 &mat44)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1ERK10QMatrix4x4(
    const QMatrix4x4 *mat44) {
  return new Qt3DRender::Render::UniformValue(*mat44);
}
#endif  // defined(__SSE2__)

//  Qt3DRender::Render::UniformValue::UniformValue(int byteSize, ValueType
//      valueType)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1EiNS1_9ValueTypeE(
    int byteSize,
    Qt3DRender::Render::UniformValue::ValueType valueType) {
  return new Qt3DRender::Render::UniformValue(byteSize, valueType);
}

//  Qt3DRender::Render::UniformValue::UniformValue(Qt3DCore::QNodeId id)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZN10Qt3DRender6Render12UniformValueC1EN8Qt3DCore7QNodeIdE(
    const Qt3DCore::QNodeId *id) {
  return new Qt3DRender::Render::UniformValue(*id);
}

//  ValueType Qt3DRender::Render::UniformValue::valueType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue::ValueType ritual_ZNK10Qt3DRender6Render12UniformValue9valueTypeEv(
    const Qt3DRender::Render::UniformValue *self) {
  return self->valueType();
}

//  UniformType Qt3DRender::Render::UniformValue::storedType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformType ritual_ZNK10Qt3DRender6Render12UniformValue10storedTypeEv(
    const Qt3DRender::Render::UniformValue *self) {
  return self->storedType();
}

//  int Qt3DRender::Render::UniformValue::byteSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12UniformValue8byteSizeEv(
    const Qt3DRender::Render::UniformValue *self) {
  return self->byteSize();
}

//  int Qt3DRender::Render::UniformValue::elementCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12UniformValue12elementCountEv(
    const Qt3DRender::Render::UniformValue *self) {
  return self->elementCount();
}

//  int Qt3DRender::Render::UniformValue::elementByteSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12UniformValue15elementByteSizeEv(
    const Qt3DRender::Render::UniformValue *self) {
  return self->elementByteSize();
}

//  bool Qt3DRender::Render::UniformValue::operator==(const UniformValue
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12UniformValueeqERKS1_(
    const Qt3DRender::Render::UniformValue *self,
    const Qt3DRender::Render::UniformValue *other) {
  return self->operator==(*other);
}

//  bool Qt3DRender::Render::UniformValue::operator!=(const UniformValue
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12UniformValueneERKS1_(
    const Qt3DRender::Render::UniformValue *self,
    const Qt3DRender::Render::UniformValue *other) {
  return self->operator!=(*other);
}

//  Qt3DRender::Render::UniformValue::~UniformValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12UniformValueD1Ev(
    Qt3DRender::Render::UniformValue *self) {
  delete self;
}

//  const float *Qt3DRender::Render::UniformValue::constData<float>() const
extern "C" Q_DECL_EXPORT
const float * ritual_ZNK10Qt3DRender6Render12UniformValue9constDataIfEEPKT_v(
    const Qt3DRender::Render::UniformValue *self) {
  return self->constData<float>();
}

//  float *Qt3DRender::Render::UniformValue::data<float>()
extern "C" Q_DECL_EXPORT
float * ritual_ZN10Qt3DRender6Render12UniformValue4dataIfEEPT_v(
    Qt3DRender::Render::UniformValue *self) {
  return self->data<float>();
}

//  const int *Qt3DRender::Render::UniformValue::constData<int>() const
extern "C" Q_DECL_EXPORT
const int * ritual_ZNK10Qt3DRender6Render12UniformValue9constDataIiEEPKT_v(
    const Qt3DRender::Render::UniformValue *self) {
  return self->constData<int>();
}

//  int *Qt3DRender::Render::UniformValue::data<int>()
extern "C" Q_DECL_EXPORT
int * ritual_ZN10Qt3DRender6Render12UniformValue4dataIiEEPT_v(
    Qt3DRender::Render::UniformValue *self) {
  return self->data<int>();
}

//  const unsigned int *Qt3DRender::Render::UniformValue::constData<unsigned
//      int>() const
extern "C" Q_DECL_EXPORT
const unsigned int * ritual_ZNK10Qt3DRender6Render12UniformValue9constDataIjEEPKT_v(
    const Qt3DRender::Render::UniformValue *self) {
  return self->constData<unsigned int>();
}

//  unsigned int *Qt3DRender::Render::UniformValue::data<unsigned int>()
extern "C" Q_DECL_EXPORT
unsigned int * ritual_ZN10Qt3DRender6Render12UniformValue4dataIjEEPT_v(
    Qt3DRender::Render::UniformValue *self) {
  return self->data<unsigned int>();
}
