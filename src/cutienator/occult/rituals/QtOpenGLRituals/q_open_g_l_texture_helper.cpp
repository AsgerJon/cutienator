//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturehelper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_OPENGL)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturehelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/qopenglpixeltransferoptions.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/private/qopengltexturehelper_p.h>
#include <QtGui/QOpenGLContext>
#include <QtGui/private/qopenglextensions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopengltexturehelper.cpp, line 371, as local:qopengltexturehelper.cpp:TextureBinder
namespace {
class TextureBinder
{
public:
    TextureBinder(QOpenGLFunctions *functions, GLuint texture, GLenum target, GLenum bindingTarget)
    : m_functions(functions)
    {
        // For cubemaps we can't use the standard DSA emulation as it is illegal to
        // try to bind a texture to one of the cubemap face targets. So we force the
        // target and binding target to the cubemap values in this case.
        switch (target) {
        case GL_TEXTURE_CUBE_MAP_NEGATIVE_X:
        case GL_TEXTURE_CUBE_MAP_POSITIVE_X:
        case GL_TEXTURE_CUBE_MAP_NEGATIVE_Y:
        case GL_TEXTURE_CUBE_MAP_POSITIVE_Y:
        case GL_TEXTURE_CUBE_MAP_NEGATIVE_Z:
        case GL_TEXTURE_CUBE_MAP_POSITIVE_Z:
            bindingTarget = GL_TEXTURE_BINDING_CUBE_MAP;
            m_target = GL_TEXTURE_CUBE_MAP;
            break;

        default:
            m_target = target;
            break;
        }

        m_functions->glGetIntegerv(bindingTarget, &m_oldTexture);
        m_functions->glBindTexture(m_target, texture);
    }

    ~TextureBinder()
    {
        m_functions->glBindTexture(m_target, m_oldTexture);
    }

private:
    QOpenGLFunctions *m_functions;
    GLenum m_target;
    GLint m_oldTexture;
};
}  // namespace

//  from src/opengl/qopengltexturehelper.cpp, line 485, as _ZN20QOpenGLTextureHelper17qt_TextureImage1DEjjjijiijjPKv
inline void QOpenGLTextureHelper::qt_TextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexImage1D(target, level, internalFormat, width, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 479, as _ZN20QOpenGLTextureHelper17qt_TextureImage2DEjjjijiiijjPKv
inline void QOpenGLTextureHelper::qt_TextureImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    functions->glTexImage2D(target, level, internalFormat, width, height, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 473, as _ZN20QOpenGLTextureHelper17qt_TextureImage3DEjjjijiiiijjPKv
inline void QOpenGLTextureHelper::qt_TextureImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexImage3D(target, level, internalFormat, width, height, depth, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 455, as _ZN20QOpenGLTextureHelper19qt_TextureStorage1DEjjjiji
inline void QOpenGLTextureHelper::qt_TextureStorage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexStorage1D(target, levels, internalFormat, width);
}

//  from src/opengl/qopengltexturehelper.cpp, line 449, as _ZN20QOpenGLTextureHelper19qt_TextureStorage2DEjjjijii
inline void QOpenGLTextureHelper::qt_TextureStorage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexStorage2D(target, levels, internalFormat, width, height);
}

//  from src/opengl/qopengltexturehelper.cpp, line 443, as _ZN20QOpenGLTextureHelper19qt_TextureStorage3DEjjjijiii
inline void QOpenGLTextureHelper::qt_TextureStorage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexStorage3D(target, levels, internalFormat, width, height, depth);
}

//  from src/opengl/qopengltexturehelper.cpp, line 425, as _ZN20QOpenGLTextureHelper20qt_TextureParameterfEjjjjf
inline void QOpenGLTextureHelper::qt_TextureParameterf(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLfloat param)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    functions->glTexParameterf(target, pname, param);
}

