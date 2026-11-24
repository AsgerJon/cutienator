//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_alpha_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_alpha_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/qtprintsupportglobal.h>
#ifndef QT_NO_PRINTER
#include <QtCore/qdebug.h>
#include <QtPrintSupport/private/qpaintengine_alpha_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/private/qpicture_p.h>
#include <QtGui/private/qfont_p.h>
#include "QtGui/qpicture.h"
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 350, as _ZN24QAlphaPaintEnginePrivateC1Ev
#if !defined(QT_NO_PRINTER)
inline QAlphaPaintEnginePrivate::QAlphaPaintEnginePrivate()
    :   m_pass(0),
        m_pic(nullptr),
        m_picengine(nullptr),
        m_picpainter(nullptr),
        m_numberOfCachedRects(0),
        m_hasalpha(false),
        m_alphaPen(false),
        m_alphaBrush(false),
        m_alphaOpacity(false),
        m_advancedPen(false),
        m_advancedBrush(false),
        m_complexTransform(false)
{

}
#endif  // !defined(QT_NO_PRINTER)

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 367, as _ZN24QAlphaPaintEnginePrivateD1Ev
#if !defined(QT_NO_PRINTER)
inline QAlphaPaintEnginePrivate::~QAlphaPaintEnginePrivate()
{
    delete m_picpainter;
    delete m_pic;
}
#endif  // !defined(QT_NO_PRINTER)

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 397, as _ZN24QAlphaPaintEnginePrivate12addAlphaRectERK6QRectF
#if !defined(QT_NO_PRINTER)
inline void QAlphaPaintEnginePrivate::addAlphaRect(const QRectF &rect)
{
    m_alphargn |= rect.toAlignedRect();
}
#endif  // !defined(QT_NO_PRINTER)

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 402, as _ZNK24QAlphaPaintEnginePrivate22canSeeTroughBackgroundEbRK6QRectF
#if !defined(QT_NO_PRINTER)
inline bool QAlphaPaintEnginePrivate::canSeeTroughBackground(bool somethingInRectHasAlpha, const QRectF &rect) const
{
    if (somethingInRectHasAlpha) {
        if (m_dirtyRects.size() != m_numberOfCachedRects) {
            m_cachedDirtyRgn.setRects(m_dirtyRects.constData(), m_dirtyRects.size());
            m_numberOfCachedRects = m_dirtyRects.size();
        }
        return m_cachedDirtyRgn.intersects(rect.toAlignedRect());
    }
    return false;
}
#endif  // !defined(QT_NO_PRINTER)

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 373, as _ZN24QAlphaPaintEnginePrivate11addPenWidthERK12QPainterPath
#if !defined(QT_NO_PRINTER)
inline QRectF QAlphaPaintEnginePrivate::addPenWidth(const QPainterPath &path)
{
    QPainterPath tmp = path;

    if (m_pen.style() == Qt::NoPen)
        return (path.controlPointRect() * m_transform).boundingRect();
    bool cosmetic = m_pen.isCosmetic();
    if (cosmetic)
        tmp = path * m_transform;

    QPainterPathStroker stroker;
    if (m_pen.widthF() == 0.0f)
        stroker.setWidth(1.0);
    else
        stroker.setWidth(m_pen.widthF());
    stroker.setJoinStyle(m_pen.joinStyle());
    stroker.setCapStyle(m_pen.capStyle());
    tmp = stroker.createStroke(tmp);
    if (cosmetic)
        return tmp.controlPointRect();

    return (tmp.controlPointRect() * m_transform).boundingRect();
}
#endif  // !defined(QT_NO_PRINTER)

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 414, as _ZN24QAlphaPaintEnginePrivate14drawAlphaImageERK6QRectF
#if !defined(QT_NO_PRINTER)
inline void QAlphaPaintEnginePrivate::drawAlphaImage(const QRectF &rect)
{
    Q_Q(QAlphaPaintEngine);

    qreal dpiX = qMax(m_pdev->logicalDpiX(), 300);
    qreal dpiY = qMax(m_pdev->logicalDpiY(), 300);
    qreal xscale = (dpiX / m_pdev->logicalDpiX());
    qreal yscale = (dpiY / m_pdev->logicalDpiY());

    QTransform picscale;
    picscale.scale(xscale, yscale);

    const int tileSize = 2048;
    QSize size((int(rect.width() * xscale)), int(rect.height() * yscale));
    int divw = (size.width() / tileSize);
    int divh = (size.height() / tileSize);
    divw += 1;
    divh += 1;

    int incx = int(rect.width() / divw);
    int incy = int(rect.height() / divh);

    for (int y=0; y<divh; ++y) {
        int ypos = int((incy * y) + rect.y());
        int height = int((y == (divh - 1)) ? (rect.height() - (incy * y)) : incy) + 1;

        for (int x=0; x<divw; ++x) {
            int xpos = int((incx * x) + rect.x());
            int width = int((x == (divw - 1)) ? (rect.width() - (incx * x)) : incx) + 1;

            QSize imgsize((int)(width * xscale), (int)(height * yscale));
            QImage img(imgsize, QImage::Format_RGB32);
            img.fill(0xffffffff);

            QPainter imgpainter(&img);
            imgpainter.setTransform(picscale);
            QPointF picpos(qreal(-xpos), qreal(-ypos));
            imgpainter.drawPicture(picpos, *m_pic);
            imgpainter.end();

            q->painter()->setTransform(QTransform());
            QRect r(xpos, ypos, width, height);
            q->painter()->drawImage(r, img);
        }
    }
}
#endif  // !defined(QT_NO_PRINTER)

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 461, as _ZNK24QAlphaPaintEnginePrivate14fullyContainedERK6QRectF
#if !defined(QT_NO_PRINTER)
inline bool QAlphaPaintEnginePrivate::fullyContained(const QRectF &rect) const
{
    QRegion r(rect.toAlignedRect());
    return (m_cliprgn.intersected(r) == r);
}
#endif  // !defined(QT_NO_PRINTER)

