//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QSGInternalRectangleNode that Python can take functions over in. Every QSGInternalRectangleNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGInternalRectangleNodeCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall1)(const void *, const QColor *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall2)(const void *, const QColor *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall3)(const void *, qreal, int *);
typedef void (*CuteQSGInternalRectangleNodeCall4)(const void *, bool, int *);
typedef void (*CuteQSGInternalRectangleNodeCall5)(const void *, qreal, int *);
typedef void (*CuteQSGInternalRectangleNodeCall6)(const void *, qreal, int *);
typedef void (*CuteQSGInternalRectangleNodeCall7)(const void *, qreal, int *);
typedef void (*CuteQSGInternalRectangleNodeCall8)(const void *, qreal, int *);
typedef void (*CuteQSGInternalRectangleNodeCall9)(const void *, qreal, int *);
typedef void (*CuteQSGInternalRectangleNodeCall10)(const void *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall11)(const void *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall12)(const void *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall13)(const void *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall14)(const void *, bool, int *);
typedef void (*CuteQSGInternalRectangleNodeCall15)(const void *, bool, int *);
typedef void (*CuteQSGInternalRectangleNodeCall16)(const void *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall17)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGInternalRectangleNodeCall18)(const void *, int *);
typedef void (*CuteQSGInternalRectangleNodeCall19)(const void *, int *);
class CuteQSGInternalRectangleNode : public QSGInternalRectangleNode {
public:
  using QSGInternalRectangleNode::QSGInternalRectangleNode;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode7setRectERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode8setColorERK6QColor")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode11setPenColorERK6QColor")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode11setPenWidthEd")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode19setGradientVerticalEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode9setRadiusEd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode16setTopLeftRadiusEd")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode17setTopRightRadiusEd")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode19setBottomLeftRadiusEd")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode20setBottomRightRadiusEd")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode18resetTopLeftRadiusEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode19resetTopRightRadiusEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode21resetBottomLeftRadiusEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode22resetBottomRightRadiusEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode15setAntialiasingEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode10setAlignedEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QSGInternalRectangleNode6updateEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  void QSGInternalRectangleNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall0 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall1 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall1>(taken[1]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setPenColor(const QColor &color)
  void setPenColor(const QColor &color) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall2 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall2>(taken[2]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setPenWidth(qreal width)
  void setPenWidth(qreal width) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall3 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall3>(taken[3]);
      call(this, width, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setGradientVertical(bool vertical)
  void setGradientVertical(bool vertical) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall4 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall4>(taken[4]);
      call(this, vertical, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setRadius(qreal radius)
  void setRadius(qreal radius) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall5 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall5>(taken[5]);
      call(this, radius, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setTopLeftRadius(qreal radius)
  void setTopLeftRadius(qreal radius) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall6 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall6>(taken[6]);
      call(this, radius, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setTopRightRadius(qreal radius)
  void setTopRightRadius(qreal radius) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall7 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall7>(taken[7]);
      call(this, radius, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setBottomLeftRadius(qreal radius)
  void setBottomLeftRadius(qreal radius) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall8 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall8>(taken[8]);
      call(this, radius, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setBottomRightRadius(qreal radius)
  void setBottomRightRadius(qreal radius) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall9 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall9>(taken[9]);
      call(this, radius, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::resetTopLeftRadius()
  void resetTopLeftRadius() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall10 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::resetTopRightRadius()
  void resetTopRightRadius() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall11 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::resetBottomLeftRadius()
  void resetBottomLeftRadius() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall12 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::resetBottomRightRadius()
  void resetBottomRightRadius() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall13 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::setAntialiasing(bool antialiasing)
  void setAntialiasing(bool antialiasing) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall14 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall14>(taken[14]);
      call(this, antialiasing, &handled);
      if (handled) return;
    }
    QSGInternalRectangleNode::setAntialiasing(antialiasing);
  }

  //  void QSGInternalRectangleNode::setAligned(bool aligned)
  void setAligned(bool aligned) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall15 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall15>(taken[15]);
      call(this, aligned, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::update()
  void update() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall16 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall17 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall17>(taken[17]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGInternalRectangleNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall18 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGInternalRectangleNodeCall19 call = reinterpret_cast<CuteQSGInternalRectangleNodeCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGInternalRectangleNode::~QSGInternalRectangleNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNodeD1Ev(
    QSGInternalRectangleNode *self) {
  delete self;
}

//  void QSGInternalRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode7setRectERK6QRectF(
    QSGInternalRectangleNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGInternalRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode8setColorERK6QColor(
    QSGInternalRectangleNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QSGInternalRectangleNode::setPenColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode11setPenColorERK6QColor(
    QSGInternalRectangleNode *self,
    const QColor *color) {
  self->setPenColor(*color);
}

//  void QSGInternalRectangleNode::setPenWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode11setPenWidthEd(
    QSGInternalRectangleNode *self,
    qreal width) {
  self->setPenWidth(width);
}

//  void QSGInternalRectangleNode::setGradientStops(const QGradientStops
//      &stops)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode16setGradientStopsERK5QListISt4pairId6QColorEE(
    QSGInternalRectangleNode *self,
    const QGradientStops *stops) {
  self->setGradientStops(*stops);
}

//  void QSGInternalRectangleNode::setGradientVertical(bool vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode19setGradientVerticalEb(
    QSGInternalRectangleNode *self,
    bool vertical) {
  self->setGradientVertical(vertical);
}

//  void QSGInternalRectangleNode::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode9setRadiusEd(
    QSGInternalRectangleNode *self,
    qreal radius) {
  self->setRadius(radius);
}

//  void QSGInternalRectangleNode::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode16setTopLeftRadiusEd(
    QSGInternalRectangleNode *self,
    qreal radius) {
  self->setTopLeftRadius(radius);
}

//  void QSGInternalRectangleNode::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode17setTopRightRadiusEd(
    QSGInternalRectangleNode *self,
    qreal radius) {
  self->setTopRightRadius(radius);
}

//  void QSGInternalRectangleNode::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode19setBottomLeftRadiusEd(
    QSGInternalRectangleNode *self,
    qreal radius) {
  self->setBottomLeftRadius(radius);
}

//  void QSGInternalRectangleNode::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode20setBottomRightRadiusEd(
    QSGInternalRectangleNode *self,
    qreal radius) {
  self->setBottomRightRadius(radius);
}

//  void QSGInternalRectangleNode::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode18resetTopLeftRadiusEv(
    QSGInternalRectangleNode *self) {
  self->resetTopLeftRadius();
}

