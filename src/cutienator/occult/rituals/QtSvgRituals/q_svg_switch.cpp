//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgSwitch that Python can take functions over in. Every QSvgSwitch
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgSwitchCall0)(const void *, int *);
typedef bool (*CuteQSvgSwitchCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgSwitchCall2)(const void *, int *);
class CuteQSvgSwitch : public QSvgSwitch {
public:
  using QSvgSwitch::QSvgSwitch;
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

  //  Type QSvgSwitch::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgSwitchCall0 call = reinterpret_cast<CuteQSvgSwitchCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgSwitch::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgSwitchCall1 call = reinterpret_cast<CuteQSvgSwitchCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgSwitchCall2 call = reinterpret_cast<CuteQSvgSwitchCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgSwitch::QSvgSwitch(QSvgNode *parent)
extern "C" Q_DECL_EXPORT
QSvgSwitch *ritual_ZN10QSvgSwitchC1EP8QSvgNode(QSvgNode *parent) {
  return new CuteQSvgSwitch(parent);
}

//  QSvgSwitch::~QSvgSwitch()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgSwitchD1Ev(QSvgSwitch *self) {
  delete self;
}

//  Type QSvgSwitch::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK10QSvgSwitch4typeEv(const QSvgSwitch *self) {
  return self->type();
}

//  QSvgNode *QSvgSwitch::childToRender() const
extern "C" Q_DECL_EXPORT
QSvgNode *ritual_ZNK10QSvgSwitch13childToRenderEv(const QSvgSwitch *self) {
  return self->childToRender();
}

//  void QSvgSwitch::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgSwitch4initEv(QSvgSwitch *self) {
  self->init();
}

//  a Python function taken by a CuteQSvgSwitch, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgSwitch(QSvgSwitch *self, const char *key, void *call) {
  return static_cast<CuteQSvgSwitch *>(self)->take(key, call);
}

//  Type QSvgSwitch::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK10QSvgSwitch4typeEv(const QSvgSwitch *self) {
  return self->QSvgSwitch::type();
}
