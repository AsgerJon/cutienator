//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_OPENGL)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/qopengltexture.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/private/qopengltexturehelper_p.h>
#include <QtGui/QOpenGLContext>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtOpenGL/qopengltexture.h>
#include <QtOpenGL/private/qopengltexture_p.h>
#include <QtOpenGL/private/qopengltexturehelper_p.h>
#include <QtGui/qopenglfunctions.h>
#include <QtGui/qcolor.h>
#include <QtGui/qopenglcontext.h>
#include <QtCore/qdebug.h>
#include <QtCore/private/qobject_p.h>
#include <QtGui/private/qopenglcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopengltexture.cpp, line 290, as local:qopengltexture.cpp:isSizedTextureFormat
static bool isSizedTextureFormat(QOpenGLTexture::TextureFormat internalFormat)
{
    switch (internalFormat) {
    case QOpenGLTexture::NoFormat:
        return false;

    case QOpenGLTexture::R8_UNorm:
    case QOpenGLTexture::RG8_UNorm:
    case QOpenGLTexture::RGB8_UNorm:
    case QOpenGLTexture::RGBA8_UNorm:
    case QOpenGLTexture::R16_UNorm:
    case QOpenGLTexture::RG16_UNorm:
    case QOpenGLTexture::RGB16_UNorm:
    case QOpenGLTexture::RGBA16_UNorm:
    case QOpenGLTexture::R8_SNorm:
    case QOpenGLTexture::RG8_SNorm:
    case QOpenGLTexture::RGB8_SNorm:
    case QOpenGLTexture::RGBA8_SNorm:
    case QOpenGLTexture::R16_SNorm:
    case QOpenGLTexture::RG16_SNorm:
    case QOpenGLTexture::RGB16_SNorm:
    case QOpenGLTexture::RGBA16_SNorm:
    case QOpenGLTexture::R8U:
    case QOpenGLTexture::RG8U:
    case QOpenGLTexture::RGB8U:
    case QOpenGLTexture::RGBA8U:
    case QOpenGLTexture::R16U:
    case QOpenGLTexture::RG16U:
    case QOpenGLTexture::RGB16U:
    case QOpenGLTexture::RGBA16U:
    case QOpenGLTexture::R32U:
    case QOpenGLTexture::RG32U:
    case QOpenGLTexture::RGB32U:
    case QOpenGLTexture::RGBA32U:
    case QOpenGLTexture::R8I:
    case QOpenGLTexture::RG8I:
    case QOpenGLTexture::RGB8I:
    case QOpenGLTexture::RGBA8I:
    case QOpenGLTexture::R16I:
    case QOpenGLTexture::RG16I:
    case QOpenGLTexture::RGB16I:
    case QOpenGLTexture::RGBA16I:
    case QOpenGLTexture::R32I:
    case QOpenGLTexture::RG32I:
    case QOpenGLTexture::RGB32I:
    case QOpenGLTexture::RGBA32I:
    case QOpenGLTexture::R16F:
    case QOpenGLTexture::RG16F:
    case QOpenGLTexture::RGB16F:
    case QOpenGLTexture::RGBA16F:
    case QOpenGLTexture::R32F:
    case QOpenGLTexture::RG32F:
    case QOpenGLTexture::RGB32F:
    case QOpenGLTexture::RGBA32F:
    case QOpenGLTexture::RGB9E5:
    case QOpenGLTexture::RG11B10F:
    case QOpenGLTexture::RG3B2:
    case QOpenGLTexture::R5G6B5:
    case QOpenGLTexture::RGB5A1:
    case QOpenGLTexture::RGBA4:
    case QOpenGLTexture::RGB10A2:

    case QOpenGLTexture::D16:
    case QOpenGLTexture::D24:
    case QOpenGLTexture::D32:
    case QOpenGLTexture::D32F:

    case QOpenGLTexture::D24S8:
    case QOpenGLTexture::D32FS8X24:

    case QOpenGLTexture::S8:

    case QOpenGLTexture::RGB_DXT1:
    case QOpenGLTexture::RGBA_DXT1:
    case QOpenGLTexture::RGBA_DXT3:
    case QOpenGLTexture::RGBA_DXT5:
    case QOpenGLTexture::R_ATI1N_UNorm:
    case QOpenGLTexture::R_ATI1N_SNorm:
    case QOpenGLTexture::RG_ATI2N_UNorm:
    case QOpenGLTexture::RG_ATI2N_SNorm:
    case QOpenGLTexture::RGB_BP_UNSIGNED_FLOAT:
    case QOpenGLTexture::RGB_BP_SIGNED_FLOAT:
    case QOpenGLTexture::RGB_BP_UNorm:
    case QOpenGLTexture::SRGB8:
    case QOpenGLTexture::SRGB8_Alpha8:
    case QOpenGLTexture::SRGB_DXT1:
    case QOpenGLTexture::SRGB_Alpha_DXT1:
    case QOpenGLTexture::SRGB_Alpha_DXT3:
    case QOpenGLTexture::SRGB_Alpha_DXT5:
    case QOpenGLTexture::SRGB_BP_UNorm:
    case QOpenGLTexture::R11_EAC_UNorm:
    case QOpenGLTexture::R11_EAC_SNorm:
    case QOpenGLTexture::RG11_EAC_UNorm:
    case QOpenGLTexture::RG11_EAC_SNorm:
    case QOpenGLTexture::RGB8_ETC2:
    case QOpenGLTexture::SRGB8_ETC2:
    case QOpenGLTexture::RGB8_PunchThrough_Alpha1_ETC2:
    case QOpenGLTexture::SRGB8_PunchThrough_Alpha1_ETC2:
    case QOpenGLTexture::RGBA8_ETC2_EAC:
    case QOpenGLTexture::SRGB8_Alpha8_ETC2_EAC:
    case QOpenGLTexture::RGBA_ASTC_4x4:
    case QOpenGLTexture::RGBA_ASTC_5x4:
    case QOpenGLTexture::RGBA_ASTC_5x5:
    case QOpenGLTexture::RGBA_ASTC_6x5:
    case QOpenGLTexture::RGBA_ASTC_6x6:
    case QOpenGLTexture::RGBA_ASTC_8x5:
    case QOpenGLTexture::RGBA_ASTC_8x6:
    case QOpenGLTexture::RGBA_ASTC_8x8:
    case QOpenGLTexture::RGBA_ASTC_10x5:
    case QOpenGLTexture::RGBA_ASTC_10x6:
    case QOpenGLTexture::RGBA_ASTC_10x8:
    case QOpenGLTexture::RGBA_ASTC_10x10:
    case QOpenGLTexture::RGBA_ASTC_12x10:
    case QOpenGLTexture::RGBA_ASTC_12x12:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_4x4:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_5x4:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_5x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_6x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_6x6:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_8x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_8x6:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_8x8:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x6:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x8:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x10:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_12x10:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_12x12:
        return true;

    case QOpenGLTexture::RGB8_ETC1:
        return false;

    case QOpenGLTexture::DepthFormat:
    case QOpenGLTexture::AlphaFormat:

    case QOpenGLTexture::RGBFormat:
    case QOpenGLTexture::RGBAFormat:

    case QOpenGLTexture::LuminanceFormat:

    case QOpenGLTexture::LuminanceAlphaFormat:
        return false;
    }

    Q_UNREACHABLE_RETURN(false);
}

//  from src/opengl/qopengltexture.cpp, line 438, as local:qopengltexture.cpp:isTextureTargetMultisample
static bool isTextureTargetMultisample(QOpenGLTexture::Target target)
{
    switch (target) {
    case QOpenGLTexture::Target1D:
    case QOpenGLTexture::Target1DArray:
    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::Target2DArray:
    case QOpenGLTexture::Target3D:
    case QOpenGLTexture::TargetCubeMap:
    case QOpenGLTexture::TargetCubeMapArray:
        return false;

    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
        return true;

    case QOpenGLTexture::TargetRectangle:
    case QOpenGLTexture::TargetBuffer:
        return false;
    }

    Q_UNREACHABLE_RETURN(false);
}

