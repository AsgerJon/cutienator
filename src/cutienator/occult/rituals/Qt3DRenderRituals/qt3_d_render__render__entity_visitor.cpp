//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/entityvisitor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/entityvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/entityvisitor_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/backend/entityvisitor.cpp, line 29, as _ZN10Qt3DRender6Render13EntityVisitor5visitEPNS0_6EntityE
namespace Qt3DRender::Render {
inline EntityVisitor::Operation EntityVisitor::visit(Entity *entity) {
    // return false to stop traversal
    if (!entity)
        return Stop;
    return Continue;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/entityvisitor.cpp, line 20, as _ZN10Qt3DRender6Render13EntityVisitorD2Ev
namespace Qt3DRender::Render {
inline EntityVisitor::~EntityVisitor() = default;
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/entityvisitor.cpp, line 43, as _ZNK10Qt3DRender6Render13EntityVisitor13pruneDisabledEv
namespace Qt3DRender::Render {
inline bool EntityVisitor::pruneDisabled() const
{
    return m_pruneDisabled;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/entityvisitor.cpp, line 48, as _ZN10Qt3DRender6Render13EntityVisitor16setPruneDisabledEb
namespace Qt3DRender::Render {
inline void EntityVisitor::setPruneDisabled(bool pruneDisabled)
{
    m_pruneDisabled = pruneDisabled;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/entityvisitor.cpp, line 59, as _ZN10Qt3DRender6Render13EntityVisitor5applyEPNS0_6EntityE
namespace Qt3DRender::Render {
inline bool EntityVisitor::apply(Entity *root) {
    if (!root)
        return false;
    if (m_pruneDisabled && !root->isEnabled())
        return true;

    const auto op = visit(root);
    if (op == Stop)
        return false;
    if (op == Prune)
        return true;

    const auto &childrenHandles = root->childrenHandles();
    for (const HEntity &handle : childrenHandles) {
        Entity *child = m_manager->renderNodesManager()->data(handle);
        if (child != nullptr && !apply(child))
            return false;
    }

    return true;
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  A Qt3DRender::Render::EntityVisitor that Python can take functions over in. Every Qt3DRender::Render::EntityVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQt3DRender_Render_EntityVisitorCall0)(const void *, Qt3DRender::Render::Entity *, int *);
class CuteQt3DRender_Render_EntityVisitor : public Qt3DRender::Render::EntityVisitor {
public:
  using Qt3DRender::Render::EntityVisitor::EntityVisitor;
  CuteQt3DRender_Render_EntityVisitor(const Qt3DRender::Render::EntityVisitor & other) : Qt3DRender::Render::EntityVisitor(other) {}
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

//  bool Qt3DRender::Render::EntityVisitor::pruneDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13EntityVisitor13pruneDisabledEv(
    const Qt3DRender::Render::EntityVisitor *self) {
  return self->pruneDisabled();
}

//  void Qt3DRender::Render::EntityVisitor::setPruneDisabled(bool
//      pruneDisabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13EntityVisitor16setPruneDisabledEb(
    Qt3DRender::Render::EntityVisitor *self,
    bool pruneDisabled) {
  self->setPruneDisabled(pruneDisabled);
}

//  bool Qt3DRender::Render::EntityVisitor::apply(Entity *root)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render13EntityVisitor5applyEPNS0_6EntityE(
    Qt3DRender::Render::EntityVisitor *self,
    Qt3DRender::Render::Entity *root) {
  return self->apply(root);
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

//  Operation Qt3DRender::Render::EntityVisitor::visit(Entity *entity)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EntityVisitor::Operation ritual_own_ZN10Qt3DRender6Render13EntityVisitor5visitEPNS0_6EntityE(
    Qt3DRender::Render::EntityVisitor *self,
    Qt3DRender::Render::Entity *entity) {
  return self->Qt3DRender::Render::EntityVisitor::visit(entity);
}
