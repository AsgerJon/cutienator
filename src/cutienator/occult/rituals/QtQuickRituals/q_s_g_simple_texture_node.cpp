//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgsimpletexturenode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgsimpletexturenode.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGSimpleTextureNode that Python can take functions over in. Every QSGSimpleTextureNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGSimpleTextureNodeCall0)(const void *, int *);
typedef void (*CuteQSGSimpleTextureNodeCall1)(const void *, int *);
class CuteQSGSimpleTextureNode : public QSGSimpleTextureNode {
public:
  using QSGSimpleTextureNode::QSGSimpleTextureNode;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSimpleTextureNodeCall0 call = reinterpret_cast<CuteQSGSimpleTextureNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSimpleTextureNodeCall1 call = reinterpret_cast<CuteQSGSimpleTextureNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGSimpleTextureNode::QSGSimpleTextureNode()
extern "C" Q_DECL_EXPORT
QSGSimpleTextureNode *ritual_ZN20QSGSimpleTextureNodeC1Ev() {
  return new CuteQSGSimpleTextureNode();
}

//  QSGSimpleTextureNode::~QSGSimpleTextureNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNodeD1Ev(QSGSimpleTextureNode *self) {
  delete self;
}

//  void QSGSimpleTextureNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode7setRectERK6QRectF(
    QSGSimpleTextureNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGSimpleTextureNode::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode7setRectEdddd(
    QSGSimpleTextureNode *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  QRectF QSGSimpleTextureNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QSGSimpleTextureNode4rectEv(
    const QSGSimpleTextureNode *self) {
  return new QRectF(self->rect());
}

//  void QSGSimpleTextureNode::setSourceRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode13setSourceRectERK6QRectF(
    QSGSimpleTextureNode *self,
    const QRectF *r) {
  self->setSourceRect(*r);
}

//  void QSGSimpleTextureNode::setSourceRect(qreal x, qreal y, qreal w, qreal
//      h)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode13setSourceRectEdddd(
    QSGSimpleTextureNode *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setSourceRect(x, y, w, h);
}

//  QRectF QSGSimpleTextureNode::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QSGSimpleTextureNode10sourceRectEv(
    const QSGSimpleTextureNode *self) {
  return new QRectF(self->sourceRect());
}

//  void QSGSimpleTextureNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode10setTextureEP10QSGTexture(
    QSGSimpleTextureNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGTexture *QSGSimpleTextureNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK20QSGSimpleTextureNode7textureEv(
    const QSGSimpleTextureNode *self) {
  return self->texture();
}

//  void QSGSimpleTextureNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSimpleTextureNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  QSGTexture::Filtering QSGSimpleTextureNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK20QSGSimpleTextureNode9filteringEv(
    const QSGSimpleTextureNode *self) {
  return self->filtering();
}

//  void QSGSimpleTextureNode::setTextureCoordinatesTransform(TextureCoordina
//      tesTransformMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode30setTextureCoordinatesTransformE6QFlagsINS_31TextureCoordinatesTransformFlagEE(
    QSGSimpleTextureNode *self,
    int mode) {
  self->setTextureCoordinatesTransform(
      QFlags<QSGSimpleTextureNode::TextureCoordinatesTransformFlag>::fromInt(mode));
}

//  TextureCoordinatesTransformMode
//      QSGSimpleTextureNode::textureCoordinatesTransform() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QSGSimpleTextureNode27textureCoordinatesTransformEv(
    const QSGSimpleTextureNode *self) {
  return static_cast<int>(self->textureCoordinatesTransform().toInt());
}

//  void QSGSimpleTextureNode::setOwnsTexture(bool owns)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSimpleTextureNode14setOwnsTextureEb(
    QSGSimpleTextureNode *self,
    bool owns) {
  self->setOwnsTexture(owns);
}

//  bool QSGSimpleTextureNode::ownsTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QSGSimpleTextureNode11ownsTextureEv(
    const QSGSimpleTextureNode *self) {
  return self->ownsTexture();
}

//  QSGSimpleTextureNodePrivate *QSGSimpleTextureNode::d_func()
extern "C" Q_DECL_EXPORT
QSGSimpleTextureNodePrivate *ritual_ZN20QSGSimpleTextureNode6d_funcEv(
    QSGSimpleTextureNode *self) {
  return self->d_func();
}

//  const QSGSimpleTextureNodePrivate *QSGSimpleTextureNode::d_func() const
extern "C" Q_DECL_EXPORT
const QSGSimpleTextureNodePrivate *ritual_ZNK20QSGSimpleTextureNode6d_funcEv(
    const QSGSimpleTextureNode *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSGSimpleTextureNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSimpleTextureNode(
    QSGSimpleTextureNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSimpleTextureNode *>(self)->take(key, call);
}
