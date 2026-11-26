//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderablenodeupdater_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 5. Kept as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderablenodeupdater_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarerenderablenodeupdater_p.h>
#include <QtQuick/private/qsgabstractsoftwarerenderer_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgsoftwareinternalrectanglenode_p.h>
#include <QtQuick/private/qsgsoftwareglyphnode_p.h>
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarepainternode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/qsgsimplerectnode.h>
#include <QtQuick/qsgsimpletexturenode.h>
#include <QtQuick/qsgrendernode.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderablenodeupdater.cpp, line 170, as _ZN32QSGSoftwareRenderableNodeUpdater11updateNodesEP7QSGNodeb
inline void QSGSoftwareRenderableNodeUpdater::updateNodes(QSGNode *node, bool isNodeRemoved)
{
    m_opacityState.clear();
    m_clipState.clear();
    m_transformState.clear();

    auto parentNode = node->parent();
    // If the node was deleted, it will have no parent
    // check if the state map has the previous parent
    if ((!parentNode || isNodeRemoved ) && m_stateMap.contains(node))
        parentNode = m_stateMap[node].parent;

    // If we find a parent, use its state for updating the new children
    if (parentNode && m_stateMap.contains(parentNode)) {
        auto state = m_stateMap[parentNode];
        m_opacityState.push(state.opacity);
        m_transformState.push(state.transform);
        m_clipState.push(state.clip);
        m_hasClip = state.hasClip;
    } else {
        // There is no parent, and no previous parent, so likely a root node
        m_opacityState.push(1.0f);
        m_transformState.push(QTransform());
        m_clipState.push(QRegion());
        m_hasClip = false;
    }

    // If the node is being removed, then cleanup the state data
    // Then just visit the children without visiting the now removed node
    if (isNodeRemoved) {
        m_stateMap.remove(node);
        return;
    }

    // Visit the current node itself first
    switch (node->type()) {
    case QSGNode::ClipNodeType: {
        QSGClipNode *c = static_cast<QSGClipNode*>(node);
        if (visit(c))
            visitChildren(c);
        endVisit(c);
        break;
    }
    case QSGNode::TransformNodeType: {
        QSGTransformNode *c = static_cast<QSGTransformNode*>(node);
        if (visit(c))
            visitChildren(c);
        endVisit(c);
        break;
    }
    case QSGNode::OpacityNodeType: {
        QSGOpacityNode *c = static_cast<QSGOpacityNode*>(node);
        if (visit(c))
            visitChildren(c);
        endVisit(c);
        break;
    }
    case QSGNode::GeometryNodeType: {
        if (node->flags() & QSGNode::IsVisitableNode) {
            QSGVisitableNode *v = static_cast<QSGVisitableNode*>(node);
            v->accept(this);
        } else {
            QSGGeometryNode *c = static_cast<QSGGeometryNode*>(node);
            if (visit(c))
                visitChildren(c);
            endVisit(c);
        }
        break;
    }
    case QSGNode::RootNodeType: {
        QSGRootNode *root = static_cast<QSGRootNode*>(node);
        if (visit(root))
            visitChildren(root);
        endVisit(root);
        break;
    }
    case QSGNode::BasicNodeType: {
            visitChildren(node);
        break;
    }
    case QSGNode::RenderNodeType: {
        QSGRenderNode *r = static_cast<QSGRenderNode*>(node);
        if (visit(r))
            visitChildren(r);
        endVisit(r);
        break;
    }
    default:
        Q_UNREACHABLE();
        break;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderablenodeupdater.cpp, line 263, as _ZNK32QSGSoftwareRenderableNodeUpdater12currentStateEP7QSGNode
inline QSGSoftwareRenderableNodeUpdater::NodeState QSGSoftwareRenderableNodeUpdater::currentState(QSGNode *node) const
{
    NodeState state;
    state.opacity = m_opacityState.top();
    state.clip = m_clipState.top();
    state.hasClip = m_hasClip;
    state.transform = m_transformState.top();
    state.parent = node->parent();
    return state;
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareRenderableNodeUpdater that Python can take functions over in. Every QSGSoftwareRenderableNodeUpdater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall0)(const void *, QSGTransformNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall1)(const void *, QSGTransformNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall2)(const void *, QSGClipNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall3)(const void *, QSGClipNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall4)(const void *, QSGGeometryNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall5)(const void *, QSGGeometryNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall6)(const void *, QSGOpacityNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall7)(const void *, QSGOpacityNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall8)(const void *, QSGInternalImageNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall9)(const void *, QSGInternalImageNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall10)(const void *, QSGPainterNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall11)(const void *, QSGPainterNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall12)(const void *, QSGInternalRectangleNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall13)(const void *, QSGInternalRectangleNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall14)(const void *, QSGGlyphNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall15)(const void *, QSGGlyphNode *, int *);
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall16)(const void *, QSGRootNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall17)(const void *, QSGRootNode *, int *);
#if QT_CONFIG(quick_sprite)
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall18)(const void *, QSGSpriteNode *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall19)(const void *, QSGSpriteNode *, int *);
#endif  // QT_CONFIG(quick_sprite)
typedef bool (*CuteQSGSoftwareRenderableNodeUpdaterCall20)(const void *, QSGRenderNode *, int *);
typedef void (*CuteQSGSoftwareRenderableNodeUpdaterCall21)(const void *, QSGRenderNode *, int *);
class CuteQSGSoftwareRenderableNodeUpdater : public QSGSoftwareRenderableNodeUpdater {
public:
  using QSGSoftwareRenderableNodeUpdater::QSGSoftwareRenderableNodeUpdater;
  CuteQSGSoftwareRenderableNodeUpdater(const QSGSoftwareRenderableNodeUpdater & other) : QSGSoftwareRenderableNodeUpdater(other) {}
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP16QSGTransformNode")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP16QSGTransformNode")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP11QSGClipNode")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP11QSGClipNode")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP15QSGGeometryNode")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP15QSGGeometryNode")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP14QSGOpacityNode")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP14QSGOpacityNode")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP20QSGInternalImageNode")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP20QSGInternalImageNode")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP14QSGPainterNode")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP14QSGPainterNode")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP24QSGInternalRectangleNode")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP24QSGInternalRectangleNode")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP12QSGGlyphNode")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP12QSGGlyphNode")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP11QSGRootNode")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP11QSGRootNode")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP13QSGSpriteNode")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP13QSGSpriteNode")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx5visitEP13QSGRenderNode")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNodeVisitorEx8endVisitEP13QSGRenderNode")) {
      taken[21] = call;
      return true;
    }
    return false;
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGTransformNode *a0)
  bool visit(QSGTransformNode *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall0 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGTransformNode *a0)
  void endVisit(QSGTransformNode *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall1 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGClipNode *a0)
  bool visit(QSGClipNode *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall2 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGClipNode *a0)
  void endVisit(QSGClipNode *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall3 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGGeometryNode *a0)
  bool visit(QSGGeometryNode *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall4 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGGeometryNode *a0)
  void endVisit(QSGGeometryNode *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall5 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGOpacityNode *a0)
  bool visit(QSGOpacityNode *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall6 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGOpacityNode *a0)
  void endVisit(QSGOpacityNode *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall7 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGInternalImageNode
  //      *a0)
  bool visit(QSGInternalImageNode *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall8 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGInternalImageNode
  //      *a0)
  void endVisit(QSGInternalImageNode *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall9 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGPainterNode *a0)
  bool visit(QSGPainterNode *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall10 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGPainterNode *a0)
  void endVisit(QSGPainterNode *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall11 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGInternalRectangleNode
  //      *a0)
  bool visit(QSGInternalRectangleNode *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall12 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall12>(taken[12]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void
  //      QSGSoftwareRenderableNodeUpdater::endVisit(QSGInternalRectangleNo
  //      de *a0)
  void endVisit(QSGInternalRectangleNode *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall13 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGGlyphNode *a0)
  bool visit(QSGGlyphNode *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall14 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGGlyphNode *a0)
  void endVisit(QSGGlyphNode *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall15 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGRootNode *a0)
  bool visit(QSGRootNode *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall16 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall16>(taken[16]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRootNode *a0)
  void endVisit(QSGRootNode *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall17 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }

#if QT_CONFIG(quick_sprite)
  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGSpriteNode *a0)
  bool visit(QSGSpriteNode *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall18 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGSpriteNode *a0)
  void endVisit(QSGSpriteNode *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall19 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }
#endif  // QT_CONFIG(quick_sprite)

  //  bool QSGSoftwareRenderableNodeUpdater::visit(QSGRenderNode *a0)
  bool visit(QSGRenderNode *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall20 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGSoftwareRenderableNodeUpdater::visit(a0);
  }

  //  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRenderNode *a0)
  void endVisit(QSGRenderNode *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGSoftwareRenderableNodeUpdaterCall21 call = reinterpret_cast<CuteQSGSoftwareRenderableNodeUpdaterCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderableNodeUpdater::endVisit(a0);
  }
};

//  QSGSoftwareRenderableNodeUpdater::~QSGSoftwareRenderableNodeUpdater()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdaterD1Ev(
    QSGSoftwareRenderableNodeUpdater *self) {
  delete self;
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP16QSGTransformNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGTransformNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP16QSGTransformNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGTransformNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP11QSGClipNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGClipNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP11QSGClipNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGClipNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP15QSGGeometryNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGGeometryNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP15QSGGeometryNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGGeometryNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP14QSGOpacityNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGOpacityNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP14QSGOpacityNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGOpacityNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP20QSGInternalImageNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGInternalImageNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP20QSGInternalImageNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGInternalImageNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP14QSGPainterNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGPainterNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP14QSGPainterNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGPainterNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGInternalRectangleNode
//      *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP24QSGInternalRectangleNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGInternalRectangleNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGInternalRectangleNode
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP24QSGInternalRectangleNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGInternalRectangleNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP12QSGGlyphNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGGlyphNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP12QSGGlyphNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGGlyphNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP11QSGRootNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGRootNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP11QSGRootNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGRootNode *a0) {
  self->endVisit(a0);
}

#if QT_CONFIG(quick_sprite)
//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP13QSGSpriteNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGSpriteNode *a0) {
  return self->visit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP13QSGSpriteNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGSpriteNode *a0) {
  self->endVisit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

//  bool QSGSoftwareRenderableNodeUpdater::visit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater5visitEP13QSGRenderNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGRenderNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::endVisit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater8endVisitEP13QSGRenderNode(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGRenderNode *a0) {
  self->endVisit(a0);
}

//  void QSGSoftwareRenderableNodeUpdater::updateNodes(QSGNode *node, bool
//      isNodeRemoved)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareRenderableNodeUpdater11updateNodesEP7QSGNodeb(
    QSGSoftwareRenderableNodeUpdater *self,
    QSGNode *node,
    bool isNodeRemoved) {
  self->updateNodes(node, isNodeRemoved);
}

//  NodeState QSGSoftwareRenderableNodeUpdater::currentState(QSGNode *node)
//      const
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderableNodeUpdater::NodeState *ritual_ZNK32QSGSoftwareRenderableNodeUpdater12currentStateEP7QSGNode(
    const QSGSoftwareRenderableNodeUpdater *self,
    QSGNode *node) {
  return new QSGSoftwareRenderableNodeUpdater::NodeState(
      self->currentState(
          node));
}

//  a Python function taken by a CuteQSGSoftwareRenderableNodeUpdater, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareRenderableNodeUpdater(
    QSGSoftwareRenderableNodeUpdater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareRenderableNodeUpdater *>(self)->take(key, call);
}

