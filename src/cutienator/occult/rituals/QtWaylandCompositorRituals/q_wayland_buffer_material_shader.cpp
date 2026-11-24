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
#include <QtCore/qstring.h>
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

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 131, as _ZN28QWaylandBufferMaterialShader22setupExternalOESShaderERK7QString
#if QT_CONFIG(opengl)
inline void QWaylandBufferMaterialShader::setupExternalOESShader(const QString &shaderFilename)
{
#if QT_CONFIG(opengl)
    QFile shaderFile(shaderFilename);
    if (!shaderFile.open(QIODevice::ReadOnly)) {
        qCWarning(qLcWaylandCompositor) << "Cannot find external OES shader file:" << shaderFilename;
        return;
    }
    QByteArray FS = shaderFile.readAll();

    static const char *FS_GLES_PREAMBLE =
        "#extension GL_OES_EGL_image_external : require\n"
        "precision highp float;\n";
    static const char *FS_GL_PREAMBLE =
            "#version 120\n"
            "#extension GL_OES_EGL_image_external : require\n";
    QByteArray fsGLES = FS_GLES_PREAMBLE + FS;
    QByteArray fsGL = FS_GL_PREAMBLE + FS;

    QShaderDescription desc;
    QShaderDescriptionPrivate *descData = QShaderDescriptionPrivate::get(&desc);

    QShaderDescription::InOutVariable texCoordInput;
    texCoordInput.name = "v_texcoord";
    texCoordInput.type = QShaderDescription::Vec2;
    texCoordInput.location = 0;

    descData->inVars = { texCoordInput };

    QShaderDescription::InOutVariable fragColorOutput;
    fragColorOutput.name = "gl_FragColor";
    fragColorOutput.type = QShaderDescription::Vec4;
    fragColorOutput.location = 0;

    descData->outVars = { fragColorOutput };

    QShaderDescription::BlockVariable matrixBlockVar;
    matrixBlockVar.name = "qt_Matrix";
    matrixBlockVar.type = QShaderDescription::Mat4;
    matrixBlockVar.offset = 0;
    matrixBlockVar.size = 64;

    QShaderDescription::BlockVariable opacityBlockVar;
    opacityBlockVar.name = "qt_Opacity";
    opacityBlockVar.type = QShaderDescription::Float;
    opacityBlockVar.offset = 64;
    opacityBlockVar.size = 4;

    QShaderDescription::UniformBlock ubufStruct;
    ubufStruct.blockName = "buf";
    ubufStruct.structName = "ubuf";
    ubufStruct.size = 64 + 4;
    ubufStruct.binding = 0;
    ubufStruct.members = { matrixBlockVar, opacityBlockVar };

    descData->uniformBlocks = { ubufStruct };

    QShaderDescription::InOutVariable samplerTex0;
    samplerTex0.name = "tex0";
    samplerTex0.type = QShaderDescription::SamplerExternalOES;
    samplerTex0.binding = 1;

    descData->combinedImageSamplers = { samplerTex0 };

    QShader shaderPack;
    shaderPack.setStage(QShader::FragmentStage);
    shaderPack.setDescription(desc);
    shaderPack.setShader(QShaderKey(QShader::GlslShader, QShaderVersion(100, QShaderVersion::GlslEs)), QShaderCode(fsGLES));
    shaderPack.setShader(QShaderKey(QShader::GlslShader, QShaderVersion(120)), QShaderCode(fsGL));

    setShader(FragmentStage, shaderPack);
#else
    Q_UNUSED(shaderFilename);
#endif
}
#endif  // QT_CONFIG(opengl)
//  -----------------------------------------------------------------------

#if QT_CONFIG(opengl)
//  void QWaylandBufferMaterialShader::setupExternalOESShader(const QString
//      &shaderFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWaylandBufferMaterialShader22setupExternalOESShaderERK7QString(
    QWaylandBufferMaterialShader *self,
    const QString *shaderFilename) {
  self->setupExternalOESShader(*shaderFilename);
}
#endif  // QT_CONFIG(opengl)

#endif  // QT_CONFIG(opengl)
#endif  // QT_CONFIG(wayland_compositor_quick)
