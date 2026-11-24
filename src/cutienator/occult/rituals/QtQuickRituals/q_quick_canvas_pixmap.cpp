//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickcanvascontext_p.h>
#include <QtQuick/private/qquickcontext2d_p.h>
#include <QtQuick/private/qquickcontext2dtexture_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/qsgtextureprovider.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtGui/QGuiApplication>
#include <QtQuick/qsgtextureprovider.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtCore/QBuffer>
#include <QtCore/QDir>
#include <QtCore/qdatetime.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 40, as _ZN18QQuickCanvasPixmapC1ERK6QImage
inline QQuickCanvasPixmap::QQuickCanvasPixmap(const QImage& image)
    : m_pixmap(nullptr)
    , m_image(image)
{

}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 47, as _ZN18QQuickCanvasPixmapC1EP12QQuickPixmap
inline QQuickCanvasPixmap::QQuickCanvasPixmap(QQuickPixmap *pixmap)
    : m_pixmap(pixmap)
{

}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 53, as _ZN18QQuickCanvasPixmapD1Ev
inline QQuickCanvasPixmap::~QQuickCanvasPixmap()
{
    delete m_pixmap;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 81, as _ZN18QQuickCanvasPixmap5imageEv
inline QImage QQuickCanvasPixmap::image()
{
    if (m_image.isNull() && m_pixmap)
        m_image = m_pixmap->image();

    return m_image;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 58, as _ZNK18QQuickCanvasPixmap5widthEv
inline qreal QQuickCanvasPixmap::width() const
{
    if (m_pixmap)
        return m_pixmap->width();

    return m_image.width();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 66, as _ZNK18QQuickCanvasPixmap6heightEv
inline qreal QQuickCanvasPixmap::height() const
{
    if (m_pixmap)
        return m_pixmap->height();

    return m_image.height();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 74, as _ZNK18QQuickCanvasPixmap7isValidEv
inline bool QQuickCanvasPixmap::isValid() const
{
    if (m_pixmap)
        return m_pixmap->isReady();
    return !m_image.isNull();
}
//  -----------------------------------------------------------------------

//  QQuickCanvasPixmap::QQuickCanvasPixmap(const QImage &image)
extern "C" Q_DECL_EXPORT
QQuickCanvasPixmap *ritual_ZN18QQuickCanvasPixmapC1ERK6QImage(
    const QImage *image) {
  return new QQuickCanvasPixmap(*image);
}

//  QQuickCanvasPixmap::QQuickCanvasPixmap(QQuickPixmap *pixmap)
extern "C" Q_DECL_EXPORT
QQuickCanvasPixmap *ritual_ZN18QQuickCanvasPixmapC1EP12QQuickPixmap(
    QQuickPixmap *pixmap) {
  return new QQuickCanvasPixmap(pixmap);
}

//  QQuickCanvasPixmap::~QQuickCanvasPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickCanvasPixmapD1Ev(QQuickCanvasPixmap *self) {
  delete self;
}

//  QImage QQuickCanvasPixmap::image()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN18QQuickCanvasPixmap5imageEv(QQuickCanvasPixmap *self) {
  return new QImage(self->image());
}

//  qreal QQuickCanvasPixmap::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickCanvasPixmap5widthEv(
    const QQuickCanvasPixmap *self) {
  return self->width();
}

//  qreal QQuickCanvasPixmap::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickCanvasPixmap6heightEv(
    const QQuickCanvasPixmap *self) {
  return self->height();
}

//  bool QQuickCanvasPixmap::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickCanvasPixmap7isValidEv(
    const QQuickCanvasPixmap *self) {
  return self->isValid();
}

//  QQuickPixmap *QQuickCanvasPixmap::pixmap() const
extern "C" Q_DECL_EXPORT
QQuickPixmap *ritual_ZNK18QQuickCanvasPixmap6pixmapEv(
    const QQuickCanvasPixmap *self) {
  return self->pixmap();
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
