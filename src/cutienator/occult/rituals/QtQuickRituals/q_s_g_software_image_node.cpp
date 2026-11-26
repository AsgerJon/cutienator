//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 42, as _ZN20QSGSoftwareImageNode10setTextureEP10QSGTexture
inline void QSGSoftwareImageNode::setTexture(QSGTexture *texture)
{
    if (m_owns)
        delete m_texture;

    m_texture = texture; markDirty(DirtyMaterial);
    m_cachedMirroredPixmapIsDirty = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 51, as _ZN20QSGSoftwareImageNode30setTextureCoordinatesTransformE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE
inline void QSGSoftwareImageNode::setTextureCoordinatesTransform(QSGImageNode::TextureCoordinatesTransformMode transformNode)
{
    if (m_transformMode == transformNode)
        return;

    m_transformMode = transformNode;
    m_cachedMirroredPixmapIsDirty = true;

    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 25, as _ZN20QSGSoftwareImageNodeC1Ev
inline QSGSoftwareImageNode::QSGSoftwareImageNode()
    : m_texture(nullptr),
      m_owns(false),
      m_filtering(QSGTexture::None),
      m_transformMode(NoTransform),
      m_cachedMirroredPixmapIsDirty(false)
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 36, as _ZN20QSGSoftwareImageNodeD1Ev
inline QSGSoftwareImageNode::~QSGSoftwareImageNode()
{
    if (m_owns)
        delete m_texture;
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareImageNode that Python can take functions over in. Every QSGSoftwareImageNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGSoftwareImageNodeCall0)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGSoftwareImageNodeCall1)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall2)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGSoftwareImageNodeCall3)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall4)(const void *, QSGTexture *, int *);
typedef void * (*CuteQSGSoftwareImageNodeCall5)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall6)(const void *, int, int *);
typedef int (*CuteQSGSoftwareImageNodeCall7)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall8)(const void *, int, int *);
typedef int (*CuteQSGSoftwareImageNodeCall9)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall10)(const void *, int, int *);
typedef int (*CuteQSGSoftwareImageNodeCall11)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall12)(const void *, int, int *);
typedef int (*CuteQSGSoftwareImageNodeCall13)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall14)(const void *, bool, int *);
typedef bool (*CuteQSGSoftwareImageNodeCall15)(const void *, int *);
typedef bool (*CuteQSGSoftwareImageNodeCall16)(const void *, int *);
typedef void (*CuteQSGSoftwareImageNodeCall17)(const void *, int *);
class CuteQSGSoftwareImageNode : public QSGSoftwareImageNode {
public:
  using QSGSoftwareImageNode::QSGSoftwareImageNode;
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

  //  void QSGSoftwareImageNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall0 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setRect(rect);
  }

  //  QRectF QSGSoftwareImageNode::rect() const
  QRectF rect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall1 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwareImageNode::rect();
  }

  //  void QSGSoftwareImageNode::setSourceRect(const QRectF &r)
  void setSourceRect(const QRectF &r) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall2 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall2>(taken[2]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setSourceRect(r);
  }

  //  QRectF QSGSoftwareImageNode::sourceRect() const
  QRectF sourceRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall3 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwareImageNode::sourceRect();
  }

  //  void QSGSoftwareImageNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall4 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall4>(taken[4]);
      call(this, texture, &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setTexture(texture);
  }

  //  QSGTexture *QSGSoftwareImageNode::texture() const
  QSGTexture *texture() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall5 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGSoftwareImageNode::texture();
  }

  //  void QSGSoftwareImageNode::setFiltering(QSGTexture::Filtering
  //      filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall6 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall6>(taken[6]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setFiltering(filtering);
  }

  //  QSGTexture::Filtering QSGSoftwareImageNode::filtering() const
  QSGTexture::Filtering filtering() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall7 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return QSGSoftwareImageNode::filtering();
  }

  //  void QSGSoftwareImageNode::setMipmapFiltering(QSGTexture::Filtering
  //      a0)
  void setMipmapFiltering(QSGTexture::Filtering a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall8 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall8>(taken[8]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setMipmapFiltering(a0);
  }

  //  QSGTexture::Filtering QSGSoftwareImageNode::mipmapFiltering() const
  QSGTexture::Filtering mipmapFiltering() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall9 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return QSGSoftwareImageNode::mipmapFiltering();
  }

  //  void
  //      QSGSoftwareImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLe
  //      vel a0)
  void setAnisotropyLevel(QSGTexture::AnisotropyLevel a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall10 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall10>(taken[10]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setAnisotropyLevel(a0);
  }

  //  QSGTexture::AnisotropyLevel QSGSoftwareImageNode::anisotropyLevel()
  //      const
  QSGTexture::AnisotropyLevel anisotropyLevel() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall11 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::AnisotropyLevel>(given);
    }
    return QSGSoftwareImageNode::anisotropyLevel();
  }

  //  void QSGSoftwareImageNode::setTextureCoordinatesTransform(TextureCoor
  //      dinatesTransformMode transformNode)
  void setTextureCoordinatesTransform(
      QSGImageNode::TextureCoordinatesTransformMode transformNode) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall12 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall12>(taken[12]);
      call(this, static_cast<int>(transformNode.toInt()), &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setTextureCoordinatesTransform(transformNode);
  }

  //  TextureCoordinatesTransformMode
  //      QSGSoftwareImageNode::textureCoordinatesTransform() const
  QSGImageNode::TextureCoordinatesTransformMode textureCoordinatesTransform() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall13 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(given);
    }
    return QSGSoftwareImageNode::textureCoordinatesTransform();
  }

  //  void QSGSoftwareImageNode::setOwnsTexture(bool owns)
  void setOwnsTexture(bool owns) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall14 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall14>(taken[14]);
      call(this, owns, &handled);
      if (handled) return;
    }
    QSGSoftwareImageNode::setOwnsTexture(owns);
  }

  //  bool QSGSoftwareImageNode::ownsTexture() const
  bool ownsTexture() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall15 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareImageNode::ownsTexture();
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall16 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareImageNodeCall17 call = reinterpret_cast<CuteQSGSoftwareImageNodeCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGSoftwareImageNode::QSGSoftwareImageNode()
extern "C" Q_DECL_EXPORT
QSGSoftwareImageNode *ritual_ZN20QSGSoftwareImageNodeC1Ev() {
  return new CuteQSGSoftwareImageNode();
}

