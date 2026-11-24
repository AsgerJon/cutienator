//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  ValueType QSSGSceneDesc::Animation::KeyPosition::getValueType() const
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Animation::KeyPosition::ValueType ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition12getValueTypeEv(
    const QSSGSceneDesc::Animation::KeyPosition *self) {
  return self->getValueType();
}

//  KeyType QSSGSceneDesc::Animation::KeyPosition::getKeyType() const
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Animation::KeyPosition::KeyType ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition10getKeyTypeEv(
    const QSSGSceneDesc::Animation::KeyPosition *self) {
  return self->getKeyType();
}

//  QVariant QSSGSceneDesc::Animation::KeyPosition::getValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition8getValueEv(
    const QSSGSceneDesc::Animation::KeyPosition *self) {
  return new QVariant(self->getValue());
}

//  QMetaType::Type
//      QSSGSceneDesc::Animation::KeyPosition::getValueQMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType::Type ritual_ZNK13QSSGSceneDesc9Animation11KeyPosition17getValueQMetaTypeEv(
    const QSSGSceneDesc::Animation::KeyPosition *self) {
  return self->getValueQMetaType();
}

//  QSSGSceneDesc::Animation::KeyPosition::~KeyPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc9Animation11KeyPositionD1Ev(
    QSSGSceneDesc::Animation::KeyPosition *self) {
  delete self;
}
