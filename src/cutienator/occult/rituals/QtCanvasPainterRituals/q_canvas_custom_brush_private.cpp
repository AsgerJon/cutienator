//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvascustombrush_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvascustombrush_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvascustombrush.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcanvascustombrush.h"
#include "qcanvascustombrush_p.h"
#include <QFile>
#include <QDebug>
#include <QDataStream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvascustombrush.cpp, line 328, as _ZNK25QCanvasCustomBrushPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasCustomBrushPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &bd = static_cast<const QCanvasCustomBrushPrivate &>(other);

    if (fragmentShader != bd.fragmentShader
        || vertexShader != bd.vertexShader
        || timeRunning != bd.timeRunning
        || time != bd.time
        || data[0] != bd.data[0]
        || data[1] != bd.data[1]
        || data[2] != bd.data[2]
        || data[3] != bd.data[3])
        return false;

    return true;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvascustombrush.cpp, line 538, as _ZN25QCanvasCustomBrushPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasCustomBrushPrivate::clone()
{
    return new QCanvasCustomBrushPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvascustombrush.cpp, line 543, as _ZNK25QCanvasCustomBrushPrivate11createPaintEP14QCanvasPainter
inline QCPaint QCanvasCustomBrushPrivate::createPaint(QCanvasPainter *) const
{
    QCPaint empty;
    return empty;
}
//  -----------------------------------------------------------------------

//  A QCanvasCustomBrushPrivate that Python can take functions over in. Every QCanvasCustomBrushPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasCustomBrushPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasCustomBrushPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasCustomBrushPrivate : public QCanvasCustomBrushPrivate {
public:
  using QCanvasCustomBrushPrivate::QCanvasCustomBrushPrivate;
  CuteQCanvasCustomBrushPrivate(const QCanvasCustomBrushPrivate &other) : QCanvasCustomBrushPrivate(other) {}
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

  //  QCanvasBrushPrivate *QCanvasCustomBrushPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasCustomBrushPrivateCall0 call = reinterpret_cast<CuteQCanvasCustomBrushPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return QCanvasCustomBrushPrivate::clone();
  }

  //  QCPaint QCanvasCustomBrushPrivate::createPaint(QCanvasPainter
  //      *painter) const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasCustomBrushPrivateCall1 call = reinterpret_cast<CuteQCanvasCustomBrushPrivateCall1>(taken[1]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return QCanvasCustomBrushPrivate::createPaint(painter);
  }
};

//  QCanvasCustomBrushPrivate::QCanvasCustomBrushPrivate()
extern "C" Q_DECL_EXPORT
QCanvasCustomBrushPrivate *ritual_ZN25QCanvasCustomBrushPrivateC1Ev() {
  return new CuteQCanvasCustomBrushPrivate();
}

//  QCanvasCustomBrushPrivate::QCanvasCustomBrushPrivate(const
//      QCanvasCustomBrushPrivate &a0)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrushPrivate *ritual_ZN25QCanvasCustomBrushPrivateC1ERKS_(
    const QCanvasCustomBrushPrivate *a0) {
  return new CuteQCanvasCustomBrushPrivate(*a0);
}

//  QCanvasBrushPrivate *QCanvasCustomBrushPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN25QCanvasCustomBrushPrivate5cloneEv(
    QCanvasCustomBrushPrivate *self) {
  return self->clone();
}

//  QCPaint QCanvasCustomBrushPrivate::createPaint(QCanvasPainter *painter)
//      const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZNK25QCanvasCustomBrushPrivate11createPaintEP14QCanvasPainter(
    const QCanvasCustomBrushPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->createPaint(painter));
}

//  QCanvasCustomBrushPrivate
//      *QCanvasCustomBrushPrivate::get(QCanvasCustomBrush *brush)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrushPrivate *ritual_ZN25QCanvasCustomBrushPrivate3getEP18QCanvasCustomBrush(
    QCanvasCustomBrush *brush) {
  return QCanvasCustomBrushPrivate::get(brush);
}

//  const QCanvasCustomBrushPrivate *QCanvasCustomBrushPrivate::get(const
//      QCanvasCustomBrush *brush)
extern "C" Q_DECL_EXPORT
const QCanvasCustomBrushPrivate *ritual_ZN25QCanvasCustomBrushPrivate3getEPK18QCanvasCustomBrush(
    const QCanvasCustomBrush *brush) {
  return QCanvasCustomBrushPrivate::get(brush);
}

//  const QCanvasCustomBrushPrivate *QCanvasCustomBrushPrivate::get(const
//      QCanvasCustomBrush &brush)
extern "C" Q_DECL_EXPORT
const QCanvasCustomBrushPrivate *ritual_ZN25QCanvasCustomBrushPrivate3getERK18QCanvasCustomBrush(
    const QCanvasCustomBrush *brush) {
  return QCanvasCustomBrushPrivate::get(*brush);
}

//  QCanvasCustomBrush
//      QCanvasCustomBrushPrivate::create(QCanvasCustomBrushPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN25QCanvasCustomBrushPrivate6createEPS_(
    QCanvasCustomBrushPrivate *p) {
  return new QCanvasCustomBrush(QCanvasCustomBrushPrivate::create(p));
}

//  QCanvasCustomBrush QCanvasCustomBrushPrivate::getFromCanvasBrush(const
//      QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN25QCanvasCustomBrushPrivate18getFromCanvasBrushERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasCustomBrush(
      QCanvasCustomBrushPrivate::getFromCanvasBrush(
          *brush));
}

//  QCanvasCustomBrushPrivate::~QCanvasCustomBrushPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanvasCustomBrushPrivateD1Ev(
    QCanvasCustomBrushPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQCanvasCustomBrushPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasCustomBrushPrivate(
    QCanvasCustomBrushPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasCustomBrushPrivate *>(self)->take(key, call);
}

//  QCanvasBrushPrivate *QCanvasCustomBrushPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_own_ZN25QCanvasCustomBrushPrivate5cloneEv(
    QCanvasCustomBrushPrivate *self) {
  return self->QCanvasCustomBrushPrivate::clone();
}

//  QCPaint QCanvasCustomBrushPrivate::createPaint(QCanvasPainter *painter)
//      const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_own_ZNK25QCanvasCustomBrushPrivate11createPaintEP14QCanvasPainter(
    const QCanvasCustomBrushPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->QCanvasCustomBrushPrivate::createPaint(painter));
}
