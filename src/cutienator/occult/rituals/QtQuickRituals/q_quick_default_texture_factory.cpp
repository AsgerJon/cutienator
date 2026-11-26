//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickDefaultTextureFactory' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickpixmapcache_p.h>
#include <QtQuick/private/qquickimageprovider_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgtexturereader_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qimage_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qimagereader.h>
#include <QtGui/qpixmapcache.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qhash.h>
#include <QtCore/qfile.h>
#include <QtCore/qthread.h>
#include <QtCore/qmutex.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qscopeguard.h>
#if QT_CONFIG(qml_network)
#include <QtQml/qqmlnetworkaccessmanagerfactory.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/qsslerror.h>
#endif
#include <QtCore/private/qdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from QtQuick__QQuickDefaultTextureFactory.cpp, line 1, as moc:QQuickDefaultTextureFactory
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN27QQuickDefaultTextureFactoryE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickDefaultTextureFactory::qt_create_metaobjectdata<qt_meta_tag_ZN27QQuickDefaultTextureFactoryE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickDefaultTextureFactory"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickDefaultTextureFactory, qt_meta_tag_ZN27QQuickDefaultTextureFactoryE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickDefaultTextureFactory::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickTextureFactory::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQuickDefaultTextureFactoryE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQuickDefaultTextureFactoryE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN27QQuickDefaultTextureFactoryE_t>.metaTypes,
    nullptr
} };

void QQuickDefaultTextureFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickDefaultTextureFactory *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickDefaultTextureFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickDefaultTextureFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQuickDefaultTextureFactoryE_t>.strings))
        return static_cast<void*>(this);
    return QQuickTextureFactory::qt_metacast(_clname);
}

int QQuickDefaultTextureFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickTextureFactory::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/util/qquickpixmapcache.cpp, line 136, as _ZNK27QQuickDefaultTextureFactory13createTextureEP12QQuickWindow
inline QSGTexture *QQuickDefaultTextureFactory::createTexture(QQuickWindow *window) const
{
    QSGTexture *t = window->createTextureFromImage(im, QQuickWindow::TextureCanUseAtlas);
    static bool transient = qEnvironmentVariableIsSet("QSG_TRANSIENT_IMAGES");
    if (transient)
        const_cast<QQuickDefaultTextureFactory *>(this)->im = QImage();
    return t;
}

//  from ../qtdeclarative/src/quick/util/qquickpixmapcache.cpp, line 118, as _ZN27QQuickDefaultTextureFactoryC1ERK6QImage
inline QQuickDefaultTextureFactory::QQuickDefaultTextureFactory(const QImage &image)
{
    if (image.format() == QImage::Format_ARGB32_Premultiplied ||
        image.format() == QImage::Format_RGB32 ||
        image.format() == QImage::Format_RGBA16FPx4_Premultiplied ||
        image.format() == QImage::Format_RGBA16FPx4 ||
        image.format() == QImage::Format_RGBX16FPx4 ||
        image.format() == QImage::Format_RGBA32FPx4_Premultiplied ||
        image.format() == QImage::Format_RGBA32FPx4 ||
        image.format() == QImage::Format_RGBX32FPx4) {
        im = image;
    } else {
        im = image.convertToFormat(QImage::Format_ARGB32_Premultiplied);
    }
    size = im.size();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickDefaultTextureFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickDefaultTextureFactory10metaObjectEv(
    const QQuickDefaultTextureFactory *self) {
  return self->metaObject();
}

//  void *QQuickDefaultTextureFactory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQuickDefaultTextureFactory11qt_metacastEPKc(
    QQuickDefaultTextureFactory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDefaultTextureFactory::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQuickDefaultTextureFactory11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDefaultTextureFactory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDefaultTextureFactory::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuickDefaultTextureFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDefaultTextureFactory::tr(s, c, n));
}

//  QQuickDefaultTextureFactory::QQuickDefaultTextureFactory(const QImage &i)
extern "C" Q_DECL_EXPORT
QQuickDefaultTextureFactory *ritual_ZN27QQuickDefaultTextureFactoryC1ERK6QImage(
    const QImage *i) {
  return new QQuickDefaultTextureFactory(*i);
}

//  QSGTexture *QQuickDefaultTextureFactory::createTexture(QQuickWindow
//      *window) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK27QQuickDefaultTextureFactory13createTextureEP12QQuickWindow(
    const QQuickDefaultTextureFactory *self,
    QQuickWindow *window) {
  return self->createTexture(window);
}

//  QSize QQuickDefaultTextureFactory::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK27QQuickDefaultTextureFactory11textureSizeEv(
    const QQuickDefaultTextureFactory *self) {
  return new QSize(self->textureSize());
}

//  int QQuickDefaultTextureFactory::textureByteCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuickDefaultTextureFactory16textureByteCountEv(
    const QQuickDefaultTextureFactory *self) {
  return self->textureByteCount();
}

//  QImage QQuickDefaultTextureFactory::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK27QQuickDefaultTextureFactory5imageEv(
    const QQuickDefaultTextureFactory *self) {
  return new QImage(self->image());
}

//  QSGTexture *QQuickDefaultTextureFactory::createTexture(QQuickWindow
//      *window) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK27QQuickDefaultTextureFactory13createTextureEP12QQuickWindow(
    const QQuickDefaultTextureFactory *self,
    QQuickWindow *window) {
  return self->QQuickDefaultTextureFactory::createTexture(window);
}

//  QSize QQuickDefaultTextureFactory::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK27QQuickDefaultTextureFactory11textureSizeEv(
    const QQuickDefaultTextureFactory *self) {
  return new QSize(self->QQuickDefaultTextureFactory::textureSize());
}

//  int QQuickDefaultTextureFactory::textureByteCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK27QQuickDefaultTextureFactory16textureByteCountEv(
    const QQuickDefaultTextureFactory *self) {
  return self->QQuickDefaultTextureFactory::textureByteCount();
}

//  QImage QQuickDefaultTextureFactory::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK27QQuickDefaultTextureFactory5imageEv(
    const QQuickDefaultTextureFactory *self) {
  return new QImage(self->QQuickDefaultTextureFactory::image());
}
