//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbasicinternalrectanglenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbasicinternalrectanglenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  Only a class built on QSGBasicInternalRectangleNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGBasicInternalRectangleNode : QSGBasicInternalRectangleNode {
  using QSGBasicInternalRectangleNode::supportsAntialiasing;
};

//  A QSGBasicInternalRectangleNode that Python can take functions over in. Every QSGBasicInternalRectangleNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGBasicInternalRectangleNodeCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall1)(const void *, const QColor *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall2)(const void *, const QColor *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall3)(const void *, qreal, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall4)(const void *, bool, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall5)(const void *, qreal, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall6)(const void *, qreal, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall7)(const void *, qreal, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall8)(const void *, qreal, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall9)(const void *, qreal, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall10)(const void *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall11)(const void *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall12)(const void *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall13)(const void *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall14)(const void *, bool, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall15)(const void *, bool, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall16)(const void *, int *);
typedef bool (*CuteQSGBasicInternalRectangleNodeCall17)(const void *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall18)(const void *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall19)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGBasicInternalRectangleNodeCall20)(const void *, int *);
typedef void (*CuteQSGBasicInternalRectangleNodeCall21)(const void *, int *);
class CuteQSGBasicInternalRectangleNode : public QSGBasicInternalRectangleNode {
public:
  using QSGBasicInternalRectangleNode::QSGBasicInternalRectangleNode;
  void *taken[22] = {};

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
    if (!std::strcmp(key, "_ZNK29QSGBasicInternalRectangleNode20supportsAntialiasingEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QSGBasicInternalRectangleNode26updateMaterialAntialiasingEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[21] = call;
      return true;
    }
    return false;
  }

  //  void QSGBasicInternalRectangleNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall0 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setRect(rect);
  }

  //  void QSGBasicInternalRectangleNode::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall1 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall1>(taken[1]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setColor(color);
  }

  //  void QSGBasicInternalRectangleNode::setPenColor(const QColor &color)
  void setPenColor(const QColor &color) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall2 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall2>(taken[2]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setPenColor(color);
  }

  //  void QSGBasicInternalRectangleNode::setPenWidth(qreal width)
  void setPenWidth(qreal width) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall3 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall3>(taken[3]);
      call(this, width, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setPenWidth(width);
  }

  //  void QSGBasicInternalRectangleNode::setGradientVertical(bool
  //      vertical)
  void setGradientVertical(bool vertical) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall4 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall4>(taken[4]);
      call(this, vertical, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setGradientVertical(vertical);
  }

  //  void QSGBasicInternalRectangleNode::setRadius(qreal radius)
  void setRadius(qreal radius) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall5 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall5>(taken[5]);
      call(this, radius, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setRadius(radius);
  }

  //  void QSGBasicInternalRectangleNode::setTopLeftRadius(qreal radius)
  void setTopLeftRadius(qreal radius) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall6 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall6>(taken[6]);
      call(this, radius, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setTopLeftRadius(radius);
  }

  //  void QSGBasicInternalRectangleNode::setTopRightRadius(qreal radius)
  void setTopRightRadius(qreal radius) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall7 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall7>(taken[7]);
      call(this, radius, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setTopRightRadius(radius);
  }

  //  void QSGBasicInternalRectangleNode::setBottomLeftRadius(qreal radius)
  void setBottomLeftRadius(qreal radius) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall8 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall8>(taken[8]);
      call(this, radius, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setBottomLeftRadius(radius);
  }

  //  void QSGBasicInternalRectangleNode::setBottomRightRadius(qreal
  //      radius)
  void setBottomRightRadius(qreal radius) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall9 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall9>(taken[9]);
      call(this, radius, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setBottomRightRadius(radius);
  }

  //  void QSGBasicInternalRectangleNode::resetTopLeftRadius()
  void resetTopLeftRadius() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall10 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::resetTopLeftRadius();
  }

  //  void QSGBasicInternalRectangleNode::resetTopRightRadius()
  void resetTopRightRadius() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall11 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::resetTopRightRadius();
  }

  //  void QSGBasicInternalRectangleNode::resetBottomLeftRadius()
  void resetBottomLeftRadius() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall12 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::resetBottomLeftRadius();
  }

  //  void QSGBasicInternalRectangleNode::resetBottomRightRadius()
  void resetBottomRightRadius() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall13 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::resetBottomRightRadius();
  }

  //  void QSGBasicInternalRectangleNode::setAntialiasing(bool
  //      antialiasing)
  void setAntialiasing(bool antialiasing) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall14 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall14>(taken[14]);
      call(this, antialiasing, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setAntialiasing(antialiasing);
  }

  //  void QSGBasicInternalRectangleNode::setAligned(bool aligned)
  void setAligned(bool aligned) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall15 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall15>(taken[15]);
      call(this, aligned, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::setAligned(aligned);
  }

  //  void QSGBasicInternalRectangleNode::update()
  void update() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall16 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBasicInternalRectangleNode::update();
  }

  //  bool QSGBasicInternalRectangleNode::supportsAntialiasing() const
  bool supportsAntialiasing() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall17 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGBasicInternalRectangleNode::supportsAntialiasing();
  }

  //  void QSGBasicInternalRectangleNode::updateMaterialAntialiasing()
  void updateMaterialAntialiasing() override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall18 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalRectangleNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall19 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall19>(taken[19]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGInternalRectangleNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall20 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGBasicInternalRectangleNodeCall21 call = reinterpret_cast<CuteQSGBasicInternalRectangleNodeCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  void QSGBasicInternalRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode7setRectERK6QRectF(
    QSGBasicInternalRectangleNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGBasicInternalRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode8setColorERK6QColor(
    QSGBasicInternalRectangleNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QSGBasicInternalRectangleNode::setPenColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode11setPenColorERK6QColor(
    QSGBasicInternalRectangleNode *self,
    const QColor *color) {
  self->setPenColor(*color);
}

//  void QSGBasicInternalRectangleNode::setPenWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode11setPenWidthEd(
    QSGBasicInternalRectangleNode *self,
    qreal width) {
  self->setPenWidth(width);
}

//  void QSGBasicInternalRectangleNode::setGradientVertical(bool vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode19setGradientVerticalEb(
    QSGBasicInternalRectangleNode *self,
    bool vertical) {
  self->setGradientVertical(vertical);
}

//  void QSGBasicInternalRectangleNode::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode9setRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->setRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode16setTopLeftRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->setTopLeftRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode17setTopRightRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->setTopRightRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode19setBottomLeftRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->setBottomLeftRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode20setBottomRightRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->setBottomRightRadius(radius);
}

//  void QSGBasicInternalRectangleNode::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode18resetTopLeftRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->resetTopLeftRadius();
}

//  void QSGBasicInternalRectangleNode::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode19resetTopRightRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->resetTopRightRadius();
}

//  void QSGBasicInternalRectangleNode::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode21resetBottomLeftRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->resetBottomLeftRadius();
}

//  void QSGBasicInternalRectangleNode::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode22resetBottomRightRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->resetBottomRightRadius();
}

//  void QSGBasicInternalRectangleNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode15setAntialiasingEb(
    QSGBasicInternalRectangleNode *self,
    bool antialiasing) {
  self->setAntialiasing(antialiasing);
}

//  void QSGBasicInternalRectangleNode::setAligned(bool aligned)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode10setAlignedEb(
    QSGBasicInternalRectangleNode *self,
    bool aligned) {
  self->setAligned(aligned);
}

//  void QSGBasicInternalRectangleNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode6updateEv(
    QSGBasicInternalRectangleNode *self) {
  self->update();
}

//  bool QSGBasicInternalRectangleNode::supportsAntialiasing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSGBasicInternalRectangleNode20supportsAntialiasingEv(
    const QSGBasicInternalRectangleNode *self) {
  return self->supportsAntialiasing();
}

//  void QSGBasicInternalRectangleNode::updateMaterialAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode26updateMaterialAntialiasingEv(
    QSGBasicInternalRectangleNode *self) {
  self->updateMaterialAntialiasing();
}

