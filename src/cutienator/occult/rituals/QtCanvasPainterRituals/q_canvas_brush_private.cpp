//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasbrush_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasbrush_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasbrush.h>
#include <cstring>

//  A QCanvasBrushPrivate that Python can take functions over in. Every QCanvasBrushPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasBrushPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasBrushPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasBrushPrivate : public QCanvasBrushPrivate {
public:
  using QCanvasBrushPrivate::QCanvasBrushPrivate;
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

  //  QCanvasBrushPrivate *QCanvasBrushPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasBrushPrivateCall0 call = reinterpret_cast<CuteQCanvasBrushPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return {};
  }

  //  QCPaint QCanvasBrushPrivate::createPaint(QCanvasPainter *painter)
  //      const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasBrushPrivateCall1 call = reinterpret_cast<CuteQCanvasBrushPrivateCall1>(taken[1]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QCanvasBrushPrivate::~QCanvasBrushPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasBrushPrivateD1Ev(QCanvasBrushPrivate *self) {
  delete self;
}

//  QCanvasBrushPrivate *QCanvasBrushPrivate::clone()
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN19QCanvasBrushPrivate5cloneEv(
    QCanvasBrushPrivate *self) {
  return self->clone();
}

//  QCPaint QCanvasBrushPrivate::createPaint(QCanvasPainter *painter) const
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZNK19QCanvasBrushPrivate11createPaintEP14QCanvasPainter(
    const QCanvasBrushPrivate *self,
    QCanvasPainter *painter) {
  return new QCPaint(self->createPaint(painter));
}

//  bool QCanvasBrushPrivate::equals(const QCanvasBrushPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCanvasBrushPrivate6equalsERKS_(
    const QCanvasBrushPrivate *self,
    const QCanvasBrushPrivate *other) {
  return self->equals(*other);
}

//  QCanvasBrushPrivate *QCanvasBrushPrivate::get(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN19QCanvasBrushPrivate3getERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return QCanvasBrushPrivate::get(*brush);
}

//  QCanvasBrushPrivate *QCanvasBrushPrivate::get(QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasBrushPrivate *ritual_ZN19QCanvasBrushPrivate3getER12QCanvasBrush(
    QCanvasBrush *brush) {
  return QCanvasBrushPrivate::get(*brush);
}

//  QCanvasBrush QCanvasBrushPrivate::create(QCanvasBrushPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZN19QCanvasBrushPrivate6createEPS_(
    QCanvasBrushPrivate *p) {
  return new QCanvasBrush(QCanvasBrushPrivate::create(p));
}

//  a Python function taken by a CuteQCanvasBrushPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasBrushPrivate(
    QCanvasBrushPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasBrushPrivate *>(self)->take(key, call);
}