//  from src/opengl/qopengltexture.cpp, line 944, as local:qopengltexture.cpp:isCompressedFormat
static bool isCompressedFormat(QOpenGLTexture::TextureFormat internalFormat)
{
    switch (internalFormat) {
    case QOpenGLTexture::NoFormat:

    case QOpenGLTexture::R8_UNorm:
    case QOpenGLTexture::RG8_UNorm:
    case QOpenGLTexture::RGB8_UNorm:
    case QOpenGLTexture::RGBA8_UNorm:
    case QOpenGLTexture::R16_UNorm:
    case QOpenGLTexture::RG16_UNorm:
    case QOpenGLTexture::RGB16_UNorm:
    case QOpenGLTexture::RGBA16_UNorm:
    case QOpenGLTexture::R8_SNorm:
    case QOpenGLTexture::RG8_SNorm:
    case QOpenGLTexture::RGB8_SNorm:
    case QOpenGLTexture::RGBA8_SNorm:
    case QOpenGLTexture::R16_SNorm:
    case QOpenGLTexture::RG16_SNorm:
    case QOpenGLTexture::RGB16_SNorm:
    case QOpenGLTexture::RGBA16_SNorm:
    case QOpenGLTexture::R8U:
    case QOpenGLTexture::RG8U:
    case QOpenGLTexture::RGB8U:
    case QOpenGLTexture::RGBA8U:
    case QOpenGLTexture::R16U:
    case QOpenGLTexture::RG16U:
    case QOpenGLTexture::RGB16U:
    case QOpenGLTexture::RGBA16U:
    case QOpenGLTexture::R32U:
    case QOpenGLTexture::RG32U:
    case QOpenGLTexture::RGB32U:
    case QOpenGLTexture::RGBA32U:
    case QOpenGLTexture::R8I:
    case QOpenGLTexture::RG8I:
    case QOpenGLTexture::RGB8I:
    case QOpenGLTexture::RGBA8I:
    case QOpenGLTexture::R16I:
    case QOpenGLTexture::RG16I:
    case QOpenGLTexture::RGB16I:
    case QOpenGLTexture::RGBA16I:
    case QOpenGLTexture::R32I:
    case QOpenGLTexture::RG32I:
    case QOpenGLTexture::RGB32I:
    case QOpenGLTexture::RGBA32I:
    case QOpenGLTexture::R16F:
    case QOpenGLTexture::RG16F:
    case QOpenGLTexture::RGB16F:
    case QOpenGLTexture::RGBA16F:
    case QOpenGLTexture::R32F:
    case QOpenGLTexture::RG32F:
    case QOpenGLTexture::RGB32F:
    case QOpenGLTexture::RGBA32F:
    case QOpenGLTexture::RGB9E5:
    case QOpenGLTexture::RG11B10F:
    case QOpenGLTexture::RG3B2:
    case QOpenGLTexture::R5G6B5:
    case QOpenGLTexture::RGB5A1:
    case QOpenGLTexture::RGBA4:
    case QOpenGLTexture::RGB10A2:

    case QOpenGLTexture::D16:
    case QOpenGLTexture::D24:
    case QOpenGLTexture::D32:
    case QOpenGLTexture::D32F:

    case QOpenGLTexture::D24S8:
    case QOpenGLTexture::D32FS8X24:

    case QOpenGLTexture::S8:

    // GL_SRGB8 and GL_SRGB8_ALPHA8 are uncompressed, unlike the rest of
    // the sRGB section of the enum.
    case QOpenGLTexture::SRGB8:
    case QOpenGLTexture::SRGB8_Alpha8:
        return false;

    case QOpenGLTexture::RGB_DXT1:
    case QOpenGLTexture::RGBA_DXT1:
    case QOpenGLTexture::RGBA_DXT3:
    case QOpenGLTexture::RGBA_DXT5:
    case QOpenGLTexture::R_ATI1N_UNorm:
    case QOpenGLTexture::R_ATI1N_SNorm:
    case QOpenGLTexture::RG_ATI2N_UNorm:
    case QOpenGLTexture::RG_ATI2N_SNorm:
    case QOpenGLTexture::RGB_BP_UNSIGNED_FLOAT:
    case QOpenGLTexture::RGB_BP_SIGNED_FLOAT:
    case QOpenGLTexture::RGB_BP_UNorm:
    case QOpenGLTexture::SRGB_DXT1:
    case QOpenGLTexture::SRGB_Alpha_DXT1:
    case QOpenGLTexture::SRGB_Alpha_DXT3:
    case QOpenGLTexture::SRGB_Alpha_DXT5:
    case QOpenGLTexture::SRGB_BP_UNorm:
    case QOpenGLTexture::R11_EAC_UNorm:
    case QOpenGLTexture::R11_EAC_SNorm:
    case QOpenGLTexture::RG11_EAC_UNorm:
    case QOpenGLTexture::RG11_EAC_SNorm:
    case QOpenGLTexture::RGB8_ETC2:
    case QOpenGLTexture::SRGB8_ETC2:
    case QOpenGLTexture::RGB8_PunchThrough_Alpha1_ETC2:
    case QOpenGLTexture::SRGB8_PunchThrough_Alpha1_ETC2:
    case QOpenGLTexture::RGBA8_ETC2_EAC:
    case QOpenGLTexture::SRGB8_Alpha8_ETC2_EAC:
    case QOpenGLTexture::RGB8_ETC1:
    case QOpenGLTexture::RGBA_ASTC_4x4:
    case QOpenGLTexture::RGBA_ASTC_5x4:
    case QOpenGLTexture::RGBA_ASTC_5x5:
    case QOpenGLTexture::RGBA_ASTC_6x5:
    case QOpenGLTexture::RGBA_ASTC_6x6:
    case QOpenGLTexture::RGBA_ASTC_8x5:
    case QOpenGLTexture::RGBA_ASTC_8x6:
    case QOpenGLTexture::RGBA_ASTC_8x8:
    case QOpenGLTexture::RGBA_ASTC_10x5:
    case QOpenGLTexture::RGBA_ASTC_10x6:
    case QOpenGLTexture::RGBA_ASTC_10x8:
    case QOpenGLTexture::RGBA_ASTC_10x10:
    case QOpenGLTexture::RGBA_ASTC_12x10:
    case QOpenGLTexture::RGBA_ASTC_12x12:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_4x4:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_5x4:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_5x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_6x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_6x6:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_8x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_8x6:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_8x8:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x5:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x6:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x8:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_10x10:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_12x10:
    case QOpenGLTexture::SRGB8_Alpha8_ASTC_12x12:
        return true;

    case QOpenGLTexture::DepthFormat:
    case QOpenGLTexture::AlphaFormat:
    case QOpenGLTexture::RGBFormat:
    case QOpenGLTexture::RGBAFormat:
    case QOpenGLTexture::LuminanceFormat:
    case QOpenGLTexture::LuminanceAlphaFormat:
        return false;
    }

    Q_UNREACHABLE_RETURN(false);
}

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

