//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshadergenerator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadergenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QByteArray Qt3DRender::QShaderGenerator::createShaderCode(const
//      QStringList &enabledLayers) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender16QShaderGenerator16createShaderCodeERK5QListI7QStringE(
    const Qt3DRender::QShaderGenerator *self,
    const QList<QString> *enabledLayers) {
  return new QByteArray(self->createShaderCode(*enabledLayers));
}

//  Qt3DRender::QShaderGenerator::~QShaderGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QShaderGeneratorD1Ev(
    Qt3DRender::QShaderGenerator *self) {
  delete self;
}
