//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrenderpluginfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrenderpluginfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList Qt3DRender::Render::QRenderPluginFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN10Qt3DRender6Render20QRenderPluginFactory4keysEv() {
  return new QList<QString>(
      Qt3DRender::Render::QRenderPluginFactory::keys());
}

//  QRenderPlugin *Qt3DRender::Render::QRenderPluginFactory::create(const
//      QString &name, const QStringList &args)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::QRenderPlugin *ritual_ZN10Qt3DRender6Render20QRenderPluginFactory6createERK7QStringRK5QListIS2_E(
    const QString *name,
    const QList<QString> *args) {
  return Qt3DRender::Render::QRenderPluginFactory::create(*name, *args);
}

//  Qt3DRender::Render::QRenderPluginFactory::~QRenderPluginFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20QRenderPluginFactoryD1Ev(
    Qt3DRender::Render::QRenderPluginFactory *self) {
  delete self;
}
