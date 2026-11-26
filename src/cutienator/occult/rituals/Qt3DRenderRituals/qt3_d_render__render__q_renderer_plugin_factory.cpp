//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrendererpluginfactory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrendererpluginfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList Qt3DRender::Render::QRendererPluginFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN10Qt3DRender6Render22QRendererPluginFactory4keysEv() {
  return new QList<QString>(
      Qt3DRender::Render::QRendererPluginFactory::keys());
}

//  AbstractRenderer
//      *Qt3DRender::Render::QRendererPluginFactory::create(const QString
//      &name)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AbstractRenderer *ritual_ZN10Qt3DRender6Render22QRendererPluginFactory6createERK7QString(
    const QString *name) {
  return Qt3DRender::Render::QRendererPluginFactory::create(*name);
}

//  Qt3DRender::Render::QRendererPluginFactory::~QRendererPluginFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render22QRendererPluginFactoryD1Ev(
    Qt3DRender::Render::QRendererPluginFactory *self) {
  delete self;
}