//  from src/opengl/qopengltexturehelper.cpp, line 503, as _ZN20QOpenGLTextureHelper20qt_TextureSubImage1DEjjjiiijjPKv
inline void QOpenGLTextureHelper::qt_TextureSubImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 497, as _ZN20QOpenGLTextureHelper20qt_TextureSubImage2DEjjjiiiiijjPKv
inline void QOpenGLTextureHelper::qt_TextureSubImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    functions->glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 491, as _ZN20QOpenGLTextureHelper20qt_TextureSubImage3DEjjjiiiiiiijjPKv
inline void QOpenGLTextureHelper::qt_TextureSubImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 431, as _ZN20QOpenGLTextureHelper21qt_TextureParameterfvEjjjjPKf
inline void QOpenGLTextureHelper::qt_TextureParameterfv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat *params)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    functions->glTexParameterfv(target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 419, as _ZN20QOpenGLTextureHelper21qt_TextureParameterivEjjjjPKi
inline void QOpenGLTextureHelper::qt_TextureParameteriv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    functions->glTexParameteriv(target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 437, as _ZN20QOpenGLTextureHelper24qt_GenerateTextureMipmapEjjj
inline void QOpenGLTextureHelper::qt_GenerateTextureMipmap(GLuint texture, GLenum target, GLenum bindingTarget)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    functions->glGenerateMipmap(target);
}

//  from src/opengl/qopengltexturehelper.cpp, line 539, as _ZN20QOpenGLTextureHelper27qt_CompressedTextureImage1DEjjjijiiiPKv
inline void QOpenGLTextureHelper::qt_CompressedTextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glCompressedTexImage1D(target, level, internalFormat, width, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 545, as _ZN20QOpenGLTextureHelper27qt_CompressedTextureImage2DEjjjijiiiiPKv
inline void QOpenGLTextureHelper::qt_CompressedTextureImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glCompressedTexImage2D(target, level, internalFormat, width, height, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 551, as _ZN20QOpenGLTextureHelper27qt_CompressedTextureImage3DEjjjijiiiiiPKv
inline void QOpenGLTextureHelper::qt_CompressedTextureImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glCompressedTexImage3D(target, level, internalFormat, width, height, depth, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 515, as _ZN20QOpenGLTextureHelper28qt_TextureImage2DMultisampleEjjjiiiih
inline void QOpenGLTextureHelper::qt_TextureImage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexImage2DMultisample(target, samples, internalFormat, width, height, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 509, as _ZN20QOpenGLTextureHelper28qt_TextureImage3DMultisampleEjjjiiiiih
inline void QOpenGLTextureHelper::qt_TextureImage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexImage3DMultisample(target, samples, internalFormat, width, height, depth, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 521, as _ZN20QOpenGLTextureHelper30qt_CompressedTextureSubImage1DEjjjiiijiPKv
inline void QOpenGLTextureHelper::qt_CompressedTextureSubImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 527, as _ZN20QOpenGLTextureHelper30qt_CompressedTextureSubImage2DEjjjiiiiijiPKv
inline void QOpenGLTextureHelper::qt_CompressedTextureSubImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 533, as _ZN20QOpenGLTextureHelper30qt_CompressedTextureSubImage3DEjjjiiiiiiijiPKv
inline void QOpenGLTextureHelper::qt_CompressedTextureSubImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 467, as _ZN20QOpenGLTextureHelper30qt_TextureStorage2DMultisampleEjjjijiih
inline void QOpenGLTextureHelper::qt_TextureStorage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexStorage2DMultisample(target, samples, internalFormat, width, height, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 461, as _ZN20QOpenGLTextureHelper30qt_TextureStorage3DMultisampleEjjjijiiih
inline void QOpenGLTextureHelper::qt_TextureStorage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexStorage3DMultisample(target, samples, internalFormat, width, height, depth, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 12, as _ZN20QOpenGLTextureHelperC1EP14QOpenGLContext
inline QOpenGLTextureHelper::QOpenGLTextureHelper(QOpenGLContext *context)
{
    functions = context->functions();
    // Resolve EXT_direct_state_access entry points if present.

    // However, disable it on some systems where DSA is known to be unreliable.
    bool allowDSA = true;
    const char *renderer = reinterpret_cast<const char *>(context->functions()->glGetString(GL_RENDERER));
    const char *version =
            reinterpret_cast<const char *>(context->functions()->glGetString(GL_VERSION));
    // QTBUG-40653, QTBUG-44988
    if (renderer && strstr(renderer, "AMD Radeon HD"))
        allowDSA = false;
    // QTBUG-147866: EXT_direct_state_access texture storage is broken on Mesa
    if (version && strstr(version, "Mesa"))
        allowDSA = false;

    if (allowDSA && !context->isOpenGLES()
        && context->hasExtension(QByteArrayLiteral("GL_EXT_direct_state_access"))) {
        TextureParameteriEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLenum , GLint )>(context->getProcAddress("glTextureParameteriEXT"));
        TextureParameterivEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLenum , const GLint *)>(context->getProcAddress("glTextureParameterivEXT"));
        TextureParameterfEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLenum , GLfloat )>(context->getProcAddress("glTextureParameterfEXT"));
        TextureParameterfvEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLenum , const GLfloat *)>(context->getProcAddress("glTextureParameterfvEXT"));
        GenerateTextureMipmapEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum )>(context->getProcAddress("glGenerateTextureMipmapEXT"));
        TextureStorage3DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLsizei , GLenum , GLsizei , GLsizei , GLsizei )>(context->getProcAddress("glTextureStorage3DEXT"));
        TextureStorage2DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLsizei , GLenum , GLsizei , GLsizei )>(context->getProcAddress("glTextureStorage2DEXT"));
        TextureStorage1DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLsizei , GLenum , GLsizei )>(context->getProcAddress("glTextureStorage1DEXT"));
        TextureStorage3DMultisampleEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLsizei , GLenum , GLsizei , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTextureStorage3DMultisampleEXT"));
        TextureStorage2DMultisampleEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLsizei , GLenum , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTextureStorage2DMultisampleEXT"));
        TextureImage3DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLenum , GLsizei , GLsizei , GLsizei , GLint , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTextureImage3DEXT"));
        TextureImage2DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLenum , GLsizei , GLsizei , GLint , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTextureImage2DEXT"));
        TextureImage1DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLenum , GLsizei , GLint , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTextureImage1DEXT"));
        TextureSubImage3DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLint , GLint , GLint , GLsizei , GLsizei , GLsizei , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTextureSubImage3DEXT"));
        TextureSubImage2DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLint , GLint , GLsizei , GLsizei , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTextureSubImage2DEXT"));
        TextureSubImage1DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLint , GLsizei , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTextureSubImage1DEXT"));
        CompressedTextureSubImage1DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLint , GLsizei , GLenum , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTextureSubImage1DEXT"));
        CompressedTextureSubImage2DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLint , GLint , GLsizei , GLsizei , GLenum , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTextureSubImage2DEXT"));
        CompressedTextureSubImage3DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLint , GLint , GLint , GLsizei , GLsizei , GLsizei , GLenum , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTextureSubImage3DEXT"));
        CompressedTextureImage1DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLenum , GLsizei , GLint , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTextureImage1DEXT"));
        CompressedTextureImage2DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLenum , GLsizei , GLsizei , GLint , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTextureImage2DEXT"));
        CompressedTextureImage3DEXT = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLint , GLenum , GLsizei , GLsizei , GLsizei , GLint , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTextureImage3DEXT"));

        // Use the real DSA functions
        TextureParameteri = &QOpenGLTextureHelper::dsa_TextureParameteri;
        TextureParameteriv = &QOpenGLTextureHelper::dsa_TextureParameteriv;
        TextureParameterf = &QOpenGLTextureHelper::dsa_TextureParameterf;
        TextureParameterfv = &QOpenGLTextureHelper::dsa_TextureParameterfv;
        GenerateTextureMipmap = &QOpenGLTextureHelper::dsa_GenerateTextureMipmap;
        TextureStorage3D = &QOpenGLTextureHelper::dsa_TextureStorage3D;
        TextureStorage2D = &QOpenGLTextureHelper::dsa_TextureStorage2D;
        TextureStorage1D = &QOpenGLTextureHelper::dsa_TextureStorage1D;
        TextureStorage3DMultisample = &QOpenGLTextureHelper::dsa_TextureStorage3DMultisample;
        TextureStorage2DMultisample = &QOpenGLTextureHelper::dsa_TextureStorage2DMultisample;
        TextureImage3D = &QOpenGLTextureHelper::dsa_TextureImage3D;
        TextureImage2D = &QOpenGLTextureHelper::dsa_TextureImage2D;
        TextureImage1D = &QOpenGLTextureHelper::dsa_TextureImage1D;
        TextureSubImage3D = &QOpenGLTextureHelper::dsa_TextureSubImage3D;
        TextureSubImage2D = &QOpenGLTextureHelper::dsa_TextureSubImage2D;
        TextureSubImage1D = &QOpenGLTextureHelper::dsa_TextureSubImage1D;
        CompressedTextureSubImage1D = &QOpenGLTextureHelper::dsa_CompressedTextureSubImage1D;
        CompressedTextureSubImage2D = &QOpenGLTextureHelper::dsa_CompressedTextureSubImage2D;
        CompressedTextureSubImage3D = &QOpenGLTextureHelper::dsa_CompressedTextureSubImage3D;
        CompressedTextureImage1D = &QOpenGLTextureHelper::dsa_CompressedTextureImage1D;
        CompressedTextureImage2D = &QOpenGLTextureHelper::dsa_CompressedTextureImage2D;
        CompressedTextureImage3D = &QOpenGLTextureHelper::dsa_CompressedTextureImage3D;
    } else {
        // Use our own DSA emulation
        TextureParameteri = &QOpenGLTextureHelper::qt_TextureParameteri;
        TextureParameteriv = &QOpenGLTextureHelper::qt_TextureParameteriv;
        TextureParameterf = &QOpenGLTextureHelper::qt_TextureParameterf;
        TextureParameterfv = &QOpenGLTextureHelper::qt_TextureParameterfv;
        GenerateTextureMipmap = &QOpenGLTextureHelper::qt_GenerateTextureMipmap;
        TextureStorage3D = &QOpenGLTextureHelper::qt_TextureStorage3D;
        TextureStorage2D = &QOpenGLTextureHelper::qt_TextureStorage2D;
        TextureStorage1D = &QOpenGLTextureHelper::qt_TextureStorage1D;
        TextureStorage3DMultisample = &QOpenGLTextureHelper::qt_TextureStorage3DMultisample;
        TextureStorage2DMultisample = &QOpenGLTextureHelper::qt_TextureStorage2DMultisample;
        TextureImage3D = &QOpenGLTextureHelper::qt_TextureImage3D;
        TextureImage2D = &QOpenGLTextureHelper::qt_TextureImage2D;
        TextureImage1D = &QOpenGLTextureHelper::qt_TextureImage1D;
        TextureSubImage3D = &QOpenGLTextureHelper::qt_TextureSubImage3D;
        TextureSubImage2D = &QOpenGLTextureHelper::qt_TextureSubImage2D;
        TextureSubImage1D = &QOpenGLTextureHelper::qt_TextureSubImage1D;
        CompressedTextureSubImage1D = &QOpenGLTextureHelper::qt_CompressedTextureSubImage1D;
        CompressedTextureSubImage2D = &QOpenGLTextureHelper::qt_CompressedTextureSubImage2D;
        CompressedTextureSubImage3D = &QOpenGLTextureHelper::qt_CompressedTextureSubImage3D;
        CompressedTextureImage1D = &QOpenGLTextureHelper::qt_CompressedTextureImage1D;
        CompressedTextureImage2D = &QOpenGLTextureHelper::qt_CompressedTextureImage2D;
        CompressedTextureImage3D = &QOpenGLTextureHelper::qt_CompressedTextureImage3D;
    }

    // Some DSA functions are part of NV_texture_multisample instead
    if (!context->isOpenGLES()
        && context->hasExtension(QByteArrayLiteral("GL_NV_texture_multisample"))) {
        TextureImage3DMultisampleNV = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLsizei , GLint , GLsizei , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTextureImage3DMultisampleNV"));
        TextureImage2DMultisampleNV = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLsizei , GLint , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTextureImage2DMultisampleNV"));

        TextureImage3DMultisample = &QOpenGLTextureHelper::dsa_TextureImage3DMultisample;
        TextureImage2DMultisample = &QOpenGLTextureHelper::dsa_TextureImage2DMultisample;
    } else {
        TextureImage3DMultisample = &QOpenGLTextureHelper::qt_TextureImage3DMultisample;
        TextureImage2DMultisample = &QOpenGLTextureHelper::qt_TextureImage2DMultisample;
    }

#if QT_CONFIG(opengles2)
    // Here we are targeting OpenGL ES 2.0+ only. This is likely using EGL, where,
    // similarly to WGL, non-extension functions (i.e. any function that is part of the
    // GLES spec) *may* not be queried via eglGetProcAddress.
    QOpenGLExtraFunctionsPrivate *extra = static_cast<QOpenGLExtensions *>(context->extraFunctions())->d();
    QOpenGLFunctionsPrivate *base = extra; // ES 2 core entry points live on the base

    // OpenGL 1.0
    TexImage1D = 0;

    // OpenGL 1.1
    TexSubImage1D = 0;

    // OpenGL 1.3
    GetCompressedTexImage = 0;
    CompressedTexSubImage1D = 0;
    CompressedTexSubImage2D = base->f.CompressedTexSubImage2D ? base->f.CompressedTexSubImage2D : ::glCompressedTexSubImage2D;
    CompressedTexImage1D = 0;
    CompressedTexImage2D = base->f.CompressedTexImage2D ? base->f.CompressedTexImage2D : ::glCompressedTexImage2D;
    ActiveTexture = base->f.ActiveTexture ? base->f.ActiveTexture : ::glActiveTexture;

    // OpenGL 3.0
    GenerateMipmap = base->f.GenerateMipmap ? base->f.GenerateMipmap : ::glGenerateMipmap;

    // OpenGL 3.2
    TexImage3DMultisample = 0;
    TexImage2DMultisample = 0;

    // OpenGL 4.2
    QOpenGLContext *ctx = QOpenGLContext::currentContext();
    if (ctx->format().majorVersion() >= 3) {
        // OpenGL ES 3.0+ has immutable storage for 2D and 3D at least.
        TexStorage3D = extra->f.TexStorage3D;
        TexStorage2D = extra->f.TexStorage2D;
    } else {
        TexStorage3D = 0;
        TexStorage2D = 0;
    }
    TexStorage1D = 0;

    // OpenGL 4.3
    TexStorage3DMultisample = 0;
    TexStorage2DMultisample = 0;
    TexBufferRange = 0;
    TextureView = 0;

    // OpenGL ES 3.1+ has TexStorage2DMultisample
    if (ctx->format().version() >= std::pair(3, 1))
        TexStorage2DMultisample = extra->f.TexStorage2DMultisample;
#endif

    if (context->isOpenGLES() && context->hasExtension(QByteArrayLiteral("GL_OES_texture_3D"))) {
        TexImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, const GLvoid*)>(context->getProcAddress("glTexImage3DOES"));
        TexSubImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, const GLvoid*)>(context->getProcAddress("glTexSubImage3DOES"));
        CompressedTexImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, const GLvoid*)>(context->getProcAddress("glCompressedTexImage3DOES"));
        CompressedTexSubImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, const GLvoid*)>(context->getProcAddress("glCompressedTexSubImage3DOES"));
    } else {
        QOpenGLContext *ctx = QOpenGLContext::currentContext();
        if (ctx->isOpenGLES() && ctx->format().majorVersion() >= 3) {
            // OpenGL ES 3.0+ has glTexImage3D.
            QOpenGLExtraFunctionsPrivate *extra = static_cast<QOpenGLExtensions *>(context->extraFunctions())->d();
            TexImage3D = extra->f.TexImage3D;
            TexSubImage3D = extra->f.TexSubImage3D;
            CompressedTexImage3D = extra->f.CompressedTexImage3D;
            CompressedTexSubImage3D = extra->f.CompressedTexSubImage3D;
        } else {
            // OpenGL 1.2
            TexImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLint , GLsizei , GLsizei , GLsizei , GLint , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTexImage3D"));
            TexSubImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLint , GLint , GLint , GLsizei , GLsizei , GLsizei , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTexSubImage3D"));

            // OpenGL 1.3
            CompressedTexImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLenum , GLsizei , GLsizei , GLsizei , GLint , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTexImage3D"));
            CompressedTexSubImage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLint , GLint , GLint , GLsizei , GLsizei , GLsizei , GLenum , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTexSubImage3D"));
        }
    }

