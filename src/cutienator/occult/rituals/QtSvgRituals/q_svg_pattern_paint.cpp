//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <cstring>

//  A QSvgPatternPaint that Python can take functions over in. Every QSvgPatternPaint
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgPatternPaintCall0)(const void *, int *);
class CuteQSvgPatternPaint : public QSvgPatternPaint {
public:
  using QSvgPatternPaint::QSvgPatternPaint;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QSvgPaintServer4typeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgPatternPaint::type() const
  QSvgPaintServer::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgPatternPaintCall0 call = reinterpret_cast<CuteQSvgPatternPaintCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgPaintServer::Type>(given);
    }
    return QSvgPatternPaint::type();
  }
};

//  QSvgPatternPaint::QSvgPatternPaint(QSvgPattern *pattern)
extern "C" Q_DECL_EXPORT
QSvgPatternPaint *ritual_ZN16QSvgPatternPaintC1EP11QSvgPattern(
    QSvgPattern *pattern) {
  return new CuteQSvgPatternPaint(pattern);
}

//  QSvgPatternPaint::~QSvgPatternPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgPatternPaintD1Ev(QSvgPatternPaint *self) {
  delete self;
}

//  Type QSvgPatternPaint::type() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer::Type ritual_ZNK16QSvgPatternPaint4typeEv(
    const QSvgPatternPaint *self) {
  return self->type();
}

//  QBrush QSvgPatternPaint::brush(QPainter *a0, const QSvgNode *a1,
//      QSvgExtraStates &a2)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN16QSvgPatternPaint5brushEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgPatternPaint *self,
    QPainter *a0,
    const QSvgNode *a1,
    QSvgExtraStates *a2) {
  return new QBrush(self->brush(a0, a1, *a2));
}

//  QSvgPattern *QSvgPatternPaint::patternNode()
extern "C" Q_DECL_EXPORT
QSvgPattern *ritual_ZN16QSvgPatternPaint11patternNodeEv(
    QSvgPatternPaint *self) {
  return self->patternNode();
}

//  a Python function taken by a CuteQSvgPatternPaint, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgPatternPaint(
    QSvgPatternPaint *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgPatternPaint *>(self)->take(key, call);
}

//  Type QSvgPatternPaint::type() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer::Type ritual_own_ZNK16QSvgPatternPaint4typeEv(
    const QSvgPatternPaint *self) {
  return self->QSvgPatternPaint::type();
}
