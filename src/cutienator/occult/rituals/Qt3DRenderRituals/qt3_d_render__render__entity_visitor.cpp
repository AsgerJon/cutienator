//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/entityvisitor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/entityvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::EntityVisitor that Python can take functions over in. Every Qt3DRender::Render::EntityVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQt3DRender_Render_EntityVisitorCall0)(const void *, Qt3DRender::Render::Entity *, int *);
class CuteQt3DRender_Render_EntityVisitor : public Qt3DRender::Render::EntityVisitor {
public:
  using Qt3DRender::Render::EntityVisitor::EntityVisitor;
  CuteQt3DRender_Render_EntityVisitor(const Qt3DRender::Render::EntityVisitor &other) : Qt3DRender::Render::EntityVisitor(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render13EntityVisitor5visitEPNS0_6EntityE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Operation Qt3DRender::Render::EntityVisitor::visit(Entity *entity)
  Qt3DRender::Render::EntityVisitor::Operation visit(
      Qt3DRender::Render::Entity *entity) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_EntityVisitorCall0 call = reinterpret_cast<CuteQt3DRender_Render_EntityVisitorCall0>(taken[0]);
      int given = call(this, entity, &handled);
      if (handled) return static_cast<Qt3DRender::Render::EntityVisitor::Operation>(given);
    }
    return Qt3DRender::Render::EntityVisitor::visit(entity);
  }
};

//  Qt3DRender::Render::EntityVisitor::~EntityVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13EntityVisitorD1Ev(
    Qt3DRender::Render::EntityVisitor *self) {
  delete self;
}

//  Operation Qt3DRender::Render::EntityVisitor::visit(Entity *entity)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EntityVisitor::Operation ritual_ZN10Qt3DRender6Render13EntityVisitor5visitEPNS0_6EntityE(
    Qt3DRender::Render::EntityVisitor *self,
    Qt3DRender::Render::Entity *entity) {
  return self->visit(entity);
}

//  a Python function taken by a CuteQt3DRender_Render_EntityVisitor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_EntityVisitor(
    Qt3DRender::Render::EntityVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_EntityVisitor *>(self)->take(key, call);
}
