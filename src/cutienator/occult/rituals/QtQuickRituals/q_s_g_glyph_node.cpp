//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGGlyphNode that Python can take functions over in. Every QSGGlyphNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGGlyphNodeCall0)(const void *, const QPointF *, const QGlyphRun *, int *);
typedef void (*CuteQSGGlyphNodeCall1)(const void *, const QColor *, int *);
typedef void (*CuteQSGGlyphNodeCall2)(const void *, int, int *);
typedef void (*CuteQSGGlyphNodeCall3)(const void *, const QColor *, int *);
typedef const QPointF * (*CuteQSGGlyphNodeCall4)(const void *, int *);
typedef const QRectF * (*CuteQSGGlyphNodeCall5)(const void *, int *);
typedef void (*CuteQSGGlyphNodeCall6)(const void *, const QRectF *, int *);
typedef void (*CuteQSGGlyphNodeCall7)(const void *, int, int *);
typedef void (*CuteQSGGlyphNodeCall8)(const void *, int, int *);
typedef void (*CuteQSGGlyphNodeCall9)(const void *, int *);
typedef void (*CuteQSGGlyphNodeCall10)(const void *, int *);
typedef void (*CuteQSGGlyphNodeCall11)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGGlyphNodeCall12)(const void *, int *);
typedef void (*CuteQSGGlyphNodeCall13)(const void *, int *);
class CuteQSGGlyphNode : public QSGGlyphNode {
public:
  using QSGGlyphNode::QSGGlyphNode;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QSGGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setColorERK6QColor")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setStyleEN10QQuickText9TextStyleE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode13setStyleColorERK6QColor")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode8baseLineEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode15setBoundingRectERK6QRectF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode28setPreferredAntialiasingModeENS_16AntialiasingModeE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode20setRenderTypeQualityEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode7recycleEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode6updateEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

  //  void QSGGlyphNode::setGlyphs(const QPointF &position, const QGlyphRun
  //      &glyphs)
  void setGlyphs(const QPointF &position, const QGlyphRun &glyphs) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGGlyphNodeCall0 call = reinterpret_cast<CuteQSGGlyphNodeCall0>(taken[0]);
      call(this, &position, &glyphs, &handled);
      if (handled) return;
    }
  }

  //  void QSGGlyphNode::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGGlyphNodeCall1 call = reinterpret_cast<CuteQSGGlyphNodeCall1>(taken[1]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  void QSGGlyphNode::setStyle(QQuickText::TextStyle style)
  void setStyle(QQuickText::TextStyle style) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGGlyphNodeCall2 call = reinterpret_cast<CuteQSGGlyphNodeCall2>(taken[2]);
      call(this, static_cast<int>(style), &handled);
      if (handled) return;
    }
  }

  //  void QSGGlyphNode::setStyleColor(const QColor &color)
  void setStyleColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGGlyphNodeCall3 call = reinterpret_cast<CuteQSGGlyphNodeCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  QPointF QSGGlyphNode::baseLine() const
  QPointF baseLine() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGGlyphNodeCall4 call = reinterpret_cast<CuteQSGGlyphNodeCall4>(taken[4]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QRectF QSGGlyphNode::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGGlyphNodeCall5 call = reinterpret_cast<CuteQSGGlyphNodeCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGGlyphNode::boundingRect();
  }

  //  void QSGGlyphNode::setBoundingRect(const QRectF &bounds)
  void setBoundingRect(const QRectF &bounds) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGGlyphNodeCall6 call = reinterpret_cast<CuteQSGGlyphNodeCall6>(taken[6]);
      call(this, &bounds, &handled);
      if (handled) return;
    }
    QSGGlyphNode::setBoundingRect(bounds);
  }

  //  void QSGGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)
  void setPreferredAntialiasingMode(
      QSGGlyphNode::AntialiasingMode a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGGlyphNodeCall7 call = reinterpret_cast<CuteQSGGlyphNodeCall7>(taken[7]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
  }

  //  void QSGGlyphNode::setRenderTypeQuality(int renderTypeQuality)
  void setRenderTypeQuality(int renderTypeQuality) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGGlyphNodeCall8 call = reinterpret_cast<CuteQSGGlyphNodeCall8>(taken[8]);
      call(this, renderTypeQuality, &handled);
      if (handled) return;
    }
    QSGGlyphNode::setRenderTypeQuality(renderTypeQuality);
  }

  //  void QSGGlyphNode::recycle()
  void recycle() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGGlyphNodeCall9 call = reinterpret_cast<CuteQSGGlyphNodeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGGlyphNode::recycle();
  }

  //  void QSGGlyphNode::update()
  void update() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGGlyphNodeCall10 call = reinterpret_cast<CuteQSGGlyphNodeCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGGlyphNodeCall11 call = reinterpret_cast<CuteQSGGlyphNodeCall11>(taken[11]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGGlyphNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGGlyphNodeCall12 call = reinterpret_cast<CuteQSGGlyphNodeCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGGlyphNodeCall13 call = reinterpret_cast<CuteQSGGlyphNodeCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGGlyphNode::QSGGlyphNode(QSGTextNode::RenderType renderType)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_ZN12QSGGlyphNodeC1EN11QSGTextNode10RenderTypeE(
    QSGTextNode::RenderType renderType) {
  return new CuteQSGGlyphNode(renderType);
}

//  QSGGlyphNode::~QSGGlyphNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNodeD1Ev(QSGGlyphNode *self) {
  delete self;
}

