//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultimagenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultimagenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGDefaultImageNode that Python can take functions over in. Every QSGDefaultImageNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGDefaultImageNodeCall0)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGDefaultImageNodeCall1)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall2)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGDefaultImageNodeCall3)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall4)(const void *, QSGTexture *, int *);
typedef void * (*CuteQSGDefaultImageNodeCall5)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall6)(const void *, int, int *);
typedef int (*CuteQSGDefaultImageNodeCall7)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall8)(const void *, int, int *);
typedef int (*CuteQSGDefaultImageNodeCall9)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall10)(const void *, int, int *);
typedef int (*CuteQSGDefaultImageNodeCall11)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall12)(const void *, int, int *);
typedef int (*CuteQSGDefaultImageNodeCall13)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall14)(const void *, bool, int *);
typedef bool (*CuteQSGDefaultImageNodeCall15)(const void *, int *);
typedef bool (*CuteQSGDefaultImageNodeCall16)(const void *, int *);
typedef void (*CuteQSGDefaultImageNodeCall17)(const void *, int *);
class CuteQSGDefaultImageNode : public QSGDefaultImageNode {
public:
  using QSGDefaultImageNode::QSGDefaultImageNode;
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

  //  void QSGDefaultImageNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall0 call = reinterpret_cast<CuteQSGDefaultImageNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setRect(rect);
  }

  //  QRectF QSGDefaultImageNode::rect() const
  QRectF rect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall1 call = reinterpret_cast<CuteQSGDefaultImageNodeCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGDefaultImageNode::rect();
  }

  //  void QSGDefaultImageNode::setSourceRect(const QRectF &r)
  void setSourceRect(const QRectF &r) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall2 call = reinterpret_cast<CuteQSGDefaultImageNodeCall2>(taken[2]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setSourceRect(r);
  }

  //  QRectF QSGDefaultImageNode::sourceRect() const
  QRectF sourceRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall3 call = reinterpret_cast<CuteQSGDefaultImageNodeCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGDefaultImageNode::sourceRect();
  }

  //  void QSGDefaultImageNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall4 call = reinterpret_cast<CuteQSGDefaultImageNodeCall4>(taken[4]);
      call(this, texture, &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setTexture(texture);
  }

  //  QSGTexture *QSGDefaultImageNode::texture() const
  QSGTexture *texture() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall5 call = reinterpret_cast<CuteQSGDefaultImageNodeCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGDefaultImageNode::texture();
  }

  //  void QSGDefaultImageNode::setFiltering(QSGTexture::Filtering
  //      filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall6 call = reinterpret_cast<CuteQSGDefaultImageNodeCall6>(taken[6]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setFiltering(filtering);
  }

  //  QSGTexture::Filtering QSGDefaultImageNode::filtering() const
  QSGTexture::Filtering filtering() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall7 call = reinterpret_cast<CuteQSGDefaultImageNodeCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return QSGDefaultImageNode::filtering();
  }

  //  void QSGDefaultImageNode::setMipmapFiltering(QSGTexture::Filtering
  //      filtering)
  void setMipmapFiltering(QSGTexture::Filtering filtering) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall8 call = reinterpret_cast<CuteQSGDefaultImageNodeCall8>(taken[8]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setMipmapFiltering(filtering);
  }

  //  QSGTexture::Filtering QSGDefaultImageNode::mipmapFiltering() const
  QSGTexture::Filtering mipmapFiltering() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall9 call = reinterpret_cast<CuteQSGDefaultImageNodeCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return QSGDefaultImageNode::mipmapFiltering();
  }

  //  void
  //      QSGDefaultImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLev
  //      el level)
  void setAnisotropyLevel(QSGTexture::AnisotropyLevel level) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall10 call = reinterpret_cast<CuteQSGDefaultImageNodeCall10>(taken[10]);
      call(this, static_cast<int>(level), &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setAnisotropyLevel(level);
  }

  //  QSGTexture::AnisotropyLevel QSGDefaultImageNode::anisotropyLevel()
  //      const
  QSGTexture::AnisotropyLevel anisotropyLevel() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall11 call = reinterpret_cast<CuteQSGDefaultImageNodeCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::AnisotropyLevel>(given);
    }
    return QSGDefaultImageNode::anisotropyLevel();
  }

  //  void QSGDefaultImageNode::setTextureCoordinatesTransform(TextureCoord
  //      inatesTransformMode mode)
  void setTextureCoordinatesTransform(
      QSGImageNode::TextureCoordinatesTransformMode mode) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall12 call = reinterpret_cast<CuteQSGDefaultImageNodeCall12>(taken[12]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setTextureCoordinatesTransform(mode);
  }

  //  TextureCoordinatesTransformMode
  //      QSGDefaultImageNode::textureCoordinatesTransform() const
  QSGImageNode::TextureCoordinatesTransformMode textureCoordinatesTransform() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall13 call = reinterpret_cast<CuteQSGDefaultImageNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(given);
    }
    return QSGDefaultImageNode::textureCoordinatesTransform();
  }

  //  void QSGDefaultImageNode::setOwnsTexture(bool owns)
  void setOwnsTexture(bool owns) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall14 call = reinterpret_cast<CuteQSGDefaultImageNodeCall14>(taken[14]);
      call(this, owns, &handled);
      if (handled) return;
    }
    QSGDefaultImageNode::setOwnsTexture(owns);
  }

  //  bool QSGDefaultImageNode::ownsTexture() const
  bool ownsTexture() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall15 call = reinterpret_cast<CuteQSGDefaultImageNodeCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGDefaultImageNode::ownsTexture();
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall16 call = reinterpret_cast<CuteQSGDefaultImageNodeCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGDefaultImageNodeCall17 call = reinterpret_cast<CuteQSGDefaultImageNodeCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGDefaultImageNode::QSGDefaultImageNode()
extern "C" Q_DECL_EXPORT
QSGDefaultImageNode *ritual_ZN19QSGDefaultImageNodeC1Ev() {
  return new CuteQSGDefaultImageNode();
}

