//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: the line pulling in 'qrhivulkan_p.h', taken from Qt's
//  'qrhi.cpp' with the rest, stands under '__has_include(<vulkan/vulkan.h>)'
//  as well, because that header names Vulkan's types ('VkBuffer') and a
//  machine with Qt built for Vulkan may lack Vulkan's headers; no ritual
//  here needs it. The line pulling in 'qrhid3d12_p.h' stands under
//  '__has_include(<D3D12MemAlloc.h>)': that header includes
//  'D3D12MemAlloc.h', a library Qt keeps in its source and never installs,
//  and no ritual here needs it. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhi_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtGui/private/qrhinull_p.h>
#ifndef QT_NO_OPENGL
#include <QtGui/private/qrhigles2_p.h>
#endif
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#if __has_include(<D3D12MemAlloc.h>)
#include <QtGui/private/qrhid3d12_p.h>
#endif
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
#endif
#include <limits>
#include <memory>
#include <QtGui/private/qrhigles2_p.h>
#include <QtGui/QOffscreenSurface>
#include <QtGui/QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformopenglcontext.h>
#include <QtCore/qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 8635, as _ZNK18QRhiImplementation18isCompressedFormatEN11QRhiTexture6FormatE
inline bool QRhiImplementation::isCompressedFormat(QRhiTexture::Format format) const
{
    return (format >= QRhiTexture::BC1 && format <= QRhiTexture::BC7)
            || (format >= QRhiTexture::ETC2_RGB8 && format <= QRhiTexture::ETC2_RGBA8)
            || (format >= QRhiTexture::ASTC_4x4 && format <= QRhiTexture::ASTC_12x12);
}

