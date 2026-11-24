//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgimagenode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgimagenode.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGImageNode that Python can take functions over in. Every QSGImageNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGImageNodeCall0)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGImageNodeCall1)(const void *, int *);
typedef void (*CuteQSGImageNodeCall2)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGImageNodeCall3)(const void *, int *);
typedef void (*CuteQSGImageNodeCall4)(const void *, QSGTexture *, int *);
typedef void * (*CuteQSGImageNodeCall5)(const void *, int *);
typedef void (*CuteQSGImageNodeCall6)(const void *, int, int *);
typedef int (*CuteQSGImageNodeCall7)(const void *, int *);
typedef void (*CuteQSGImageNodeCall8)(const void *, int, int *);
typedef int (*CuteQSGImageNodeCall9)(const void *, int *);
typedef void (*CuteQSGImageNodeCall10)(const void *, int, int *);
typedef int (*CuteQSGImageNodeCall11)(const void *, int *);
typedef void (*CuteQSGImageNodeCall12)(const void *, int, int *);
typedef int (*CuteQSGImageNodeCall13)(const void *, int *);
typedef void (*CuteQSGImageNodeCall14)(const void *, bool, int *);
typedef bool (*CuteQSGImageNodeCall15)(const void *, int *);
typedef bool (*CuteQSGImageNodeCall16)(const void *, int *);
typedef void (*CuteQSGImageNodeCall17)(const void *, int *);
class CuteQSGImageNode : public QSGImageNode {
public:
  using QSGImageNode::QSGImageNode;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QSGImageNode7setRectERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode4rectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGImageNode13setSourceRectERK6QRectF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode10sourceRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGImageNode10setTextureEP10QSGTexture")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode7textureEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGImageNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode9filteringEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGImageNode18setMipmapFilteringEN10QSGTexture9FilteringE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode15mipmapFilteringEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGImageNode18setAnisotropyLevelEN10QSGTexture15AnisotropyLevelE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode15anisotropyLevelEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGImageNode30setTextureCoordinatesTransformE6QFlagsINS_31TextureCoordinatesTransformFlagEE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode27textureCoordinatesTransformEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGImageNode14setOwnsTextureEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGImageNode11ownsTextureEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QSGImageNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGImageNodeCall0 call = reinterpret_cast<CuteQSGImageNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  QRectF QSGImageNode::rect() const
  QRectF rect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGImageNodeCall1 call = reinterpret_cast<CuteQSGImageNodeCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGImageNode::setSourceRect(const QRectF &r)
  void setSourceRect(const QRectF &r) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGImageNodeCall2 call = reinterpret_cast<CuteQSGImageNodeCall2>(taken[2]);
      call(this, &r, &handled);
      if (handled) return;
    }
  }

  //  QRectF QSGImageNode::sourceRect() const
  QRectF sourceRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGImageNodeCall3 call = reinterpret_cast<CuteQSGImageNodeCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGImageNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGImageNodeCall4 call = reinterpret_cast<CuteQSGImageNodeCall4>(taken[4]);
      call(this, texture, &handled);
      if (handled) return;
    }
  }

  //  QSGTexture *QSGImageNode::texture() const
  QSGTexture *texture() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGImageNodeCall5 call = reinterpret_cast<CuteQSGImageNodeCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return {};
  }

  //  void QSGImageNode::setFiltering(QSGTexture::Filtering filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGImageNodeCall6 call = reinterpret_cast<CuteQSGImageNodeCall6>(taken[6]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
  }

  //  QSGTexture::Filtering QSGImageNode::filtering() const
  QSGTexture::Filtering filtering() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGImageNodeCall7 call = reinterpret_cast<CuteQSGImageNodeCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return {};
  }

  //  void QSGImageNode::setMipmapFiltering(QSGTexture::Filtering
  //      filtering)
  void setMipmapFiltering(QSGTexture::Filtering filtering) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGImageNodeCall8 call = reinterpret_cast<CuteQSGImageNodeCall8>(taken[8]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
  }

  //  QSGTexture::Filtering QSGImageNode::mipmapFiltering() const
  QSGTexture::Filtering mipmapFiltering() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGImageNodeCall9 call = reinterpret_cast<CuteQSGImageNodeCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return {};
  }

  //  void QSGImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
  //      level)
  void setAnisotropyLevel(QSGTexture::AnisotropyLevel level) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGImageNodeCall10 call = reinterpret_cast<CuteQSGImageNodeCall10>(taken[10]);
      call(this, static_cast<int>(level), &handled);
      if (handled) return;
    }
  }

  //  QSGTexture::AnisotropyLevel QSGImageNode::anisotropyLevel() const
  QSGTexture::AnisotropyLevel anisotropyLevel() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGImageNodeCall11 call = reinterpret_cast<CuteQSGImageNodeCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::AnisotropyLevel>(given);
    }
    return {};
  }

  //  void QSGImageNode::setTextureCoordinatesTransform(TextureCoordinatesT
  //      ransformMode mode)
  void setTextureCoordinatesTransform(
      QSGImageNode::TextureCoordinatesTransformMode mode) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGImageNodeCall12 call = reinterpret_cast<CuteQSGImageNodeCall12>(taken[12]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
  }

  //  TextureCoordinatesTransformMode
  //      QSGImageNode::textureCoordinatesTransform() const
  QSGImageNode::TextureCoordinatesTransformMode textureCoordinatesTransform() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGImageNodeCall13 call = reinterpret_cast<CuteQSGImageNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(given);
    }
    return {};
  }

  //  void QSGImageNode::setOwnsTexture(bool owns)
  void setOwnsTexture(bool owns) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGImageNodeCall14 call = reinterpret_cast<CuteQSGImageNodeCall14>(taken[14]);
      call(this, owns, &handled);
      if (handled) return;
    }
  }

  //  bool QSGImageNode::ownsTexture() const
  bool ownsTexture() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGImageNodeCall15 call = reinterpret_cast<CuteQSGImageNodeCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGImageNodeCall16 call = reinterpret_cast<CuteQSGImageNodeCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGImageNodeCall17 call = reinterpret_cast<CuteQSGImageNodeCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGImageNode::~QSGImageNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNodeD1Ev(QSGImageNode *self) {
  delete self;
}