//  from src/opengl/qopengltexturehelper.cpp, line 485, as _ZN20QOpenGLTextureHelper17qt_TextureImage1DEjjjijiijjPKv
inline void QOpenGLTextureHelper::qt_TextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    TextureBinder binder(functions, texture, target, bindingTarget);
    glTexImage1D(target, level, internalFormat, width, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 297, as _ZN20QOpenGLTextureHelper18dsa_TextureImage1DEjjjijiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage1DEXT(texture, target, level, internalFormat, width, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 291, as _ZN20QOpenGLTextureHelper18dsa_TextureImage2DEjjjijiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage2DEXT(texture, target, level, internalFormat, width, height, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 285, as _ZN20QOpenGLTextureHelper18dsa_TextureImage3DEjjjijiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureImage3DEXT(texture, target, level, internalFormat, width, height, depth, border, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 267, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage1DEjjjiji
inline void QOpenGLTextureHelper::dsa_TextureStorage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width)
{
    Q_UNUSED(bindingTarget);
    TextureStorage1DEXT(texture, target, levels, internalFormat, width);
}

//  from src/opengl/qopengltexturehelper.cpp, line 261, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage2DEjjjijii
inline void QOpenGLTextureHelper::dsa_TextureStorage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height)
{
    Q_UNUSED(bindingTarget);
    TextureStorage2DEXT(texture, target, levels, internalFormat, width, height);
}

//  from src/opengl/qopengltexturehelper.cpp, line 255, as _ZN20QOpenGLTextureHelper20dsa_TextureStorage3DEjjjijiii
inline void QOpenGLTextureHelper::dsa_TextureStorage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth)
{
    Q_UNUSED(bindingTarget);
    TextureStorage3DEXT(texture, target, levels, internalFormat, width, height, depth);
}

//  from src/opengl/qopengltexturehelper.cpp, line 237, as _ZN20QOpenGLTextureHelper21dsa_TextureParameterfEjjjjf
inline void QOpenGLTextureHelper::dsa_TextureParameterf(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLfloat param)
{
    Q_UNUSED(bindingTarget);
    TextureParameterfEXT(texture, target, pname, param);
}

//  from src/opengl/qopengltexturehelper.cpp, line 225, as _ZN20QOpenGLTextureHelper21dsa_TextureParameteriEjjjji
inline void QOpenGLTextureHelper::dsa_TextureParameteri(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, GLint param)
{
    Q_UNUSED(bindingTarget);
    TextureParameteriEXT(texture, target, pname, param);
}

//  from src/opengl/qopengltexturehelper.cpp, line 315, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage1DEjjjiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage1D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage1DEXT(texture, target, level, xoffset, width, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 309, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage2DEjjjiiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage2D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage2DEXT(texture, target, level, xoffset, yoffset, width, height, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 303, as _ZN20QOpenGLTextureHelper21dsa_TextureSubImage3DEjjjiiiiiiijjPKv
inline void QOpenGLTextureHelper::dsa_TextureSubImage3D(GLuint texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels)
{
    Q_UNUSED(bindingTarget);
    TextureSubImage3DEXT(texture, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels);
}

//  from src/opengl/qopengltexturehelper.cpp, line 243, as _ZN20QOpenGLTextureHelper22dsa_TextureParameterfvEjjjjPKf
inline void QOpenGLTextureHelper::dsa_TextureParameterfv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat *params)
{
    Q_UNUSED(bindingTarget);
    TextureParameterfvEXT(texture, target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 231, as _ZN20QOpenGLTextureHelper22dsa_TextureParameterivEjjjjPKi
inline void QOpenGLTextureHelper::dsa_TextureParameteriv(GLuint texture, GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)
{
    Q_UNUSED(bindingTarget);
    TextureParameterivEXT(texture, target, pname, params);
}

//  from src/opengl/qopengltexturehelper.cpp, line 249, as _ZN20QOpenGLTextureHelper25dsa_GenerateTextureMipmapEjjj
inline void QOpenGLTextureHelper::dsa_GenerateTextureMipmap(GLuint texture, GLenum target, GLenum bindingTarget)
{
    Q_UNUSED(bindingTarget);
    GenerateTextureMipmapEXT(texture, target);
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

//  from src/opengl/qopengltexturehelper.cpp, line 327, as _ZN20QOpenGLTextureHelper29dsa_TextureImage2DMultisampleEjjjiiiih
inline void QOpenGLTextureHelper::dsa_TextureImage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureImage2DMultisampleNV(texture, target, samples, internalFormat, width, height, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 321, as _ZN20QOpenGLTextureHelper29dsa_TextureImage3DMultisampleEjjjiiiiih
inline void QOpenGLTextureHelper::dsa_TextureImage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureImage3DMultisampleNV(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations);
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

//  from src/opengl/qopengltexturehelper.cpp, line 279, as _ZN20QOpenGLTextureHelper31dsa_TextureStorage2DMultisampleEjjjijiih
inline void QOpenGLTextureHelper::dsa_TextureStorage2DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureStorage2DMultisampleEXT(texture, target, samples, internalFormat, width, height, fixedSampleLocations);
}

//  from src/opengl/qopengltexturehelper.cpp, line 273, as _ZN20QOpenGLTextureHelper31dsa_TextureStorage3DMultisampleEjjjijiiih
inline void QOpenGLTextureHelper::dsa_TextureStorage3DMultisample(GLuint texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedSampleLocations)
{
    Q_UNUSED(bindingTarget);
    TextureStorage3DMultisampleEXT(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations);
}

//  from src/opengl/qopengltexture.cpp, line 23, as _ZN21QOpenGLTexturePrivateC1EN14QOpenGLTexture6TargetEPS0_
inline QOpenGLTexturePrivate::QOpenGLTexturePrivate(QOpenGLTexture::Target textureTarget,
                                             QOpenGLTexture *qq)
    : q_ptr(qq),
      context(nullptr),
      target(textureTarget),
      textureId(0),
      format(QOpenGLTexture::NoFormat),
      formatClass(QOpenGLTexture::NoFormatClass),
      requestedMipLevels(1),
      mipLevels(-1),
      layers(1),
      faces(1),
      samples(0),
      fixedSamplePositions(true),
      baseLevel(0),
      maxLevel(1000),
      depthStencilMode(QOpenGLTexture::DepthMode),
      comparisonFunction(QOpenGLTexture::CompareLessEqual),
      comparisonMode(QOpenGLTexture::CompareNone),
      minFilter(QOpenGLTexture::Nearest),
      magFilter(QOpenGLTexture::Nearest),
      maxAnisotropy(1.0f),
      minLevelOfDetail(-1000.0f),
      maxLevelOfDetail(1000.0f),
      levelOfDetailBias(0.0f),
      textureView(false),
      autoGenerateMipMaps(true),
      storageAllocated(false),
      texFuncs(nullptr),
      functions(nullptr)
{
    dimensions[0] = dimensions[1] = dimensions[2] = 1;

    switch (target) {
    case QOpenGLTexture::Target1D:
        bindingTarget = QOpenGLTexture::BindingTarget1D;
        break;
    case QOpenGLTexture::Target1DArray:
        bindingTarget = QOpenGLTexture::BindingTarget1DArray;
        break;
    case QOpenGLTexture::Target2D:
        bindingTarget = QOpenGLTexture::BindingTarget2D;
        break;
    case QOpenGLTexture::Target2DArray:
        bindingTarget = QOpenGLTexture::BindingTarget2DArray;
        break;
    case QOpenGLTexture::Target3D:
        bindingTarget = QOpenGLTexture::BindingTarget3D;
        break;
    case QOpenGLTexture::TargetCubeMap:
        bindingTarget = QOpenGLTexture::BindingTargetCubeMap;
        faces = 6;
        break;
    case QOpenGLTexture::TargetCubeMapArray:
        bindingTarget = QOpenGLTexture::BindingTargetCubeMapArray;
        faces = 6;
        break;
    case QOpenGLTexture::Target2DMultisample:
        bindingTarget = QOpenGLTexture::BindingTarget2DMultisample;
        break;
    case QOpenGLTexture::Target2DMultisampleArray:
        bindingTarget = QOpenGLTexture::BindingTarget2DMultisampleArray;
        break;
    case QOpenGLTexture::TargetRectangle:
        bindingTarget = QOpenGLTexture::BindingTargetRectangle;
        break;
    case QOpenGLTexture::TargetBuffer:
        bindingTarget = QOpenGLTexture::BindingTargetBuffer;
        break;
    }

    swizzleMask[0] = QOpenGLTexture::RedValue;
    swizzleMask[1] = QOpenGLTexture::GreenValue;
    swizzleMask[2] = QOpenGLTexture::BlueValue;
    swizzleMask[3] = QOpenGLTexture::AlphaValue;

    wrapModes[0] = wrapModes[1] = wrapModes[2] = target == QOpenGLTexture::TargetRectangle
        ? QOpenGLTexture::ClampToEdge : QOpenGLTexture::Repeat;
}

//  from src/opengl/qopengltexture.cpp, line 103, as _ZN21QOpenGLTexturePrivateD1Ev
inline QOpenGLTexturePrivate::~QOpenGLTexturePrivate()
{
    destroy();
}

//  from src/opengl/qopengltexture.cpp, line 154, as _ZN21QOpenGLTexturePrivate7destroyEv
inline void QOpenGLTexturePrivate::destroy()
{
    if (!textureId) {
        // not created or already destroyed
        return;
    }
    QOpenGLContext *currentContext = QOpenGLContext::currentContext();
    if (!currentContext) {
        qWarning("QOpenGLTexturePrivate::destroy() called without a current context.\n"
                 "Texture has not been destroyed");
        return;
    }
    if (!QOpenGLContext::areSharing(currentContext, context)) {

        qWarning("QOpenGLTexturePrivate::destroy() called but texture context %p"
                 " is not shared with current context %p.\n"
                 "Texture has not been destroyed",
                 static_cast<const void *>(context),
                 static_cast<const void *>(currentContext));
        return;
    }

    functions->glDeleteTextures(1, &textureId);

    context = nullptr;
    functions = nullptr;
    textureId = 0;
    format = QOpenGLTexture::NoFormat;
    formatClass = QOpenGLTexture::NoFormatClass;
    requestedMipLevels = 1;
    mipLevels = -1;
    layers = 1;
    faces = 1;
    samples = 0;
    fixedSamplePositions = true,
    baseLevel = 0;
    maxLevel = 1000;
    depthStencilMode = QOpenGLTexture::DepthMode;
    minFilter = QOpenGLTexture::Nearest;
    magFilter = QOpenGLTexture::Nearest;
    maxAnisotropy = 1.0f;
    minLevelOfDetail = -1000.0f;
    maxLevelOfDetail = 1000.0f;
    levelOfDetailBias = 0.0f;
    textureView = false;
    autoGenerateMipMaps = true;
    storageAllocated = false;
    texFuncs = nullptr;

    swizzleMask[0] = QOpenGLTexture::RedValue;
    swizzleMask[1] = QOpenGLTexture::GreenValue;
    swizzleMask[2] = QOpenGLTexture::BlueValue;
    swizzleMask[3] = QOpenGLTexture::AlphaValue;

    wrapModes[0] = wrapModes[1] = wrapModes[2] = target == QOpenGLTexture::TargetRectangle
        ? QOpenGLTexture::ClampToEdge : QOpenGLTexture::Repeat;
}

//  from src/opengl/qopengltexture.cpp, line 212, as _ZN21QOpenGLTexturePrivate4bindEv
inline void QOpenGLTexturePrivate::bind()
{
    functions->glBindTexture(target, textureId);
}

//  from src/opengl/qopengltexture.cpp, line 217, as _ZN21QOpenGLTexturePrivate4bindEjN14QOpenGLTexture16TextureUnitResetE
inline void QOpenGLTexturePrivate::bind(uint unit, QOpenGLTexture::TextureUnitReset reset)
{
    GLint oldTextureUnit = 0;
    if (reset == QOpenGLTexture::ResetTextureUnit)
        functions->glGetIntegerv(GL_ACTIVE_TEXTURE, &oldTextureUnit);

    texFuncs->glActiveTexture(GL_TEXTURE0 + unit);
    functions->glBindTexture(target, textureId);

    if (reset == QOpenGLTexture::ResetTextureUnit)
        texFuncs->glActiveTexture(GL_TEXTURE0 + oldTextureUnit);
}

//  from src/opengl/qopengltexture.cpp, line 230, as _ZN21QOpenGLTexturePrivate7releaseEv
inline void QOpenGLTexturePrivate::release()
{
    functions->glBindTexture(target, 0);
}

//  from src/opengl/qopengltexture.cpp, line 235, as _ZN21QOpenGLTexturePrivate7releaseEjN14QOpenGLTexture16TextureUnitResetE
inline void QOpenGLTexturePrivate::release(uint unit, QOpenGLTexture::TextureUnitReset reset)
{
    GLint oldTextureUnit = 0;
    if (reset == QOpenGLTexture::ResetTextureUnit)
        functions->glGetIntegerv(GL_ACTIVE_TEXTURE, &oldTextureUnit);

    texFuncs->glActiveTexture(GL_TEXTURE0 + unit);
    functions->glBindTexture(target, 0);

    if (reset == QOpenGLTexture::ResetTextureUnit)
        texFuncs->glActiveTexture(GL_TEXTURE0 + oldTextureUnit);
}

//  from src/opengl/qopengltexture.cpp, line 248, as _ZNK21QOpenGLTexturePrivate7isBoundEv
inline bool QOpenGLTexturePrivate::isBound() const
{
    GLint boundTextureId = 0;
    functions->glGetIntegerv(bindingTarget, &boundTextureId);
    return (static_cast<GLuint>(boundTextureId) == textureId);
}

//  from src/opengl/qopengltexture.cpp, line 255, as _ZNK21QOpenGLTexturePrivate7isBoundEj
inline bool QOpenGLTexturePrivate::isBound(uint unit) const
{
    GLint oldTextureUnit = 0;
    functions->glGetIntegerv(GL_ACTIVE_TEXTURE, &oldTextureUnit);

    GLint boundTextureId = 0;
    texFuncs->glActiveTexture(GL_TEXTURE0 + unit);
    functions->glGetIntegerv(bindingTarget, &boundTextureId);
    bool result = (static_cast<GLuint>(boundTextureId) == textureId);

    texFuncs->glActiveTexture(GL_TEXTURE0 + oldTextureUnit);
    return result;
}

//  from src/opengl/qopengltexture.cpp, line 473, as _ZN21QOpenGLTexturePrivate15allocateStorageEN14QOpenGLTexture11PixelFormatENS0_9PixelTypeE
inline void QOpenGLTexturePrivate::allocateStorage(QOpenGLTexture::PixelFormat pixelFormat, QOpenGLTexture::PixelType pixelType)
{
    // Resolve the actual number of mipmap levels we can use
    mipLevels = evaluateMipLevels();

    if (isUsingImmutableStorage())
        allocateImmutableStorage();
    else
        allocateMutableStorage(pixelFormat, pixelType);
}

//  from src/opengl/qopengltexture.cpp, line 1090, as _ZN21QOpenGLTexturePrivate22allocateMutableStorageEN14QOpenGLTexture11PixelFormatENS0_9PixelTypeE
inline void QOpenGLTexturePrivate::allocateMutableStorage(QOpenGLTexture::PixelFormat pixelFormat, QOpenGLTexture::PixelType pixelType)
{
    // There is no way to allocate mutable storage for compressed textures in in
    // versions older than OpenGL 3.1 and OpenGL ES 3.0, because the older specs
    // do not mandate accepting null data pointers for glCompressedTexImage*D,
    // unlike glTexImage*D (which in turn does not accept compressed formats).
    if (isCompressedFormat(format)) {
        storageAllocated = true;
        return;
    }

    switch (target) {
    case QOpenGLTexture::TargetBuffer:
        // Buffer textures get their storage from an external OpenGL buffer
        qWarning("Buffer textures do not allocate storage");
        return;

    case QOpenGLTexture::Target1D:
        if (features.testFlag(QOpenGLTexture::Texture1D)) {
            for (int level = 0; level < mipLevels; ++level)
                texFuncs->glTextureImage1D(textureId, target, bindingTarget, level, format,
                                           mipLevelSize(level, dimensions[0]),
                                           0,
                                           pixelFormat, pixelType, nullptr);
        } else {
            qWarning("1D textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target1DArray:
        if (features.testFlag(QOpenGLTexture::Texture1D)
                && features.testFlag(QOpenGLTexture::TextureArrays)) {
            for (int level = 0; level < mipLevels; ++level)
                texFuncs->glTextureImage2D(textureId, target, bindingTarget, level, format,
                                           mipLevelSize(level, dimensions[0]),
                                           layers,
                                           0,
                                           pixelFormat, pixelType, nullptr);
        } else {
            qWarning("1D array textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::TargetRectangle:
        for (int level = 0; level < mipLevels; ++level)
            texFuncs->glTextureImage2D(textureId, target, bindingTarget, level, format,
                                       mipLevelSize(level, dimensions[0]),
                                       mipLevelSize(level, dimensions[1]),
                                       0,
                                       pixelFormat, pixelType, nullptr);
        break;

    case QOpenGLTexture::TargetCubeMap: {
        // Cubemaps are the odd one out. We have to allocate storage for each
        // face and miplevel using the special cubemap face targets rather than
        // GL_TARGET_CUBEMAP.
        const QOpenGLTexture::CubeMapFace faceTargets[] = {
            QOpenGLTexture::CubeMapPositiveX, QOpenGLTexture::CubeMapNegativeX,
            QOpenGLTexture::CubeMapPositiveY, QOpenGLTexture::CubeMapNegativeY,
            QOpenGLTexture::CubeMapPositiveZ, QOpenGLTexture::CubeMapNegativeZ
        };

        for (int faceTarget = 0; faceTarget < 6; ++faceTarget) {
            for (int level = 0; level < mipLevels; ++level) {
                texFuncs->glTextureImage2D(textureId, faceTargets[faceTarget], bindingTarget,
                                           level, format,
                                           mipLevelSize(level, dimensions[0]),
                                           mipLevelSize(level, dimensions[1]),
                                           0,
                                           pixelFormat, pixelType, nullptr);
            }
        }
        break;
    }

    case QOpenGLTexture::Target2DArray:
        if (features.testFlag(QOpenGLTexture::TextureArrays)) {
            for (int level = 0; level < mipLevels; ++level)
                texFuncs->glTextureImage3D(textureId, target, bindingTarget, level, format,
                                           mipLevelSize(level, dimensions[0]),
                                           mipLevelSize(level, dimensions[1]),
                                           layers,
                                           0,
                                           pixelFormat, pixelType, nullptr);
        } else {
            qWarning("Array textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::TargetCubeMapArray:
        // Cubemap arrays must specify number of layer-faces (6 * layers) as depth parameter
        if (features.testFlag(QOpenGLTexture::TextureCubeMapArrays)) {
            for (int level = 0; level < mipLevels; ++level)
                texFuncs->glTextureImage3D(textureId, target, bindingTarget, level, format,
                                           mipLevelSize(level, dimensions[0]),
                                           mipLevelSize(level, dimensions[1]),
                                           6 * layers,
                                           0,
                                           pixelFormat, pixelType, nullptr);
        } else {
            qWarning("Cubemap Array textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target3D:
        if (features.testFlag(QOpenGLTexture::Texture3D)) {
            for (int level = 0; level < mipLevels; ++level)
                texFuncs->glTextureImage3D(textureId, target, bindingTarget, level, format,
                                           mipLevelSize(level, dimensions[0]),
                                           mipLevelSize(level, dimensions[1]),
                                           mipLevelSize(level, dimensions[2]),
                                           0,
                                           pixelFormat, pixelType, nullptr);
        } else {
            qWarning("3D textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target2DMultisample:
        if (features.testFlag(QOpenGLTexture::TextureMultisample)) {
            texFuncs->glTextureImage2DMultisample(textureId, target, bindingTarget, samples, format,
                                                  dimensions[0], dimensions[1],
                                                  fixedSamplePositions);
        } else {
            qWarning("Multisample textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target2DMultisampleArray:
        if (features.testFlag(QOpenGLTexture::TextureMultisample)
                && features.testFlag(QOpenGLTexture::TextureArrays)) {
            texFuncs->glTextureImage3DMultisample(textureId, target, bindingTarget, samples, format,
                                                  dimensions[0], dimensions[1], layers,
                                                  fixedSamplePositions);
        } else {
            qWarning("Multisample array textures are not supported");
            return;
        }
        break;
    }

    storageAllocated = true;
}

//  from src/opengl/qopengltexture.cpp, line 1241, as _ZN21QOpenGLTexturePrivate24allocateImmutableStorageEv
inline void QOpenGLTexturePrivate::allocateImmutableStorage()
{
    switch (target) {
    case QOpenGLTexture::TargetBuffer:
        // Buffer textures get their storage from an external OpenGL buffer
        qWarning("Buffer textures do not allocate storage");
        return;

    case QOpenGLTexture::Target1D:
        if (features.testFlag(QOpenGLTexture::Texture1D)) {
            texFuncs->glTextureStorage1D(textureId, target, bindingTarget, mipLevels, format,
                                         dimensions[0]);
        } else {
            qWarning("1D textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target1DArray:
        if (features.testFlag(QOpenGLTexture::Texture1D)
                && features.testFlag(QOpenGLTexture::TextureArrays)) {
            texFuncs->glTextureStorage2D(textureId, target, bindingTarget, mipLevels, format,
                                         dimensions[0], layers);
        } else {
            qWarning("1D array textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::TargetCubeMap:
    case QOpenGLTexture::TargetRectangle:
        texFuncs->glTextureStorage2D(textureId, target, bindingTarget, mipLevels, format,
                                     dimensions[0], dimensions[1]);
        break;

    case QOpenGLTexture::Target2DArray:
        if (features.testFlag(QOpenGLTexture::TextureArrays)) {
            texFuncs->glTextureStorage3D(textureId, target, bindingTarget, mipLevels, format,
                                         dimensions[0], dimensions[1], layers);
        } else {
            qWarning("Array textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::TargetCubeMapArray:
        // Cubemap arrays must specify number of layer-faces (6 * layers) as depth parameter
        if (features.testFlag(QOpenGLTexture::TextureCubeMapArrays)) {
            texFuncs->glTextureStorage3D(textureId, target, bindingTarget, mipLevels, format,
                                         dimensions[0], dimensions[1], 6 * layers);
        } else {
            qWarning("Cubemap Array textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target3D:
        if (features.testFlag(QOpenGLTexture::Texture3D)) {
            texFuncs->glTextureStorage3D(textureId, target, bindingTarget, mipLevels, format,
                                         dimensions[0], dimensions[1], dimensions[2]);
        } else {
            qWarning("3D textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target2DMultisample:
        if (features.testFlag(QOpenGLTexture::ImmutableMultisampleStorage)) {
            texFuncs->glTextureStorage2DMultisample(textureId, target, bindingTarget, samples, format,
                                                    dimensions[0], dimensions[1],
                                                    fixedSamplePositions);
        } else {
            qWarning("Multisample textures are not supported");
            return;
        }
        break;

    case QOpenGLTexture::Target2DMultisampleArray:
        if (features.testFlag(QOpenGLTexture::ImmutableMultisampleStorage)
                && features.testFlag(QOpenGLTexture::TextureArrays)) {
            texFuncs->glTextureStorage3DMultisample(textureId, target, bindingTarget, samples, format,
                                                    dimensions[0], dimensions[1], layers,
                                                    fixedSamplePositions);
        } else {
            qWarning("Multisample array textures are not supported");
            return;
        }
        break;
    }

    storageAllocated = true;
}

//  from src/opengl/qopengltexture.cpp, line 1335, as _ZN21QOpenGLTexturePrivate7setDataEiiiN14QOpenGLTexture11CubeMapFaceENS0_11PixelFormatENS0_9PixelTypeEPKvPK27QOpenGLPixelTransferOptions
inline void QOpenGLTexturePrivate::setData(int mipLevel, int layer, int layerCount, QOpenGLTexture::CubeMapFace cubeFace,
                                    QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType sourceType,
                                    const void *data, const QOpenGLPixelTransferOptions * const options)
{
    switch (target) {
    case QOpenGLTexture::Target1D:
        Q_UNUSED(layer);
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        texFuncs->glTextureSubImage1D(textureId, target, bindingTarget, mipLevel,
                                      0, mipLevelSize( mipLevel, dimensions[0] ),
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target1DArray:
        Q_UNUSED(cubeFace);
        texFuncs->glTextureSubImage2D(textureId, target, bindingTarget, mipLevel,
                                      0, layer,
                                      mipLevelSize(mipLevel, dimensions[0]),
                                      layerCount,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target2D:
        Q_UNUSED(layer);
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        texFuncs->glTextureSubImage2D(textureId, target, bindingTarget, mipLevel,
                                      0, 0,
                                      mipLevelSize(mipLevel, dimensions[0]),
                                      mipLevelSize(mipLevel, dimensions[1]),
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target2DArray:
        Q_UNUSED(cubeFace);
        texFuncs->glTextureSubImage3D(textureId, target, bindingTarget, mipLevel,
                                      0, 0, layer,
                                      mipLevelSize(mipLevel, dimensions[0]),
                                      mipLevelSize(mipLevel, dimensions[1]),
                                      layerCount,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target3D:
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        texFuncs->glTextureSubImage3D(textureId, target, bindingTarget, mipLevel,
                                      0, 0, layer,
                                      mipLevelSize(mipLevel, dimensions[0]),
                                      mipLevelSize(mipLevel, dimensions[1]),
                                      mipLevelSize(mipLevel, dimensions[2]),
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::TargetCubeMap:
        Q_UNUSED(layer);
        Q_UNUSED(layerCount);
        texFuncs->glTextureSubImage2D(textureId, cubeFace, bindingTarget, mipLevel,
                                      0, 0,
                                      mipLevelSize(mipLevel, dimensions[0]),
                                      mipLevelSize(mipLevel, dimensions[1]),
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::TargetCubeMapArray: {
        int faceIndex = cubeFace - QOpenGLTexture::CubeMapPositiveX;
        int layerFace = 6 * layer + faceIndex;
        texFuncs->glTextureSubImage3D(textureId, target, bindingTarget, mipLevel,
                                      0, 0, layerFace,
                                      mipLevelSize(mipLevel, dimensions[0]),
                                      mipLevelSize(mipLevel, dimensions[1]),
                                      layerCount,
                                      sourceFormat, sourceType, data, options);
        break;
    }

    case QOpenGLTexture::TargetRectangle:
        Q_UNUSED(mipLevel);
        Q_UNUSED(layer);
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        texFuncs->glTextureSubImage2D(textureId, target, bindingTarget, 0,
                                      0, 0,
                                      dimensions[0],
                                      dimensions[1],
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
    case QOpenGLTexture::TargetBuffer:
        // We don't upload pixel data for these targets
        qWarning("QOpenGLTexture::setData(): Texture target does not support pixel data upload");
        break;
    }

    // If requested perform automatic mip map generation
    if (mipLevel == 0 && autoGenerateMipMaps && mipLevels > 1) {
        Q_Q(QOpenGLTexture);
        q->generateMipMaps();
    }
}

//  from src/opengl/qopengltexture.cpp, line 1439, as _ZN21QOpenGLTexturePrivate7setDataEiiiiiiiiiN14QOpenGLTexture11CubeMapFaceENS0_11PixelFormatENS0_9PixelTypeEPKvPK27QOpenGLPixelTransferOptions
inline void QOpenGLTexturePrivate::setData(int xOffset, int yOffset, int zOffset, int width, int height, int depth,
                                    int mipLevel, int layer, int layerCount, QOpenGLTexture::CubeMapFace cubeFace,
                                    QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType sourceType,
                                    const void *data, const QOpenGLPixelTransferOptions * const options)
{
    switch (target) {
    case QOpenGLTexture::Target1D:
        Q_UNUSED(layer);
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        Q_UNUSED(yOffset);
        Q_UNUSED(zOffset);
        Q_UNUSED(height);
        Q_UNUSED(depth);
        texFuncs->glTextureSubImage1D(textureId, target, bindingTarget, mipLevel,
                                      xOffset, width,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target1DArray:
        Q_UNUSED(cubeFace);
        Q_UNUSED(yOffset);
        Q_UNUSED(zOffset);
        Q_UNUSED(height);
        Q_UNUSED(depth);
        texFuncs->glTextureSubImage2D(textureId, target, bindingTarget, mipLevel,
                                      xOffset, layer,
                                      width,
                                      layerCount,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target2D:
        Q_UNUSED(layer);
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        Q_UNUSED(zOffset);
        Q_UNUSED(depth);
        texFuncs->glTextureSubImage2D(textureId, target, bindingTarget, mipLevel,
                                      xOffset, yOffset,
                                      width, height,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target2DArray:
        Q_UNUSED(cubeFace);
        Q_UNUSED(zOffset);
        Q_UNUSED(depth);
        texFuncs->glTextureSubImage3D(textureId, target, bindingTarget, mipLevel,
                                      xOffset, yOffset, layer,
                                      width, height, layerCount,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target3D:
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        texFuncs->glTextureSubImage3D(textureId, target, bindingTarget, mipLevel,
                                      xOffset, yOffset, zOffset,
                                      width, height, depth,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::TargetCubeMap:
        Q_UNUSED(layer);
        Q_UNUSED(layerCount);
        Q_UNUSED(zOffset);
        Q_UNUSED(depth);
        texFuncs->glTextureSubImage2D(textureId, cubeFace, bindingTarget, mipLevel,
                                      xOffset, yOffset,
                                      width, height,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::TargetCubeMapArray: {
        Q_UNUSED(zOffset);
        Q_UNUSED(depth);
        int faceIndex = cubeFace - QOpenGLTexture::CubeMapPositiveX;
        int layerFace = 6 * layer + faceIndex;
        texFuncs->glTextureSubImage3D(textureId, target, bindingTarget, mipLevel,
                                      xOffset, yOffset, layerFace,
                                      width, height,
                                      layerCount,
                                      sourceFormat, sourceType, data, options);
        break;
    }

    case QOpenGLTexture::TargetRectangle:
        Q_UNUSED(mipLevel);
        Q_UNUSED(layer);
        Q_UNUSED(cubeFace);
        Q_UNUSED(layerCount);
        Q_UNUSED(zOffset);
        Q_UNUSED(depth);
        texFuncs->glTextureSubImage2D(textureId, target, bindingTarget, 0,
                                      xOffset, yOffset,
                                      width, height,
                                      sourceFormat, sourceType, data, options);
        break;

    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
    case QOpenGLTexture::TargetBuffer:
        // We don't upload pixel data for these targets
        qWarning("QOpenGLTexture::setData(): Texture target does not support pixel data upload");
        break;
    }

    // If requested perform automatic mip map generation
    if (mipLevel == 0 && autoGenerateMipMaps && mipLevels > 1) {
        Q_Q(QOpenGLTexture);
        q->generateMipMaps();
    }
}

//  from src/opengl/qopengltexture.cpp, line 1694, as _ZN21QOpenGLTexturePrivate11setWrapModeEN14QOpenGLTexture8WrapModeE
inline void QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::WrapMode mode)
{
    switch (target) {
    case QOpenGLTexture::Target1D:
    case QOpenGLTexture::Target1DArray:
    case QOpenGLTexture::TargetBuffer:
        wrapModes[0] = mode;
        texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_S, mode);
        break;

    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::Target2DArray:
    case QOpenGLTexture::TargetCubeMap:
    case QOpenGLTexture::TargetCubeMapArray:
    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
    case QOpenGLTexture::TargetRectangle:
        wrapModes[0] = wrapModes[1] = mode;
        texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_S, mode);
        texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_T, mode);
        break;

    case QOpenGLTexture::Target3D:
        wrapModes[0] = wrapModes[1] = wrapModes[2] = mode;
        texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_S, mode);
        texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_T, mode);
        texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_R, mode);
        break;
    }
}

//  from src/opengl/qopengltexture.cpp, line 1725, as _ZN21QOpenGLTexturePrivate11setWrapModeEN14QOpenGLTexture19CoordinateDirectionENS0_8WrapModeE
inline void QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::CoordinateDirection direction, QOpenGLTexture::WrapMode mode)
{
    switch (target) {
    case QOpenGLTexture::Target1D:
    case QOpenGLTexture::Target1DArray:
    case QOpenGLTexture::TargetBuffer:
        switch (direction) {
        case QOpenGLTexture::DirectionS:
            wrapModes[0] = mode;
            texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_S, mode);
            break;

        case QOpenGLTexture::DirectionT:
        case QOpenGLTexture::DirectionR:
            qWarning("QOpenGLTexture::setWrapMode() direction not valid for this texture target");
            break;
        }
        break;

    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::Target2DArray:
    case QOpenGLTexture::TargetCubeMap:
    case QOpenGLTexture::TargetCubeMapArray:
    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
    case QOpenGLTexture::TargetRectangle:
        switch (direction) {
        case QOpenGLTexture::DirectionS:
            wrapModes[0] = mode;
            texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_S, mode);
            break;

        case QOpenGLTexture::DirectionT:
            wrapModes[1] = mode;
            texFuncs->glTextureParameteri(textureId, target, bindingTarget, GL_TEXTURE_WRAP_T, mode);
            break;

        case QOpenGLTexture::DirectionR:
            qWarning("QOpenGLTexture::setWrapMode() direction not valid for this texture target");
            break;
        }
        break;

    case QOpenGLTexture::Target3D:
        switch (direction) {
        case QOpenGLTexture::DirectionS:
            wrapModes[0] = mode;
            texFuncs->glTextureParameteri(textureId, target, bindingTarget, direction, mode);
            break;

        case QOpenGLTexture::DirectionT:
            wrapModes[1] = mode;
            texFuncs->glTextureParameteri(textureId, target, bindingTarget, direction, mode);
            break;

        case QOpenGLTexture::DirectionR:
            wrapModes[2] = mode;
            texFuncs->glTextureParameteri(textureId, target, bindingTarget, direction, mode);
            break;
        }
        break;
    }
}

//  from src/opengl/qopengltexture.cpp, line 1789, as _ZNK21QOpenGLTexturePrivate8wrapModeEN14QOpenGLTexture19CoordinateDirectionE
inline QOpenGLTexture::WrapMode QOpenGLTexturePrivate::wrapMode(QOpenGLTexture::CoordinateDirection direction) const
{
    switch (target) {
    case QOpenGLTexture::Target1D:
    case QOpenGLTexture::Target1DArray:
    case QOpenGLTexture::TargetBuffer:
        switch (direction) {
        case QOpenGLTexture::DirectionS:
            return wrapModes[0];

        case QOpenGLTexture::DirectionT:
        case QOpenGLTexture::DirectionR:
            qWarning("QOpenGLTexture::wrapMode() direction not valid for this texture target");
            return QOpenGLTexture::Repeat;
        }
        break;

    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::Target2DArray:
    case QOpenGLTexture::TargetCubeMap:
    case QOpenGLTexture::TargetCubeMapArray:
    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
    case QOpenGLTexture::TargetRectangle:
        switch (direction) {
        case QOpenGLTexture::DirectionS:
            return wrapModes[0];

        case QOpenGLTexture::DirectionT:
            return wrapModes[1];

        case QOpenGLTexture::DirectionR:
            qWarning("QOpenGLTexture::wrapMode() direction not valid for this texture target");
            return QOpenGLTexture::Repeat;
        }
        break;

    case QOpenGLTexture::Target3D:
        switch (direction) {
        case QOpenGLTexture::DirectionS:
            return wrapModes[0];

        case QOpenGLTexture::DirectionT:
            return wrapModes[1];

        case QOpenGLTexture::DirectionR:
            return wrapModes[2];
        }
        break;
    }
    // Should never get here
    Q_ASSERT(false);
    return QOpenGLTexture::Repeat;
}

//  from src/opengl/qopengltexture.cpp, line 1844, as _ZNK21QOpenGLTexturePrivate17createTextureViewEN14QOpenGLTexture6TargetENS0_13TextureFormatEiiii
inline QOpenGLTexture *QOpenGLTexturePrivate::createTextureView(QOpenGLTexture::Target viewTarget,
                                                         QOpenGLTexture::TextureFormat viewFormat,
                                                         int minimumMipmapLevel, int maximumMipmapLevel,
                                                         int minimumLayer, int maximumLayer) const
{
    // Do sanity checks - see http://www.opengl.org/wiki/GLAPI/glTextureView

    // Check the targets are compatible
    bool viewTargetCompatible = false;
    switch (target) {
    case QOpenGLTexture::Target1D:
    case QOpenGLTexture::Target1DArray:
        viewTargetCompatible = (viewTarget == QOpenGLTexture::Target1D
                             || viewTarget == QOpenGLTexture::Target1DArray);
        break;


    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::Target2DArray:
        viewTargetCompatible = (viewTarget == QOpenGLTexture::Target2D
                             || viewTarget == QOpenGLTexture::Target2DArray);
        break;

    case QOpenGLTexture::Target3D:
        viewTargetCompatible = (viewTarget == QOpenGLTexture::Target3D);
        break;

    case QOpenGLTexture::TargetCubeMap:
    case QOpenGLTexture::TargetCubeMapArray:
        viewTargetCompatible = (viewTarget == QOpenGLTexture::TargetCubeMap
                             || viewTarget == QOpenGLTexture::Target2D
                             || viewTarget == QOpenGLTexture::Target2DArray
                             || viewTarget == QOpenGLTexture::TargetCubeMapArray);
        break;

    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
        viewTargetCompatible = (viewTarget == QOpenGLTexture::Target2DMultisample
                             || viewTarget == QOpenGLTexture::Target2DMultisampleArray);
        break;

    case QOpenGLTexture::TargetRectangle:
        viewTargetCompatible = (viewTarget == QOpenGLTexture::TargetRectangle);
        break;

    case QOpenGLTexture::TargetBuffer:
        // Cannot be used with texture views
        break;
    }

    if (!viewTargetCompatible) {
        qWarning("QOpenGLTexture::createTextureView(): Incompatible source and view targets");
        return nullptr;
    }

    // Check the formats are compatible
    bool viewFormatCompatible = false;
    switch (formatClass) {
    case QOpenGLTexture::NoFormatClass:
        break;

    case QOpenGLTexture::FormatClass_128Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGBA32F
                             || viewFormat == QOpenGLTexture::RGBA32U
                             || viewFormat == QOpenGLTexture::RGBA32I);
        break;

    case QOpenGLTexture::FormatClass_96Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGB32F
                             || viewFormat == QOpenGLTexture::RGB32U
                             || viewFormat == QOpenGLTexture::RGB32I);
        break;

    case QOpenGLTexture::FormatClass_64Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGBA16F
                             || viewFormat == QOpenGLTexture::RG32F
                             || viewFormat == QOpenGLTexture::RGBA16U
                             || viewFormat == QOpenGLTexture::RG32U
                             || viewFormat == QOpenGLTexture::RGBA16I
                             || viewFormat == QOpenGLTexture::RG32I
                             || viewFormat == QOpenGLTexture::RGBA16_UNorm
                             || viewFormat == QOpenGLTexture::RGBA16_SNorm);
        break;

    case QOpenGLTexture::FormatClass_48Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGB16_UNorm
                             || viewFormat == QOpenGLTexture::RGB16_SNorm
                             || viewFormat == QOpenGLTexture::RGB16F
                             || viewFormat == QOpenGLTexture::RGB16U
                             || viewFormat == QOpenGLTexture::RGB16I);
        break;

    case QOpenGLTexture::FormatClass_32Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RG16F
                             || viewFormat == QOpenGLTexture::RG11B10F
                             || viewFormat == QOpenGLTexture::R32F
                             || viewFormat == QOpenGLTexture::RGB10A2
                             || viewFormat == QOpenGLTexture::RGBA8U
                             || viewFormat == QOpenGLTexture::RG16U
                             || viewFormat == QOpenGLTexture::R32U
                             || viewFormat == QOpenGLTexture::RGBA8I
                             || viewFormat == QOpenGLTexture::RG16I
                             || viewFormat == QOpenGLTexture::R32I
                             || viewFormat == QOpenGLTexture::RGBA8_UNorm
                             || viewFormat == QOpenGLTexture::RG16_UNorm
                             || viewFormat == QOpenGLTexture::RGBA8_SNorm
                             || viewFormat == QOpenGLTexture::RG16_SNorm
                             || viewFormat == QOpenGLTexture::SRGB8_Alpha8
                             || viewFormat == QOpenGLTexture::RGB9E5);
        break;

    case QOpenGLTexture::FormatClass_24Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGB8_UNorm
                             || viewFormat == QOpenGLTexture::RGB8_SNorm
                             || viewFormat == QOpenGLTexture::SRGB8
                             || viewFormat == QOpenGLTexture::RGB8U
                             || viewFormat == QOpenGLTexture::RGB8I);
        break;

    case QOpenGLTexture::FormatClass_16Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::R16F
                             || viewFormat == QOpenGLTexture::RG8U
                             || viewFormat == QOpenGLTexture::R16U
                             || viewFormat == QOpenGLTexture::RG8I
                             || viewFormat == QOpenGLTexture::R16I
                             || viewFormat == QOpenGLTexture::RG8_UNorm
                             || viewFormat == QOpenGLTexture::R16_UNorm
                             || viewFormat == QOpenGLTexture::RG8_SNorm
                             || viewFormat == QOpenGLTexture::R16_SNorm);
        break;

    case QOpenGLTexture::FormatClass_8Bit:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::R8U
                             || viewFormat == QOpenGLTexture::R8I
                             || viewFormat == QOpenGLTexture::R8_UNorm
                             || viewFormat == QOpenGLTexture::R8_SNorm);
        break;

    case QOpenGLTexture::FormatClass_RGTC1_R:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::R_ATI1N_UNorm
                             || viewFormat == QOpenGLTexture::R_ATI1N_SNorm);
        break;

    case QOpenGLTexture::FormatClass_RGTC2_RG:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RG_ATI2N_UNorm
                             || viewFormat == QOpenGLTexture::RG_ATI2N_SNorm);
        break;

    case QOpenGLTexture::FormatClass_BPTC_Unorm:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGB_BP_UNorm
                             || viewFormat == QOpenGLTexture::SRGB_BP_UNorm);
        break;

    case QOpenGLTexture::FormatClass_BPTC_Float:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGB_BP_UNSIGNED_FLOAT
                             || viewFormat == QOpenGLTexture::RGB_BP_SIGNED_FLOAT);
        break;

    case QOpenGLTexture::FormatClass_S3TC_DXT1_RGB:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGB_DXT1
                             || viewFormat == QOpenGLTexture::SRGB_DXT1);
        break;

    case QOpenGLTexture::FormatClass_S3TC_DXT1_RGBA:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGBA_DXT1
                             || viewFormat == QOpenGLTexture::SRGB_Alpha_DXT1);
        break;

    case QOpenGLTexture::FormatClass_S3TC_DXT3_RGBA:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGBA_DXT3
                             || viewFormat == QOpenGLTexture::SRGB_Alpha_DXT3);
        break;

    case QOpenGLTexture::FormatClass_S3TC_DXT5_RGBA:
        viewFormatCompatible = (viewFormat == QOpenGLTexture::RGBA_DXT5
                             || viewFormat == QOpenGLTexture::SRGB_Alpha_DXT5);
        break;

    case QOpenGLTexture::FormatClass_Unique:
        viewFormatCompatible = (viewFormat == format);
        break;
    }

    if (!viewFormatCompatible) {
        qWarning("QOpenGLTexture::createTextureView(): Incompatible source and view formats");
        return nullptr;
    }


    // Create a view
    QOpenGLTexture *view = new QOpenGLTexture(viewTarget);
    view->setFormat(viewFormat);
    view->create();
    view->d_ptr->textureView = true;
    texFuncs->glTextureView(view->textureId(), viewTarget, textureId, viewFormat,
                            minimumMipmapLevel, maximumMipmapLevel - minimumMipmapLevel + 1,
                            minimumLayer, maximumLayer - minimumLayer + 1);
    return view;
}

//  from src/opengl/qopengltexture.cpp, line 269, as _ZNK21QOpenGLTexturePrivate17evaluateMipLevelsEv
inline int QOpenGLTexturePrivate::evaluateMipLevels() const
{
    switch (target) {
    case QOpenGLTexture::Target1D:
    case QOpenGLTexture::Target1DArray:
    case QOpenGLTexture::Target2D:
    case QOpenGLTexture::Target2DArray:
    case QOpenGLTexture::Target3D:
    case QOpenGLTexture::TargetCubeMap:
    case QOpenGLTexture::TargetCubeMapArray:
        return qMin(maximumMipLevelCount(), qMax(1, requestedMipLevels));

    case QOpenGLTexture::TargetRectangle:
    case QOpenGLTexture::Target2DMultisample:
    case QOpenGLTexture::Target2DMultisampleArray:
    case QOpenGLTexture::TargetBuffer:
    default:
        return 1;
    }
}

//  from src/opengl/qopengltexture.cpp, line 462, as _ZNK21QOpenGLTexturePrivate23isUsingImmutableStorageEv
inline bool QOpenGLTexturePrivate::isUsingImmutableStorage() const
{
    // Use immutable storage whenever possible, falling back to mutable
    // Note that if multisample textures are not supported at all, we'll still fail into
    // the mutable storage allocation
    return isSizedTextureFormat(format)
            && (isTextureTargetMultisample(target)
                ? features.testFlag(QOpenGLTexture::ImmutableMultisampleStorage)
                : features.testFlag(QOpenGLTexture::ImmutableStorage));
}
//  -----------------------------------------------------------------------

//  QOpenGLTexturePrivate::QOpenGLTexturePrivate(QOpenGLTexture::Target
//      textureTarget, QOpenGLTexture *qq)
extern "C" Q_DECL_EXPORT
QOpenGLTexturePrivate *ritual_ZN21QOpenGLTexturePrivateC1EN14QOpenGLTexture6TargetEPS0_(
    QOpenGLTexture::Target textureTarget,
    QOpenGLTexture *qq) {
  return new QOpenGLTexturePrivate(textureTarget, qq);
}

//  QOpenGLTexturePrivate::~QOpenGLTexturePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivateD1Ev(QOpenGLTexturePrivate *self) {
  delete self;
}

//  QOpenGLTexture *QOpenGLTexturePrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZN21QOpenGLTexturePrivate6q_funcEv(
    QOpenGLTexturePrivate *self) {
  return self->q_func();
}

//  const QOpenGLTexture *QOpenGLTexturePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLTexture *ritual_ZNK21QOpenGLTexturePrivate6q_funcEv(
    const QOpenGLTexturePrivate *self) {
  return self->q_func();
}

//  void QOpenGLTexturePrivate::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate7destroyEv(
    QOpenGLTexturePrivate *self) {
  self->destroy();
}

//  void QOpenGLTexturePrivate::bind()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate4bindEv(QOpenGLTexturePrivate *self) {
  self->bind();
}

//  void QOpenGLTexturePrivate::bind(uint unit,
//      QOpenGLTexture::TextureUnitReset reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate4bindEjN14QOpenGLTexture16TextureUnitResetE(
    QOpenGLTexturePrivate *self,
    uint unit,
    QOpenGLTexture::TextureUnitReset reset) {
  self->bind(unit, reset);
}

//  void QOpenGLTexturePrivate::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate7releaseEv(
    QOpenGLTexturePrivate *self) {
  self->release();
}

//  void QOpenGLTexturePrivate::release(uint unit,
//      QOpenGLTexture::TextureUnitReset reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate7releaseEjN14QOpenGLTexture16TextureUnitResetE(
    QOpenGLTexturePrivate *self,
    uint unit,
    QOpenGLTexture::TextureUnitReset reset) {
  self->release(unit, reset);
}

//  bool QOpenGLTexturePrivate::isBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLTexturePrivate7isBoundEv(
    const QOpenGLTexturePrivate *self) {
  return self->isBound();
}

//  bool QOpenGLTexturePrivate::isBound(uint unit) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLTexturePrivate7isBoundEj(
    const QOpenGLTexturePrivate *self,
    uint unit) {
  return self->isBound(unit);
}

//  void QOpenGLTexturePrivate::allocateStorage(QOpenGLTexture::PixelFormat
//      pixelFormat, QOpenGLTexture::PixelType pixelType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate15allocateStorageEN14QOpenGLTexture11PixelFormatENS0_9PixelTypeE(
    QOpenGLTexturePrivate *self,
    QOpenGLTexture::PixelFormat pixelFormat,
    QOpenGLTexture::PixelType pixelType) {
  self->allocateStorage(pixelFormat, pixelType);
}

//  void
//      QOpenGLTexturePrivate::allocateMutableStorage(QOpenGLTexture::PixelFo
//      rmat pixelFormat, QOpenGLTexture::PixelType pixelType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate22allocateMutableStorageEN14QOpenGLTexture11PixelFormatENS0_9PixelTypeE(
    QOpenGLTexturePrivate *self,
    QOpenGLTexture::PixelFormat pixelFormat,
    QOpenGLTexture::PixelType pixelType) {
  self->allocateMutableStorage(pixelFormat, pixelType);
}

//  void QOpenGLTexturePrivate::allocateImmutableStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate24allocateImmutableStorageEv(
    QOpenGLTexturePrivate *self) {
  self->allocateImmutableStorage();
}

