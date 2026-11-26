//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgridpattern_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgridpattern_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasgridpattern.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasgridpattern.h>
#include <QtCanvasPainter/private/qcanvasgridpattern_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtCore/QVariant>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 427, as local:qcanvasgridpattern.cpp:DECONST
#define DECONST(d) const_cast<QCanvasGridPatternPrivate *>(d)

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 465, as _ZN25QCanvasGridPatternPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasGridPatternPrivate::clone()
{
    return new QCanvasGridPatternPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 429, as _ZNK25QCanvasGridPatternPrivate11createPaintEP14QCanvasPainter
inline QCPaint QCanvasGridPatternPrivate::createPaint(QCanvasPainter *painter) const
{
    auto *d = this;
    Q_UNUSED(painter);
    if (d->changed) {
        createGridPattern();
        DECONST(d)->changed = false;
    }
    return d->paint;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 157, as _ZNK25QCanvasGridPatternPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasGridPatternPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &pd = static_cast<const QCanvasGridPatternPrivate &>(other);

    if (x != pd.x
        || y != pd.y
        || width != pd.width
        || height != pd.height
        || feather != pd.feather
        || angle != pd.angle
        || lineWidth != pd.lineWidth
        || lineColor != pd.lineColor
        || backgroundColor != pd.backgroundColor)
        return false;

    return true;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 440, as _ZNK25QCanvasGridPatternPrivate17createGridPatternEv
inline void QCanvasGridPatternPrivate::createGridPattern() const
{
    auto *d = this;
    QCPaint &p = DECONST(d)->paint;
    p.brushType = BrushGrid;
    p.transform = QTransform::fromTranslate(d->x, d->y);
    if (!qFuzzyIsNull(d->angle))
        p.transform = p.transform.rotateRadians(d->angle);

    p.extent[0] = float(d->width);
    p.extent[1] = float(d->height);

    p.feather = float(d->feather);
    p.radius = float(d->lineWidth);

    p.innerColor = { d->lineColor.redF(),
                     d->lineColor.greenF(),
                     d->lineColor.blueF(),
                     d->lineColor.alphaF() };
    p.outerColor = { d->backgroundColor.redF(),
                     d->backgroundColor.greenF(),
                     d->backgroundColor.blueF(),
                     d->backgroundColor.alphaF() };
}
//  -----------------------------------------------------------------------

//  A QCanvasGridPatternPrivate that Python can take functions over in. Every QCanvasGridPatternPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasGridPatternPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasGridPatternPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasGridPatternPrivate : public QCanvasGridPatternPrivate {
public:
  using QCanvasGridPatternPrivate::QCanvasGridPatternPrivate;
  CuteQCanvasGridPatternPrivate(const QCanvasGridPatternPrivate & other) : QCanvasGridPatternPrivate(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QCanvasBrushPrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QCanvasBrushPrivate11createPaintEP14QCanvasPainter")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QCanvasBrushPrivate *QCanvasGridPatternPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasGridPatternPrivateCall0 call = reinterpret_cast<CuteQCanvasGridPatternPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return QCanvasGridPatternPrivate::clone();
  }

  //  QCPaint QCanvasGridPatternPrivate::createPaint(QCanvasPainter
  //      *painter) const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasGridPatternPrivateCall1 call = reinterpret_cast<CuteQCanvasGridPatternPrivateCall1>(taken[1]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return QCanvasGridPatternPrivate::createPaint(painter);
  }
};

//  QCanvasBrushPrivate *QCanvasGridPatternPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN25QCanvasGridPatternPrivate5cloneEv(
    QCanvasGridPatternPrivate *self) {
  return self->clone();
}

//  bool QCanvasGridPatternPrivate::equals(const QCanvasBrushPrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QCanvasGridPatternPrivate6equalsERK19QCanvasBrushPrivate(
    const QCanvasGridPatternPrivate *self,
    const QCanvasBrushPrivate *other) {
  return self->equals(*other);
}

//  QCPaint QCanvasGridPatternPrivate::createPaint(QCanvasPainter *painter)
//      const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZNK25QCanvasGridPatternPrivate11createPaintEP14QCanvasPainter(
    const QCanvasGridPatternPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->createPaint(painter));
}

//  QCanvasGridPatternPrivate
//      *QCanvasGridPatternPrivate::get(QCanvasGridPattern *brush)
extern "C" Q_DECL_EXPORT
QCanvasGridPatternPrivate *ritual_ZN25QCanvasGridPatternPrivate3getEP18QCanvasGridPattern(
    QCanvasGridPattern *brush) {
  return QCanvasGridPatternPrivate::get(brush);
}

//  const QCanvasGridPatternPrivate *QCanvasGridPatternPrivate::get(const
//      QCanvasGridPattern *brush)
extern "C" Q_DECL_EXPORT
const QCanvasGridPatternPrivate *ritual_ZN25QCanvasGridPatternPrivate3getEPK18QCanvasGridPattern(
    const QCanvasGridPattern *brush) {
  return QCanvasGridPatternPrivate::get(brush);
}

//  QCanvasGridPattern
//      QCanvasGridPatternPrivate::create(QCanvasGridPatternPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN25QCanvasGridPatternPrivate6createEPS_(
    QCanvasGridPatternPrivate *p) {
  return new QCanvasGridPattern(QCanvasGridPatternPrivate::create(p));
}

//  QCanvasGridPattern QCanvasGridPatternPrivate::getFromCanvasBrush(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN25QCanvasGridPatternPrivate18getFromCanvasBrushERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasGridPattern(
      QCanvasGridPatternPrivate::getFromCanvasBrush(
          *brush));
}

//  void QCanvasGridPatternPrivate::createGridPattern() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QCanvasGridPatternPrivate17createGridPatternEv(
    const QCanvasGridPatternPrivate *self) {
  self->createGridPattern();
}

//  QCanvasGridPatternPrivate::~QCanvasGridPatternPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanvasGridPatternPrivateD1Ev(
    QCanvasGridPatternPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQCanvasGridPatternPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasGridPatternPrivate(
    QCanvasGridPatternPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasGridPatternPrivate *>(self)->take(key, call);
}

//  QCanvasBrushPrivate *QCanvasGridPatternPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_own_ZN25QCanvasGridPatternPrivate5cloneEv(
    QCanvasGridPatternPrivate *self) {
  return self->QCanvasGridPatternPrivate::clone();
}

//  QCPaint QCanvasGridPatternPrivate::createPaint(QCanvasPainter *painter)
//      const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_own_ZNK25QCanvasGridPatternPrivate11createPaintEP14QCanvasPainter(
    const QCanvasGridPatternPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->QCanvasGridPatternPrivate::createPaint(painter));
}