#if !QT_CONFIG(opengles2)
    // OpenGL 1.0 and 1.1
    TexImage1D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLint , GLsizei , GLint , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTexImage1D"));
    TexSubImage1D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLint , GLsizei , GLenum , GLenum , const GLvoid *)>(context->getProcAddress("glTexSubImage1D"));\

    // OpenGL 1.3
    GetCompressedTexImage = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLvoid *)>(context->getProcAddress("glGetCompressedTexImage"));
    CompressedTexSubImage1D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLint , GLsizei , GLenum , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTexSubImage1D"));
    CompressedTexSubImage2D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLint , GLint , GLsizei , GLsizei , GLenum , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTexSubImage2D"));
    CompressedTexImage1D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLenum , GLsizei , GLint , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTexImage1D"));
    CompressedTexImage2D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLint , GLenum , GLsizei , GLsizei , GLint , GLsizei , const GLvoid *)>(context->getProcAddress("glCompressedTexImage2D"));
    ActiveTexture = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum )>(context->getProcAddress("glActiveTexture"));

    // OpenGL 3.0
    GenerateMipmap = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum )>(context->getProcAddress("glGenerateMipmap"));

    // OpenGL 3.2
    TexImage3DMultisample = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLsizei , GLint , GLsizei , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTexImage3DMultisample"));
    TexImage2DMultisample = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLsizei , GLint , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTexImage2DMultisample"));

    // OpenGL 4.2
    TexStorage3D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLsizei , GLenum , GLsizei , GLsizei , GLsizei )>(context->getProcAddress("glTexStorage3D"));
    TexStorage2D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLsizei , GLenum , GLsizei , GLsizei )>(context->getProcAddress("glTexStorage2D"));
    TexStorage1D = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLsizei , GLenum , GLsizei )>(context->getProcAddress("glTexStorage1D"));

    // OpenGL 4.3
    TexStorage3DMultisample = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLsizei , GLenum , GLsizei , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTexStorage3DMultisample"));
    TexStorage2DMultisample = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLsizei , GLenum , GLsizei , GLsizei , GLboolean )>(context->getProcAddress("glTexStorage2DMultisample"));
    TexBufferRange = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLenum , GLenum , GLuint , GLintptr , GLsizeiptr )>(context->getProcAddress("glTexBufferRange"));
    TextureView = reinterpret_cast<void (QOPENGLF_APIENTRYP)(GLuint , GLenum , GLuint , GLenum , GLuint , GLuint , GLuint , GLuint )>(context->getProcAddress("glTextureView"));