//  from src/printsupport/kernel/qpaintengine_alpha.cpp, line 467, as _ZN24QAlphaPaintEnginePrivate10resetStateEP8QPainter
#if !defined(QT_NO_PRINTER)
inline void QAlphaPaintEnginePrivate::resetState(QPainter *p)
{
    p->setPen(QPen());
    p->setBrush(QBrush());
    p->setBrushOrigin(0,0);
    p->setBackground(QBrush());
    p->setFont(QFont());
    p->setTransform(QTransform());
    // The view transform is already recorded and included in the
    // picture we're about to replay. If we don't turn if off,
    // the view matrix will be applied twice.
    p->setViewTransformEnabled(false);
    p->setClipRegion(QRegion(), Qt::NoClip);
    p->setClipPath(QPainterPath(), Qt::NoClip);
    p->setClipping(false);
    p->setOpacity(1.0f);
}
#endif  // !defined(QT_NO_PRINTER)
//  -----------------------------------------------------------------------

//  A QAlphaPaintEnginePrivate that Python can take functions over in. Every QAlphaPaintEnginePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAlphaPaintEnginePrivateCall0)(const void *, int *);
typedef void * (*CuteQAlphaPaintEnginePrivateCall1)(const void *, int *);
class CuteQAlphaPaintEnginePrivate : public QAlphaPaintEnginePrivate {
public:
  using QAlphaPaintEnginePrivate::QAlphaPaintEnginePrivate;
  CuteQAlphaPaintEnginePrivate(const QAlphaPaintEnginePrivate &other) : QAlphaPaintEnginePrivate(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate18systemStateChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate15aggregateEngineEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QPaintEnginePrivate::systemStateChanged()
  void systemStateChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAlphaPaintEnginePrivateCall0 call = reinterpret_cast<CuteQAlphaPaintEnginePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEnginePrivate::systemStateChanged();
  }