//  QSGDefaultImageNode::~QSGDefaultImageNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNodeD1Ev(QSGDefaultImageNode *self) {
  delete self;
}

//  void QSGDefaultImageNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode7setRectERK6QRectF(
    QSGDefaultImageNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  QRectF QSGDefaultImageNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QSGDefaultImageNode4rectEv(
    const QSGDefaultImageNode *self) {
  return new QRectF(self->rect());
}

//  void QSGDefaultImageNode::setSourceRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode13setSourceRectERK6QRectF(
    QSGDefaultImageNode *self,
    const QRectF *r) {
  self->setSourceRect(*r);
}

//  QRectF QSGDefaultImageNode::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QSGDefaultImageNode10sourceRectEv(
    const QSGDefaultImageNode *self) {
  return new QRectF(self->sourceRect());
}

//  void QSGDefaultImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode10setTextureEP10QSGTexture(
    QSGDefaultImageNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGTexture *QSGDefaultImageNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK19QSGDefaultImageNode7textureEv(
    const QSGDefaultImageNode *self) {
  return self->texture();
}

//  void QSGDefaultImageNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGDefaultImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  QSGTexture::Filtering QSGDefaultImageNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK19QSGDefaultImageNode9filteringEv(
    const QSGDefaultImageNode *self) {
  return self->filtering();
}

//  void QSGDefaultImageNode::setMipmapFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGDefaultImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setMipmapFiltering(filtering);
}

//  QSGTexture::Filtering QSGDefaultImageNode::mipmapFiltering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK19QSGDefaultImageNode15mipmapFilteringEv(
    const QSGDefaultImageNode *self) {
  return self->mipmapFiltering();
}

//  void QSGDefaultImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode18setAnisotropyLevelEN10QSGTexture15AnisotropyLevelE(
    QSGDefaultImageNode *self,
    QSGTexture::AnisotropyLevel level) {
  self->setAnisotropyLevel(level);
}

//  QSGTexture::AnisotropyLevel QSGDefaultImageNode::anisotropyLevel() const
extern "C" Q_DECL_EXPORT
QSGTexture::AnisotropyLevel ritual_ZNK19QSGDefaultImageNode15anisotropyLevelEv(
    const QSGDefaultImageNode *self) {
  return self->anisotropyLevel();
}

//  void QSGDefaultImageNode::setTextureCoordinatesTransform(TextureCoordinat
//      esTransformMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode30setTextureCoordinatesTransformE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE(
    QSGDefaultImageNode *self,
    int mode) {
  self->setTextureCoordinatesTransform(
      QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(mode));
}

//  TextureCoordinatesTransformMode
//      QSGDefaultImageNode::textureCoordinatesTransform() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSGDefaultImageNode27textureCoordinatesTransformEv(
    const QSGDefaultImageNode *self) {
  return static_cast<int>(self->textureCoordinatesTransform().toInt());
}

