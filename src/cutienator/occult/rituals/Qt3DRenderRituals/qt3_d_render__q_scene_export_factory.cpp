//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qsceneexportfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qsceneexportfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList Qt3DRender::QSceneExportFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN10Qt3DRender19QSceneExportFactory4keysEv() {
  return new QList<QString>(Qt3DRender::QSceneExportFactory::keys());
}

//  QSceneExporter *Qt3DRender::QSceneExportFactory::create(const QString
//      &name, const QStringList &args)
extern "C" Q_DECL_EXPORT
Qt3DRender::QSceneExporter *ritual_ZN10Qt3DRender19QSceneExportFactory6createERK7QStringRK5QListIS1_E(
    const QString *name,
    const QList<QString> *args) {
  return Qt3DRender::QSceneExportFactory::create(*name, *args);
}

//  Qt3DRender::QSceneExportFactory::~QSceneExportFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QSceneExportFactoryD1Ev(
    Qt3DRender::QSceneExportFactory *self) {
  delete self;
}
