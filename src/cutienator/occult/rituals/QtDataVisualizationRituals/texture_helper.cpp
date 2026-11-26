//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/texturehelper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/texturehelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QPainter>
#include <QtGui/QOpenGLContext>
#include <QtGui/QOffscreenSurface>
#include <QtGui/qquaternion.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QRegularExpression>
#include <QtCore/QLocale>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 17, as local:utils.cpp:NUM_IN_POWER
#define NUM_IN_POWER(y, x) for (;y<x;y<<=1)

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 18, as local:utils.cpp:MIN_POWER
#define MIN_POWER 2

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 25, as _ZN5Utils20getNearestPowerOfTwoEj
inline GLuint Utils::getNearestPowerOfTwo(GLuint value)
{
    GLuint powOfTwoValue = MIN_POWER;
    NUM_IN_POWER(powOfTwoValue, value);
    return powOfTwoValue;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 37, as _ZN13TextureHelperD1Ev
inline TextureHelper::~TextureHelper()
{
#if !QT_CONFIG(opengles2)
    delete m_openGlFunctions_2_1;
#endif
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 133, as _ZN13TextureHelper20createCubeMapTextureERK6QImageb
inline GLuint TextureHelper::createCubeMapTexture(const QImage &image, bool useTrilinearFiltering)
{
    if (image.isNull())
        return 0;

    GLuint textureId;
    glGenTextures(1, &textureId);
    glBindTexture(GL_TEXTURE_CUBE_MAP, textureId);
    QImage glTexture = convertToGLFormat(image);
    glTexImage2D(GL_TEXTURE_CUBE_MAP, 0, GL_RGBA, glTexture.width(), glTexture.height(),
                 0, GL_RGBA, GL_UNSIGNED_BYTE, glTexture.bits());
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    if (useTrilinearFiltering) {
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
        glGenerateMipmap(GL_TEXTURE_CUBE_MAP);
    } else {
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    }
    glBindTexture(GL_TEXTURE_2D, 0);
    return textureId;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 217, as _ZN13TextureHelper27createCursorPositionTextureERK5QSizeRj
inline GLuint TextureHelper::createCursorPositionTexture(const QSize &size, GLuint &frameBuffer)
{
    GLuint textureid;
    glGenTextures(1, &textureid);
    glBindTexture(GL_TEXTURE_2D, textureid);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, size.width(), size.height(), 0, GL_RGBA,
                 GL_UNSIGNED_BYTE, NULL);
    glBindTexture(GL_TEXTURE_2D, 0);

    glGenFramebuffers(1, &frameBuffer);
    glBindFramebuffer(GL_FRAMEBUFFER, frameBuffer);
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D,
                           textureid, 0);

    GLenum status = glCheckFramebufferStatus(GL_FRAMEBUFFER);
    if (status != GL_FRAMEBUFFER_COMPLETE) {
        qCritical() << "Cursor position mapper frame buffer creation failed:" << status;
        glDeleteTextures(1, &textureid);
        textureid = 0;
    }
    glBindFramebuffer(GL_FRAMEBUFFER, 0);

    return textureid;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 325, as _ZN13TextureHelper13deleteTextureEPj
inline void TextureHelper::deleteTexture(GLuint *texture)
{
    if (texture && *texture) {
        if (QOpenGLContext::currentContext())
            glDeleteTextures(1, texture);
        *texture = 0;
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 334, as _ZN13TextureHelper17convertToGLFormatERK6QImage
inline QImage TextureHelper::convertToGLFormat(const QImage &srcImage)
{
    QImage res(srcImage.size(), QImage::Format_ARGB32);
    convertToGLFormatHelper(res, srcImage.convertToFormat(QImage::Format_ARGB32), GL_RGBA);
    return res;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 341, as _ZN13TextureHelper23convertToGLFormatHelperER6QImageRKS0_j
inline void TextureHelper::convertToGLFormatHelper(QImage &dstImage, const QImage &srcImage,
                                            GLenum texture_format)
{
    Q_ASSERT(dstImage.depth() == 32);
    Q_ASSERT(srcImage.depth() == 32);

    if (dstImage.size() != srcImage.size()) {
        int target_width = dstImage.width();
        int target_height = dstImage.height();
        float sx = target_width / float(srcImage.width());
        float sy = target_height / float(srcImage.height());

        quint32 *dest = (quint32 *) dstImage.scanLine(0); // NB! avoid detach here
        uchar *srcPixels = (uchar *) srcImage.scanLine(srcImage.height() - 1);
        int sbpl = srcImage.bytesPerLine();
        int dbpl = dstImage.bytesPerLine();

        int ix = int(0x00010000 / sx);
        int iy = int(0x00010000 / sy);

        quint32 basex = int(0.5 * ix);
        quint32 srcy = int(0.5 * iy);

        // scale, swizzle and mirror in one loop
        while (target_height--) {
            const uint *src = (const quint32 *) (srcPixels - (srcy >> 16) * sbpl);
            int srcx = basex;
            for (int x=0; x<target_width; ++x) {
                dest[x] = qt_gl_convertToGLFormatHelper(src[srcx >> 16], texture_format);
                srcx += ix;
            }
            dest = (quint32 *)(((uchar *) dest) + dbpl);
            srcy += iy;
        }
    } else {
        const int width = srcImage.width();
        const int height = srcImage.height();
        const uint *p = (const uint*) srcImage.scanLine(srcImage.height() - 1);
        uint *q = (uint*) dstImage.scanLine(0);

#if !QT_CONFIG(opengles2)
        if (texture_format == GL_BGRA) {
#else
        if (texture_format == GL_BGRA8_EXT) {
#endif
            if (QSysInfo::ByteOrder == QSysInfo::BigEndian) {
                // mirror + swizzle
                for (int i=0; i < height; ++i) {
                    const uint *end = p + width;
                    while (p < end) {
                        *q = ((*p << 24) & 0xff000000)
                                | ((*p >> 24) & 0x000000ff)
                                | ((*p << 8) & 0x00ff0000)
                                | ((*p >> 8) & 0x0000ff00);
                        p++;
                        q++;
                    }
                    p -= 2 * width;
                }
            } else {
                const uint bytesPerLine = srcImage.bytesPerLine();
                for (int i=0; i < height; ++i) {
                    memcpy(q, p, bytesPerLine);
                    q += width;
                    p -= width;
                }
            }
        } else {
            if (QSysInfo::ByteOrder == QSysInfo::BigEndian) {
                for (int i=0; i < height; ++i) {
                    const uint *end = p + width;
                    while (p < end) {
                        *q = (*p << 8) | ((*p >> 24) & 0xff);
                        p++;
                        q++;
                    }
                    p -= 2 * width;
                }
            } else {
                for (int i=0; i < height; ++i) {
                    const uint *end = p + width;
                    while (p < end) {
                        *q = ((*p << 16) & 0xff0000) | ((*p >> 16) & 0xff) | (*p & 0xff00ff00);
                        p++;
                        q++;
                    }
                    p -= 2 * width;
                }
            }
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 434, as _ZN13TextureHelper29qt_gl_convertToGLFormatHelperEjj
inline QRgb TextureHelper::qt_gl_convertToGLFormatHelper(QRgb src_pixel, GLenum texture_format)
{
#if !QT_CONFIG(opengles2)
    if (texture_format == GL_BGRA) {
#else
    if (texture_format == GL_BGRA8_EXT) {
#endif
        if (QSysInfo::ByteOrder == QSysInfo::BigEndian) {
            return ((src_pixel << 24) & 0xff000000)
                    | ((src_pixel >> 24) & 0x000000ff)
                    | ((src_pixel << 8) & 0x00ff0000)
                    | ((src_pixel >> 8) & 0x0000ff00);
        } else {
            return src_pixel;
        }
    } else {  // GL_RGBA
        if (QSysInfo::ByteOrder == QSysInfo::BigEndian) {
            return (src_pixel << 8) | ((src_pixel >> 24) & 0xff);
        } else {
            return ((src_pixel << 16) & 0xff0000)
                    | ((src_pixel >> 16) & 0xff)
                    | (src_pixel & 0xff00ff00);
        }
    }
}
//  -----------------------------------------------------------------------

//  TextureHelper::~TextureHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TextureHelperD1Ev(TextureHelper *self) {
  delete self;
}

//  GLuint TextureHelper::createCubeMapTexture(const QImage &image, bool
//      useTrilinearFiltering)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN13TextureHelper20createCubeMapTextureERK6QImageb(
    TextureHelper *self,
    const QImage *image,
    bool useTrilinearFiltering) {
  return self->createCubeMapTexture(*image, useTrilinearFiltering);
}

//  GLuint TextureHelper::createCursorPositionTexture(const QSize &size,
//      GLuint &frameBuffer)
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN13TextureHelper27createCursorPositionTextureERK5QSizeRj(
    TextureHelper *self,
    const QSize *size,
    GLuint *frameBuffer) {
  return self->createCursorPositionTexture(*size, *frameBuffer);
}

//  void TextureHelper::deleteTexture(GLuint *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TextureHelper13deleteTextureEPj(
    TextureHelper *self,
    GLuint *texture) {
  self->deleteTexture(texture);
}

//  QImage TextureHelper::convertToGLFormat(const QImage &srcImage)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13TextureHelper17convertToGLFormatERK6QImage(
    TextureHelper *self,
    const QImage *srcImage) {
  return new QImage(self->convertToGLFormat(*srcImage));
}

//  void TextureHelper::convertToGLFormatHelper(QImage &dstImage, const
//      QImage &srcImage, GLenum texture_format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13TextureHelper23convertToGLFormatHelperER6QImageRKS0_j(
    TextureHelper *self,
    QImage *dstImage,
    const QImage *srcImage,
    GLenum texture_format) {
  self->convertToGLFormatHelper(*dstImage, *srcImage, texture_format);
}

//  QRgb TextureHelper::qt_gl_convertToGLFormatHelper(QRgb src_pixel, GLenum
//      texture_format)
extern "C" Q_DECL_EXPORT
QRgb ritual_ZN13TextureHelper29qt_gl_convertToGLFormatHelperEjj(
    TextureHelper *self,
    QRgb src_pixel,
    GLenum texture_format) {
  return self->qt_gl_convertToGLFormatHelper(src_pixel, texture_format);
}