//  void QOpenGLTexturePrivate::setData(int mipLevel, int layer, int
//      layerCount, QOpenGLTexture::CubeMapFace cubeFace,
//      QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType
//      sourceType, const void *data, const QOpenGLPixelTransferOptions
//      *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate7setDataEiiiN14QOpenGLTexture11CubeMapFaceENS0_11PixelFormatENS0_9PixelTypeEPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTexturePrivate *self,
    int mipLevel,
    int layer,
    int layerCount,
    QOpenGLTexture::CubeMapFace cubeFace,
    QOpenGLTexture::PixelFormat sourceFormat,
    QOpenGLTexture::PixelType sourceType,
    const void *data,
    const QOpenGLPixelTransferOptions *const options) {
  self->setData(
      mipLevel,
      layer,
      layerCount,
      cubeFace,
      sourceFormat,
      sourceType,
      data,
      options);
}

//  void QOpenGLTexturePrivate::setData(int xOffset, int yOffset, int
//      zOffset, int width, int height, int depth, int mipLevel, int layer,
//      int layerCount, QOpenGLTexture::CubeMapFace cubeFace,
//      QOpenGLTexture::PixelFormat sourceFormat, QOpenGLTexture::PixelType
//      sourceType, const void *data, const QOpenGLPixelTransferOptions
//      *const options)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate7setDataEiiiiiiiiiN14QOpenGLTexture11CubeMapFaceENS0_11PixelFormatENS0_9PixelTypeEPKvPK27QOpenGLPixelTransferOptions(
    QOpenGLTexturePrivate *self,
    int xOffset,
    int yOffset,
    int zOffset,
    int width,
    int height,
    int depth,
    int mipLevel,
    int layer,
    int layerCount,
    QOpenGLTexture::CubeMapFace cubeFace,
    QOpenGLTexture::PixelFormat sourceFormat,
    QOpenGLTexture::PixelType sourceType,
    const void *data,
    const QOpenGLPixelTransferOptions *const options) {
  self->setData(
      xOffset,
      yOffset,
      zOffset,
      width,
      height,
      depth,
      mipLevel,
      layer,
      layerCount,
      cubeFace,
      sourceFormat,
      sourceType,
      data,
      options);
}

