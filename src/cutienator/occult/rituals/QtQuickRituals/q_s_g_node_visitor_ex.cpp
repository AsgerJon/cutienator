//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGNodeVisitorEx that Python can take functions over in. Every QSGNodeVisitorEx
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGNodeVisitorExCall0)(const void *, QSGTransformNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall1)(const void *, QSGTransformNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall2)(const void *, QSGClipNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall3)(const void *, QSGClipNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall4)(const void *, QSGGeometryNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall5)(const void *, QSGGeometryNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall6)(const void *, QSGOpacityNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall7)(const void *, QSGOpacityNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall8)(const void *, QSGInternalImageNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall9)(const void *, QSGInternalImageNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall10)(const void *, QSGPainterNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall11)(const void *, QSGPainterNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall12)(const void *, QSGInternalRectangleNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall13)(const void *, QSGInternalRectangleNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall14)(const void *, QSGGlyphNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall15)(const void *, QSGGlyphNode *, int *);
typedef bool (*CuteQSGNodeVisitorExCall16)(const void *, QSGRootNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall17)(const void *, QSGRootNode *, int *);
#if QT_CONFIG(quick_sprite)
typedef bool (*CuteQSGNodeVisitorExCall18)(const void *, QSGSpriteNode *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGNodeVisitorExCall19)(const void *, QSGSpriteNode *, int *);
#endif  // QT_CONFIG(quick_sprite)
typedef bool (*CuteQSGNodeVisitorExCall20)(const void *, QSGRenderNode *, int *);
typedef void (*CuteQSGNodeVisitorExCall21)(const void *, QSGRenderNode *, int *);
class CuteQSGNodeVisitorEx : public QSGNodeVisitorEx {
public:
  using QSGNodeVisitorEx::QSGNodeVisitorEx;
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

