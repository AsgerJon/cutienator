//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapesoftwarerenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesoftwarerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/private/qquickshapesoftwarerenderer_p.h>
#include <private/qquickpath_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 249, as _ZN29QQuickShapeSoftwareRenderNodeC1EP11QQuickShape
inline QQuickShapeSoftwareRenderNode::QQuickShapeSoftwareRenderNode(QQuickShape *item)
    : m_item(item)
{
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 254, as _ZN29QQuickShapeSoftwareRenderNodeD1Ev
inline QQuickShapeSoftwareRenderNode::~QQuickShapeSoftwareRenderNode()
{
    releaseResources();
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 263, as _ZN29QQuickShapeSoftwareRenderNode6renderEPKN13QSGRenderNode11RenderStateE
inline void QQuickShapeSoftwareRenderNode::render(const RenderState *state)
{
    if (m_sp.isEmpty())
        return;

    QSGRendererInterface *rif = m_item->window()->rendererInterface();
    QPainter *p = static_cast<QPainter *>(rif->getResource(m_item->window(), QSGRendererInterface::PainterResource));
    Q_ASSERT(p);

    const QRegion *clipRegion = state->clipRegion();
    if (clipRegion && !clipRegion->isEmpty())
        p->setClipRegion(*clipRegion, Qt::ReplaceClip); // must be done before setTransform

    p->setTransform(matrix()->toTransform());
    p->setOpacity(inheritedOpacity());

    for (const ShapePathRenderData &d : std::as_const(m_sp)) {
        p->setPen(d.strokeWidth > 0.0f && d.pen.color() != Qt::transparent ? d.pen : Qt::NoPen);
        p->setBrush(d.brush.color() != Qt::transparent ? d.brush : Qt::NoBrush);
        p->drawPath(d.path);
    }
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 259, as _ZN29QQuickShapeSoftwareRenderNode16releaseResourcesEv
inline void QQuickShapeSoftwareRenderNode::releaseResources()
{
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 286, as _ZNK29QQuickShapeSoftwareRenderNode13changedStatesEv
inline QSGRenderNode::StateFlags QQuickShapeSoftwareRenderNode::changedStates() const
{
    return {};
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 291, as _ZNK29QQuickShapeSoftwareRenderNode5flagsEv
inline QSGRenderNode::RenderingFlags QQuickShapeSoftwareRenderNode::flags() const
{
    return BoundedRectRendering; // avoid fullscreen updates by saying we won't draw outside rect()
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 296, as _ZNK29QQuickShapeSoftwareRenderNode4rectEv
inline QRectF QQuickShapeSoftwareRenderNode::rect() const
{
    return m_boundingRect;
}
//  -----------------------------------------------------------------------

//  A QQuickShapeSoftwareRenderNode that Python can take functions over in. Every QQuickShapeSoftwareRenderNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickShapeSoftwareRenderNodeCall0)(const void *, const QSGRenderNode::RenderState *, int *);
typedef void (*CuteQQuickShapeSoftwareRenderNodeCall1)(const void *, int *);
typedef int (*CuteQQuickShapeSoftwareRenderNodeCall2)(const void *, int *);
typedef int (*CuteQQuickShapeSoftwareRenderNodeCall3)(const void *, int *);
typedef const QRectF * (*CuteQQuickShapeSoftwareRenderNodeCall4)(const void *, int *);
typedef void (*CuteQQuickShapeSoftwareRenderNodeCall5)(const void *, int *);
typedef bool (*CuteQQuickShapeSoftwareRenderNodeCall6)(const void *, int *);
typedef void (*CuteQQuickShapeSoftwareRenderNodeCall7)(const void *, int *);
class CuteQQuickShapeSoftwareRenderNode : public QQuickShapeSoftwareRenderNode {
public:
  using QQuickShapeSoftwareRenderNode::QQuickShapeSoftwareRenderNode;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QSGRenderNode6renderEPKNS_11RenderStateE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderNode16releaseResourcesEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode13changedStatesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode5flagsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode4rectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderNode7prepareEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QQuickShapeSoftwareRenderNode::render(const RenderState *state)
  void render(const QSGRenderNode::RenderState *state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall0 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall0>(taken[0]);
      call(this, state, &handled);
      if (handled) return;
    }
    QQuickShapeSoftwareRenderNode::render(state);
  }

  //  void QQuickShapeSoftwareRenderNode::releaseResources()
  void releaseResources() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall1 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShapeSoftwareRenderNode::releaseResources();
  }

  //  StateFlags QQuickShapeSoftwareRenderNode::changedStates() const
  QSGRenderNode::StateFlags changedStates() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall2 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRenderNode::StateFlag>::fromInt(given);
    }
    return QQuickShapeSoftwareRenderNode::changedStates();
  }

  //  RenderingFlags QQuickShapeSoftwareRenderNode::flags() const
  QSGRenderNode::RenderingFlags flags() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall3 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRenderNode::RenderingFlag>::fromInt(given);
    }
    return QQuickShapeSoftwareRenderNode::flags();
  }

  //  QRectF QQuickShapeSoftwareRenderNode::rect() const
  QRectF rect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall4 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickShapeSoftwareRenderNode::rect();
  }

  //  void QSGRenderNode::prepare()
  void prepare() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall5 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderNode::prepare();
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall6 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShapeSoftwareRenderNodeCall7 call = reinterpret_cast<CuteQQuickShapeSoftwareRenderNodeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QQuickShapeSoftwareRenderNode::QQuickShapeSoftwareRenderNode(QQuickShape
//      *item)
extern "C" Q_DECL_EXPORT
QQuickShapeSoftwareRenderNode *ritual_ZN29QQuickShapeSoftwareRenderNodeC1EP11QQuickShape(
    QQuickShape *item) {
  return new CuteQQuickShapeSoftwareRenderNode(item);
}

//  QQuickShapeSoftwareRenderNode::~QQuickShapeSoftwareRenderNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickShapeSoftwareRenderNodeD1Ev(
    QQuickShapeSoftwareRenderNode *self) {
  delete self;
}