  //  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
  QPaintEngine *aggregateEngine() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAlphaPaintEnginePrivateCall1 call = reinterpret_cast<CuteQAlphaPaintEnginePrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintEnginePrivate::aggregateEngine();
  }
};

//  QAlphaPaintEngine *QAlphaPaintEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QAlphaPaintEngine *ritual_ZN24QAlphaPaintEnginePrivate6q_funcEv(
    QAlphaPaintEnginePrivate *self) {
  return self->q_func();
}

//  const QAlphaPaintEngine *QAlphaPaintEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAlphaPaintEngine *ritual_ZNK24QAlphaPaintEnginePrivate6q_funcEv(
    const QAlphaPaintEnginePrivate *self) {
  return self->q_func();
}

//  QAlphaPaintEnginePrivate::QAlphaPaintEnginePrivate()
extern "C" Q_DECL_EXPORT
QAlphaPaintEnginePrivate *ritual_ZN24QAlphaPaintEnginePrivateC1Ev() {
  return new CuteQAlphaPaintEnginePrivate();
}

//  QAlphaPaintEnginePrivate::~QAlphaPaintEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAlphaPaintEnginePrivateD1Ev(
    QAlphaPaintEnginePrivate *self) {
  delete self;
}

#if !defined(QT_NO_PRINTER)
//  void QAlphaPaintEnginePrivate::addAlphaRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAlphaPaintEnginePrivate12addAlphaRectERK6QRectF(
    QAlphaPaintEnginePrivate *self,
    const QRectF *rect) {
  self->addAlphaRect(*rect);
}
#endif  // !defined(QT_NO_PRINTER)

//  void QAlphaPaintEnginePrivate::addDirtyRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAlphaPaintEnginePrivate12addDirtyRectERK6QRectF(
    QAlphaPaintEnginePrivate *self,
    const QRectF *rect) {
  self->addDirtyRect(*rect);
}

#if !defined(QT_NO_PRINTER)
//  bool QAlphaPaintEnginePrivate::canSeeTroughBackground(bool
//      somethingInRectHasAlpha, const QRectF &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAlphaPaintEnginePrivate22canSeeTroughBackgroundEbRK6QRectF(
    const QAlphaPaintEnginePrivate *self,
    bool somethingInRectHasAlpha,
    const QRectF *rect) {
  return self->canSeeTroughBackground(somethingInRectHasAlpha, *rect);
}
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
//  QRectF QAlphaPaintEnginePrivate::addPenWidth(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN24QAlphaPaintEnginePrivate11addPenWidthERK12QPainterPath(
    QAlphaPaintEnginePrivate *self,
    const QPainterPath *path) {
  return new QRectF(self->addPenWidth(*path));
}
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
//  void QAlphaPaintEnginePrivate::drawAlphaImage(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAlphaPaintEnginePrivate14drawAlphaImageERK6QRectF(
    QAlphaPaintEnginePrivate *self,
    const QRectF *rect) {
  self->drawAlphaImage(*rect);
}
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
//  bool QAlphaPaintEnginePrivate::fullyContained(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAlphaPaintEnginePrivate14fullyContainedERK6QRectF(
    const QAlphaPaintEnginePrivate *self,
    const QRectF *rect) {
  return self->fullyContained(*rect);
}
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
//  void QAlphaPaintEnginePrivate::resetState(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAlphaPaintEnginePrivate10resetStateEP8QPainter(
    QAlphaPaintEnginePrivate *self,
    QPainter *p) {
  self->resetState(p);
}
#endif  // !defined(QT_NO_PRINTER)

//  a Python function taken by a CuteQAlphaPaintEnginePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAlphaPaintEnginePrivate(
    QAlphaPaintEnginePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAlphaPaintEnginePrivate *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_PRINTER)
