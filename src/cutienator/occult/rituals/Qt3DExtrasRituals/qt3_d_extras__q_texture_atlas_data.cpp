//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/private/qtextureatlas_p.h>
#include <Qt3DExtras/private/qtextureatlas_p_p.h>
#include <Qt3DRender/qtexturedata.h>
#include <Qt3DRender/qabstracttextureimage.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 16, as _ZN10Qt3DExtras17QTextureAtlasDataC1EiiN6QImage6FormatE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasData::QTextureAtlasData(int w, int h, QImage::Format fmt)
    : m_image(w, h, fmt)
{
    m_image.fill(0);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 22, as _ZN10Qt3DExtras17QTextureAtlasDataD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasData::~QTextureAtlasData()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 26, as _ZN10Qt3DExtras17QTextureAtlasData8addImageERKNS_12AtlasTextureERK6QImage
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QTextureAtlasData::addImage(const AtlasTexture &texture, const QImage &image)
{
    QMutexLocker lock(&m_mutex);

    Update update;
    update.textureInfo = texture;
    update.image = image;
    m_updates << update;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 36, as _ZN10Qt3DExtras17QTextureAtlasData22createUpdatedImageDataEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QByteArray QTextureAtlasData::createUpdatedImageData()
{
    m_mutex.lock();
    const QList<Update> updates = std::move(m_updates);
    m_mutex.unlock();

    // copy sub-images into the actual texture image
    for (const Update &update : updates) {
        const QImage &image = update.image;

        const int padding = update.textureInfo.padding;
        const QRect imgRect = update.textureInfo.position;
        const QRect alloc = imgRect.adjusted(-padding, -padding, padding, padding);

        // bytes per pixel
        if (image.depth() != m_image.depth()) {
            qWarning() << "[QTextureAtlas] Image depth does not match. Original =" << m_image.depth() << ", Sub-Image =" << image.depth();
            continue;
        }
        int bpp = image.depth() / 8;

        // copy image contents into texture image
        // use image border pixels to fill the padding region
        for (int y = alloc.top(); y <= alloc.bottom(); y++) {
            uchar *dstLine = m_image.scanLine(y);

            uchar *dstPadL = &dstLine[bpp * alloc.left()];
            uchar *dstPadR = &dstLine[bpp * imgRect.right()];
            uchar *dstImg  = &dstLine[bpp * imgRect.left()];

            // do padding with 0 in the upper/lower padding parts around the actual image
            if (y < imgRect.top() || y > imgRect.bottom()) {
                memset(dstPadL, 0, bpp * (imgRect.width() + 2 * padding));
                continue;
            }

            // copy left and right padding pixels
            memset(dstPadL, 0, bpp * padding);
            memset(dstPadR, 0, bpp * padding);

            // copy image scanline
            const int ySrc = qBound(0, y - imgRect.top(), image.height()-1);
            memcpy(dstImg, image.scanLine(ySrc), bpp * imgRect.width());
        }
    }

    return QByteArray(reinterpret_cast<const char*>(m_image.constBits()), m_image.sizeInBytes());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  Qt3DExtras::QTextureAtlasData::QTextureAtlasData(int w, int h,
//      QImage::Format fmt)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureAtlasData *ritual_ZN10Qt3DExtras17QTextureAtlasDataC1EiiN6QImage6FormatE(
    int w,
    int h,
    QImage::Format fmt) {
  return new Qt3DExtras::QTextureAtlasData(w, h, fmt);
}

//  Qt3DExtras::QTextureAtlasData::~QTextureAtlasData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QTextureAtlasDataD1Ev(
    Qt3DExtras::QTextureAtlasData *self) {
  delete self;
}

//  int Qt3DExtras::QTextureAtlasData::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras17QTextureAtlasData5widthEv(
    const Qt3DExtras::QTextureAtlasData *self) {
  return self->width();
}

//  int Qt3DExtras::QTextureAtlasData::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras17QTextureAtlasData6heightEv(
    const Qt3DExtras::QTextureAtlasData *self) {
  return self->height();
}

//  void Qt3DExtras::QTextureAtlasData::addImage(const AtlasTexture &texture,
//      const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QTextureAtlasData8addImageERKNS_12AtlasTextureERK6QImage(
    Qt3DExtras::QTextureAtlasData *self,
    const Qt3DExtras::AtlasTexture *texture,
    const QImage *image) {
  self->addImage(*texture, *image);
}

//  QByteArray Qt3DExtras::QTextureAtlasData::createUpdatedImageData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10Qt3DExtras17QTextureAtlasData22createUpdatedImageDataEv(
    Qt3DExtras::QTextureAtlasData *self) {
  return new QByteArray(self->createUpdatedImageData());
}