//  void QSGGlyphNode::setGlyphs(const QPointF &position, const QGlyphRun
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->setGlyphs(*position, *glyphs);
}

//  void QSGGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode8setColorERK6QColor(
    QSGGlyphNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QSGGlyphNode::setStyle(QQuickText::TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGGlyphNode *self,
    QQuickText::TextStyle style) {
  self->setStyle(style);
}

//  void QSGGlyphNode::setStyleColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode13setStyleColorERK6QColor(
    QSGGlyphNode *self,
    const QColor *color) {
  self->setStyleColor(*color);
}

//  QPointF QSGGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QSGGlyphNode8baseLineEv(const QSGGlyphNode *self) {
  return new QPointF(self->baseLine());
}

//  QRectF QSGGlyphNode::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QSGGlyphNode12boundingRectEv(const QSGGlyphNode *self) {
  return new QRectF(self->boundingRect());
}

//  void QSGGlyphNode::setBoundingRect(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode15setBoundingRectERK6QRectF(
    QSGGlyphNode *self,
    const QRectF *bounds) {
  self->setBoundingRect(*bounds);
}

//  void QSGGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode28setPreferredAntialiasingModeENS_16AntialiasingModeE(
    QSGGlyphNode *self,
    QSGGlyphNode::AntialiasingMode a0) {
  self->setPreferredAntialiasingMode(a0);
}

//  void QSGGlyphNode::setRenderTypeQuality(int renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode20setRenderTypeQualityEi(
    QSGGlyphNode *self,
    int renderTypeQuality) {
  self->setRenderTypeQuality(renderTypeQuality);
}

//  QSGTextNode::RenderType QSGGlyphNode::renderType() const
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_ZNK12QSGGlyphNode10renderTypeEv(
    const QSGGlyphNode *self) {
  return self->renderType();
}

//  void QSGGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode7recycleEv(QSGGlyphNode *self) {
  self->recycle();
}

//  void QSGGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode6updateEv(QSGGlyphNode *self) {
  self->update();
}

//  void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGGlyphNode6acceptEP16QSGNodeVisitorEx(
    QSGGlyphNode *self,
    QSGNodeVisitorEx *visitor) {
  self->accept(visitor);
}

//  a Python function taken by a CuteQSGGlyphNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGGlyphNode(
    QSGGlyphNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGGlyphNode *>(self)->take(key, call);
}

//  QRectF QSGGlyphNode::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK12QSGGlyphNode12boundingRectEv(
    const QSGGlyphNode *self) {
  return new QRectF(self->QSGGlyphNode::boundingRect());
}

//  void QSGGlyphNode::setBoundingRect(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QSGGlyphNode15setBoundingRectERK6QRectF(
    QSGGlyphNode *self,
    const QRectF *bounds) {
  self->QSGGlyphNode::setBoundingRect(*bounds);
}

//  void QSGGlyphNode::setRenderTypeQuality(int renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QSGGlyphNode20setRenderTypeQualityEi(
    QSGGlyphNode *self,
    int renderTypeQuality) {
  self->QSGGlyphNode::setRenderTypeQuality(renderTypeQuality);
}

//  void QSGGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QSGGlyphNode7recycleEv(QSGGlyphNode *self) {
  self->QSGGlyphNode::recycle();
}

//  void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QSGGlyphNode6acceptEP16QSGNodeVisitorEx(
    QSGGlyphNode *self,
    QSGNodeVisitorEx *visitor) {
  self->QSGGlyphNode::accept(visitor);
}
