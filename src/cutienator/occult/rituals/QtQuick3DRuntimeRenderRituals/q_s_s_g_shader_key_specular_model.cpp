//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArray>

//  QSSGShaderKeySpecularModel::QSSGShaderKeySpecularModel(const char
//      *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeySpecularModel *ritual_ZN26QSSGShaderKeySpecularModelC1EPKc(
    const char *inName) {
  return new QSSGShaderKeySpecularModel(inName);
}

//  void QSSGShaderKeySpecularModel::setSpecularModel(QSSGDataRef<quint32>
//      inKeySet, QSSGRenderDefaultMaterial::MaterialSpecularModel inModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGShaderKeySpecularModel16setSpecularModelE11QSSGDataRefIjEN25QSSGRenderDefaultMaterial21MaterialSpecularModelE(
    QSSGShaderKeySpecularModel *self,
    const QSSGDataRef<quint32> *inKeySet,
    QSSGRenderDefaultMaterial::MaterialSpecularModel inModel) {
  self->setSpecularModel(*inKeySet, inModel);
}

//  QSSGRenderDefaultMaterial::MaterialSpecularModel
//      QSSGShaderKeySpecularModel::getSpecularModel(QSSGDataView<quint32>
//      inKeySet) const
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialSpecularModel ritual_ZNK26QSSGShaderKeySpecularModel16getSpecularModelE12QSSGDataViewIjE(
    const QSSGShaderKeySpecularModel *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->getSpecularModel(*inKeySet);
}

//  void QSSGShaderKeySpecularModel::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QSSGShaderKeySpecularModel8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeySpecularModel *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  void QSSGShaderKeySpecularModel::fromString(const QByteArray &ioStr,
//      QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGShaderKeySpecularModel10fromStringERK10QByteArray11QSSGDataRefIjE(
    QSSGShaderKeySpecularModel *self,
    const QByteArray *ioStr,
    const QSSGDataRef<quint32> *inKeySet) {
  self->fromString(*ioStr, *inKeySet);
}

//  QSSGShaderKeySpecularModel::~QSSGShaderKeySpecularModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGShaderKeySpecularModelD1Ev(
    QSSGShaderKeySpecularModel *self) {
  delete self;
}