#endif
}

//  from src/opengl/qopengltexturehelper.cpp, line 225, as _ZN20QOpenGLTextureHelper21dsa_TextureParameteriEjjjji
inline void QOpenGLTextureHelper::dsa_TextureParameteri(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLint param)
{
    Q_UNUSED(bindingTarget);
    TextureParameteriEXT(texture, target, pname, param);
}

//  from src/opengl/qopengltexturehelper.cpp, line 231, as _ZN20QOpenGLTextureHelper22dsa_TextureParameterivEjjjjPKi
inline void QOpenGLTextureHelper::dsa_TextureParameteriv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)
{
    Q_UNUSED(bindingTarget);
    TextureParameterivEXT(texture, target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 237, as _ZN20QOpenGLTextureHelper21dsa_TextureParameterfEjjjjf
inline void QOpenGLTextureHelper::dsa_TextureParameterf(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLfloat param)
{
    Q_UNUSED(bindingTarget);
    TextureParameterfEXT(texture, target, pname, param);
}

//  from src/opengl/qopengltexturehelper.cpp, line 243, as _ZN20QOpenGLTextureHelper22dsa_TextureParameterfvEjjjjPKf
inline void QOpenGLTextureHelper::dsa_TextureParameterfv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat *params)
{
    Q_UNUSED(bindingTarget);
    TextureParameterfvEXT(texture, target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 249, as _ZN20QOpenGLTextureHelper25dsa_GenerateTextureMipmapEjjj
inline void QOpenGLTextureHelper::dsa_GenerateTextureMipmap(GLuint texture, GLenum target, GLenum bindingTarget)
{
    Q_UNUSED(bindingTarget);
    GenerateTextureMipmapEXT(texture, target);
}

//  from src/opengl/qopengltexturehelper.cpp, line 255, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage3DEjjjijiii
inline void QOpenGLTextureHelper::dsa_TextureStorage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth)
{
    Q_UNUSED(bindingTarget);
    TextureStorage3DEXT(texture, target, levels, internalFormat, width, height, depth);
}

//  from src/opengl/qopengltexturehelper.cpp, line 261, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage2DEjjjijii
inline void QOpenGLTextureHelper::dsa_TextureStorage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height)
{
    Q_UNUSED(bindingTarget);
    TextureStorage2DEXT(texture, target, levels, internalFormat, width, height);
}

//  from src/opengl/qopengltexturehelper.cpp, line 267, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage1DEjjjiji
inline void QOpenGLTextureHelper::dsa_TextureStorage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width)
{
    Q_UNUSED(bindingTarget);
    TextureStorage1DEXT(texture, target, levels, internalFormat, width);
}

