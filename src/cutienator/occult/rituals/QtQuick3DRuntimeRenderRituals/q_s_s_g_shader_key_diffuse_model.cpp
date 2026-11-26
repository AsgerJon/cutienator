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

//  QSSGShaderKeyDiffuseModel::QSSGShaderKeyDiffuseModel(const char *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyDiffuseModel *ritual_ZN25QSSGShaderKeyDiffuseModelC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyDiffuseModel(inName);
}

//  void QSSGShaderKeyDiffuseModel::setDiffuseModel(QSSGDataRef<quint32>
//      inKeySet, QSSGRenderDefaultMaterial::MaterialDiffuseModel inModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderKeyDiffuseModel15setDiffuseModelE11QSSGDataRefIjEN25QSSGRenderDefaultMaterial20MaterialDiffuseModelE(
    QSSGShaderKeyDiffuseModel *self,
    const QSSGDataRef<quint32> *inKeySet,
    QSSGRenderDefaultMaterial::MaterialDiffuseModel inModel) {
  self->setDiffuseModel(*inKeySet, inModel);
}

//  QSSGRenderDefaultMaterial::MaterialDiffuseModel
//      QSSGShaderKeyDiffuseModel::getDiffuseModel(QSSGDataView<quint32>
//      inKeySet) const
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialDiffuseModel ritual_ZNK25QSSGShaderKeyDiffuseModel15getDiffuseModelE12QSSGDataViewIjE(
    const QSSGShaderKeyDiffuseModel *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->getDiffuseModel(*inKeySet);
}

//  void QSSGShaderKeyDiffuseModel::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QSSGShaderKeyDiffuseModel8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeyDiffuseModel *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  void QSSGShaderKeyDiffuseModel::fromString(const QByteArray &ioStr,
//      QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderKeyDiffuseModel10fromStringERK10QByteArray11QSSGDataRefIjE(
    QSSGShaderKeyDiffuseModel *self,
    const QByteArray *ioStr,
    const QSSGDataRef<quint32> *inKeySet) {
  self->fromString(*ioStr, *inKeySet);
}

//  QSSGShaderKeyDiffuseModel::~QSSGShaderKeyDiffuseModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderKeyDiffuseModelD1Ev(
    QSSGShaderKeyDiffuseModel *self) {
  delete self;
}
