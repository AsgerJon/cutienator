//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcurveglyphnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcurveglyphnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGCurveGlyphNode that Python can take functions over in. Every QSGCurveGlyphNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGCurveGlyphNodeCall0)(const void *, const QPointF *, const QGlyphRun *, int *);
typedef void (*CuteQSGCurveGlyphNodeCall1)(const void *, int *);
typedef void (*CuteQSGCurveGlyphNodeCall2)(const void *, int *);
typedef void (*CuteQSGCurveGlyphNodeCall3)(const void *, int, int *);
typedef void (*CuteQSGCurveGlyphNodeCall4)(const void *, const QColor *, int *);
typedef void (*CuteQSGCurveGlyphNodeCall5)(const void *, int, int *);
typedef void (*CuteQSGCurveGlyphNodeCall6)(const void *, const QColor *, int *);
typedef const QPointF * (*CuteQSGCurveGlyphNodeCall7)(const void *, int *);
typedef void (*CuteQSGCurveGlyphNodeCall8)(const void *, int *);
typedef const QRectF * (*CuteQSGCurveGlyphNodeCall9)(const void *, int *);
typedef void (*CuteQSGCurveGlyphNodeCall10)(const void *, const QRectF *, int *);
typedef void (*CuteQSGCurveGlyphNodeCall11)(const void *, int, int *);
typedef void (*CuteQSGCurveGlyphNodeCall12)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGCurveGlyphNodeCall13)(const void *, int *);
class CuteQSGCurveGlyphNode : public QSGCurveGlyphNode {
public:
  using QSGCurveGlyphNode::QSGCurveGlyphNode;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QSGGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode6updateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode28setPreferredAntialiasingModeENS_16AntialiasingModeE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setColorERK6QColor")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setStyleEN10QQuickText9TextStyleE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode13setStyleColorERK6QColor")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode8baseLineEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode7recycleEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode12boundingRectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode15setBoundingRectERK6QRectF")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode20setRenderTypeQualityEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

  //  void QSGCurveGlyphNode::setGlyphs(const QPointF &position, const
  //      QGlyphRun &glyphs)
  void setGlyphs(const QPointF &position, const QGlyphRun &glyphs) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall0 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall0>(taken[0]);
      call(this, &position, &glyphs, &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::setGlyphs(position, glyphs);
  }

  //  void QSGCurveGlyphNode::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall1 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::update();
  }

  //  void QSGCurveGlyphNode::preprocess()
  void preprocess() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall2 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::preprocess();
  }

  //  void QSGCurveGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
  //      a0)
  void setPreferredAntialiasingMode(
      QSGGlyphNode::AntialiasingMode a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall3 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall3>(taken[3]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::setPreferredAntialiasingMode(a0);
  }

  //  void QSGCurveGlyphNode::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall4 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall4>(taken[4]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::setColor(color);
  }

  //  void QSGCurveGlyphNode::setStyle(QQuickText::TextStyle style)
  void setStyle(QQuickText::TextStyle style) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall5 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall5>(taken[5]);
      call(this, static_cast<int>(style), &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::setStyle(style);
  }

  //  void QSGCurveGlyphNode::setStyleColor(const QColor &color)
  void setStyleColor(const QColor &color) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall6 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall6>(taken[6]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::setStyleColor(color);
  }

  //  QPointF QSGCurveGlyphNode::baseLine() const
  QPointF baseLine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall7 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall7>(taken[7]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGCurveGlyphNode::baseLine();
  }

  //  void QSGCurveGlyphNode::recycle()
  void recycle() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall8 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGCurveGlyphNode::recycle();
  }

  //  QRectF QSGGlyphNode::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall9 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGGlyphNode::boundingRect();
  }

  //  void QSGGlyphNode::setBoundingRect(const QRectF &bounds)
  void setBoundingRect(const QRectF &bounds) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall10 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall10>(taken[10]);
      call(this, &bounds, &handled);
      if (handled) return;
    }
    QSGGlyphNode::setBoundingRect(bounds);
  }

  //  void QSGGlyphNode::setRenderTypeQuality(int renderTypeQuality)
  void setRenderTypeQuality(int renderTypeQuality) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall11 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall11>(taken[11]);
      call(this, renderTypeQuality, &handled);
      if (handled) return;
    }
    QSGGlyphNode::setRenderTypeQuality(renderTypeQuality);
  }

  //  void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall12 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall12>(taken[12]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGGlyphNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGCurveGlyphNodeCall13 call = reinterpret_cast<CuteQSGCurveGlyphNodeCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }
};

