//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimate_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgAnimateNode that Python can take functions over in. Every QSvgAnimateNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgAnimateNodeCall0)(const void *, int *);
typedef bool (*CuteQSvgAnimateNodeCall1)(const void *, int *);
typedef bool (*CuteQSvgAnimateNodeCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgAnimateNodeCall3)(const void *, int *);
typedef bool (*CuteQSvgAnimateNodeCall4)(const void *, int *);
typedef void (*CuteQSvgAnimateNodeCall5)(const void *, QSvgAbstractAnimatedProperty *, int *);
class CuteQSvgAnimateNode : public QSvgAnimateNode {
public:
  using QSvgAnimateNode::QSvgAnimateNode;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation13animationTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation8isActiveEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAnimatedProperty")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  AnimationType QSvgAnimateNode::animationType() const
  QSvgAbstractAnimation::AnimationType animationType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAnimateNodeCall0 call = reinterpret_cast<CuteQSvgAnimateNodeCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgAbstractAnimation::AnimationType>(given);
    }
    return QSvgAnimateNode::animationType();
  }

  //  bool QSvgAnimateNode::isActive() const
  bool isActive() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgAnimateNodeCall1 call = reinterpret_cast<CuteQSvgAnimateNodeCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgAnimateNode::isActive();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgAnimateNodeCall2 call = reinterpret_cast<CuteQSvgAnimateNodeCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  Type QSvgNode::type() const
  QSvgNode::Type type() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgAnimateNodeCall3 call = reinterpret_cast<CuteQSvgAnimateNodeCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return {};
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSvgAnimateNodeCall4 call = reinterpret_cast<CuteQSvgAnimateNodeCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }

  //  void
  //      QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedPropert
  //      y *property)
  void appendProperty(QSvgAbstractAnimatedProperty *property) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSvgAnimateNodeCall5 call = reinterpret_cast<CuteQSvgAnimateNodeCall5>(taken[5]);
      call(this, property, &handled);
      if (handled) return;
    }
    QSvgAbstractAnimation::appendProperty(property);
  }
};

//  QSvgAnimateNode::~QSvgAnimateNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgAnimateNodeD1Ev(QSvgAnimateNode *self) {
  delete self;
}

//  void QSvgAnimateNode::setLinkId(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgAnimateNode9setLinkIdERK7QString(
    QSvgAnimateNode *self,
    const QString *link) {
  self->setLinkId(*link);
}

//  const QString &QSvgAnimateNode::linkId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSvgAnimateNode6linkIdEv(const QSvgAnimateNode *self) {
  return new QString(self->linkId());
}

//  AnimationType QSvgAnimateNode::animationType() const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimation::AnimationType ritual_ZNK15QSvgAnimateNode13animationTypeEv(
    const QSvgAnimateNode *self) {
  return self->animationType();
}

//  bool QSvgAnimateNode::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSvgAnimateNode8isActiveEv(const QSvgAnimateNode *self) {
  return self->isActive();
}

//  void QSvgAnimateNode::setRunningTime(int startMs, int durMs, int endMs,
//      int by)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgAnimateNode14setRunningTimeEiiii(
    QSvgAnimateNode *self,
    int startMs,
    int durMs,
    int endMs,
    int by) {
  self->setRunningTime(startMs, durMs, endMs, by);
}

//  void QSvgAnimateNode::setRepeatCount(qreal repeatCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgAnimateNode14setRepeatCountEd(
    QSvgAnimateNode *self,
    qreal repeatCount) {
  self->setRepeatCount(repeatCount);
}

//  void QSvgAnimateNode::setFill(Fill fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgAnimateNode7setFillENS_4FillE(
    QSvgAnimateNode *self,
    QSvgAnimateNode::Fill fill) {
  self->setFill(fill);
}

//  Fill QSvgAnimateNode::fill() const
extern "C" Q_DECL_EXPORT
QSvgAnimateNode::Fill ritual_ZNK15QSvgAnimateNode4fillEv(
    const QSvgAnimateNode *self) {
  return self->fill();
}

//  void QSvgAnimateNode::setAdditiveType(Additive additive)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgAnimateNode15setAdditiveTypeENS_8AdditiveE(
    QSvgAnimateNode *self,
    QSvgAnimateNode::Additive additive) {
  self->setAdditiveType(additive);
}

//  Additive QSvgAnimateNode::additiveType() const
extern "C" Q_DECL_EXPORT
QSvgAnimateNode::Additive ritual_ZNK15QSvgAnimateNode12additiveTypeEv(
    const QSvgAnimateNode *self) {
  return self->additiveType();
}

//  QSvgAnimateNode as the QSvgAbstractAnimation it is built on
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimation *ritual_cast_QSvgAnimateNode_QSvgAbstractAnimation(
    QSvgAnimateNode *self) {
  return static_cast<QSvgAbstractAnimation *>(self);
}

//  a Python function taken by a CuteQSvgAnimateNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAnimateNode(
    QSvgAnimateNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAnimateNode *>(self)->take(key, call);
}

//  AnimationType QSvgAnimateNode::animationType() const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimation::AnimationType ritual_own_ZNK15QSvgAnimateNode13animationTypeEv(
    const QSvgAnimateNode *self) {
  return self->QSvgAnimateNode::animationType();
}

//  bool QSvgAnimateNode::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QSvgAnimateNode8isActiveEv(
    const QSvgAnimateNode *self) {
  return self->QSvgAnimateNode::isActive();
}