//  QSGSoftwareImageNode::~QSGSoftwareImageNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNodeD1Ev(QSGSoftwareImageNode *self) {
  delete self;
}

//  void QSGSoftwareImageNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode7setRectERK6QRectF(
    QSGSoftwareImageNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  QRectF QSGSoftwareImageNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QSGSoftwareImageNode4rectEv(
    const QSGSoftwareImageNode *self) {
  return new QRectF(self->rect());
}

//  void QSGSoftwareImageNode::setSourceRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode13setSourceRectERK6QRectF(
    QSGSoftwareImageNode *self,
    const QRectF *r) {
  self->setSourceRect(*r);
}

//  QRectF QSGSoftwareImageNode::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QSGSoftwareImageNode10sourceRectEv(
    const QSGSoftwareImageNode *self) {
  return new QRectF(self->sourceRect());
}

//  void QSGSoftwareImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode10setTextureEP10QSGTexture(
    QSGSoftwareImageNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGTexture *QSGSoftwareImageNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK20QSGSoftwareImageNode7textureEv(
    const QSGSoftwareImageNode *self) {
  return self->texture();
}

//  void QSGSoftwareImageNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  QSGTexture::Filtering QSGSoftwareImageNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK20QSGSoftwareImageNode9filteringEv(
    const QSGSoftwareImageNode *self) {
  return self->filtering();
}

//  void QSGSoftwareImageNode::setMipmapFiltering(QSGTexture::Filtering a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareImageNode *self,
    QSGTexture::Filtering a0) {
  self->setMipmapFiltering(a0);
}

//  QSGTexture::Filtering QSGSoftwareImageNode::mipmapFiltering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK20QSGSoftwareImageNode15mipmapFilteringEv(
    const QSGSoftwareImageNode *self) {
  return self->mipmapFiltering();
}

//  void QSGSoftwareImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode18setAnisotropyLevelEN10QSGTexture15AnisotropyLevelE(
    QSGSoftwareImageNode *self,
    QSGTexture::AnisotropyLevel a0) {
  self->setAnisotropyLevel(a0);
}

//  QSGTexture::AnisotropyLevel QSGSoftwareImageNode::anisotropyLevel() const
extern "C" Q_DECL_EXPORT
QSGTexture::AnisotropyLevel ritual_ZNK20QSGSoftwareImageNode15anisotropyLevelEv(
    const QSGSoftwareImageNode *self) {
  return self->anisotropyLevel();
}

//  void QSGSoftwareImageNode::setTextureCoordinatesTransform(TextureCoordina
//      tesTransformMode transformNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode30setTextureCoordinatesTransformE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE(
    QSGSoftwareImageNode *self,
    int transformNode) {
  self->setTextureCoordinatesTransform(
      QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(transformNode));
}

//  TextureCoordinatesTransformMode
//      QSGSoftwareImageNode::textureCoordinatesTransform() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QSGSoftwareImageNode27textureCoordinatesTransformEv(
    const QSGSoftwareImageNode *self) {
  return static_cast<int>(self->textureCoordinatesTransform().toInt());
}