//  void QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::WrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate11setWrapModeEN14QOpenGLTexture8WrapModeE(
    QOpenGLTexturePrivate *self,
    QOpenGLTexture::WrapMode mode) {
  self->setWrapMode(mode);
}

//  void
//      QOpenGLTexturePrivate::setWrapMode(QOpenGLTexture::CoordinateDirectio
//      n direction, QOpenGLTexture::WrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTexturePrivate11setWrapModeEN14QOpenGLTexture19CoordinateDirectionENS0_8WrapModeE(
    QOpenGLTexturePrivate *self,
    QOpenGLTexture::CoordinateDirection direction,
    QOpenGLTexture::WrapMode mode) {
  self->setWrapMode(direction, mode);
}

//  QOpenGLTexture::WrapMode
//      QOpenGLTexturePrivate::wrapMode(QOpenGLTexture::CoordinateDirection
//      direction) const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::WrapMode ritual_ZNK21QOpenGLTexturePrivate8wrapModeEN14QOpenGLTexture19CoordinateDirectionE(
    const QOpenGLTexturePrivate *self,
    QOpenGLTexture::CoordinateDirection direction) {
  return self->wrapMode(direction);
}

//  QOpenGLTexture
//      *QOpenGLTexturePrivate::createTextureView(QOpenGLTexture::Target
//      target, QOpenGLTexture::TextureFormat viewFormat, int
//      minimumMipmapLevel, int maximumMipmapLevel, int minimumLayer, int
//      maximumLayer) const
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZNK21QOpenGLTexturePrivate17createTextureViewEN14QOpenGLTexture6TargetENS0_13TextureFormatEiiii(
    const QOpenGLTexturePrivate *self,
    QOpenGLTexture::Target target,
    QOpenGLTexture::TextureFormat viewFormat,
    int minimumMipmapLevel,
    int maximumMipmapLevel,
    int minimumLayer,
    int maximumLayer) {
  return self->createTextureView(
      target,
      viewFormat,
      minimumMipmapLevel,
      maximumMipmapLevel,
      minimumLayer,
      maximumLayer);
}

//  int QOpenGLTexturePrivate::evaluateMipLevels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QOpenGLTexturePrivate17evaluateMipLevelsEv(
    const QOpenGLTexturePrivate *self) {
  return self->evaluateMipLevels();
}

//  int QOpenGLTexturePrivate::maximumMipLevelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QOpenGLTexturePrivate20maximumMipLevelCountEv(
    const QOpenGLTexturePrivate *self) {
  return self->maximumMipLevelCount();
}

//  int QOpenGLTexturePrivate::mipLevelSize(int mipLevel, int baseLevelSize)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QOpenGLTexturePrivate12mipLevelSizeEii(
    int mipLevel,
    int baseLevelSize) {
  return QOpenGLTexturePrivate::mipLevelSize(mipLevel, baseLevelSize);
}

//  bool QOpenGLTexturePrivate::isUsingImmutableStorage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLTexturePrivate23isUsingImmutableStorageEv(
    const QOpenGLTexturePrivate *self) {
  return self->isUsingImmutableStorage();
}

#endif  // !defined(QT_NO_OPENGL)