//  void QSGImageNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode7setRectERK6QRectF(
    QSGImageNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGImageNode::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode7setRectEdddd(
    QSGImageNode *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  QRectF QSGImageNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QSGImageNode4rectEv(const QSGImageNode *self) {
  return new QRectF(self->rect());
}

//  void QSGImageNode::setSourceRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode13setSourceRectERK6QRectF(
    QSGImageNode *self,
    const QRectF *r) {
  self->setSourceRect(*r);
}

//  void QSGImageNode::setSourceRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode13setSourceRectEdddd(
    QSGImageNode *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setSourceRect(x, y, w, h);
}

//  QRectF QSGImageNode::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QSGImageNode10sourceRectEv(const QSGImageNode *self) {
  return new QRectF(self->sourceRect());
}

//  void QSGImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode10setTextureEP10QSGTexture(
    QSGImageNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGTexture *QSGImageNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK12QSGImageNode7textureEv(const QSGImageNode *self) {
  return self->texture();
}

//  void QSGImageNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  QSGTexture::Filtering QSGImageNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK12QSGImageNode9filteringEv(
    const QSGImageNode *self) {
  return self->filtering();
}

//  void QSGImageNode::setMipmapFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setMipmapFiltering(filtering);
}

//  QSGTexture::Filtering QSGImageNode::mipmapFiltering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK12QSGImageNode15mipmapFilteringEv(
    const QSGImageNode *self) {
  return self->mipmapFiltering();
}

//  void QSGImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel level)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode18setAnisotropyLevelEN10QSGTexture15AnisotropyLevelE(
    QSGImageNode *self,
    QSGTexture::AnisotropyLevel level) {
  self->setAnisotropyLevel(level);
}

//  QSGTexture::AnisotropyLevel QSGImageNode::anisotropyLevel() const
extern "C" Q_DECL_EXPORT
QSGTexture::AnisotropyLevel ritual_ZNK12QSGImageNode15anisotropyLevelEv(
    const QSGImageNode *self) {
  return self->anisotropyLevel();
}

//  void QSGImageNode::setTextureCoordinatesTransform(TextureCoordinatesTrans
//      formMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode30setTextureCoordinatesTransformE6QFlagsINS_31TextureCoordinatesTransformFlagEE(
    QSGImageNode *self,
    int mode) {
  self->setTextureCoordinatesTransform(
      QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(mode));
}

//  TextureCoordinatesTransformMode
//      QSGImageNode::textureCoordinatesTransform() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSGImageNode27textureCoordinatesTransformEv(
    const QSGImageNode *self) {
  return static_cast<int>(self->textureCoordinatesTransform().toInt());
}

//  void QSGImageNode::setOwnsTexture(bool owns)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode14setOwnsTextureEb(
    QSGImageNode *self,
    bool owns) {
  self->setOwnsTexture(owns);
}

//  bool QSGImageNode::ownsTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSGImageNode11ownsTextureEv(const QSGImageNode *self) {
  return self->ownsTexture();
}

//  void QSGImageNode::rebuildGeometry(QSGGeometry *g, QSGTexture *texture,
//      const QRectF &rect, QRectF sourceRect,
//      TextureCoordinatesTransformMode texCoordMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGImageNode15rebuildGeometryEP11QSGGeometryP10QSGTextureRK6QRectFS4_6QFlagsINS_31TextureCoordinatesTransformFlagEE(
    QSGGeometry *g,
    QSGTexture *texture,
    const QRectF *rect,
    const QRectF *sourceRect,
    int texCoordMode) {
  QSGImageNode::rebuildGeometry(
      g,
      texture,
      *rect,
      *sourceRect,
      QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(texCoordMode));
}

//  a Python function taken by a CuteQSGImageNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGImageNode(
    QSGImageNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGImageNode *>(self)->take(key, call);
}
