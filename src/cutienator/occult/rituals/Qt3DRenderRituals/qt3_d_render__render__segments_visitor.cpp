//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/segmentsvisitor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: Qt's 'Vector3D' is the SSE class
//  Qt3DCore::Vector3D_SSE where __SSE2__ is defined and QVector3D
//  elsewhere; the 'visit' ritual and its key for 'take' are written
//  for both, under that #if (the compiler refused a QVector3D for the
//  SSE class). Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/segmentsvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <cstring>

//  A Qt3DRender::Render::SegmentsVisitor that Python can take functions over in. Every Qt3DRender::Render::SegmentsVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_SegmentsVisitorCall0)(const void *, uint, const Vector3D *, uint, const Vector3D *, int *);
class CuteQt3DRender_Render_SegmentsVisitor : public Qt3DRender::Render::SegmentsVisitor {
public:
  using Qt3DRender::Render::SegmentsVisitor::SegmentsVisitor;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if defined(__SSE2__)
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render15SegmentsVisitor5visitEjRKN8Qt3DCore12Vector3D_SSEEjS5_")) {
      taken[0] = call;
      return true;
    }
#else
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render15SegmentsVisitor5visitEjRK9QVector3DjS4_")) {
      taken[0] = call;
      return true;
    }
#endif  // defined(__SSE2__)
    return false;
  }

  //  void Qt3DRender::Render::SegmentsVisitor::visit(uint andx, const
  //      Vector3D &a, uint bndx, const Vector3D &b)
  void visit(
      uint andx,
      const Vector3D &a,
      uint bndx,
      const Vector3D &b) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_SegmentsVisitorCall0 call = reinterpret_cast<CuteQt3DRender_Render_SegmentsVisitorCall0>(taken[0]);
      call(this, andx, &a, bndx, &b, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DRender::Render::SegmentsVisitor::~SegmentsVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15SegmentsVisitorD1Ev(
    Qt3DRender::Render::SegmentsVisitor *self) {
  delete self;
}

#if defined(__SSE2__)
//  void Qt3DRender::Render::SegmentsVisitor::visit(uint andx, const Vector3D
//      &a, uint bndx, const Vector3D &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15SegmentsVisitor5visitEjRKN8Qt3DCore12Vector3D_SSEEjS5_(
    Qt3DRender::Render::SegmentsVisitor *self,
    uint andx,
    const Qt3DCore::Vector3D_SSE *a,
    uint bndx,
    const Qt3DCore::Vector3D_SSE *b) {
  self->visit(andx, *a, bndx, *b);
}
#else
//  void Qt3DRender::Render::SegmentsVisitor::visit(uint andx, const Vector3D
//      &a, uint bndx, const Vector3D &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15SegmentsVisitor5visitEjRK9QVector3DjS4_(
    Qt3DRender::Render::SegmentsVisitor *self,
    uint andx,
    const QVector3D *a,
    uint bndx,
    const QVector3D *b) {
  self->visit(andx, *a, bndx, *b);
}
#endif  // defined(__SSE2__)

//  a Python function taken by a CuteQt3DRender_Render_SegmentsVisitor, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_SegmentsVisitor(
    Qt3DRender::Render::SegmentsVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_SegmentsVisitor *>(self)->take(key, call);
}
