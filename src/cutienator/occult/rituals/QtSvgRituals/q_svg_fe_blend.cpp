//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QSvgFeBlend that Python can take functions over in. Every QSvgFeBlend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFeBlendCall0)(const void *, int *);
typedef bool (*CuteQSvgFeBlendCall1)(const void *, int *);
typedef bool (*CuteQSvgFeBlendCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFeBlendCall3)(const void *, int *);
class CuteQSvgFeBlend : public QSvgFeBlend {
public:
  using QSvgFeBlend::QSvgFeBlend;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgFeBlend::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeBlendCall0 call = reinterpret_cast<CuteQSvgFeBlendCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFeBlend::type();
  }

  //  bool QSvgFeBlend::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeBlendCall1 call = reinterpret_cast<CuteQSvgFeBlendCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgFeBlend::requiresSourceAlpha();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgFeBlendCall2 call = reinterpret_cast<CuteQSvgFeBlendCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeBlendCall3 call = reinterpret_cast<CuteQSvgFeBlendCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeBlend::QSvgFeBlend(QSvgNode *parent, const QString &input, const
//      QString &result, const QSvgRectF &rect, const QString &input2, Mode
//      mode)
extern "C" Q_DECL_EXPORT
QSvgFeBlend *ritual_ZN11QSvgFeBlendC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFS4_NS_4ModeE(
    QSvgNode *parent,
    const QString *input,
    const QString *result,
    const QSvgRectF *rect,
    const QString *input2,
    QSvgFeBlend::Mode mode) {
  return new CuteQSvgFeBlend(parent, *input, *result, *rect, *input2, mode);
}

//  QSvgFeBlend::~QSvgFeBlend()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgFeBlendD1Ev(QSvgFeBlend *self) {
  delete self;
}

//  Type QSvgFeBlend::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK11QSvgFeBlend4typeEv(const QSvgFeBlend *self) {
  return self->type();
}

//  QImage QSvgFeBlend::apply(const QMap<QString, QImage> &sources, QPainter
//      *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK11QSvgFeBlend5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeBlend *self,
    const QMap<QString, QImage> *sources,
    QPainter *p,
    const QRectF *itemBounds,
    const QRectF *filterBounds,
    QtSvg::UnitTypes primitiveUnits,
    QtSvg::UnitTypes filterUnits) {
  return new QImage(
      self->apply(
          *sources,
          p,
          *itemBounds,
          *filterBounds,
          primitiveUnits,
          filterUnits));
}

//  bool QSvgFeBlend::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgFeBlend19requiresSourceAlphaEv(
    const QSvgFeBlend *self) {
  return self->requiresSourceAlpha();
}

//  QString QSvgFeBlend::input2() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QSvgFeBlend6input2Ev(const QSvgFeBlend *self) {
  return new QString(self->input2());
}

//  Mode QSvgFeBlend::mode() const
extern "C" Q_DECL_EXPORT
QSvgFeBlend::Mode ritual_ZNK11QSvgFeBlend4modeEv(const QSvgFeBlend *self) {
  return self->mode();
}

//  a Python function taken by a CuteQSvgFeBlend, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeBlend(
    QSvgFeBlend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeBlend *>(self)->take(key, call);
}

//  Type QSvgFeBlend::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK11QSvgFeBlend4typeEv(const QSvgFeBlend *self) {
  return self->QSvgFeBlend::type();
}

//  bool QSvgFeBlend::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSvgFeBlend19requiresSourceAlphaEv(
    const QSvgFeBlend *self) {
  return self->QSvgFeBlend::requiresSourceAlpha();
}
