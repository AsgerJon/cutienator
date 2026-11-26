//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qbrush.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmapcache.h>
#include <QtGui/qpa/qplatformpixmap.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qvariant.h>
#include <QtCore/qline.h>
#include <QtCore/qdebug.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qcoreapplication.h>
#include <QtGui/private/qhexstring_p.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qfile.h>
#include <QtCore/qmutex.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/painting/qbrush.cpp, line 152, as local:qbrush.cpp:QBasicBrushData
struct QBasicBrushData : public QBrushData
{
};

//  from src/gui/painting/qbrush.cpp, line 156, as local:qbrush.cpp:QTexturedBrushData
struct QTexturedBrushData : public QBrushData
{
    QTexturedBrushData() {
        m_has_pixmap_texture = false;
        m_pixmap = nullptr;
    }
    ~QTexturedBrushData() {
        delete m_pixmap;
    }

    void setPixmap(const QPixmap &pm) {
        delete m_pixmap;

        if (pm.isNull()) {
            m_pixmap = nullptr;
            m_has_pixmap_texture = false;
        } else {
            m_pixmap = new QPixmap(pm);
            m_has_pixmap_texture = true;
        }

        m_image = QImage();
    }

    void setImage(const QImage &image) {
        m_image = image;
        delete m_pixmap;
        m_pixmap = nullptr;
        m_has_pixmap_texture = false;
    }

    QPixmap &pixmap() {
        if (!m_pixmap) {
            m_pixmap = new QPixmap(QPixmap::fromImage(m_image));
        }
        return *m_pixmap;
    }

    QImage &image() {
        if (m_image.isNull() && m_pixmap)
            m_image = m_pixmap->toImage();
        return m_image;
    }

    QPixmap *m_pixmap;
    QImage m_image;
    bool m_has_pixmap_texture;
};

//  from src/gui/painting/qbrush.cpp, line 215, as local:qbrush.cpp:QGradientBrushData
struct QGradientBrushData : public QBrushData
{
    QGradient gradient;
};

//  from src/gui/painting/qbrush.cpp, line 220, as local:qbrush.cpp:deleteData
static void deleteData(QBrushData *d)
{
    switch (d->style) {
    case Qt::TexturePattern:
        delete static_cast<QTexturedBrushData*>(d);
        break;
    case Qt::LinearGradientPattern:
    case Qt::RadialGradientPattern:
    case Qt::ConicalGradientPattern:
        delete static_cast<QGradientBrushData*>(d);
        break;
    case Qt::NoBrush:
    case Qt::SolidPattern:
    case Qt::Dense1Pattern:
    case Qt::Dense2Pattern:
    case Qt::Dense3Pattern:
    case Qt::Dense4Pattern:
    case Qt::Dense5Pattern:
    case Qt::Dense6Pattern:
    case Qt::Dense7Pattern:
    case Qt::HorPattern:
    case Qt::VerPattern:
    case Qt::CrossPattern:
    case Qt::BDiagPattern:
    case Qt::FDiagPattern:
    case Qt::DiagCrossPattern:
        delete static_cast<QBasicBrushData*>(d);
        break;
    }
}

//  from src/gui/painting/qbrush.cpp, line 251, as _ZNK24QBrushDataPointerDeleterclEP10QBrushData
inline void QBrushDataPointerDeleter::operator()(QBrushData *d) const noexcept
{
    if (d && !d->ref.deref())
        deleteData(d);
}
//  -----------------------------------------------------------------------

//  void QBrushDataPointerDeleter::operator()(QBrushData *d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QBrushDataPointerDeleterclEP10QBrushData(
    const QBrushDataPointerDeleter *self,
    QBrushData *d) {
  self->operator()(d);
}

//  QBrushDataPointerDeleter::~QBrushDataPointerDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QBrushDataPointerDeleterD1Ev(
    QBrushDataPointerDeleter *self) {
  delete self;
}
