//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasimagepattern_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasimagepattern_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasimagepattern.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasimagepattern.h>
#include <QtCanvasPainter/private/qcanvasimagepattern_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimagepattern.cpp, line 414, as local:qcanvasimagepattern.cpp:DECONST
#define DECONST(d) const_cast<QCanvasImagePatternPrivate *>(d)

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimagepattern.cpp, line 435, as _ZN26QCanvasImagePatternPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasImagePatternPrivate::clone()
{
    return new QCanvasImagePatternPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimagepattern.cpp, line 178, as _ZNK26QCanvasImagePatternPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasImagePatternPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &pd = static_cast<const QCanvasImagePatternPrivate &>(other);

    if (x != pd.x
        || y != pd.y
        || width != pd.width
        || height != pd.height
        || angle != pd.angle
        || tintColor != pd.tintColor)
        return false;

    // For images comparing the id is enough
    if (image.id() != pd.image.id())
        return false;

    return true;
}
//  -----------------------------------------------------------------------

//  A QCanvasImagePatternPrivate that Python can take functions over in. Every QCanvasImagePatternPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasImagePatternPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasImagePatternPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasImagePatternPrivate : public QCanvasImagePatternPrivate {
public:
  using QCanvasImagePatternPrivate::QCanvasImagePatternPrivate;
  CuteQCanvasImagePatternPrivate(const QCanvasImagePatternPrivate & other) : QCanvasImagePatternPrivate(other) {}
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

  //  QCanvasBrushPrivate *QCanvasImagePatternPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasImagePatternPrivateCall0 call = reinterpret_cast<CuteQCanvasImagePatternPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return QCanvasImagePatternPrivate::clone();
  }

  //  QCPaint QCanvasImagePatternPrivate::createPaint(QCanvasPainter
  //      *painter) const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasImagePatternPrivateCall1 call = reinterpret_cast<CuteQCanvasImagePatternPrivateCall1>(taken[1]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return QCanvasImagePatternPrivate::createPaint(painter);
  }
};

//  uint QCanvasImagePatternPrivate::nextSerialNumber()
extern "C" Q_DECL_EXPORT
uint ritual_ZN26QCanvasImagePatternPrivate16nextSerialNumberEv() {
  return QCanvasImagePatternPrivate::nextSerialNumber();
}

//  QCanvasBrushPrivate *QCanvasImagePatternPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN26QCanvasImagePatternPrivate5cloneEv(
    QCanvasImagePatternPrivate *self) {
  return self->clone();
}

//  bool QCanvasImagePatternPrivate::equals(const QCanvasBrushPrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QCanvasImagePatternPrivate6equalsERK19QCanvasBrushPrivate(
    const QCanvasImagePatternPrivate *self,
    const QCanvasBrushPrivate *other) {
  return self->equals(*other);
}

//  QCPaint QCanvasImagePatternPrivate::createPaint(QCanvasPainter *painter)
//      const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZNK26QCanvasImagePatternPrivate11createPaintEP14QCanvasPainter(
    const QCanvasImagePatternPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->createPaint(painter));
}

//  QCanvasImagePatternPrivate
//      *QCanvasImagePatternPrivate::get(QCanvasImagePattern *brush)
extern "C" Q_DECL_EXPORT
QCanvasImagePatternPrivate *ritual_ZN26QCanvasImagePatternPrivate3getEP19QCanvasImagePattern(
    QCanvasImagePattern *brush) {
  return QCanvasImagePatternPrivate::get(brush);
}

//  const QCanvasImagePatternPrivate *QCanvasImagePatternPrivate::get(const
//      QCanvasImagePattern *brush)
extern "C" Q_DECL_EXPORT
const QCanvasImagePatternPrivate *ritual_ZN26QCanvasImagePatternPrivate3getEPK19QCanvasImagePattern(
    const QCanvasImagePattern *brush) {
  return QCanvasImagePatternPrivate::get(brush);
}

//  QCanvasImagePattern
//      QCanvasImagePatternPrivate::create(QCanvasImagePatternPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN26QCanvasImagePatternPrivate6createEPS_(
    QCanvasImagePatternPrivate *p) {
  return new QCanvasImagePattern(QCanvasImagePatternPrivate::create(p));
}

//  QCanvasImagePattern QCanvasImagePatternPrivate::getFromCanvasBrush(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN26QCanvasImagePatternPrivate18getFromCanvasBrushERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasImagePattern(
      QCanvasImagePatternPrivate::getFromCanvasBrush(
          *brush));
}

//  QCanvasImagePatternPrivate::~QCanvasImagePatternPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasImagePatternPrivateD1Ev(
    QCanvasImagePatternPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQCanvasImagePatternPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasImagePatternPrivate(
    QCanvasImagePatternPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasImagePatternPrivate *>(self)->take(key, call);
}
