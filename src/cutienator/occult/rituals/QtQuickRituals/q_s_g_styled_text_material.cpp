//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsgdefaultglyphnode_p_p.h"
#include <private/qsgmaterialshader_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <qpa/qplatformintegration.h>
#include <private/qfontengine_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <private/qrawfont_p.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 313, as _ZN19QSGTextMaskMaterialC2EP16QSGRenderContextRK9QVector4DRK8QRawFontN11QFontEngine11GlyphFormatE
inline QSGTextMaskMaterial::QSGTextMaskMaterial(QSGRenderContext *rc, const QVector4D &color, const QRawFont &font, QFontEngine::GlyphFormat glyphFormat)
    : m_rc(qobject_cast<QSGDefaultRenderContext *>(rc))
    , m_texture(nullptr)
    , m_glyphCache(nullptr)
    , m_font(font)
    , m_color(color)
{
    init(glyphFormat);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 323, as _ZN19QSGTextMaskMaterialD2Ev
inline QSGTextMaskMaterial::~QSGTextMaskMaterial()
{
    if (m_retainedFontEngine != nullptr)
        m_rc->unregisterFontengineForCleanup(m_retainedFontEngine);
    delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 584, as _ZNK21QSGStyledTextMaterial4typeEv
inline QSGMaterialType *QSGStyledTextMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}
//  -----------------------------------------------------------------------

//  A QSGStyledTextMaterial that Python can take functions over in. Every QSGStyledTextMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGStyledTextMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGStyledTextMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGStyledTextMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGStyledTextMaterial : public QSGStyledTextMaterial {
public:
  using QSGStyledTextMaterial::QSGStyledTextMaterial;
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

  //  QSGMaterialType *QSGStyledTextMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGStyledTextMaterialCall0 call = reinterpret_cast<CuteQSGStyledTextMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGStyledTextMaterial::type();
  }

  //  QSGMaterialShader
  //      *QSGStyledTextMaterial::createShader(QSGRendererInterface::Render
  //      Mode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGStyledTextMaterialCall1 call = reinterpret_cast<CuteQSGStyledTextMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGStyledTextMaterial::createShader(renderMode);
  }

  //  int QSGStyledTextMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGStyledTextMaterialCall2 call = reinterpret_cast<CuteQSGStyledTextMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGStyledTextMaterial::compare(other);
  }
};

//  QSGStyledTextMaterial::~QSGStyledTextMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGStyledTextMaterialD1Ev(QSGStyledTextMaterial *self) {
  delete self;
}

//  void QSGStyledTextMaterial::setStyleShift(const QVector2D &shift)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGStyledTextMaterial13setStyleShiftERK9QVector2D(
    QSGStyledTextMaterial *self,
    const QVector2D *shift) {
  self->setStyleShift(*shift);
}

//  const QVector2D &QSGStyledTextMaterial::styleShift() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK21QSGStyledTextMaterial10styleShiftEv(
    const QSGStyledTextMaterial *self) {
  return new QVector2D(self->styleShift());
}

//  void QSGStyledTextMaterial::setStyleColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGStyledTextMaterial13setStyleColorERK6QColor(
    QSGStyledTextMaterial *self,
    const QColor *c) {
  self->setStyleColor(*c);
}

//  void QSGStyledTextMaterial::setStyleColor(const QVector4D &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGStyledTextMaterial13setStyleColorERK9QVector4D(
    QSGStyledTextMaterial *self,
    const QVector4D *color) {
  self->setStyleColor(*color);
}

//  const QVector4D &QSGStyledTextMaterial::styleColor() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK21QSGStyledTextMaterial10styleColorEv(
    const QSGStyledTextMaterial *self) {
  return new QVector4D(self->styleColor());
}

//  QSGMaterialType *QSGStyledTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK21QSGStyledTextMaterial4typeEv(
    const QSGStyledTextMaterial *self) {
  return self->type();
}

//  a Python function taken by a CuteQSGStyledTextMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGStyledTextMaterial(
    QSGStyledTextMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGStyledTextMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGStyledTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK21QSGStyledTextMaterial4typeEv(
    const QSGStyledTextMaterial *self) {
  return self->QSGStyledTextMaterial::type();
}