//  void QSGDefaultImageNode::setOwnsTexture(bool owns)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultImageNode14setOwnsTextureEb(
    QSGDefaultImageNode *self,
    bool owns) {
  self->setOwnsTexture(owns);
}

//  bool QSGDefaultImageNode::ownsTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSGDefaultImageNode11ownsTextureEv(
    const QSGDefaultImageNode *self) {
  return self->ownsTexture();
}

//  a Python function taken by a CuteQSGDefaultImageNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDefaultImageNode(
    QSGDefaultImageNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDefaultImageNode *>(self)->take(key, call);
}

//  void QSGDefaultImageNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode7setRectERK6QRectF(
    QSGDefaultImageNode *self,
    const QRectF *rect) {
  self->QSGDefaultImageNode::setRect(*rect);
}

//  QRectF QSGDefaultImageNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QSGDefaultImageNode4rectEv(
    const QSGDefaultImageNode *self) {
  return new QRectF(self->QSGDefaultImageNode::rect());
}

//  void QSGDefaultImageNode::setSourceRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode13setSourceRectERK6QRectF(
    QSGDefaultImageNode *self,
    const QRectF *r) {
  self->QSGDefaultImageNode::setSourceRect(*r);
}

//  QRectF QSGDefaultImageNode::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QSGDefaultImageNode10sourceRectEv(
    const QSGDefaultImageNode *self) {
  return new QRectF(self->QSGDefaultImageNode::sourceRect());
}

//  void QSGDefaultImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode10setTextureEP10QSGTexture(
    QSGDefaultImageNode *self,
    QSGTexture *texture) {
  self->QSGDefaultImageNode::setTexture(texture);
}

//  QSGTexture *QSGDefaultImageNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK19QSGDefaultImageNode7textureEv(
    const QSGDefaultImageNode *self) {
  return self->QSGDefaultImageNode::texture();
}

//  void QSGDefaultImageNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGDefaultImageNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGDefaultImageNode::setFiltering(filtering);
}

//  QSGTexture::Filtering QSGDefaultImageNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_own_ZNK19QSGDefaultImageNode9filteringEv(
    const QSGDefaultImageNode *self) {
  return self->QSGDefaultImageNode::filtering();
}

//  void QSGDefaultImageNode::setMipmapFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGDefaultImageNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGDefaultImageNode::setMipmapFiltering(filtering);
}

//  QSGTexture::Filtering QSGDefaultImageNode::mipmapFiltering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_own_ZNK19QSGDefaultImageNode15mipmapFilteringEv(
    const QSGDefaultImageNode *self) {
  return self->QSGDefaultImageNode::mipmapFiltering();
}

//  void QSGDefaultImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
//      level)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode18setAnisotropyLevelEN10QSGTexture15AnisotropyLevelE(
    QSGDefaultImageNode *self,
    QSGTexture::AnisotropyLevel level) {
  self->QSGDefaultImageNode::setAnisotropyLevel(level);
}

//  QSGTexture::AnisotropyLevel QSGDefaultImageNode::anisotropyLevel() const
extern "C" Q_DECL_EXPORT
QSGTexture::AnisotropyLevel ritual_own_ZNK19QSGDefaultImageNode15anisotropyLevelEv(
    const QSGDefaultImageNode *self) {
  return self->QSGDefaultImageNode::anisotropyLevel();
}

//  void QSGDefaultImageNode::setTextureCoordinatesTransform(TextureCoordinat
//      esTransformMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode30setTextureCoordinatesTransformE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE(
    QSGDefaultImageNode *self,
    int mode) {
  self->QSGDefaultImageNode::setTextureCoordinatesTransform(
      QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(mode));
}

//  TextureCoordinatesTransformMode
//      QSGDefaultImageNode::textureCoordinatesTransform() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QSGDefaultImageNode27textureCoordinatesTransformEv(
    const QSGDefaultImageNode *self) {
  return static_cast<int>(
      self->QSGDefaultImageNode::textureCoordinatesTransform().toInt());
}

//  void QSGDefaultImageNode::setOwnsTexture(bool owns)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultImageNode14setOwnsTextureEb(
    QSGDefaultImageNode *self,
    bool owns) {
  self->QSGDefaultImageNode::setOwnsTexture(owns);
}

//  bool QSGDefaultImageNode::ownsTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QSGDefaultImageNode11ownsTextureEv(
    const QSGDefaultImageNode *self) {
  return self->QSGDefaultImageNode::ownsTexture();
}