  //  bool QSGNodeVisitorEx::visit(QSGTransformNode *a0)
  bool visit(QSGTransformNode *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall0 call = reinterpret_cast<CuteQSGNodeVisitorExCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGTransformNode *a0)
  void endVisit(QSGTransformNode *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall1 call = reinterpret_cast<CuteQSGNodeVisitorExCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGClipNode *a0)
  bool visit(QSGClipNode *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall2 call = reinterpret_cast<CuteQSGNodeVisitorExCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGClipNode *a0)
  void endVisit(QSGClipNode *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall3 call = reinterpret_cast<CuteQSGNodeVisitorExCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGGeometryNode *a0)
  bool visit(QSGGeometryNode *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall4 call = reinterpret_cast<CuteQSGNodeVisitorExCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGGeometryNode *a0)
  void endVisit(QSGGeometryNode *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall5 call = reinterpret_cast<CuteQSGNodeVisitorExCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGOpacityNode *a0)
  bool visit(QSGOpacityNode *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall6 call = reinterpret_cast<CuteQSGNodeVisitorExCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGOpacityNode *a0)
  void endVisit(QSGOpacityNode *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall7 call = reinterpret_cast<CuteQSGNodeVisitorExCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGInternalImageNode *a0)
  bool visit(QSGInternalImageNode *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall8 call = reinterpret_cast<CuteQSGNodeVisitorExCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGInternalImageNode *a0)
  void endVisit(QSGInternalImageNode *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall9 call = reinterpret_cast<CuteQSGNodeVisitorExCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGPainterNode *a0)
  bool visit(QSGPainterNode *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall10 call = reinterpret_cast<CuteQSGNodeVisitorExCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGPainterNode *a0)
  void endVisit(QSGPainterNode *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall11 call = reinterpret_cast<CuteQSGNodeVisitorExCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGInternalRectangleNode *a0)
  bool visit(QSGInternalRectangleNode *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall12 call = reinterpret_cast<CuteQSGNodeVisitorExCall12>(taken[12]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGInternalRectangleNode *a0)
  void endVisit(QSGInternalRectangleNode *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall13 call = reinterpret_cast<CuteQSGNodeVisitorExCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGGlyphNode *a0)
  bool visit(QSGGlyphNode *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall14 call = reinterpret_cast<CuteQSGNodeVisitorExCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGGlyphNode *a0)
  void endVisit(QSGGlyphNode *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall15 call = reinterpret_cast<CuteQSGNodeVisitorExCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNodeVisitorEx::visit(QSGRootNode *a0)
  bool visit(QSGRootNode *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall16 call = reinterpret_cast<CuteQSGNodeVisitorExCall16>(taken[16]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGRootNode *a0)
  void endVisit(QSGRootNode *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall17 call = reinterpret_cast<CuteQSGNodeVisitorExCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

#if QT_CONFIG(quick_sprite)
  //  bool QSGNodeVisitorEx::visit(QSGSpriteNode *a0)
  bool visit(QSGSpriteNode *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall18 call = reinterpret_cast<CuteQSGNodeVisitorExCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGNodeVisitorEx::endVisit(QSGSpriteNode *a0)
  void endVisit(QSGSpriteNode *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall19 call = reinterpret_cast<CuteQSGNodeVisitorExCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

  //  bool QSGNodeVisitorEx::visit(QSGRenderNode *a0)
  bool visit(QSGRenderNode *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall20 call = reinterpret_cast<CuteQSGNodeVisitorExCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGNodeVisitorEx::endVisit(QSGRenderNode *a0)
  void endVisit(QSGRenderNode *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGNodeVisitorExCall21 call = reinterpret_cast<CuteQSGNodeVisitorExCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
};

//  QSGNodeVisitorEx::~QSGNodeVisitorEx()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorExD1Ev(QSGNodeVisitorEx *self) {
  delete self;
}

//  bool QSGNodeVisitorEx::visit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP16QSGTransformNode(
    QSGNodeVisitorEx *self,
    QSGTransformNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP16QSGTransformNode(
    QSGNodeVisitorEx *self,
    QSGTransformNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP11QSGClipNode(
    QSGNodeVisitorEx *self,
    QSGClipNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP11QSGClipNode(
    QSGNodeVisitorEx *self,
    QSGClipNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP15QSGGeometryNode(
    QSGNodeVisitorEx *self,
    QSGGeometryNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP15QSGGeometryNode(
    QSGNodeVisitorEx *self,
    QSGGeometryNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP14QSGOpacityNode(
    QSGNodeVisitorEx *self,
    QSGOpacityNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP14QSGOpacityNode(
    QSGNodeVisitorEx *self,
    QSGOpacityNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP20QSGInternalImageNode(
    QSGNodeVisitorEx *self,
    QSGInternalImageNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP20QSGInternalImageNode(
    QSGNodeVisitorEx *self,
    QSGInternalImageNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP14QSGPainterNode(
    QSGNodeVisitorEx *self,
    QSGPainterNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP14QSGPainterNode(
    QSGNodeVisitorEx *self,
    QSGPainterNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGInternalRectangleNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP24QSGInternalRectangleNode(
    QSGNodeVisitorEx *self,
    QSGInternalRectangleNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGInternalRectangleNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP24QSGInternalRectangleNode(
    QSGNodeVisitorEx *self,
    QSGInternalRectangleNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP12QSGGlyphNode(
    QSGNodeVisitorEx *self,
    QSGGlyphNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP12QSGGlyphNode(
    QSGNodeVisitorEx *self,
    QSGGlyphNode *a0) {
  self->endVisit(a0);
}

//  bool QSGNodeVisitorEx::visit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP11QSGRootNode(
    QSGNodeVisitorEx *self,
    QSGRootNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP11QSGRootNode(
    QSGNodeVisitorEx *self,
    QSGRootNode *a0) {
  self->endVisit(a0);
}

#if QT_CONFIG(quick_sprite)
//  bool QSGNodeVisitorEx::visit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP13QSGSpriteNode(
    QSGNodeVisitorEx *self,
    QSGSpriteNode *a0) {
  return self->visit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
//  void QSGNodeVisitorEx::endVisit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP13QSGSpriteNode(
    QSGNodeVisitorEx *self,
    QSGSpriteNode *a0) {
  self->endVisit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

//  bool QSGNodeVisitorEx::visit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGNodeVisitorEx5visitEP13QSGRenderNode(
    QSGNodeVisitorEx *self,
    QSGRenderNode *a0) {
  return self->visit(a0);
}

//  void QSGNodeVisitorEx::endVisit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx8endVisitEP13QSGRenderNode(
    QSGNodeVisitorEx *self,
    QSGRenderNode *a0) {
  self->endVisit(a0);
}

//  void QSGNodeVisitorEx::visitChildren(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNodeVisitorEx13visitChildrenEP7QSGNode(
    QSGNodeVisitorEx *self,
    QSGNode *node) {
  self->visitChildren(node);
}

//  a Python function taken by a CuteQSGNodeVisitorEx, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGNodeVisitorEx(
    QSGNodeVisitorEx *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGNodeVisitorEx *>(self)->take(key, call);
}
