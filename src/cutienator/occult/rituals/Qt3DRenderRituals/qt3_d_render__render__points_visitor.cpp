//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pointsvisitor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: Qt's 'Vector3D' is the SSE class
//  Qt3DCore::Vector3D_SSE where __SSE2__ is defined and QVector3D
//  elsewhere; the 'visit' ritual and its key for 'take' are written
//  for both, under that #if (the compiler refused a QVector3D for the
//  SSE class). Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pointsvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <cstring>

//  A Qt3DRender::Render::PointsVisitor that Python can take functions over in. Every Qt3DRender::Render::PointsVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_PointsVisitorCall0)(const void *, uint, const Vector3D *, int *);
class CuteQt3DRender_Render_PointsVisitor : public Qt3DRender::Render::PointsVisitor {
public:
  using Qt3DRender::Render::PointsVisitor::PointsVisitor;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if defined(__SSE2__)
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render13PointsVisitor5visitEjRKN8Qt3DCore12Vector3D_SSEE")) {
      taken[0] = call;
      return true;
    }
#else
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render13PointsVisitor5visitEjRK9QVector3D")) {
      taken[0] = call;
      return true;
    }
#endif  // defined(__SSE2__)
    return false;
  }

  //  void Qt3DRender::Render::PointsVisitor::visit(uint ndx, const
  //      Vector3D &c)
  void visit(uint ndx, const Vector3D &c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_PointsVisitorCall0 call = reinterpret_cast<CuteQt3DRender_Render_PointsVisitorCall0>(taken[0]);
      call(this, ndx, &c, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DRender::Render::PointsVisitor::~PointsVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13PointsVisitorD1Ev(
    Qt3DRender::Render::PointsVisitor *self) {
  delete self;
}

#if defined(__SSE2__)
//  void Qt3DRender::Render::PointsVisitor::visit(uint ndx, const Vector3D
//      &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13PointsVisitor5visitEjRKN8Qt3DCore12Vector3D_SSEE(
    Qt3DRender::Render::PointsVisitor *self,
    uint ndx,
    const Qt3DCore::Vector3D_SSE *c) {
  self->visit(ndx, *c);
}
#else
//  void Qt3DRender::Render::PointsVisitor::visit(uint ndx, const Vector3D
//      &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13PointsVisitor5visitEjRK9QVector3D(
    Qt3DRender::Render::PointsVisitor *self,
    uint ndx,
    const QVector3D *c) {
  self->visit(ndx, *c);
}
#endif  // defined(__SSE2__)

//  a Python function taken by a CuteQt3DRender_Render_PointsVisitor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_PointsVisitor(
    Qt3DRender::Render::PointsVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_PointsVisitor *>(self)->take(key, call);
}
