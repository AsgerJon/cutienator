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
//  -----------------------------------------------------------------------

//  Only a class built on QQuickContext2DTile may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickContext2DTile : QQuickContext2DTile {
  using QQuickContext2DTile::aboutToDraw;
};

//  A QQuickContext2DTile that Python can take functions over in. Every QQuickContext2DTile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DTileCall0)(const void *, const QRect *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DTileCall1)(const void *, bool, bool, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DTileCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DTileCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
class CuteQQuickContext2DTile : public QQuickContext2DTile {
public:
  using QQuickContext2DTile::QQuickContext2DTile;
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
  //  void QQuickContext2DTile::setRect(const QRect &r)
  void setRect(const QRect &r) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContext2DTileCall0 call = reinterpret_cast<CuteQQuickContext2DTileCall0>(taken[0]);
      call(this, &r, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QPainter *QQuickContext2DTile::createPainter(bool smooth, bool
  //      antialiasing)
  QPainter *createPainter(bool smooth, bool antialiasing) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DTileCall1 call = reinterpret_cast<CuteQQuickContext2DTileCall1>(taken[1]);
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
      CuteQQuickContext2DTileCall2 call = reinterpret_cast<CuteQQuickContext2DTileCall2>(taken[2]);
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
      CuteQQuickContext2DTileCall3 call = reinterpret_cast<CuteQQuickContext2DTileCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickContext2DTile::aboutToDraw();
  }
#endif  // QT_CONFIG(quick_canvas)
};

//  QQuickContext2DTile::~QQuickContext2DTile()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickContext2DTileD1Ev(QQuickContext2DTile *self) {
  delete self;
}

//  bool QQuickContext2DTile::dirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickContext2DTile5dirtyEv(
    const QQuickContext2DTile *self) {
  return self->dirty();
}

//  void QQuickContext2DTile::markDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickContext2DTile9markDirtyEb(
    QQuickContext2DTile *self,
    bool dirty) {
  self->markDirty(dirty);
}

//  QRect QQuickContext2DTile::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QQuickContext2DTile4rectEv(
    const QQuickContext2DTile *self) {
  return new QRect(self->rect());
}

//  void QQuickContext2DTile::setRect(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickContext2DTile7setRectERK5QRect(
    QQuickContext2DTile *self,
    const QRect *r) {
  self->setRect(*r);
}

//  QPainter *QQuickContext2DTile::createPainter(bool smooth, bool
//      antialiasing)
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZN19QQuickContext2DTile13createPainterEbb(
    QQuickContext2DTile *self,
    bool smooth,
    bool antialiasing) {
  return self->createPainter(smooth, antialiasing);
}

//  void QQuickContext2DTile::drawFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickContext2DTile12drawFinishedEv(
    QQuickContext2DTile *self) {
  self->drawFinished();
}

//  void QQuickContext2DTile::aboutToDraw()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickContext2DTile11aboutToDrawEv(
    QQuickContext2DTile *self) {
  self->aboutToDraw();
}

//  a Python function taken by a CuteQQuickContext2DTile, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2DTile(
    QQuickContext2DTile *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2DTile *>(self)->take(key, call);
}

//  QPainter *QQuickContext2DTile::createPainter(bool smooth, bool
//      antialiasing)
extern "C" Q_DECL_EXPORT
QPainter *ritual_own_ZN19QQuickContext2DTile13createPainterEbb(
    QQuickContext2DTile *self,
    bool smooth,
    bool antialiasing) {
  return self->QQuickContext2DTile::createPainter(smooth, antialiasing);
}

//  void QQuickContext2DTile::drawFinished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickContext2DTile12drawFinishedEv(
    QQuickContext2DTile *self) {
  self->QQuickContext2DTile::drawFinished();
}

//  void QQuickContext2DTile::aboutToDraw()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickContext2DTile11aboutToDrawEv(
    QQuickContext2DTile *self) {
  static_cast<OwnQQuickContext2DTile *>(self)->OwnQQuickContext2DTile::aboutToDraw();
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
