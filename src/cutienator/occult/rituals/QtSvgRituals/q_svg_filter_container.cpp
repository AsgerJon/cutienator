//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgFilterContainer that Python can take functions over in. Every QSvgFilterContainer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFilterContainerCall0)(const void *, int *);
typedef bool (*CuteQSvgFilterContainerCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFilterContainerCall2)(const void *, int *);
class CuteQSvgFilterContainer : public QSvgFilterContainer {
public:
  using QSvgFilterContainer::QSvgFilterContainer;
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

  //  Type QSvgFilterContainer::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFilterContainerCall0 call = reinterpret_cast<CuteQSvgFilterContainerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFilterContainer::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFilterContainerCall1 call = reinterpret_cast<CuteQSvgFilterContainerCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgFilterContainerCall2 call = reinterpret_cast<CuteQSvgFilterContainerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFilterContainer::QSvgFilterContainer(QSvgNode *parent, const
//      QSvgRectF &bounds, QtSvg::UnitTypes filterUnits, QtSvg::UnitTypes
//      primitiveUnits)
extern "C" Q_DECL_EXPORT
QSvgFilterContainer *ritual_ZN19QSvgFilterContainerC1EP8QSvgNodeRK9QSvgRectFN5QtSvg9UnitTypesES6_(
    QSvgNode *parent,
    const QSvgRectF *bounds,
    QtSvg::UnitTypes filterUnits,
    QtSvg::UnitTypes primitiveUnits) {
  return new CuteQSvgFilterContainer(
      parent,
      *bounds,
      filterUnits,
      primitiveUnits);
}

//  QSvgFilterContainer::~QSvgFilterContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSvgFilterContainerD1Ev(QSvgFilterContainer *self) {
  delete self;
}

//  void QSvgFilterContainer::drawCommand(QPainter *a0, QSvgExtraStates &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSvgFilterContainer11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgFilterContainer *self,
    QPainter *a0,
    QSvgExtraStates *a1) {
  self->drawCommand(a0, *a1);
}

//  bool QSvgFilterContainer::shouldDrawNode(QPainter *a0, QSvgExtraStates
//      &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSvgFilterContainer14shouldDrawNodeEP8QPainterR15QSvgExtraStates(
    const QSvgFilterContainer *self,
    QPainter *a0,
    QSvgExtraStates *a1) {
  return self->shouldDrawNode(a0, *a1);
}

//  Type QSvgFilterContainer::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK19QSvgFilterContainer4typeEv(
    const QSvgFilterContainer *self) {
  return self->type();
}

//  QImage QSvgFilterContainer::applyFilter(const QImage &buffer, QPainter
//      *p, const QRectF &bounds) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK19QSvgFilterContainer11applyFilterERK6QImageP8QPainterRK6QRectF(
    const QSvgFilterContainer *self,
    const QImage *buffer,
    QPainter *p,
    const QRectF *bounds) {
  return new QImage(self->applyFilter(*buffer, p, *bounds));
}

//  void QSvgFilterContainer::setSupported(bool supported)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSvgFilterContainer12setSupportedEb(
    QSvgFilterContainer *self,
    bool supported) {
  self->setSupported(supported);
}

//  bool QSvgFilterContainer::supported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSvgFilterContainer9supportedEv(
    const QSvgFilterContainer *self) {
  return self->supported();
}

//  QRectF QSvgFilterContainer::filterRegion(const QRectF &itemBounds) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QSvgFilterContainer12filterRegionERK6QRectF(
    const QSvgFilterContainer *self,
    const QRectF *itemBounds) {
  return new QRectF(self->filterRegion(*itemBounds));
}

//  QSvgRectF QSvgFilterContainer::rect() const
extern "C" Q_DECL_EXPORT
QSvgRectF *ritual_ZNK19QSvgFilterContainer4rectEv(
    const QSvgFilterContainer *self) {
  return new QSvgRectF(self->rect());
}

//  QtSvg::UnitTypes QSvgFilterContainer::filterUnits() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK19QSvgFilterContainer11filterUnitsEv(
    const QSvgFilterContainer *self) {
  return self->filterUnits();
}

//  QtSvg::UnitTypes QSvgFilterContainer::primitiveUnits() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK19QSvgFilterContainer14primitiveUnitsEv(
    const QSvgFilterContainer *self) {
  return self->primitiveUnits();
}

//  a Python function taken by a CuteQSvgFilterContainer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFilterContainer(
    QSvgFilterContainer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFilterContainer *>(self)->take(key, call);
}

//  Type QSvgFilterContainer::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK19QSvgFilterContainer4typeEv(
    const QSvgFilterContainer *self) {
  return self->QSvgFilterContainer::type();
}
