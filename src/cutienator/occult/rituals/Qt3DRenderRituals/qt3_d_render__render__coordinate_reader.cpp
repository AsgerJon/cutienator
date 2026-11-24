//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/trianglesvisitor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/trianglesvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::CoordinateReader::CoordinateReader(NodeManagers
//      *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::CoordinateReader *ritual_ZN10Qt3DRender6Render16CoordinateReaderC1EPNS0_12NodeManagersE(
    Qt3DRender::Render::NodeManagers *manager) {
  return new Qt3DRender::Render::CoordinateReader(manager);
}

//  Qt3DRender::Render::CoordinateReader::~CoordinateReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16CoordinateReaderD1Ev(
    Qt3DRender::Render::CoordinateReader *self) {
  delete self;
}