//  a QSGSoftwareRenderableNodeUpdater::NodeState a ritual of
//      QSGSoftwareRenderableNodeUpdater gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSGSoftwareRenderableNodeUpdater__QSGSoftwareRenderableNodeUpdater_NodeState(
    QSGSoftwareRenderableNodeUpdater::NodeState *self) {
  delete self;
}

//  bool
//      QSGSoftwareRenderableNodeUpdater::updateRenderableNode<QSGSimpleRectNode>(
//      QSGSoftwareRenderableNode::NodeType type, QSGSimpleRectNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater20updateRenderableNodeI17QSGSimpleRectNodeEEbN25QSGSoftwareRenderableNode8NodeTypeEPT_(QSGSoftwareRenderableNodeUpdater *self, int type, QSGSimpleRectNode *node) {
  return self->updateRenderableNode<QSGSimpleRectNode>(
      static_cast<QSGSoftwareRenderableNode::NodeType>(type), node);
}

//  bool
//      QSGSoftwareRenderableNodeUpdater::updateRenderableNode<QSGSimpleTextureNode>(
//      QSGSoftwareRenderableNode::NodeType type, QSGSimpleTextureNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater20updateRenderableNodeI20QSGSimpleTextureNodeEEbN25QSGSoftwareRenderableNode8NodeTypeEPT_(QSGSoftwareRenderableNodeUpdater *self, int type, QSGSimpleTextureNode *node) {
  return self->updateRenderableNode<QSGSimpleTextureNode>(
      static_cast<QSGSoftwareRenderableNode::NodeType>(type), node);
}