//  void QQuickShapeSoftwareRenderNode::render(const RenderState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickShapeSoftwareRenderNode6renderEPKN13QSGRenderNode11RenderStateE(
    QQuickShapeSoftwareRenderNode *self,
    const QSGRenderNode::RenderState *state) {
  self->render(state);
}

//  void QQuickShapeSoftwareRenderNode::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickShapeSoftwareRenderNode16releaseResourcesEv(
    QQuickShapeSoftwareRenderNode *self) {
  self->releaseResources();
}

//  StateFlags QQuickShapeSoftwareRenderNode::changedStates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickShapeSoftwareRenderNode13changedStatesEv(
    const QQuickShapeSoftwareRenderNode *self) {
  return static_cast<int>(self->changedStates().toInt());
}

//  RenderingFlags QQuickShapeSoftwareRenderNode::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickShapeSoftwareRenderNode5flagsEv(
    const QQuickShapeSoftwareRenderNode *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QRectF QQuickShapeSoftwareRenderNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK29QQuickShapeSoftwareRenderNode4rectEv(
    const QQuickShapeSoftwareRenderNode *self) {
  return new QRectF(self->rect());
}

//  a Python function taken by a CuteQQuickShapeSoftwareRenderNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapeSoftwareRenderNode(
    QQuickShapeSoftwareRenderNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapeSoftwareRenderNode *>(self)->take(key, call);
}

//  void QQuickShapeSoftwareRenderNode::render(const RenderState *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickShapeSoftwareRenderNode6renderEPKN13QSGRenderNode11RenderStateE(
    QQuickShapeSoftwareRenderNode *self,
    const QSGRenderNode::RenderState *state) {
  self->QQuickShapeSoftwareRenderNode::render(state);
}

//  void QQuickShapeSoftwareRenderNode::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickShapeSoftwareRenderNode16releaseResourcesEv(
    QQuickShapeSoftwareRenderNode *self) {
  self->QQuickShapeSoftwareRenderNode::releaseResources();
}

//  StateFlags QQuickShapeSoftwareRenderNode::changedStates() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QQuickShapeSoftwareRenderNode13changedStatesEv(
    const QQuickShapeSoftwareRenderNode *self) {
  return static_cast<int>(
      self->QQuickShapeSoftwareRenderNode::changedStates().toInt());
}

//  RenderingFlags QQuickShapeSoftwareRenderNode::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QQuickShapeSoftwareRenderNode5flagsEv(
    const QQuickShapeSoftwareRenderNode *self) {
  return static_cast<int>(
      self->QQuickShapeSoftwareRenderNode::flags().toInt());
}

//  QRectF QQuickShapeSoftwareRenderNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK29QQuickShapeSoftwareRenderNode4rectEv(
    const QQuickShapeSoftwareRenderNode *self) {
  return new QRectF(self->QQuickShapeSoftwareRenderNode::rect());
}
