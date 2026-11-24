//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 323, as _ZN19QSGTextMaskMaterialD2Ev
inline QSGTextMaskMaterial::~QSGTextMaskMaterial()
{
    if (m_retainedFontEngine != nullptr)
        m_rc->unregisterFontengineForCleanup(m_retainedFontEngine);
    delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 579, as _ZN21QSGStyledTextMaterialC2EP16QSGRenderContextRK8QRawFont
inline QSGStyledTextMaterial::QSGStyledTextMaterial(QSGRenderContext *rc, const QRawFont &font)
    : QSGTextMaskMaterial(rc, QVector4D(), font, QFontEngine::Format_A8)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 616, as _ZNK23QSGOutlinedTextMaterial4typeEv
inline QSGMaterialType *QSGOutlinedTextMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}
//  -----------------------------------------------------------------------

//  A QSGOutlinedTextMaterial that Python can take functions over in. Every QSGOutlinedTextMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGOutlinedTextMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGOutlinedTextMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGOutlinedTextMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGOutlinedTextMaterial : public QSGOutlinedTextMaterial {
public:
  using QSGOutlinedTextMaterial::QSGOutlinedTextMaterial;
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

  //  QSGMaterialType *QSGOutlinedTextMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGOutlinedTextMaterialCall0 call = reinterpret_cast<CuteQSGOutlinedTextMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGOutlinedTextMaterial::type();
  }

  //  QSGMaterialShader *QSGOutlinedTextMaterial::createShader(QSGRendererI
  //      nterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGOutlinedTextMaterialCall1 call = reinterpret_cast<CuteQSGOutlinedTextMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGOutlinedTextMaterial::createShader(renderMode);
  }

  //  int QSGStyledTextMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGOutlinedTextMaterialCall2 call = reinterpret_cast<CuteQSGOutlinedTextMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGStyledTextMaterial::compare(other);
  }
};

//  QSGOutlinedTextMaterial::~QSGOutlinedTextMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGOutlinedTextMaterialD1Ev(QSGOutlinedTextMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGOutlinedTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK23QSGOutlinedTextMaterial4typeEv(
    const QSGOutlinedTextMaterial *self) {
  return self->type();
}

//  a Python function taken by a CuteQSGOutlinedTextMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGOutlinedTextMaterial(
    QSGOutlinedTextMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGOutlinedTextMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGOutlinedTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK23QSGOutlinedTextMaterial4typeEv(
    const QSGOutlinedTextMaterial *self) {
  return self->QSGOutlinedTextMaterial::type();
}
