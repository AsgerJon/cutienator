//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandquickitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/qwaylandquickitem.h>
#include <QtWaylandCompositor/private/qwaylandquickitem_p.h>
#include <QtWaylandCompositor/qwaylandquicksurface.h>
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#include <QtWaylandCompositor/qwaylandtextinput.h>
#include <QtWaylandCompositor/qwaylandtextinputv3.h>
#include <QtWaylandCompositor/qwaylandqttextinputmethod.h>
#include <QtWaylandCompositor/qwaylandquickoutput.h>
#include <QtWaylandCompositor/qwaylandcompositor.h>
#include <QtWaylandCompositor/qwaylandseat.h>
#include <QtWaylandCompositor/qwaylandbufferref.h>
#if QT_CONFIG(draganddrop)
#include <QtWaylandCompositor/QWaylandDrag>
#endif
#include <QtWaylandCompositor/private/qwlclientbufferintegration_p.h>
#if QT_CONFIG(opengl)
#  include <QtOpenGL/QOpenGLTexture>
#  include <QtGui/QOpenGLFunctions>
#endif
#include <QtGui/QKeyEvent>
#include <QtGui/QGuiApplication>
#include <QtGui/QScreen>
#include <QtQuick/QSGSimpleTextureNode>
#include <QtQuick/QQuickWindow>
#include <QtQuick/qsgtexture.h>
#include <QtCore/QFile>
#include <QtCore/QMutexLocker>
#include <QtCore/QMutex>
#include <wayland-server-core.h>
#include <QtCore/QThread>
#if QT_CONFIG(opengl)
#include <QtGui/private/qshaderdescription_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 261, as _ZN22QWaylandBufferMaterialD1Ev
#if QT_CONFIG(opengl)
inline QWaylandBufferMaterial::~QWaylandBufferMaterial()
{
    qDeleteAll(m_scenegraphTextures);
}
#endif  // QT_CONFIG(opengl)

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 315, as _ZNK22QWaylandBufferMaterial12createShaderEN20QSGRendererInterface10RenderModeE
#if QT_CONFIG(opengl)
inline QSGMaterialShader *QWaylandBufferMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QWaylandBufferMaterialShader(m_format);
}
#endif  // QT_CONFIG(opengl)

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 322, as _ZN22QWaylandBufferMaterial20setTextureParametersEj
#if QT_CONFIG(opengl)
inline void QWaylandBufferMaterial::setTextureParameters(GLenum target)
{
    QOpenGLFunctions *gl = QOpenGLContext::currentContext()->functions();
    gl->glTexParameteri(target, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    gl->glTexParameteri(target, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    gl->glTexParameteri(target, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    gl->glTexParameteri(target, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
}
#endif  // QT_CONFIG(opengl)

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 332, as _ZN22QWaylandBufferMaterial14ensureTexturesEi
#if QT_CONFIG(opengl)
inline void QWaylandBufferMaterial::ensureTextures(int count)
{
    for (int plane = m_textures.size(); plane < count; plane++) {
        m_textures << nullptr;
        m_scenegraphTextures << nullptr;
    }
}
#endif  // QT_CONFIG(opengl)
//  -----------------------------------------------------------------------

//  A QWaylandBufferMaterial that Python can take functions over in. Every QWaylandBufferMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(opengl)
typedef void * (*CuteQWaylandBufferMaterialCall0)(const void *, int *);
#endif  // QT_CONFIG(opengl)
#if QT_CONFIG(opengl)
typedef void * (*CuteQWaylandBufferMaterialCall1)(const void *, int, int *);
#endif  // QT_CONFIG(opengl)
typedef int (*CuteQWaylandBufferMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQWaylandBufferMaterial : public QWaylandBufferMaterial {
public:
  using QWaylandBufferMaterial::QWaylandBufferMaterial;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(opengl)
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(opengl)
#if QT_CONFIG(opengl)
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(opengl)
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(opengl)
  //  QSGMaterialType *QWaylandBufferMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandBufferMaterialCall0 call = reinterpret_cast<CuteQWaylandBufferMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QWaylandBufferMaterial::type();
  }
#endif  // QT_CONFIG(opengl)

#if QT_CONFIG(opengl)
  //  QSGMaterialShader *QWaylandBufferMaterial::createShader(QSGRendererIn
  //      terface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandBufferMaterialCall1 call = reinterpret_cast<CuteQWaylandBufferMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QWaylandBufferMaterial::createShader(renderMode);
  }
#endif  // QT_CONFIG(opengl)

  //  int QSGMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandBufferMaterialCall2 call = reinterpret_cast<CuteQWaylandBufferMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGMaterial::compare(other);
  }
};

//  QWaylandBufferMaterial::~QWaylandBufferMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandBufferMaterialD1Ev(QWaylandBufferMaterial *self) {
  delete self;
}

//  QSGMaterialShader
//      *QWaylandBufferMaterial::createShader(QSGRendererInterface::RenderMod
//      e renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK22QWaylandBufferMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QWaylandBufferMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

#if QT_CONFIG(opengl)
//  void QWaylandBufferMaterial::setTextureParameters(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandBufferMaterial20setTextureParametersEj(
    QWaylandBufferMaterial *self,
    GLenum target) {
  self->setTextureParameters(target);
}
#endif  // QT_CONFIG(opengl)

#if QT_CONFIG(opengl)
//  void QWaylandBufferMaterial::ensureTextures(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandBufferMaterial14ensureTexturesEi(
    QWaylandBufferMaterial *self,
    int count) {
  self->ensureTextures(count);
}
#endif  // QT_CONFIG(opengl)

//  a Python function taken by a CuteQWaylandBufferMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandBufferMaterial(
    QWaylandBufferMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandBufferMaterial *>(self)->take(key, call);
}

#endif  // QT_CONFIG(opengl)
#endif  // QT_CONFIG(wayland_compositor_quick)