//  from src/opengl/qopengltexturehelper.cpp, line 273, as _ZN20QOpenGLTextureHelper31dsa_TextureStorage3DMultisampleEjjjijiiih
inline void QOpenGLTextureHelper::dsa_TextureStorage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureStorage3DMultisampleEXT(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 279, as _ZN20QOpenGLTextureHelper31dsa_TextureStorage2DMultisampleEjjjijiih
inline void QOpenGLTextureHelper::dsa_TextureStorage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureStorage2DMultisampleEXT(texture, target, samples, internalFormat, width, height, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 285, as _ZN20QOpenGLTextureHelper18dsa_TextureImage3DEjjjijiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage3DEXT(texture, target, level, internalFormat, width, height, depth, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 291, as _ZN20QOpenGLTextureHelper18dsa_TextureImage2DEjjjijiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage2DEXT(texture, target, level, internalFormat, width, height, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 297, as _ZN20QOpenGLTextureHelper18dsa_TextureImage1DEjjjijiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage1DEXT(texture, target, level, internalFormat, width, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 303, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage3DEjjjiiiiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 309, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage2DEjjjiiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 315, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage1DEjjjiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage1DEXT(texture, target, level, xoffset, width, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 321, as _ZN20QOpenGLTextureHelper29dsa_TextureImage3DMultisampleEjjjiiiiih
inline void QOpenGLTextureHelper::dsa_TextureImage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureImage3DMultisampleNV(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 327, as _ZN20QOpenGLTextureHelper29dsa_TextureImage2DMultisampleEjjjiiiih
inline void QOpenGLTextureHelper::dsa_TextureImage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureImage2DMultisampleNV(texture, target, samples, internalFormat, width, height, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 333, as _ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage1DEjjjiiijiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureSubImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureSubImage1DEXT(texture, target, level, xoffset, width, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 339, as _ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage2DEjjjiiiiijiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureSubImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 345, as _ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage3DEjjjiiiiiiijiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureSubImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 351, as _ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage1DEjjjijiiiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureImage1DEXT(texture, target, level, internalFormat, width, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 357, as _ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage2DEjjjijiiiiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureImage2DEXT(texture, target, level, internalFormat, width, height, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 363, as _ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage3DEjjjijiiiiiPKv
inline void QOpenGLTextureHelper::dsa_CompressedTextureImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *bits)
{
    Q_UNUSED(bindingTarget);
    CompressedTextureImage3DEXT(texture, target, level, internalFormat, width, height, depth, border, imageSize, bits);
}

//  from src/opengl/qopengltexturehelper.cpp, line 413, as _ZN20QOpenGLTextureHelper20qt_TextureParameteriEjjjji
inline void QOpenGLTextureHelper::qt_TextureParameteri(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLint param)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    functions->glTexParameteri(target, pname, param);
}
//  -----------------------------------------------------------------------

//  QOpenGLTextureHelper::QOpenGLTextureHelper(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLTextureHelper *ritual_ZN20QOpenGLTextureHelperC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLTextureHelper(context);
}

//  void QOpenGLTextureHelper::glTextureParameteri(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper19glTextureParameteriEjjjji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLint param) {
  self->glTextureParameteri(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::glTextureParameteriv(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20glTextureParameterivEjjjjPKi(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    const GLint *params) {
  self->glTextureParameteriv(texture, target, bindingTarget, pname, params);
}

//  void QOpenGLTextureHelper::glTextureParameterf(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper19glTextureParameterfEjjjjf(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLfloat param) {
  self->glTextureParameterf(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::glTextureParameterfv(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20glTextureParameterfvEjjjjPKf(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    const GLfloat *params) {
  self->glTextureParameterfv(texture, target, bindingTarget, pname, params);
}

//  void QOpenGLTextureHelper::glGenerateTextureMipmap(GLuint texture, GLenum
//      target, GLenum bindingTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper23glGenerateTextureMipmapEjjj(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget) {
  self->glGenerateTextureMipmap(texture, target, bindingTarget);
}

//  void QOpenGLTextureHelper::glTextureStorage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18glTextureStorage3DEjjjijiii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glTextureStorage3D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height,
      depth);
}

//  void QOpenGLTextureHelper::glTextureStorage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18glTextureStorage2DEjjjijii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height) {
  self->glTextureStorage2D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height);
}

//  void QOpenGLTextureHelper::glTextureStorage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18glTextureStorage1DEjjjiji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width) {
  self->glTextureStorage1D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width);
}

//  void QOpenGLTextureHelper::glTextureStorage3DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29glTextureStorage3DMultisampleEjjjijiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTextureStorage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTextureStorage2DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29glTextureStorage2DMultisampleEjjjijiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTextureStorage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTextureImage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper16glTextureImage3DEjjjijiiiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTextureImage3D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      depth,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::glTextureImage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper16glTextureImage2DEjjjijiiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTextureImage2D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::glTextureImage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLenum internalFormat,
//      GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper16glTextureImage1DEjjjijiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTextureImage1D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::glTextureSubImage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
//      yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth,
//      GLenum format, GLenum type, const GLvoid *pixels, const
//      QOpenGLPixelTransferOptions *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper19glTextureSubImage3DEjjjiiiiiiijjPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLenum type,
    const GLvoid *pixels,
    const QOpenGLPixelTransferOptions *const options) {
  self->glTextureSubImage3D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      type,
      pixels,
      options);
}

//  void QOpenGLTextureHelper::glTextureSubImage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
//      yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type,
//      const GLvoid *pixels, const QOpenGLPixelTransferOptions *const
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper19glTextureSubImage2DEjjjiiiiijjPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels,
    const QOpenGLPixelTransferOptions *const options) {
  self->glTextureSubImage2D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      width,
      height,
      format,
      type,
      pixels,
      options);
}

//  void QOpenGLTextureHelper::glTextureSubImage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei
//      width, GLenum format, GLenum type, const GLvoid *pixels, const
//      QOpenGLPixelTransferOptions *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper19glTextureSubImage1DEjjjiiijjPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels,
    const QOpenGLPixelTransferOptions *const options) {
  self->glTextureSubImage1D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      width,
      format,
      type,
      pixels,
      options);
}