//  void QSGSoftwareImageNode::setOwnsTexture(bool owns)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareImageNode14setOwnsTextureEb(
    QSGSoftwareImageNode *self,
    bool owns) {
  self->setOwnsTexture(owns);
}

//  bool QSGSoftwareImageNode::ownsTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QSGSoftwareImageNode11ownsTextureEv(
    const QSGSoftwareImageNode *self) {
  return self->ownsTexture();
}

//  a Python function taken by a CuteQSGSoftwareImageNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareImageNode(
    QSGSoftwareImageNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareImageNode *>(self)->take(key, call);
}

//  void QSGSoftwareImageNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode7setRectERK6QRectF(
    QSGSoftwareImageNode *self,
    const QRectF *rect) {
  self->QSGSoftwareImageNode::setRect(*rect);
}

//  QRectF QSGSoftwareImageNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK20QSGSoftwareImageNode4rectEv(
    const QSGSoftwareImageNode *self) {
  return new QRectF(self->QSGSoftwareImageNode::rect());
}

//  void QSGSoftwareImageNode::setSourceRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode13setSourceRectERK6QRectF(
    QSGSoftwareImageNode *self,
    const QRectF *r) {
  self->QSGSoftwareImageNode::setSourceRect(*r);
}

//  QRectF QSGSoftwareImageNode::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK20QSGSoftwareImageNode10sourceRectEv(
    const QSGSoftwareImageNode *self) {
  return new QRectF(self->QSGSoftwareImageNode::sourceRect());
}

//  void QSGSoftwareImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode10setTextureEP10QSGTexture(
    QSGSoftwareImageNode *self,
    QSGTexture *texture) {
  self->QSGSoftwareImageNode::setTexture(texture);
}

//  QSGTexture *QSGSoftwareImageNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK20QSGSoftwareImageNode7textureEv(
    const QSGSoftwareImageNode *self) {
  return self->QSGSoftwareImageNode::texture();
}

//  void QSGSoftwareImageNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareImageNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGSoftwareImageNode::setFiltering(filtering);
}

//  QSGTexture::Filtering QSGSoftwareImageNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_own_ZNK20QSGSoftwareImageNode9filteringEv(
    const QSGSoftwareImageNode *self) {
  return self->QSGSoftwareImageNode::filtering();
}

//  void QSGSoftwareImageNode::setMipmapFiltering(QSGTexture::Filtering a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareImageNode *self,
    QSGTexture::Filtering a0) {
  self->QSGSoftwareImageNode::setMipmapFiltering(a0);
}

//  QSGTexture::Filtering QSGSoftwareImageNode::mipmapFiltering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_own_ZNK20QSGSoftwareImageNode15mipmapFilteringEv(
    const QSGSoftwareImageNode *self) {
  return self->QSGSoftwareImageNode::mipmapFiltering();
}

//  void QSGSoftwareImageNode::setAnisotropyLevel(QSGTexture::AnisotropyLevel
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode18setAnisotropyLevelEN10QSGTexture15AnisotropyLevelE(
    QSGSoftwareImageNode *self,
    QSGTexture::AnisotropyLevel a0) {
  self->QSGSoftwareImageNode::setAnisotropyLevel(a0);
}

//  QSGTexture::AnisotropyLevel QSGSoftwareImageNode::anisotropyLevel() const
extern "C" Q_DECL_EXPORT
QSGTexture::AnisotropyLevel ritual_own_ZNK20QSGSoftwareImageNode15anisotropyLevelEv(
    const QSGSoftwareImageNode *self) {
  return self->QSGSoftwareImageNode::anisotropyLevel();
}

//  void QSGSoftwareImageNode::setTextureCoordinatesTransform(TextureCoordina
//      tesTransformMode transformNode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode30setTextureCoordinatesTransformE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE(
    QSGSoftwareImageNode *self,
    int transformNode) {
  self->QSGSoftwareImageNode::setTextureCoordinatesTransform(
      QFlags<QSGImageNode::TextureCoordinatesTransformFlag>::fromInt(transformNode));
}

//  TextureCoordinatesTransformMode
//      QSGSoftwareImageNode::textureCoordinatesTransform() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QSGSoftwareImageNode27textureCoordinatesTransformEv(
    const QSGSoftwareImageNode *self) {
  return static_cast<int>(
      self->QSGSoftwareImageNode::textureCoordinatesTransform().toInt());
}

//  void QSGSoftwareImageNode::setOwnsTexture(bool owns)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareImageNode14setOwnsTextureEb(
    QSGSoftwareImageNode *self,
    bool owns) {
  self->QSGSoftwareImageNode::setOwnsTexture(owns);
}

//  bool QSGSoftwareImageNode::ownsTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QSGSoftwareImageNode11ownsTextureEv(
    const QSGSoftwareImageNode *self) {
  return self->QSGSoftwareImageNode::ownsTexture();
}