//  QSGCurveGlyphNode::QSGCurveGlyphNode(QSGRenderContext *context)
extern "C" Q_DECL_EXPORT
QSGCurveGlyphNode *ritual_ZN17QSGCurveGlyphNodeC1EP16QSGRenderContext(
    QSGRenderContext *context) {
  return new CuteQSGCurveGlyphNode(context);
}

//  QSGCurveGlyphNode::~QSGCurveGlyphNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNodeD1Ev(QSGCurveGlyphNode *self) {
  delete self;
}

//  void QSGCurveGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGCurveGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->setGlyphs(*position, *glyphs);
}

//  void QSGCurveGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode6updateEv(QSGCurveGlyphNode *self) {
  self->update();
}

//  void QSGCurveGlyphNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode10preprocessEv(QSGCurveGlyphNode *self) {
  self->preprocess();
}

//  void QSGCurveGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGCurveGlyphNode *self,
    QSGGlyphNode::AntialiasingMode a0) {
  self->setPreferredAntialiasingMode(a0);
}

//  void QSGCurveGlyphNode::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode14updateGeometryEv(
    QSGCurveGlyphNode *self) {
  self->updateGeometry();
}

//  void QSGCurveGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode8setColorERK6QColor(
    QSGCurveGlyphNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QSGCurveGlyphNode::setStyle(QQuickText::TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGCurveGlyphNode *self,
    QQuickText::TextStyle style) {
  self->setStyle(style);
}

//  void QSGCurveGlyphNode::setStyleColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode13setStyleColorERK6QColor(
    QSGCurveGlyphNode *self,
    const QColor *color) {
  self->setStyleColor(*color);
}

//  QPointF QSGCurveGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QSGCurveGlyphNode8baseLineEv(
    const QSGCurveGlyphNode *self) {
  return new QPointF(self->baseLine());
}

//  void QSGCurveGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode7recycleEv(QSGCurveGlyphNode *self) {
  self->recycle();
}

//  void QSGCurveGlyphNode::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGCurveGlyphNode7cleanupEv(QSGCurveGlyphNode *self) {
  self->cleanup();
}

//  a Python function taken by a CuteQSGCurveGlyphNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCurveGlyphNode(
    QSGCurveGlyphNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCurveGlyphNode *>(self)->take(key, call);
}

//  void QSGCurveGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGCurveGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->QSGCurveGlyphNode::setGlyphs(*position, *glyphs);
}

//  void QSGCurveGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode6updateEv(QSGCurveGlyphNode *self) {
  self->QSGCurveGlyphNode::update();
}

//  void QSGCurveGlyphNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode10preprocessEv(
    QSGCurveGlyphNode *self) {
  self->QSGCurveGlyphNode::preprocess();
}

//  void QSGCurveGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGCurveGlyphNode *self,
    QSGGlyphNode::AntialiasingMode a0) {
  self->QSGCurveGlyphNode::setPreferredAntialiasingMode(a0);
}

//  void QSGCurveGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode8setColorERK6QColor(
    QSGCurveGlyphNode *self,
    const QColor *color) {
  self->QSGCurveGlyphNode::setColor(*color);
}

//  void QSGCurveGlyphNode::setStyle(QQuickText::TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGCurveGlyphNode *self,
    QQuickText::TextStyle style) {
  self->QSGCurveGlyphNode::setStyle(style);
}

//  void QSGCurveGlyphNode::setStyleColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode13setStyleColorERK6QColor(
    QSGCurveGlyphNode *self,
    const QColor *color) {
  self->QSGCurveGlyphNode::setStyleColor(*color);
}

//  QPointF QSGCurveGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK17QSGCurveGlyphNode8baseLineEv(
    const QSGCurveGlyphNode *self) {
  return new QPointF(self->QSGCurveGlyphNode::baseLine());
}

//  void QSGCurveGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGCurveGlyphNode7recycleEv(QSGCurveGlyphNode *self) {
  self->QSGCurveGlyphNode::recycle();
}
