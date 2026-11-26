//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qshaderdescription.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshaderdescription.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qdebug.h>
#include <QtCore/QList>
#include <array>

//  QShaderDescription::QShaderDescription()
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZN18QShaderDescriptionC1Ev() {
  return new QShaderDescription();
}

//  QShaderDescription::QShaderDescription(const QShaderDescription &other)
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZN18QShaderDescriptionC1ERKS_(
    const QShaderDescription *other) {
  return new QShaderDescription(*other);
}

//  QShaderDescription &QShaderDescription::operator=(const
//      QShaderDescription &other)
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZN18QShaderDescriptionaSERKS_(
    QShaderDescription *self,
    const QShaderDescription *other) {
  return &(self->operator=(*other));
}

//  QShaderDescription::~QShaderDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QShaderDescriptionD1Ev(QShaderDescription *self) {
  delete self;
}

//  void QShaderDescription::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QShaderDescription6detachEv(QShaderDescription *self) {
  self->detach();
}

//  bool QShaderDescription::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QShaderDescription7isValidEv(
    const QShaderDescription *self) {
  return self->isValid();
}

//  void QShaderDescription::serialize(QDataStream *stream, int version)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QShaderDescription9serializeEP11QDataStreami(
    const QShaderDescription *self,
    QDataStream *stream,
    int version) {
  self->serialize(stream, version);
}

//  QByteArray QShaderDescription::toJson() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QShaderDescription6toJsonEv(
    const QShaderDescription *self) {
  return new QByteArray(self->toJson());
}

//  QShaderDescription QShaderDescription::deserialize(QDataStream *stream,
//      int version)
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZN18QShaderDescription11deserializeEP11QDataStreami(
    QDataStream *stream,
    int version) {
  return new QShaderDescription(
      QShaderDescription::deserialize(
          stream,
          version));
}

//  QList<InOutVariable> QShaderDescription::inputVariables() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::InOutVariable> *ritual_ZNK18QShaderDescription14inputVariablesEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::InOutVariable>(
      self->inputVariables());
}

//  QList<InOutVariable> QShaderDescription::outputVariables() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::InOutVariable> *ritual_ZNK18QShaderDescription15outputVariablesEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::InOutVariable>(
      self->outputVariables());
}

//  QList<UniformBlock> QShaderDescription::uniformBlocks() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::UniformBlock> *ritual_ZNK18QShaderDescription13uniformBlocksEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::UniformBlock>(self->uniformBlocks());
}

//  QList<PushConstantBlock> QShaderDescription::pushConstantBlocks() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::PushConstantBlock> *ritual_ZNK18QShaderDescription18pushConstantBlocksEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::PushConstantBlock>(
      self->pushConstantBlocks());
}

//  QList<StorageBlock> QShaderDescription::storageBlocks() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::StorageBlock> *ritual_ZNK18QShaderDescription13storageBlocksEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::StorageBlock>(self->storageBlocks());
}

//  QList<InOutVariable> QShaderDescription::combinedImageSamplers() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::InOutVariable> *ritual_ZNK18QShaderDescription21combinedImageSamplersEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::InOutVariable>(
      self->combinedImageSamplers());
}

//  QList<InOutVariable> QShaderDescription::separateImages() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::InOutVariable> *ritual_ZNK18QShaderDescription14separateImagesEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::InOutVariable>(
      self->separateImages());
}

//  QList<InOutVariable> QShaderDescription::separateSamplers() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::InOutVariable> *ritual_ZNK18QShaderDescription16separateSamplersEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::InOutVariable>(
      self->separateSamplers());
}

//  QList<InOutVariable> QShaderDescription::storageImages() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::InOutVariable> *ritual_ZNK18QShaderDescription13storageImagesEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::InOutVariable>(self->storageImages());
}

//  QList<BuiltinVariable> QShaderDescription::inputBuiltinVariables() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::BuiltinVariable> *ritual_ZNK18QShaderDescription21inputBuiltinVariablesEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::BuiltinVariable>(
      self->inputBuiltinVariables());
}

//  QList<BuiltinVariable> QShaderDescription::outputBuiltinVariables() const
extern "C" Q_DECL_EXPORT
QList<QShaderDescription::BuiltinVariable> *ritual_ZNK18QShaderDescription22outputBuiltinVariablesEv(
    const QShaderDescription *self) {
  return new QList<QShaderDescription::BuiltinVariable>(
      self->outputBuiltinVariables());
}

//  std::array<uint, 3> QShaderDescription::computeShaderLocalSize() const
extern "C" Q_DECL_EXPORT
std::array<uint, 3> *ritual_ZNK18QShaderDescription22computeShaderLocalSizeEv(
    const QShaderDescription *self) {
  return new std::array<uint, 3>(self->computeShaderLocalSize());
}

//  uint QShaderDescription::tessellationOutputVertexCount() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QShaderDescription29tessellationOutputVertexCountEv(
    const QShaderDescription *self) {
  return self->tessellationOutputVertexCount();
}

//  TessellationMode QShaderDescription::tessellationMode() const
extern "C" Q_DECL_EXPORT
QShaderDescription::TessellationMode ritual_ZNK18QShaderDescription16tessellationModeEv(
    const QShaderDescription *self) {
  return self->tessellationMode();
}

//  TessellationWindingOrder QShaderDescription::tessellationWindingOrder()
//      const
extern "C" Q_DECL_EXPORT
QShaderDescription::TessellationWindingOrder ritual_ZNK18QShaderDescription24tessellationWindingOrderEv(
    const QShaderDescription *self) {
  return self->tessellationWindingOrder();
}

//  TessellationPartitioning QShaderDescription::tessellationPartitioning()
//      const
extern "C" Q_DECL_EXPORT
QShaderDescription::TessellationPartitioning ritual_ZNK18QShaderDescription24tessellationPartitioningEv(
    const QShaderDescription *self) {
  return self->tessellationPartitioning();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QShaderDescription &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QShaderDescription(
    const QDebug *a0,
    const QShaderDescription *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  bool operator==(const QShaderDescription &lhs, const QShaderDescription
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QShaderDescriptionS1_(
    const QShaderDescription *lhs,
    const QShaderDescription *rhs) {
  return operator==(*lhs, *rhs);
}

//  a QList<QShaderDescription::InOutVariable> a ritual of QShaderDescription
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShaderDescription__QList_QShaderDescription_InOutVariable(
    QList<QShaderDescription::InOutVariable> *self) {
  delete self;
}

//  a QList<QShaderDescription::UniformBlock> a ritual of QShaderDescription
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShaderDescription__QList_QShaderDescription_UniformBlock(
    QList<QShaderDescription::UniformBlock> *self) {
  delete self;
}

//  a QList<QShaderDescription::PushConstantBlock> a ritual of
//      QShaderDescription gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShaderDescription__QList_QShaderDescription_PushConstantBlock(
    QList<QShaderDescription::PushConstantBlock> *self) {
  delete self;
}

//  a QList<QShaderDescription::StorageBlock> a ritual of QShaderDescription
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShaderDescription__QList_QShaderDescription_StorageBlock(
    QList<QShaderDescription::StorageBlock> *self) {
  delete self;
}

//  a QList<QShaderDescription::BuiltinVariable> a ritual of
//      QShaderDescription gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShaderDescription__QList_QShaderDescription_BuiltinVariable(
    QList<QShaderDescription::BuiltinVariable> *self) {
  delete self;
}

//  a std::array<uint, 3> a ritual of QShaderDescription gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShaderDescription__std_array_uint_3(
    std::array<uint, 3> *self) {
  delete self;
}