//  from src/gui/rhi/qrhigles2.cpp, line 6157, as _ZN13QGles2TextureD1Ev
inline QGles2Texture::~QGles2Texture()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6162, as _ZN13QGles2Texture7destroyEv
inline void QGles2Texture::destroy()
{
    if (!texture)
        return;

    QRhiGles2::DeferredReleaseEntry e;
    e.type = QRhiGles2::DeferredReleaseEntry::Texture;

    e.texture.texture = texture;

    texture = 0;
    specified = false;
    zeroInitialized = false;

    QRHI_RES_RHI(QRhiGles2);
    if (rhiD) {
        if (owns)
            rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 6287, as _ZN13QGles2Texture6createEv
inline bool QGles2Texture::create()
{
    QSize size;
    if (!prepareCreate(&size))
        return false;

    QRHI_RES_RHI(QRhiGles2);
    rhiD->f->glGenTextures(1, &texture);

    const bool isCube = m_flags.testFlag(CubeMap);
    const bool isArray = m_flags.testFlag(QRhiTexture::TextureArray);
    const bool is3D = m_flags.testFlag(ThreeDimensional);
    const bool hasMipMaps = m_flags.testFlag(MipMapped);
    const bool isCompressed = rhiD->isCompressedFormat(m_format);
    const bool is1D = m_flags.testFlag(OneDimensional);

    if (!isCompressed) {
        rhiD->f->glBindTexture(target, texture);
        if (!m_flags.testFlag(UsedWithLoadStore)) {
            if (is1D) {
                for (int level = 0; level < mipLevelCount; ++level) {
                    const QSize mipSize = rhiD->q->sizeForMipLevel(level, size);
                    if (isArray)
                        rhiD->f->glTexImage2D(target, level, GLint(glintformat), mipSize.width(),
                                              qMax(0, m_arraySize), 0, glformat, gltype, nullptr);
                    else
                        rhiD->glTexImage1D(target, level, GLint(glintformat), mipSize.width(), 0,
                                           glformat, gltype, nullptr);
                }
            } else if (isArray) {
                const int layerCount = qMax(0, m_arraySize);
                if (hasMipMaps) {
                    for (int level = 0; level != mipLevelCount; ++level) {
                        const QSize mipSize = rhiD->q->sizeForMipLevel(level, size);
                        rhiD->f->glTexImage3D(target, level, GLint(glintformat), mipSize.width(), mipSize.height(), layerCount,
                                              0, glformat, gltype, nullptr);
                    }
                } else {
                    rhiD->f->glTexImage3D(target, 0, GLint(glintformat), size.width(), size.height(), layerCount,
                                          0, glformat, gltype, nullptr);
                }
            } else if (is3D) {
                if (hasMipMaps) {
                    const int depth = qMax(1, m_depth);
                    for (int level = 0; level != mipLevelCount; ++level) {
                        const QSize mipSize = rhiD->q->sizeForMipLevel(level, size);
                        const int mipDepth = rhiD->q->sizeForMipLevel(level, QSize(depth, depth)).width();
                        rhiD->f->glTexImage3D(target, level, GLint(glintformat), mipSize.width(), mipSize.height(), mipDepth,
                                              0, glformat, gltype, nullptr);
                    }
                } else {
                    rhiD->f->glTexImage3D(target, 0, GLint(glintformat), size.width(), size.height(), qMax(1, m_depth),
                                          0, glformat, gltype, nullptr);
                }
            } else if (hasMipMaps || isCube) {
                const GLenum faceTargetBase = isCube ? GL_TEXTURE_CUBE_MAP_POSITIVE_X : target;
                for (int layer = 0, layerCount = isCube ? 6 : 1; layer != layerCount; ++layer) {
                    for (int level = 0; level != mipLevelCount; ++level) {
                        const QSize mipSize = rhiD->q->sizeForMipLevel(level, size);
                        rhiD->f->glTexImage2D(faceTargetBase + uint(layer), level, GLint(glintformat),
                                              mipSize.width(), mipSize.height(), 0,
                                              glformat, gltype, nullptr);
                    }
                }
            } else {
                // 2D texture. For multisample textures the GLES 3.1
                // glStorage2DMultisample must be used for portability.
                if (samples > 1 && rhiD->caps.multisampledTexture) {
                    // internal format must be sized
                    rhiD->f->glTexStorage2DMultisample(target, samples, glsizedintformat,
                                                       size.width(), size.height(), GL_TRUE);
                } else {
                    rhiD->f->glTexImage2D(target, 0, GLint(glintformat), size.width(), size.height(),
                                          0, glformat, gltype, nullptr);
                }
            }
        } else {
            // Must be specified with immutable storage functions otherwise
            // bindImageTexture may fail. Also, the internal format must be a
            // sized format here.
            if (is1D && !isArray)
                rhiD->glTexStorage1D(target, mipLevelCount, glsizedintformat, size.width());
            else if (!is1D && (is3D || isArray))
                rhiD->f->glTexStorage3D(target, mipLevelCount, glsizedintformat, size.width(), size.height(),
                                        is3D ? qMax(1, m_depth) : qMax(0, m_arraySize));
            else if (samples > 1)
                rhiD->f->glTexStorage2DMultisample(target, samples, glsizedintformat,
                                                   size.width(), size.height(), GL_TRUE);
            else
                rhiD->f->glTexStorage2D(target, mipLevelCount, glsizedintformat, size.width(),
                                        is1D ? qMax(0, m_arraySize) : size.height());
        }
        // Make sure the min filter is set to something non-mipmap-based already
        // here, given the ridiculous default of GL. It is changed based on
        // the sampler later, but there could be cases when one pulls the native
        // object out via nativeTexture() right away.
        rhiD->f->glTexParameteri(target, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        specified = true;
    } else {
        // Cannot use glCompressedTexImage2D without valid data, so defer.
        // Compressed textures will not be used as render targets so this is
        // not an issue.
        specified = false;
    }

    if (rhiD->glObjectLabel)
        rhiD->glObjectLabel(GL_TEXTURE, texture, -1, m_objectName.constData());

    owns = true;

    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6402, as _ZN13QGles2Texture10createFromEN11QRhiTexture13NativeTextureE
inline bool QGles2Texture::createFrom(QRhiTexture::NativeTexture src)
{
    const uint textureId = uint(src.object);
    if (textureId == 0)
        return false;

    if (!prepareCreate())
        return false;

    texture = textureId;
    specified = true;
    zeroInitialized = true;

    owns = false;

    generation += 1;
    QRHI_RES_RHI(QRhiGles2);
    rhiD->registerResource(this);
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6423, as _ZN13QGles2Texture13nativeTextureEv
inline QRhiTexture::NativeTexture QGles2Texture::nativeTexture()
{
    return {texture, 0};
}
//  -----------------------------------------------------------------------

//  A QGles2Texture that Python can take functions over in. Every QGles2Texture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2TextureCall0)(const void *, int *);
typedef bool (*CuteQGles2TextureCall1)(const void *, int *);
typedef bool (*CuteQGles2TextureCall2)(const void *, const QRhiTexture::NativeTexture *, int *);
typedef const QRhiTexture::NativeTexture * (*CuteQGles2TextureCall3)(const void *, int *);
typedef int (*CuteQGles2TextureCall4)(const void *, int *);
typedef void (*CuteQGles2TextureCall5)(const void *, int, int *);
class CuteQGles2Texture : public QGles2Texture {
public:
  using QGles2Texture::QGles2Texture;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture10createFromENS_13NativeTextureE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture13nativeTextureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture15setNativeLayoutEi")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QGles2Texture::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2TextureCall0 call = reinterpret_cast<CuteQGles2TextureCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2Texture::destroy();
  }

  //  bool QGles2Texture::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2TextureCall1 call = reinterpret_cast<CuteQGles2TextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2Texture::create();
  }

  //  bool QGles2Texture::createFrom(NativeTexture src)
  bool createFrom(QRhiTexture::NativeTexture src) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2TextureCall2 call = reinterpret_cast<CuteQGles2TextureCall2>(taken[2]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QGles2Texture::createFrom(src);
  }

  //  NativeTexture QGles2Texture::nativeTexture()
  QRhiTexture::NativeTexture nativeTexture() override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2TextureCall3 call = reinterpret_cast<CuteQGles2TextureCall3>(taken[3]);
      const QRhiTexture::NativeTexture * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGles2Texture::nativeTexture();
  }

  //  QRhiResource::Type QRhiTexture::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGles2TextureCall4 call = reinterpret_cast<CuteQGles2TextureCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTexture::resourceType();
  }

  //  void QRhiTexture::setNativeLayout(int layout)
  void setNativeLayout(int layout) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGles2TextureCall5 call = reinterpret_cast<CuteQGles2TextureCall5>(taken[5]);
      call(this, layout, &handled);
      if (handled) return;
    }
    QRhiTexture::setNativeLayout(layout);
  }
};

