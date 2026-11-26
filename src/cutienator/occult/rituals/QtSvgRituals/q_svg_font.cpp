//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QList>
#include <QtCore/QStringView>

//  A QSvgFont that Python can take functions over in. Every QSvgFont
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFontCall0)(const void *, int *);
typedef bool (*CuteQSvgFontCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFontCall2)(const void *, int *);
class CuteQSvgFont : public QSvgFont {
public:
  using QSvgFont::QSvgFont;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgFont::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFontCall0 call = reinterpret_cast<CuteQSvgFontCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFont::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFontCall1 call = reinterpret_cast<CuteQSvgFontCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgFontCall2 call = reinterpret_cast<CuteQSvgFontCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFont::QSvgFont(qreal horizAdvX)
extern "C" Q_DECL_EXPORT
QSvgFont *ritual_ZN8QSvgFontC1Ed(qreal horizAdvX) {
  return new CuteQSvgFont(horizAdvX);
}

//  QSvgFont::~QSvgFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgFontD1Ev(QSvgFont *self) {
  delete self;
}

//  Type QSvgFont::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgFont4typeEv(const QSvgFont *self) {
  return self->type();
}

//  void QSvgFont::setUnitsPerEm(qreal upem)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgFont13setUnitsPerEmEd(QSvgFont *self, qreal upem) {
  self->setUnitsPerEm(upem);
}

//  void QSvgFont::addGlyph(const QString &unicode, const QPainterPath &path,
//      qreal horizAdvX)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgFont8addGlyphERK7QStringRK12QPainterPathd(
    QSvgFont *self,
    const QString *unicode,
    const QPainterPath *path,
    qreal horizAdvX) {
  self->addGlyph(*unicode, *path, horizAdvX);
}

//  bool QSvgFont::addMissingGlyph(const QPainterPath &path, qreal horizAdvX)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QSvgFont15addMissingGlyphERK12QPainterPathd(
    QSvgFont *self,
    const QPainterPath *path,
    qreal horizAdvX) {
  return self->addMissingGlyph(*path, horizAdvX);
}

//  void QSvgFont::drawCommand(QPainter *a0, QSvgExtraStates &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgFont11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgFont *self,
    QPainter *a0,
    QSvgExtraStates *a1) {
  self->drawCommand(a0, *a1);
}

//  void QSvgFont::draw(QPainter *p, const QPointF &point, const QList<const
//      QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment alignment) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QSvgFont4drawEP8QPainterRK7QPointFRK5QListIPK9QSvgGlyphEd6QFlagsIN2Qt13AlignmentFlagEE(
    const QSvgFont *self,
    QPainter *p,
    const QPointF *point,
    const QList<const QSvgGlyph *> *glyphs,
    qreal pixelSize,
    int alignment) {
  self->draw(
      p,
      *point,
      *glyphs,
      pixelSize,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QRectF QSvgFont::boundingRect(QPainter *p, const QPointF &point, const
//      QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment
//      alignment) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QSvgFont12boundingRectEP8QPainterRK7QPointFRK5QListIPK9QSvgGlyphEd6QFlagsIN2Qt13AlignmentFlagEE(
    const QSvgFont *self,
    QPainter *p,
    const QPointF *point,
    const QList<const QSvgGlyph *> *glyphs,
    qreal pixelSize,
    int alignment) {
  return new QRectF(
      self->boundingRect(
          p,
          *point,
          *glyphs,
          pixelSize,
          QFlags<Qt::AlignmentFlag>::fromInt(alignment)));
}

//  const QSvgGlyph *QSvgFont::findFirstGlyphFor(QStringView text) const
extern "C" Q_DECL_EXPORT
const QSvgGlyph *ritual_ZNK8QSvgFont17findFirstGlyphForE11QStringView(
    const QSvgFont *self,
    const QString *text) {
  return self->findFirstGlyphFor(QStringView(*text));
}

//  QList<const QSvgGlyph *> QSvgFont::toGlyphs(QStringView text) const
extern "C" Q_DECL_EXPORT
QList<const QSvgGlyph *> *ritual_ZNK8QSvgFont8toGlyphsE11QStringView(
    const QSvgFont *self,
    const QString *text) {
  return new QList<const QSvgGlyph *>(self->toGlyphs(QStringView(*text)));
}

//  void QSvgFont::draw_helper(QPainter *p, const QPointF &point, const
//      QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment
//      alignment, QRectF *boundingRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QSvgFont11draw_helperEP8QPainterRK7QPointFRK5QListIPK9QSvgGlyphEd6QFlagsIN2Qt13AlignmentFlagEEP6QRectF(
    const QSvgFont *self,
    QPainter *p,
    const QPointF *point,
    const QList<const QSvgGlyph *> *glyphs,
    qreal pixelSize,
    int alignment,
    QRectF *boundingRect) {
  self->draw_helper(
      p,
      *point,
      *glyphs,
      pixelSize,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      boundingRect);
}

//  a Python function taken by a CuteQSvgFont, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFont(QSvgFont *self, const char *key, void *call) {
  return static_cast<CuteQSvgFont *>(self)->take(key, call);
}

//  Type QSvgFont::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK8QSvgFont4typeEv(const QSvgFont *self) {
  return self->QSvgFont::type();
}

//  a QList<const QSvgGlyph *> a ritual of QSvgFont gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgFont__QList_const_QSvgGlyph(
    QList<const QSvgGlyph *> *self) {
  delete self;
}
