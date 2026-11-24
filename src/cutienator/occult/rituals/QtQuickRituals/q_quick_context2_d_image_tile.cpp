//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtile_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2dtile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickcontext2dtile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtile.cpp, line 22, as _ZN19QQuickContext2DTile13createPainterEbb
inline QPainter* QQuickContext2DTile::createPainter(bool smooth, bool antialiasing)
{
    if (m_painter.isActive())
        m_painter.end();

    aboutToDraw();
    if (m_device) {
        m_painter.begin(m_device);
        m_painter.resetTransform();
        m_painter.setCompositionMode(QPainter::CompositionMode_Source);

#ifdef QQUICKCONTEXT2D_DEBUG
        int v = 100;
        int gray = (m_rect.x() / m_rect.width() + m_rect.y() / m_rect.height()) % 2;
        if (gray)
            v = 150;
        m_painter.fillRect(QRect(0, 0, m_rect.width(), m_rect.height()), QColor(v, v, v, 255));
#endif

        if (antialiasing)
            m_painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing, true);
        else
            m_painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing, false);

        if (smooth)
            m_painter.setRenderHint(QPainter::SmoothPixmapTransform, true);
        else
            m_painter.setRenderHint(QPainter::SmoothPixmapTransform, false);

        m_painter.setCompositionMode(QPainter::CompositionMode_SourceOver);
        m_painter.translate(-m_rect.left(), -m_rect.top());
        m_painter.setClipRect(m_rect);
        m_painter.setClipping(false);
        return &m_painter;
    }

    return nullptr;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtile.cpp, line 9, as _ZN19QQuickContext2DTileC2Ev
inline QQuickContext2DTile::QQuickContext2DTile()
    : m_dirty(true)
    , m_rect(QRect(0, 0, 1, 1))
    , m_device(nullptr)
{
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtile.cpp, line 16, as _ZN19QQuickContext2DTileD2Ev
inline QQuickContext2DTile::~QQuickContext2DTile()
{
    if (m_painter.isActive())
        m_painter.end();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtile.cpp, line 66, as _ZN24QQuickContext2DImageTileD1Ev
inline QQuickContext2DImageTile::~QQuickContext2DImageTile()
{
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtile.cpp, line 70, as _ZN24QQuickContext2DImageTile7setRectERK5QRect
inline void QQuickContext2DImageTile::setRect(const QRect& r)
{
    if (m_rect == r)
        return;
    m_rect = r;
    m_dirty = true;
    if (m_image.size() != r.size()) {
        m_image = QImage(r.size(), QImage::Format_ARGB32_Premultiplied);
    }
    m_device = &m_image;
}
//  -----------------------------------------------------------------------

//  A QQuickContext2DImageTile that Python can take functions over in. Every QQuickContext2DImageTile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DImageTileCall0)(const void *, const QRect *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DImageTileCall1)(const void *, bool, bool, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DImageTileCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DImageTileCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
class CuteQQuickContext2DImageTile : public QQuickContext2DImageTile {
public:
  using QQuickContext2DImageTile::QQuickContext2DImageTile;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickContext2DTile7setRectERK5QRect")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickContext2DTile13createPainterEbb")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickContext2DTile12drawFinishedEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickContext2DTile11aboutToDrawEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
    return false;
  }

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DImageTile::setRect(const QRect &r)
  void setRect(const QRect &r) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContext2DImageTileCall0 call = reinterpret_cast<CuteQQuickContext2DImageTileCall0>(taken[0]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QQuickContext2DImageTile::setRect(r);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QPainter *QQuickContext2DTile::createPainter(bool smooth, bool
  //      antialiasing)
  QPainter *createPainter(bool smooth, bool antialiasing) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DImageTileCall1 call = reinterpret_cast<CuteQQuickContext2DImageTileCall1>(taken[1]);
      void * given = call(this, smooth, antialiasing, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QQuickContext2DTile::createPainter(smooth, antialiasing);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DTile::drawFinished()
  void drawFinished() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickContext2DImageTileCall2 call = reinterpret_cast<CuteQQuickContext2DImageTileCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickContext2DTile::drawFinished();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2DTile::aboutToDraw()
  void aboutToDraw() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickContext2DImageTileCall3 call = reinterpret_cast<CuteQQuickContext2DImageTileCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickContext2DTile::aboutToDraw();
  }
#endif  // QT_CONFIG(quick_canvas)
};

//  QQuickContext2DImageTile::~QQuickContext2DImageTile()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickContext2DImageTileD1Ev(
    QQuickContext2DImageTile *self) {
  delete self;
}

//  void QQuickContext2DImageTile::setRect(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickContext2DImageTile7setRectERK5QRect(
    QQuickContext2DImageTile *self,
    const QRect *r) {
  self->setRect(*r);
}

//  const QImage &QQuickContext2DImageTile::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK24QQuickContext2DImageTile5imageEv(
    const QQuickContext2DImageTile *self) {
  return new QImage(self->image());
}

//  a Python function taken by a CuteQQuickContext2DImageTile, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2DImageTile(
    QQuickContext2DImageTile *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2DImageTile *>(self)->take(key, call);
}

//  void QQuickContext2DImageTile::setRect(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickContext2DImageTile7setRectERK5QRect(
    QQuickContext2DImageTile *self,
    const QRect *r) {
  self->QQuickContext2DImageTile::setRect(*r);
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