//  QGles2Texture::~QGles2Texture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGles2TextureD1Ev(QGles2Texture *self) {
  delete self;
}

//  void QGles2Texture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGles2Texture7destroyEv(QGles2Texture *self) {
  self->destroy();
}

//  bool QGles2Texture::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QGles2Texture6createEv(QGles2Texture *self) {
  return self->create();
}

//  bool QGles2Texture::createFrom(NativeTexture src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QGles2Texture10createFromEN11QRhiTexture13NativeTextureE(
    QGles2Texture *self,
    const QRhiTexture::NativeTexture *src) {
  return self->createFrom(*src);
}

//  NativeTexture QGles2Texture::nativeTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture::NativeTexture *ritual_ZN13QGles2Texture13nativeTextureEv(
    QGles2Texture *self) {
  return new QRhiTexture::NativeTexture(self->nativeTexture());
}

//  a Python function taken by a CuteQGles2Texture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2Texture(
    QGles2Texture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2Texture *>(self)->take(key, call);
}

//  void QGles2Texture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGles2Texture7destroyEv(QGles2Texture *self) {
  self->QGles2Texture::destroy();
}

//  NativeTexture QGles2Texture::nativeTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture::NativeTexture *ritual_own_ZN13QGles2Texture13nativeTextureEv(
    QGles2Texture *self) {
  return new QRhiTexture::NativeTexture(
      self->QGles2Texture::nativeTexture());
}

#endif  // QT_CONFIG(opengl)
