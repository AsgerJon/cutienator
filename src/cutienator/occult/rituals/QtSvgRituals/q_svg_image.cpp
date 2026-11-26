//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgImage that Python can take functions over in. Every QSvgImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgImageCall0)(const void *, int *);
typedef bool (*CuteQSvgImageCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgImageCall2)(const void *, int *);
class CuteQSvgImage : public QSvgImage {
public:
  using QSvgImage::QSvgImage;
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

  //  Type QSvgImage::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgImageCall0 call = reinterpret_cast<CuteQSvgImageCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgImage::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgImageCall1 call = reinterpret_cast<CuteQSvgImageCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgImageCall2 call = reinterpret_cast<CuteQSvgImageCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgImage::QSvgImage(QSvgNode *parent, const QImage &image, const QString
//      &filename, const QRectF &bounds)
extern "C" Q_DECL_EXPORT
QSvgImage *ritual_ZN9QSvgImageC1EP8QSvgNodeRK6QImageRK7QStringRK6QRectF(
    QSvgNode *parent,
    const QImage *image,
    const QString *filename,
    const QRectF *bounds) {
  return new CuteQSvgImage(parent, *image, *filename, *bounds);
}

//  QSvgImage::~QSvgImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgImageD1Ev(QSvgImage *self) {
  delete self;
}

//  void QSvgImage::drawCommand(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgImage11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgImage *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->drawCommand(p, *states);
}

//  Type QSvgImage::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK9QSvgImage4typeEv(const QSvgImage *self) {
  return self->type();
}

//  QRectF QSvgImage::internalBounds(QPainter *p, QSvgExtraStates &states)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QSvgImage14internalBoundsEP8QPainterR15QSvgExtraStates(
    const QSvgImage *self,
    QPainter *p,
    QSvgExtraStates *states) {
  return new QRectF(self->internalBounds(p, *states));
}

//  QRectF QSvgImage::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QSvgImage4rectEv(const QSvgImage *self) {
  return new QRectF(self->rect());
}

//  const QImage &QSvgImage::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK9QSvgImage5imageEv(const QSvgImage *self) {
  return new QImage(self->image());
}

//  QString QSvgImage::filename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSvgImage8filenameEv(const QSvgImage *self) {
  return new QString(self->filename());
}

//  a Python function taken by a CuteQSvgImage, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgImage(QSvgImage *self, const char *key, void *call) {
  return static_cast<CuteQSvgImage *>(self)->take(key, call);
}

//  Type QSvgImage::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK9QSvgImage4typeEv(const QSvgImage *self) {
  return self->QSvgImage::type();
}