//  void QOpenGLTextureHelper::glTextureImage3DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper27glTextureImage3DMultisampleEjjjiiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTextureImage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTextureImage2DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper27glTextureImage2DMultisampleEjjjiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTextureImage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glCompressedTextureSubImage1D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
//      GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits,
//      const QOpenGLPixelTransferOptions *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29glCompressedTextureSubImage1DEjjjiiijiPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options) {
  self->glCompressedTextureSubImage1D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      width,
      format,
      imageSize,
      bits,
      options);
}

//  void QOpenGLTextureHelper::glCompressedTextureSubImage2D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
//      GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei
//      imageSize, const GLvoid *bits, const QOpenGLPixelTransferOptions
//      *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29glCompressedTextureSubImage2DEjjjiiiiijiPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options) {
  self->glCompressedTextureSubImage2D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      width,
      height,
      format,
      imageSize,
      bits,
      options);
}

//  void QOpenGLTextureHelper::glCompressedTextureSubImage3D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
//      GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei
//      depth, GLenum format, GLsizei imageSize, const GLvoid *bits, const
//      QOpenGLPixelTransferOptions *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29glCompressedTextureSubImage3DEjjjiiiiiiijiPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options) {
  self->glCompressedTextureSubImage3D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      imageSize,
      bits,
      options);
}

//  void QOpenGLTextureHelper::glCompressedTextureImage1D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLenum
//      internalFormat, GLsizei width, GLint border, GLsizei imageSize, const
//      GLvoid *bits, const QOpenGLPixelTransferOptions *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper26glCompressedTextureImage1DEjjjijiiiPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLint border,
    GLsizei imageSize,
    const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options) {
  self->glCompressedTextureImage1D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      border,
      imageSize,
      bits,
      options);
}

//  void QOpenGLTextureHelper::glCompressedTextureImage2D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei
//      imageSize, const GLvoid *bits, const QOpenGLPixelTransferOptions
//      *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper26glCompressedTextureImage2DEjjjijiiiiPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLsizei imageSize,
    const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options) {
  self->glCompressedTextureImage2D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      border,
      imageSize,
      bits,
      options);
}

//  void QOpenGLTextureHelper::glCompressedTextureImage3D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
//      border, GLsizei imageSize, const GLvoid *bits, const
//      QOpenGLPixelTransferOptions *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper26glCompressedTextureImage3DEjjjijiiiiiPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLsizei imageSize,
    const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options) {
  self->glCompressedTextureImage3D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      depth,
      border,
      imageSize,
      bits,
      options);
}

