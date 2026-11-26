//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qblittable_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_BLITTABLE)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qblittable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpixmap.h>
#include <cstring>

//  A QBlittable that Python can take functions over in. Every QBlittable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittableCall0)(const void *, const QRectF *, const QColor *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittableCall1)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittableCall2)(const void *, const QRectF *, const QColor *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittableCall3)(const void *, const QRectF *, const QPixmap *, const QRectF *, int, qreal, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef bool (*CuteQBlittableCall4)(const void *, const QPaintEngineState *, int, int, const glyph_t *, const QFixedPoint *, QFontEngine *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void * (*CuteQBlittableCall5)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlittableCall6)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
class CuteQBlittable : public QBlittable {
public:
  using QBlittable::QBlittable;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN10QBlittable8fillRectERK6QRectFRK6QColor")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN10QBlittable10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN10QBlittable13alphaFillRectERK6QRectFRK6QColorN8QPainter15CompositionModeE")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN10QBlittable17drawPixmapOpacityERK6QRectFRK7QPixmapS2_N8QPainter15CompositionModeEd")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN10QBlittable16drawCachedGlyphsEPK17QPaintEngineStateN11QFontEngine11GlyphFormatEiPKjPK11QFixedPointPS3_")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN10QBlittable6doLockEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN10QBlittable8doUnlockEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
    return false;
  }

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittable::fillRect(const QRectF &rect, const QColor &color)
  void fillRect(const QRectF &rect, const QColor &color) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBlittableCall0 call = reinterpret_cast<CuteQBlittableCall0>(taken[0]);
      call(this, &rect, &color, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittable::drawPixmap(const QRectF &rect, const QPixmap
  //      &pixmap, const QRectF &subrect)
  void drawPixmap(
      const QRectF &rect,
      const QPixmap &pixmap,
      const QRectF &subrect) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBlittableCall1 call = reinterpret_cast<CuteQBlittableCall1>(taken[1]);
      call(this, &rect, &pixmap, &subrect, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittable::alphaFillRect(const QRectF &rect, const QColor
  //      &color, QPainter::CompositionMode cmode)
  void alphaFillRect(
      const QRectF &rect,
      const QColor &color,
      QPainter::CompositionMode cmode) override {
    if (taken[2]) {
      int handled = 0;
      CuteQBlittableCall2 call = reinterpret_cast<CuteQBlittableCall2>(taken[2]);
      call(this, &rect, &color, static_cast<int>(cmode), &handled);
      if (handled) return;
    }
    QBlittable::alphaFillRect(rect, color, cmode);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittable::drawPixmapOpacity(const QRectF &rect, const QPixmap
  //      &pixmap, const QRectF &subrect, QPainter::CompositionMode cmode,
  //      qreal opacity)
  void drawPixmapOpacity(
      const QRectF &rect,
      const QPixmap &pixmap,
      const QRectF &subrect,
      QPainter::CompositionMode cmode,
      qreal opacity) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBlittableCall3 call = reinterpret_cast<CuteQBlittableCall3>(taken[3]);
      call(this, &rect, &pixmap, &subrect, static_cast<int>(cmode), opacity, &handled);
      if (handled) return;
    }
    QBlittable::drawPixmapOpacity(rect, pixmap, subrect, cmode, opacity);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  bool QBlittable::drawCachedGlyphs(const QPaintEngineState *state,
  //      QFontEngine::GlyphFormat glyphFormat, int numGlyphs, const
  //      glyph_t *glyphs, const QFixedPoint *positions, QFontEngine
  //      *fontEngine)
  bool drawCachedGlyphs(
      const QPaintEngineState *state,
      QFontEngine::GlyphFormat glyphFormat,
      int numGlyphs,
      const glyph_t *glyphs,
      const QFixedPoint *positions,
      QFontEngine *fontEngine) override {
    if (taken[4]) {
      int handled = 0;
      CuteQBlittableCall4 call = reinterpret_cast<CuteQBlittableCall4>(taken[4]);
      bool given = call(this, state, static_cast<int>(glyphFormat), numGlyphs, glyphs, positions, fontEngine, &handled);
      if (handled) return given;
    }
    return QBlittable::drawCachedGlyphs(state, glyphFormat, numGlyphs, glyphs, positions, fontEngine);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  QImage *QBlittable::doLock()
  QImage *doLock() override {
    if (taken[5]) {
      int handled = 0;
      CuteQBlittableCall5 call = reinterpret_cast<CuteQBlittableCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QImage *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlittable::doUnlock()
  void doUnlock() override {
    if (taken[6]) {
      int handled = 0;
      CuteQBlittableCall6 call = reinterpret_cast<CuteQBlittableCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_BLITTABLE)
};

//  QBlittablePrivate *QBlittable::d_func()
extern "C" Q_DECL_EXPORT
QBlittablePrivate *ritual_ZN10QBlittable6d_funcEv(QBlittable *self) {
  return self->d_func();
}

//  const QBlittablePrivate *QBlittable::d_func() const
extern "C" Q_DECL_EXPORT
const QBlittablePrivate *ritual_ZNK10QBlittable6d_funcEv(
    const QBlittable *self) {
  return self->d_func();
}

//  QBlittable::QBlittable(const QSize &size, Capabilities caps)
extern "C" Q_DECL_EXPORT
QBlittable *ritual_ZN10QBlittableC1ERK5QSize6QFlagsINS_10CapabilityEE(
    const QSize *size,
    int caps) {
  return new CuteQBlittable(
      *size,
      QFlags<QBlittable::Capability>::fromInt(caps));
}

//  QBlittable::~QBlittable()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBlittableD1Ev(QBlittable *self) {
  delete self;
}

//  Capabilities QBlittable::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBlittable12capabilitiesEv(const QBlittable *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  QSize QBlittable::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QBlittable4sizeEv(const QBlittable *self) {
  return new QSize(self->size());
}

//  void QBlittable::fillRect(const QRectF &rect, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBlittable8fillRectERK6QRectFRK6QColor(
    QBlittable *self,
    const QRectF *rect,
    const QColor *color) {
  self->fillRect(*rect, *color);
}

//  void QBlittable::drawPixmap(const QRectF &rect, const QPixmap &pixmap,
//      const QRectF &subrect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBlittable10drawPixmapERK6QRectFRK7QPixmapS2_(
    QBlittable *self,
    const QRectF *rect,
    const QPixmap *pixmap,
    const QRectF *subrect) {
  self->drawPixmap(*rect, *pixmap, *subrect);
}

//  void QBlittable::alphaFillRect(const QRectF &rect, const QColor &color,
//      QPainter::CompositionMode cmode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBlittable13alphaFillRectERK6QRectFRK6QColorN8QPainter15CompositionModeE(
    QBlittable *self,
    const QRectF *rect,
    const QColor *color,
    QPainter::CompositionMode cmode) {
  self->alphaFillRect(*rect, *color, cmode);
}

//  void QBlittable::drawPixmapOpacity(const QRectF &rect, const QPixmap
//      &pixmap, const QRectF &subrect, QPainter::CompositionMode cmode,
//      qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBlittable17drawPixmapOpacityERK6QRectFRK7QPixmapS2_N8QPainter15CompositionModeEd(
    QBlittable *self,
    const QRectF *rect,
    const QPixmap *pixmap,
    const QRectF *subrect,
    QPainter::CompositionMode cmode,
    qreal opacity) {
  self->drawPixmapOpacity(*rect, *pixmap, *subrect, cmode, opacity);
}

//  bool QBlittable::drawCachedGlyphs(const QPaintEngineState *state,
//      QFontEngine::GlyphFormat glyphFormat, int numGlyphs, const glyph_t
//      *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBlittable16drawCachedGlyphsEPK17QPaintEngineStateN11QFontEngine11GlyphFormatEiPKjPK11QFixedPointPS3_(
    QBlittable *self,
    const QPaintEngineState *state,
    QFontEngine::GlyphFormat glyphFormat,
    int numGlyphs,
    const glyph_t *glyphs,
    const QFixedPoint *positions,
    QFontEngine *fontEngine) {
  return self->drawCachedGlyphs(
      state,
      glyphFormat,
      numGlyphs,
      glyphs,
      positions,
      fontEngine);
}

//  QImage *QBlittable::lock()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN10QBlittable4lockEv(QBlittable *self) {
  return self->lock();
}

//  void QBlittable::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBlittable6unlockEv(QBlittable *self) {
  self->unlock();
}

