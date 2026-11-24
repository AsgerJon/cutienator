//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshaderdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshaderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  QVariant Qt3DRender::QShaderDataPropertyReader::readProperty(const
//      QVariant &v)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN10Qt3DRender25QShaderDataPropertyReader12readPropertyERK8QVariant(
    Qt3DRender::QShaderDataPropertyReader *self,
    const QVariant *v) {
  return new QVariant(self->readProperty(*v));
}

//  Qt3DRender::QShaderDataPropertyReader::~QShaderDataPropertyReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender25QShaderDataPropertyReaderD1Ev(
    Qt3DRender::QShaderDataPropertyReader *self) {
  delete self;
}

//  QVariant Qt3DRender::QShaderDataPropertyReader::readProperty(const
//      QVariant &v)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN10Qt3DRender25QShaderDataPropertyReader12readPropertyERK8QVariant(
    Qt3DRender::QShaderDataPropertyReader *self,
    const QVariant *v) {
  return new QVariant(
      self->Qt3DRender::QShaderDataPropertyReader::readProperty(
          *v));
}