//  void QOpenGLTextureHelper::dsa_TextureParameteri(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21dsa_TextureParameteriEjjjji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLint param) {
  self->dsa_TextureParameteri(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::dsa_TextureParameteriv(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, const GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper22dsa_TextureParameterivEjjjjPKi(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    const GLint *params) {
  self->dsa_TextureParameteriv(
      texture,
      target,
      bindingTarget,
      pname,
      params);
}

//  void QOpenGLTextureHelper::dsa_TextureParameterf(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLfloat param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21dsa_TextureParameterfEjjjjf(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLfloat param) {
  self->dsa_TextureParameterf(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::dsa_TextureParameterfv(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, const GLfloat *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper22dsa_TextureParameterfvEjjjjPKf(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    const GLfloat *params) {
  self->dsa_TextureParameterfv(
      texture,
      target,
      bindingTarget,
      pname,
      params);
}

//  void QOpenGLTextureHelper::dsa_GenerateTextureMipmap(GLuint texture,
//      GLenum target, GLenum bindingTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25dsa_GenerateTextureMipmapEjjj(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget) {
  self->dsa_GenerateTextureMipmap(texture, target, bindingTarget);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage3DEjjjijiii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->dsa_TextureStorage3D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height,
      depth);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage2DEjjjijii(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height) {
  self->dsa_TextureStorage2D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width,
      height);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat,
//      GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage1DEjjjiji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width) {
  self->dsa_TextureStorage1D(
      texture,
      target,
      bindingTarget,
      levels,
      internalFormat,
      width);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage3DMultisample(GLuint
//      texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper31dsa_TextureStorage3DMultisampleEjjjijiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureStorage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_TextureStorage2DMultisample(GLuint
//      texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper31dsa_TextureStorage2DMultisampleEjjjijiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureStorage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_TextureImage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum
//      format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18dsa_TextureImage3DEjjjijiiiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->dsa_TextureImage3D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      depth,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::dsa_TextureImage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLenum internalFormat,
//      GLsizei width, GLsizei height, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18dsa_TextureImage2DEjjjijiiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->dsa_TextureImage2D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::dsa_TextureImage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLenum internalFormat,
//      GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper18dsa_TextureImage1DEjjjijiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->dsa_TextureImage1D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::dsa_TextureSubImage3D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
//      yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth,
//      GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21dsa_TextureSubImage3DEjjjiiiiiiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->dsa_TextureSubImage3D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::dsa_TextureSubImage2D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
//      yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type,
//      const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21dsa_TextureSubImage2DEjjjiiiiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->dsa_TextureSubImage2D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      width,
      height,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::dsa_TextureSubImage1D(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei
//      width, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21dsa_TextureSubImage1DEjjjiiijjPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->dsa_TextureSubImage1D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      width,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::dsa_TextureImage3DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29dsa_TextureImage3DMultisampleEjjjiiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureImage3DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_TextureImage2DMultisample(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
//      internalFormat, GLsizei width, GLsizei height, GLboolean
//      fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper29dsa_TextureImage2DMultisampleEjjjiiiih(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->dsa_TextureImage2DMultisample(
      texture,
      target,
      bindingTarget,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::dsa_CompressedTextureSubImage1D(GLuint
//      texture, GLenum target, GLenum bindingTarget, GLint level, GLint
//      xoffset, GLsizei width, GLenum format, GLsizei imageSize, const
//      GLvoid *bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage1DEjjjiiijiPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *bits) {
  self->dsa_CompressedTextureSubImage1D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      width,
      format,
      imageSize,
      bits);
}

//  void QOpenGLTextureHelper::dsa_CompressedTextureSubImage2D(GLuint
//      texture, GLenum target, GLenum bindingTarget, GLint level, GLint
//      xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format,
//      GLsizei imageSize, const GLvoid *bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage2DEjjjiiiiijiPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *bits) {
  self->dsa_CompressedTextureSubImage2D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      width,
      height,
      format,
      imageSize,
      bits);
}

//  void QOpenGLTextureHelper::dsa_CompressedTextureSubImage3D(GLuint
//      texture, GLenum target, GLenum bindingTarget, GLint level, GLint
//      xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height,
//      GLsizei depth, GLenum format, GLsizei imageSize, const GLvoid *bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper31dsa_CompressedTextureSubImage3DEjjjiiiiiiijiPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *bits) {
  self->dsa_CompressedTextureSubImage3D(
      texture,
      target,
      bindingTarget,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      imageSize,
      bits);
}

//  void QOpenGLTextureHelper::dsa_CompressedTextureImage1D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLenum
//      internalFormat, GLsizei width, GLint border, GLsizei imageSize, const
//      GLvoid *bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage1DEjjjijiiiPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLint border,
    GLsizei imageSize,
    const GLvoid *bits) {
  self->dsa_CompressedTextureImage1D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      border,
      imageSize,
      bits);
}

//  void QOpenGLTextureHelper::dsa_CompressedTextureImage2D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei
//      imageSize, const GLvoid *bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage2DEjjjijiiiiPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLsizei imageSize,
    const GLvoid *bits) {
  self->dsa_CompressedTextureImage2D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      border,
      imageSize,
      bits);
}

//  void QOpenGLTextureHelper::dsa_CompressedTextureImage3D(GLuint texture,
//      GLenum target, GLenum bindingTarget, GLint level, GLenum
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
//      border, GLsizei imageSize, const GLvoid *bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper28dsa_CompressedTextureImage3DEjjjijiiiiiPKv(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLsizei imageSize,
    const GLvoid *bits) {
  self->dsa_CompressedTextureImage3D(
      texture,
      target,
      bindingTarget,
      level,
      internalFormat,
      width,
      height,
      depth,
      border,
      imageSize,
      bits);
}

//  void QOpenGLTextureHelper::qt_TextureParameteri(GLuint texture, GLenum
//      target, GLenum bindingTarget, GLenum pname, GLint param)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper20qt_TextureParameteriEjjjji(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLenum bindingTarget,
    GLenum pname,
    GLint param) {
  self->qt_TextureParameteri(texture, target, bindingTarget, pname, param);
}

//  void QOpenGLTextureHelper::glTexImage1D(GLenum target, GLint level, GLint
//      internalFormat, GLsizei width, GLint border, GLenum format, GLenum
//      type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper12glTexImage1DEjiiiijjPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLint internalFormat,
    GLsizei width,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexImage1D(
      target,
      level,
      internalFormat,
      width,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::glTexSubImage1D(GLenum target, GLint level,
//      GLint xoffset, GLsizei width, GLenum format, GLenum type, const
//      GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper15glTexSubImage1DEjiiijjPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage1D(target, level, xoffset, width, format, type, pixels);
}

//  void QOpenGLTextureHelper::glTexImage3D(GLenum target, GLint level, GLint
//      internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
//      border, GLenum format, GLenum type, const GLvoid *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper12glTexImage3DEjiiiiiijjPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexImage3D(
      target,
      level,
      internalFormat,
      width,
      height,
      depth,
      border,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::glTexSubImage3D(GLenum target, GLint level,
//      GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei
//      height, GLsizei depth, GLenum format, GLenum type, const GLvoid
//      *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper15glTexSubImage3DEjiiiiiiijjPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLenum type,
    const GLvoid *pixels) {
  self->glTexSubImage3D(
      target,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      type,
      pixels);
}

//  void QOpenGLTextureHelper::glGetCompressedTexImage(GLenum target, GLint
//      level, GLvoid *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper23glGetCompressedTexImageEjiPv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLvoid *img) {
  self->glGetCompressedTexImage(target, level, img);
}

//  void QOpenGLTextureHelper::glCompressedTexSubImage1D(GLenum target, GLint
//      level, GLint xoffset, GLsizei width, GLenum format, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25glCompressedTexSubImage1DEjiiijiPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLsizei width,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexSubImage1D(
      target,
      level,
      xoffset,
      width,
      format,
      imageSize,
      data);
}

//  void QOpenGLTextureHelper::glCompressedTexSubImage2D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
//      GLenum format, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25glCompressedTexSubImage2DEjiiiiijiPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLsizei width,
    GLsizei height,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexSubImage2D(
      target,
      level,
      xoffset,
      yoffset,
      width,
      height,
      format,
      imageSize,
      data);
}

