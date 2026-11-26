//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#include <QtGui/6.12.0/QtGui/rhi/qshaderdescription.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QShader::QShader()
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN7QShaderC1Ev() {
  return new QShader();
}

//  QShader::QShader(const QShader &other)
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN7QShaderC1ERKS_(const QShader *other) {
  return new QShader(*other);
}

//  QShader &QShader::operator=(const QShader &other)
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN7QShaderaSERKS_(QShader *self, const QShader *other) {
  return &(self->operator=(*other));
}

//  QShader::QShader(QShader &&other)
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN7QShaderC1EOS_(QShader *other) {
  return new QShader(std::move(*other));
}

//  QShader &QShader::operator=(QShader &&other)
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN7QShaderaSEOS_(QShader *self, QShader *other) {
  return &(self->operator=(std::move(*other)));
}

//  QShader::~QShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShaderD1Ev(QShader *self) {
  delete self;
}

//  void QShader::swap(QShader &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader4swapERS_(QShader *self, QShader *other) {
  self->swap(*other);
}

//  void QShader::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader6detachEv(QShader *self) {
  self->detach();
}

//  bool QShader::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QShader7isValidEv(const QShader *self) {
  return self->isValid();
}

//  Stage QShader::stage() const
extern "C" Q_DECL_EXPORT
QShader::Stage ritual_ZNK7QShader5stageEv(const QShader *self) {
  return self->stage();
}

//  void QShader::setStage(Stage stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader8setStageENS_5StageE(
    QShader *self,
    QShader::Stage stage) {
  self->setStage(stage);
}

//  QShaderDescription QShader::description() const
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZNK7QShader11descriptionEv(const QShader *self) {
  return new QShaderDescription(self->description());
}

//  void QShader::setDescription(const QShaderDescription &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader14setDescriptionERK18QShaderDescription(
    QShader *self,
    const QShaderDescription *desc) {
  self->setDescription(*desc);
}

//  QList<QShaderKey> QShader::availableShaders() const
extern "C" Q_DECL_EXPORT
QList<QShaderKey> *ritual_ZNK7QShader16availableShadersEv(
    const QShader *self) {
  return new QList<QShaderKey>(self->availableShaders());
}

//  QShaderCode QShader::shader(const QShaderKey &key) const
extern "C" Q_DECL_EXPORT
QShaderCode *ritual_ZNK7QShader6shaderERK10QShaderKey(
    const QShader *self,
    const QShaderKey *key) {
  return new QShaderCode(self->shader(*key));
}

//  void QShader::setShader(const QShaderKey &key, const QShaderCode &shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader9setShaderERK10QShaderKeyRK11QShaderCode(
    QShader *self,
    const QShaderKey *key,
    const QShaderCode *shader) {
  self->setShader(*key, *shader);
}

//  void QShader::removeShader(const QShaderKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader12removeShaderERK10QShaderKey(
    QShader *self,
    const QShaderKey *key) {
  self->removeShader(*key);
}

//  QByteArray QShader::serialized(SerializedFormatVersion version) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QShader10serializedENS_23SerializedFormatVersionE(
    const QShader *self,
    QShader::SerializedFormatVersion version) {
  return new QByteArray(self->serialized(version));
}

//  QShader QShader::fromSerialized(const QByteArray &data)
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN7QShader14fromSerializedERK10QByteArray(
    const QByteArray *data) {
  return new QShader(QShader::fromSerialized(*data));
}

//  NativeResourceBindingMap QShader::nativeResourceBindingMap(const
//      QShaderKey &key) const
extern "C" Q_DECL_EXPORT
QShader::NativeResourceBindingMap *ritual_ZNK7QShader24nativeResourceBindingMapERK10QShaderKey(
    const QShader *self,
    const QShaderKey *key) {
  return new QShader::NativeResourceBindingMap(
      self->nativeResourceBindingMap(
          *key));
}

//  void QShader::setResourceBindingMap(const QShaderKey &key, const
//      NativeResourceBindingMap &map)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader21setResourceBindingMapERK10QShaderKeyRK4QMapIiSt4pairIiiEE(
    QShader *self,
    const QShaderKey *key,
    const QShader::NativeResourceBindingMap *map) {
  self->setResourceBindingMap(*key, *map);
}

//  void QShader::removeResourceBindingMap(const QShaderKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader24removeResourceBindingMapERK10QShaderKey(
    QShader *self,
    const QShaderKey *key) {
  self->removeResourceBindingMap(*key);
}

//  SeparateToCombinedImageSamplerMappingList
//      QShader::separateToCombinedImageSamplerMappingList(const QShaderKey
//      &key) const
extern "C" Q_DECL_EXPORT
QShader::SeparateToCombinedImageSamplerMappingList *ritual_ZNK7QShader41separateToCombinedImageSamplerMappingListERK10QShaderKey(
    const QShader *self,
    const QShaderKey *key) {
  return new QShader::SeparateToCombinedImageSamplerMappingList(
      self->separateToCombinedImageSamplerMappingList(
          *key));
}

//  void QShader::setSeparateToCombinedImageSamplerMappingList(const
//      QShaderKey &key, const SeparateToCombinedImageSamplerMappingList
//      &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader44setSeparateToCombinedImageSamplerMappingListERK10QShaderKeyRK5QListINS_37SeparateToCombinedImageSamplerMappingEE(
    QShader *self,
    const QShaderKey *key,
    const QShader::SeparateToCombinedImageSamplerMappingList *list) {
  self->setSeparateToCombinedImageSamplerMappingList(*key, *list);
}

//  void QShader::removeSeparateToCombinedImageSamplerMappingList(const
//      QShaderKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader47removeSeparateToCombinedImageSamplerMappingListERK10QShaderKey(
    QShader *self,
    const QShaderKey *key) {
  self->removeSeparateToCombinedImageSamplerMappingList(*key);
}

//  NativeShaderInfo QShader::nativeShaderInfo(const QShaderKey &key) const
extern "C" Q_DECL_EXPORT
QShader::NativeShaderInfo *ritual_ZNK7QShader16nativeShaderInfoERK10QShaderKey(
    const QShader *self,
    const QShaderKey *key) {
  return new QShader::NativeShaderInfo(self->nativeShaderInfo(*key));
}

//  void QShader::setNativeShaderInfo(const QShaderKey &key, const
//      NativeShaderInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader19setNativeShaderInfoERK10QShaderKeyRKNS_16NativeShaderInfoE(
    QShader *self,
    const QShaderKey *key,
    const QShader::NativeShaderInfo *info) {
  self->setNativeShaderInfo(*key, *info);
}

//  void QShader::removeNativeShaderInfo(const QShaderKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QShader22removeNativeShaderInfoERK10QShaderKey(
    QShader *self,
    const QShaderKey *key) {
  self->removeNativeShaderInfo(*key);
}

//  bool operator==(const QShader &a0, const QShader &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QShaderS1_(const QShader *a0, const QShader *a1) {
  return operator==(*a0, *a1);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QShader &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK7QShader(const QDebug *a0, const QShader *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  a QShader::NativeResourceBindingMap a ritual of QShader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShader__QShader_NativeResourceBindingMap(
    QShader::NativeResourceBindingMap *self) {
  delete self;
}

//  a QShader::SeparateToCombinedImageSamplerMappingList a ritual of QShader
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QShader__QShader_SeparateToCombinedImageSamplerMappingList(
    QShader::SeparateToCombinedImageSamplerMappingList *self) {
  delete self;
}
