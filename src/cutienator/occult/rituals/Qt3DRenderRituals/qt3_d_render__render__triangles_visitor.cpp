//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/trianglesvisitor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: Qt's 'Vector3D' is the SSE class
//  Qt3DCore::Vector3D_SSE where __SSE2__ is defined and QVector3D
//  elsewhere; the 'visit' ritual and its key for 'take' are written
//  for both, under that #if (the compiler refused a QVector3D for the
//  SSE class). Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/trianglesvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <cstring>

//  A Qt3DRender::Render::TrianglesVisitor that Python can take functions over in. Every Qt3DRender::Render::TrianglesVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_TrianglesVisitorCall0)(const void *, uint, const Vector3D *, uint, const Vector3D *, uint, const Vector3D *, int *);
class CuteQt3DRender_Render_TrianglesVisitor : public Qt3DRender::Render::TrianglesVisitor {
public:
  using Qt3DRender::Render::TrianglesVisitor::TrianglesVisitor;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if defined(__SSE2__)
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16TrianglesVisitor5visitEjRKN8Qt3DCore12Vector3D_SSEEjS5_jS5_")) {
      taken[0] = call;
      return true;
    }
#else
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16TrianglesVisitor5visitEjRK9QVector3DjS4_jS4_")) {
      taken[0] = call;
      return true;
    }
#endif  // defined(__SSE2__)
    return false;
  }

  //  void Qt3DRender::Render::TrianglesVisitor::visit(uint andx, const
  //      Vector3D &a, uint bndx, const Vector3D &b, uint cndx, const
  //      Vector3D &c)
  void visit(
      uint andx,
      const Vector3D &a,
      uint bndx,
      const Vector3D &b,
      uint cndx,
      const Vector3D &c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_TrianglesVisitorCall0 call = reinterpret_cast<CuteQt3DRender_Render_TrianglesVisitorCall0>(taken[0]);
      call(this, andx, &a, bndx, &b, cndx, &c, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DRender::Render::TrianglesVisitor::~TrianglesVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16TrianglesVisitorD1Ev(
    Qt3DRender::Render::TrianglesVisitor *self) {
  delete self;
}

#if defined(__SSE2__)
//  void Qt3DRender::Render::TrianglesVisitor::visit(uint andx, const
//      Vector3D &a, uint bndx, const Vector3D &b, uint cndx, const Vector3D
//      &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16TrianglesVisitor5visitEjRKN8Qt3DCore12Vector3D_SSEEjS5_jS5_(
    Qt3DRender::Render::TrianglesVisitor *self,
    uint andx,
    const Qt3DCore::Vector3D_SSE *a,
    uint bndx,
    const Qt3DCore::Vector3D_SSE *b,
    uint cndx,
    const Qt3DCore::Vector3D_SSE *c) {
  self->visit(andx, *a, bndx, *b, cndx, *c);
}
#else
//  void Qt3DRender::Render::TrianglesVisitor::visit(uint andx, const
//      Vector3D &a, uint bndx, const Vector3D &b, uint cndx, const Vector3D
//      &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16TrianglesVisitor5visitEjRK9QVector3DjS4_jS4_(
    Qt3DRender::Render::TrianglesVisitor *self,
    uint andx,
    const QVector3D *a,
    uint bndx,
    const QVector3D *b,
    uint cndx,
    const QVector3D *c) {
  self->visit(andx, *a, bndx, *b, cndx, *c);
}
#endif  // defined(__SSE2__)

//  a Python function taken by a CuteQt3DRender_Render_TrianglesVisitor, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_TrianglesVisitor(
    Qt3DRender::Render::TrianglesVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_TrianglesVisitor *>(self)->take(key, call);
}