//  bool QBlittable::isLocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QBlittable8isLockedEv(const QBlittable *self) {
  return self->isLocked();
}

//  QImage *QBlittable::doLock()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN10QBlittable6doLockEv(QBlittable *self) {
  return self->doLock();
}

//  void QBlittable::doUnlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBlittable8doUnlockEv(QBlittable *self) {
  self->doUnlock();
}

//  a Python function taken by a CuteQBlittable, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBlittable(QBlittable *self, const char *key, void *call) {
  return static_cast<CuteQBlittable *>(self)->take(key, call);
}

//  void QBlittable::alphaFillRect(const QRectF &rect, const QColor &color,
//      QPainter::CompositionMode cmode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBlittable13alphaFillRectERK6QRectFRK6QColorN8QPainter15CompositionModeE(
    QBlittable *self,
    const QRectF *rect,
    const QColor *color,
    QPainter::CompositionMode cmode) {
  self->QBlittable::alphaFillRect(*rect, *color, cmode);
}

//  void QBlittable::drawPixmapOpacity(const QRectF &rect, const QPixmap
//      &pixmap, const QRectF &subrect, QPainter::CompositionMode cmode,
//      qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBlittable17drawPixmapOpacityERK6QRectFRK7QPixmapS2_N8QPainter15CompositionModeEd(
    QBlittable *self,
    const QRectF *rect,
    const QPixmap *pixmap,
    const QRectF *subrect,
    QPainter::CompositionMode cmode,
    qreal opacity) {
  self->QBlittable::drawPixmapOpacity(
      *rect,
      *pixmap,
      *subrect,
      cmode,
      opacity);
}

//  bool QBlittable::drawCachedGlyphs(const QPaintEngineState *state,
//      QFontEngine::GlyphFormat glyphFormat, int numGlyphs, const glyph_t
//      *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QBlittable16drawCachedGlyphsEPK17QPaintEngineStateN11QFontEngine11GlyphFormatEiPKjPK11QFixedPointPS3_(
    QBlittable *self,
    const QPaintEngineState *state,
    QFontEngine::GlyphFormat glyphFormat,
    int numGlyphs,
    const glyph_t *glyphs,
    const QFixedPoint *positions,
    QFontEngine *fontEngine) {
  return self->QBlittable::drawCachedGlyphs(
      state,
      glyphFormat,
      numGlyphs,
      glyphs,
      positions,
      fontEngine);
}

#endif  // !defined(QT_NO_BLITTABLE)