//  void QSGBasicInternalRectangleNode::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGBasicInternalRectangleNode14updateGeometryEv(
    QSGBasicInternalRectangleNode *self) {
  self->updateGeometry();
}

//  a Python function taken by a CuteQSGBasicInternalRectangleNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBasicInternalRectangleNode(
    QSGBasicInternalRectangleNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBasicInternalRectangleNode *>(self)->take(key, call);
}

//  void QSGBasicInternalRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode7setRectERK6QRectF(
    QSGBasicInternalRectangleNode *self,
    const QRectF *rect) {
  self->QSGBasicInternalRectangleNode::setRect(*rect);
}

//  void QSGBasicInternalRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode8setColorERK6QColor(
    QSGBasicInternalRectangleNode *self,
    const QColor *color) {
  self->QSGBasicInternalRectangleNode::setColor(*color);
}

//  void QSGBasicInternalRectangleNode::setPenColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode11setPenColorERK6QColor(
    QSGBasicInternalRectangleNode *self,
    const QColor *color) {
  self->QSGBasicInternalRectangleNode::setPenColor(*color);
}

//  void QSGBasicInternalRectangleNode::setPenWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode11setPenWidthEd(
    QSGBasicInternalRectangleNode *self,
    qreal width) {
  self->QSGBasicInternalRectangleNode::setPenWidth(width);
}

//  void QSGBasicInternalRectangleNode::setGradientVertical(bool vertical)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode19setGradientVerticalEb(
    QSGBasicInternalRectangleNode *self,
    bool vertical) {
  self->QSGBasicInternalRectangleNode::setGradientVertical(vertical);
}

//  void QSGBasicInternalRectangleNode::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode9setRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->QSGBasicInternalRectangleNode::setRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode16setTopLeftRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->QSGBasicInternalRectangleNode::setTopLeftRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode17setTopRightRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->QSGBasicInternalRectangleNode::setTopRightRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode19setBottomLeftRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->QSGBasicInternalRectangleNode::setBottomLeftRadius(radius);
}

//  void QSGBasicInternalRectangleNode::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode20setBottomRightRadiusEd(
    QSGBasicInternalRectangleNode *self,
    qreal radius) {
  self->QSGBasicInternalRectangleNode::setBottomRightRadius(radius);
}

//  void QSGBasicInternalRectangleNode::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode18resetTopLeftRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->QSGBasicInternalRectangleNode::resetTopLeftRadius();
}

//  void QSGBasicInternalRectangleNode::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode19resetTopRightRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->QSGBasicInternalRectangleNode::resetTopRightRadius();
}

//  void QSGBasicInternalRectangleNode::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode21resetBottomLeftRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->QSGBasicInternalRectangleNode::resetBottomLeftRadius();
}

//  void QSGBasicInternalRectangleNode::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode22resetBottomRightRadiusEv(
    QSGBasicInternalRectangleNode *self) {
  self->QSGBasicInternalRectangleNode::resetBottomRightRadius();
}

//  void QSGBasicInternalRectangleNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode15setAntialiasingEb(
    QSGBasicInternalRectangleNode *self,
    bool antialiasing) {
  self->QSGBasicInternalRectangleNode::setAntialiasing(antialiasing);
}

//  void QSGBasicInternalRectangleNode::setAligned(bool aligned)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode10setAlignedEb(
    QSGBasicInternalRectangleNode *self,
    bool aligned) {
  self->QSGBasicInternalRectangleNode::setAligned(aligned);
}

//  void QSGBasicInternalRectangleNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGBasicInternalRectangleNode6updateEv(
    QSGBasicInternalRectangleNode *self) {
  self->QSGBasicInternalRectangleNode::update();
}

//  bool QSGBasicInternalRectangleNode::supportsAntialiasing() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QSGBasicInternalRectangleNode20supportsAntialiasingEv(
    const QSGBasicInternalRectangleNode *self) {
  return static_cast<const OwnQSGBasicInternalRectangleNode *>(self)->OwnQSGBasicInternalRectangleNode::supportsAntialiasing();
}
