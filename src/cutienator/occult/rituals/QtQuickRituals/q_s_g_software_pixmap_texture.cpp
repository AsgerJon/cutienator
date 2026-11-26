//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaptexture_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSGSoftwarePixmapTexture'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 3 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QSGSoftwarePixmapTexture.cpp, line 1, as moc:QSGSoftwarePixmapTexture
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN24QSGSoftwarePixmapTextureE_t {};
} // unnamed namespace

template <> constexpr inline auto QSGSoftwarePixmapTexture::qt_create_metaobjectdata<qt_meta_tag_ZN24QSGSoftwarePixmapTextureE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSGSoftwarePixmapTexture"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSGSoftwarePixmapTexture, qt_meta_tag_ZN24QSGSoftwarePixmapTextureE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSGSoftwarePixmapTexture::staticMetaObject = { {
    QMetaObject::SuperData::link<QSGTexture::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSGSoftwarePixmapTextureE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSGSoftwarePixmapTextureE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN24QSGSoftwarePixmapTextureE_t>.metaTypes,
    nullptr
} };

void QSGSoftwarePixmapTexture::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSGSoftwarePixmapTexture *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QSGSoftwarePixmapTexture::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSGSoftwarePixmapTexture::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QSGSoftwarePixmapTextureE_t>.strings))
        return static_cast<void*>(this);
    return QSGTexture::qt_metacast(_clname);
}

int QSGSoftwarePixmapTexture::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSGTexture::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 38, as _ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv
inline bool QSGSoftwarePixmapTexture::hasMipmaps() const
{
    return false;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 28, as _ZNK24QSGSoftwarePixmapTexture11textureSizeEv
inline QSize QSGSoftwarePixmapTexture::textureSize() const
{
    return m_pixmap.size();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 43, as _ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv
inline qint64 QSGSoftwarePixmapTexture::comparisonKey() const
{
    return 0;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 33, as _ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv
inline bool QSGSoftwarePixmapTexture::hasAlphaChannel() const
{
    return m_pixmap.hasAlphaChannel();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 10, as _ZN24QSGSoftwarePixmapTextureC1ERK6QImagej
inline QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QImage &image, uint flags)
{
    // Prevent pixmap format conversion to reduce memory consumption
    // and surprises in calling code. (See QTBUG-47328)
    if (flags & QSGRenderContext::CreateTexture_Alpha) {
        //If texture should have an alpha
        m_pixmap = QPixmap::fromImage(image, Qt::NoFormatConversion);
    } else {
        //Force opaque texture
        m_pixmap = QPixmap::fromImage(image.convertToFormat(QImage::Format_RGB32), Qt::NoFormatConversion);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 23, as _ZN24QSGSoftwarePixmapTextureC1ERK7QPixmap
inline QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QPixmap &pixmap)
    : m_pixmap(pixmap)
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QSGSoftwarePixmapTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QSGSoftwarePixmapTexture10metaObjectEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->metaObject();
}

//  void *QSGSoftwarePixmapTexture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QSGSoftwarePixmapTexture11qt_metacastEPKc(
    QSGSoftwarePixmapTexture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGSoftwarePixmapTexture::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QSGSoftwarePixmapTexture11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGSoftwarePixmapTexture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGSoftwarePixmapTexture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QSGSoftwarePixmapTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGSoftwarePixmapTexture::tr(s, c, n));
}

//  QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QImage &image,
//      uint flags)
extern "C" Q_DECL_EXPORT
QSGSoftwarePixmapTexture *ritual_ZN24QSGSoftwarePixmapTextureC1ERK6QImagej(
    const QImage *image,
    uint flags) {
  return new QSGSoftwarePixmapTexture(*image, flags);
}

//  QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QSGSoftwarePixmapTexture *ritual_ZN24QSGSoftwarePixmapTextureC1ERK7QPixmap(
    const QPixmap *pixmap) {
  return new QSGSoftwarePixmapTexture(*pixmap);
}

//  qint64 QSGSoftwarePixmapTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->comparisonKey();
}

//  QSize QSGSoftwarePixmapTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK24QSGSoftwarePixmapTexture11textureSizeEv(
    const QSGSoftwarePixmapTexture *self) {
  return new QSize(self->textureSize());
}

//  bool QSGSoftwarePixmapTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGSoftwarePixmapTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->hasMipmaps();
}

//  const QPixmap &QSGSoftwarePixmapTexture::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK24QSGSoftwarePixmapTexture6pixmapEv(
    const QSGSoftwarePixmapTexture *self) {
  return new QPixmap(self->pixmap());
}

//  qint64 QSGSoftwarePixmapTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK24QSGSoftwarePixmapTexture13comparisonKeyEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->QSGSoftwarePixmapTexture::comparisonKey();
}

//  QSize QSGSoftwarePixmapTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK24QSGSoftwarePixmapTexture11textureSizeEv(
    const QSGSoftwarePixmapTexture *self) {
  return new QSize(self->QSGSoftwarePixmapTexture::textureSize());
}

//  bool QSGSoftwarePixmapTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QSGSoftwarePixmapTexture15hasAlphaChannelEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->QSGSoftwarePixmapTexture::hasAlphaChannel();
}

//  bool QSGSoftwarePixmapTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QSGSoftwarePixmapTexture10hasMipmapsEv(
    const QSGSoftwarePixmapTexture *self) {
  return self->QSGSoftwarePixmapTexture::hasMipmaps();
}