//  bool
//      QSGSoftwareRenderableNodeUpdater::updateRenderableNode<QSGInternalImageNode>(
//      QSGSoftwareRenderableNode::NodeType type, QSGInternalImageNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater20updateRenderableNodeI20QSGInternalImageNodeEEbN25QSGSoftwareRenderableNode8NodeTypeEPT_(QSGSoftwareRenderableNodeUpdater *self, int type, QSGInternalImageNode *node) {
  return self->updateRenderableNode<QSGInternalImageNode>(
      static_cast<QSGSoftwareRenderableNode::NodeType>(type), node);
}

//  bool
//      QSGSoftwareRenderableNodeUpdater::updateRenderableNode<QSGInternalRectangleNode>(
//      QSGSoftwareRenderableNode::NodeType type, QSGInternalRectangleNode
//      *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater20updateRenderableNodeI24QSGInternalRectangleNodeEEbN25QSGSoftwareRenderableNode8NodeTypeEPT_(QSGSoftwareRenderableNodeUpdater *self, int type, QSGInternalRectangleNode *node) {
  return self->updateRenderableNode<QSGInternalRectangleNode>(
      static_cast<QSGSoftwareRenderableNode::NodeType>(type), node);
}

//  bool
//      QSGSoftwareRenderableNodeUpdater::updateRenderableNode<QSGGlyphNode>(
//      QSGSoftwareRenderableNode::NodeType type, QSGGlyphNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSGSoftwareRenderableNodeUpdater20updateRenderableNodeI12QSGGlyphNodeEEbN25QSGSoftwareRenderableNode8NodeTypeEPT_(QSGSoftwareRenderableNodeUpdater *self, int type, QSGGlyphNode *node) {
  return self->updateRenderableNode<QSGGlyphNode>(
      static_cast<QSGSoftwareRenderableNode::NodeType>(type), node);
}
