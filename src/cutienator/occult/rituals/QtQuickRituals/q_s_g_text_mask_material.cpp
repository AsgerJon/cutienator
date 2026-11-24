//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgdefaultglyphnode_p_p.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtCore/qmath.h>
#include <QtQuick/private/qsgrhitextureglyphcache_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtGui/qrgb.h>
#include <QtGui/private/qdrawhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 323, as _ZN19QSGTextMaskMaterialD2Ev
inline QSGTextMaskMaterial::~QSGTextMaskMaterial()
{
    if (m_retainedFontEngine != nullptr)
        m_rc->unregisterFontengineForCleanup(m_retainedFontEngine);
    delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 12, as _ZN23QSGRhiTextureGlyphCacheC1EP23QSGDefaultRenderContextN11QFontEngine11GlyphFormatERK10QTransformRK6QColor
inline QSGRhiTextureGlyphCache::QSGRhiTextureGlyphCache(QSGDefaultRenderContext *rc,
                                                 QFontEngine::GlyphFormat format, const QTransform &matrix,
                                                 const QColor &color)
    : QImageTextureGlyphCache(format, matrix, color),
      m_rc(rc),
      m_rhi(rc->rhi())
{
    // Some OpenGL implementations, for instance macOS, have issues with
    // GL_ALPHA render targets. Similarly, BGRA may be problematic on GLES 2.0.
    // So stick with plain image uploads on GL.
    m_resizeWithTextureCopy = m_rhi->backend() != QRhi::OpenGLES2;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 499, as _ZNK19QSGTextMaskMaterial4typeEv
inline QSGMaterialType *QSGTextMaskMaterial::type() const
{
    static QSGMaterialType argb, rgb, gray;
    switch (glyphCache()->glyphFormat()) {
    case QFontEngine::Format_ARGB:
        return &argb;
    case QFontEngine::Format_A32:
        return &rgb;
    case QFontEngine::Format_A8:
    default:
        return &gray;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 561, as _ZN19QSGTextMaskMaterial14ensureUpToDateEv
inline bool QSGTextMaskMaterial::ensureUpToDate()
{
    QSGRhiTextureGlyphCache *gc = rhiGlyphCache();
    QSize glyphCacheSize(gc->width(), gc->height());
    if (glyphCacheSize != m_size) {
        if (m_texture)
            delete m_texture;
        m_texture = new QSGPlainTexture;
        m_texture->setTexture(gc->texture());
        m_texture->setTextureSize(QSize(gc->width(), gc->height()));
        m_texture->setOwnsTexture(false);
        m_size = glyphCacheSize;
        return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 513, as _ZNK19QSGTextMaskMaterial10glyphCacheEv
inline QTextureGlyphCache *QSGTextMaskMaterial::glyphCache() const
{
    return static_cast<QTextureGlyphCache *>(m_glyphCache.data());
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 518, as _ZNK19QSGTextMaskMaterial13rhiGlyphCacheEv
inline QSGRhiTextureGlyphCache *QSGTextMaskMaterial::rhiGlyphCache() const
{
    return static_cast<QSGRhiTextureGlyphCache *>(glyphCache());
}
//  -----------------------------------------------------------------------

//  A QSGTextMaskMaterial that Python can take functions over in. Every QSGTextMaskMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGTextMaskMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGTextMaskMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGTextMaskMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGTextMaskMaterial : public QSGTextMaskMaterial {
public:
  using QSGTextMaskMaterial::QSGTextMaskMaterial;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QSGMaterialType *QSGTextMaskMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTextMaskMaterialCall0 call = reinterpret_cast<CuteQSGTextMaskMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGTextMaskMaterial::type();
  }

  //  QSGMaterialShader
  //      *QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMo
  //      de renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGTextMaskMaterialCall1 call = reinterpret_cast<CuteQSGTextMaskMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGTextMaskMaterial::createShader(renderMode);
  }

  //  int QSGTextMaskMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGTextMaskMaterialCall2 call = reinterpret_cast<CuteQSGTextMaskMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGTextMaskMaterial::compare(other);
  }
};

//  QSGTextMaskMaterial::~QSGTextMaskMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGTextMaskMaterialD1Ev(QSGTextMaskMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGTextMaskMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK19QSGTextMaskMaterial4typeEv(
    const QSGTextMaskMaterial *self) {
  return self->type();
}

//  const QVector4D &QSGTextMaskMaterial::color() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK19QSGTextMaskMaterial5colorEv(
    const QSGTextMaskMaterial *self) {
  return new QVector4D(self->color());
}

//  QSGTexture *QSGTextMaskMaterial::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK19QSGTextMaskMaterial7textureEv(
    const QSGTextMaskMaterial *self) {
  return self->texture();
}

//  bool QSGTextMaskMaterial::ensureUpToDate()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSGTextMaskMaterial14ensureUpToDateEv(
    QSGTextMaskMaterial *self) {
  return self->ensureUpToDate();
}

//  QTextureGlyphCache *QSGTextMaskMaterial::glyphCache() const
extern "C" Q_DECL_EXPORT
QTextureGlyphCache *ritual_ZNK19QSGTextMaskMaterial10glyphCacheEv(
    const QSGTextMaskMaterial *self) {
  return self->glyphCache();
}

//  QSGRhiTextureGlyphCache *QSGTextMaskMaterial::rhiGlyphCache() const
extern "C" Q_DECL_EXPORT
QSGRhiTextureGlyphCache *ritual_ZNK19QSGTextMaskMaterial13rhiGlyphCacheEv(
    const QSGTextMaskMaterial *self) {
  return self->rhiGlyphCache();
}

//  a Python function taken by a CuteQSGTextMaskMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTextMaskMaterial(
    QSGTextMaskMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTextMaskMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGTextMaskMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK19QSGTextMaskMaterial4typeEv(
    const QSGTextMaskMaterial *self) {
  return self->QSGTextMaskMaterial::type();
}