//  void QOpenGLTextureHelper::glCompressedTexSubImage3D(GLenum target, GLint
//      level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
//      GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize,
//      const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25glCompressedTexSubImage3DEjiiiiiiijiPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLint xoffset,
    GLint yoffset,
    GLint zoffset,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLenum format,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexSubImage3D(
      target,
      level,
      xoffset,
      yoffset,
      zoffset,
      width,
      height,
      depth,
      format,
      imageSize,
      data);
}

//  void QOpenGLTextureHelper::glCompressedTexImage1D(GLenum target, GLint
//      level, GLenum internalFormat, GLsizei width, GLint border, GLsizei
//      imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper22glCompressedTexImage1DEjijiiiPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLint border,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexImage1D(
      target,
      level,
      internalFormat,
      width,
      border,
      imageSize,
      data);
}

//  void QOpenGLTextureHelper::glCompressedTexImage2D(GLenum target, GLint
//      level, GLenum internalFormat, GLsizei width, GLsizei height, GLint
//      border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper22glCompressedTexImage2DEjijiiiiPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLint border,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexImage2D(
      target,
      level,
      internalFormat,
      width,
      height,
      border,
      imageSize,
      data);
}

//  void QOpenGLTextureHelper::glCompressedTexImage3D(GLenum target, GLint
//      level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei
//      depth, GLint border, GLsizei imageSize, const GLvoid *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper22glCompressedTexImage3DEjijiiiiiPKv(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLint level,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLint border,
    GLsizei imageSize,
    const GLvoid *data) {
  self->glCompressedTexImage3D(
      target,
      level,
      internalFormat,
      width,
      height,
      depth,
      border,
      imageSize,
      data);
}

//  void QOpenGLTextureHelper::glActiveTexture(GLenum texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper15glActiveTextureEj(
    QOpenGLTextureHelper *self,
    GLenum texture) {
  self->glActiveTexture(texture);
}

//  void QOpenGLTextureHelper::glGenerateMipmap(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper16glGenerateMipmapEj(
    QOpenGLTextureHelper *self,
    GLenum target) {
  self->glGenerateMipmap(target);
}

//  void QOpenGLTextureHelper::glTexImage3DMultisample(GLenum target, GLsizei
//      samples, GLint internalFormat, GLsizei width, GLsizei height, GLsizei
//      depth, GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper23glTexImage3DMultisampleEjiiiiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTexImage3DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTexImage2DMultisample(GLenum target, GLsizei
//      samples, GLint internalFormat, GLsizei width, GLsizei height,
//      GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper23glTexImage2DMultisampleEjiiiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLint internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTexImage2DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTexStorage3D(GLenum target, GLsizei levels,
//      GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper14glTexStorage3DEjijiii(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth) {
  self->glTexStorage3D(target, levels, internalFormat, width, height, depth);
}

//  void QOpenGLTextureHelper::glTexStorage2D(GLenum target, GLsizei levels,
//      GLenum internalFormat, GLsizei width, GLsizei height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper14glTexStorage2DEjijii(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height) {
  self->glTexStorage2D(target, levels, internalFormat, width, height);
}

//  void QOpenGLTextureHelper::glTexStorage1D(GLenum target, GLsizei levels,
//      GLenum internalFormat, GLsizei width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper14glTexStorage1DEjiji(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei levels,
    GLenum internalFormat,
    GLsizei width) {
  self->glTexStorage1D(target, levels, internalFormat, width);
}

//  void QOpenGLTextureHelper::glTexStorage3DMultisample(GLenum target,
//      GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
//      height, GLsizei depth, GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25glTexStorage3DMultisampleEjijiiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLsizei depth,
    GLboolean fixedSampleLocations) {
  self->glTexStorage3DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      depth,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTexStorage2DMultisample(GLenum target,
//      GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
//      height, GLboolean fixedSampleLocations)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper25glTexStorage2DMultisampleEjijiih(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLsizei samples,
    GLenum internalFormat,
    GLsizei width,
    GLsizei height,
    GLboolean fixedSampleLocations) {
  self->glTexStorage2DMultisample(
      target,
      samples,
      internalFormat,
      width,
      height,
      fixedSampleLocations);
}

//  void QOpenGLTextureHelper::glTexBufferRange(GLenum target, GLenum
//      internalFormat, GLuint buffer, GLintptr offset, GLsizeiptr size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper16glTexBufferRangeEjjjll(
    QOpenGLTextureHelper *self,
    GLenum target,
    GLenum internalFormat,
    GLuint buffer,
    long long offset,
    long long size) {
  self->glTexBufferRange(target, internalFormat, buffer, offset, size);
}

//  void QOpenGLTextureHelper::glTextureView(GLuint texture, GLenum target,
//      GLuint origTexture, GLenum internalFormat, GLuint minLevel, GLuint
//      numLevels, GLuint minLayer, GLuint numLayers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper13glTextureViewEjjjjjjjj(
    QOpenGLTextureHelper *self,
    GLuint texture,
    GLenum target,
    GLuint origTexture,
    GLenum internalFormat,
    GLuint minLevel,
    GLuint numLevels,
    GLuint minLayer,
    GLuint numLayers) {
  self->glTextureView(
      texture,
      target,
      origTexture,
      internalFormat,
      minLevel,
      numLevels,
      minLayer,
      numLayers);
}

//  QOpenGLPixelTransferOptions
//      QOpenGLTextureHelper::savePixelUploadOptions()
extern "C" Q_DECL_EXPORT
QOpenGLPixelTransferOptions *ritual_ZN20QOpenGLTextureHelper22savePixelUploadOptionsEv(
    QOpenGLTextureHelper *self) {
  return new QOpenGLPixelTransferOptions(self->savePixelUploadOptions());
}

//  void QOpenGLTextureHelper::setPixelUploadOptions(const
//      QOpenGLPixelTransferOptions &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelper21setPixelUploadOptionsERK27QOpenGLPixelTransferOptions(
    QOpenGLTextureHelper *self,
    const QOpenGLPixelTransferOptions *options) {
  self->setPixelUploadOptions(*options);
}

//  QOpenGLTextureHelper::~QOpenGLTextureHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpenGLTextureHelperD1Ev(QOpenGLTextureHelper *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