//  void QSGInternalRectangleNode::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode19resetTopRightRadiusEv(
    QSGInternalRectangleNode *self) {
  self->resetTopRightRadius();
}

//  void QSGInternalRectangleNode::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode21resetBottomLeftRadiusEv(
    QSGInternalRectangleNode *self) {
  self->resetBottomLeftRadius();
}

//  void QSGInternalRectangleNode::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode22resetBottomRightRadiusEv(
    QSGInternalRectangleNode *self) {
  self->resetBottomRightRadius();
}

//  void QSGInternalRectangleNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode15setAntialiasingEb(
    QSGInternalRectangleNode *self,
    bool antialiasing) {
  self->setAntialiasing(antialiasing);
}

//  void QSGInternalRectangleNode::setAligned(bool aligned)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode10setAlignedEb(
    QSGInternalRectangleNode *self,
    bool aligned) {
  self->setAligned(aligned);
}

//  void QSGInternalRectangleNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode6updateEv(
    QSGInternalRectangleNode *self) {
  self->update();
}

//  void QSGInternalRectangleNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGInternalRectangleNode6acceptEP16QSGNodeVisitorEx(
    QSGInternalRectangleNode *self,
    QSGNodeVisitorEx *visitor) {
  self->accept(visitor);
}

//  a Python function taken by a CuteQSGInternalRectangleNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGInternalRectangleNode(
    QSGInternalRectangleNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGInternalRectangleNode *>(self)->take(key, call);
}

//  void QSGInternalRectangleNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGInternalRectangleNode15setAntialiasingEb(
    QSGInternalRectangleNode *self,
    bool antialiasing) {
  self->QSGInternalRectangleNode::setAntialiasing(antialiasing);
}

//  void QSGInternalRectangleNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGInternalRectangleNode6acceptEP16QSGNodeVisitorEx(
    QSGInternalRectangleNode *self,
    QSGNodeVisitorEx *visitor) {
  self->QSGInternalRectangleNode::accept(visitor);
}
