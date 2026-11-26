//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSvgText that Python can take functions over in. Every QSvgText
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgTextCall0)(const void *, int *);
typedef bool (*CuteQSvgTextCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgTextCall2)(const void *, int *);
class CuteQSvgText : public QSvgText {
public:
  using QSvgText::QSvgText;
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

  //  Type QSvgText::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgTextCall0 call = reinterpret_cast<CuteQSvgTextCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgText::type();
  }

  //  bool QSvgText::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgTextCall1 call = reinterpret_cast<CuteQSvgTextCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgText::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgTextCall2 call = reinterpret_cast<CuteQSvgTextCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgText::QSvgText(QSvgNode *parent, const QPointF &coord)
extern "C" Q_DECL_EXPORT
QSvgText *ritual_ZN8QSvgTextC1EP8QSvgNodeRK7QPointF(
    QSvgNode *parent,
    const QPointF *coord) {
  return new CuteQSvgText(parent, *coord);
}

//  QSvgText::~QSvgText()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgTextD1Ev(QSvgText *self) {
  delete self;
}

//  void QSvgText::setTextArea(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgText11setTextAreaERK6QSizeF(
    QSvgText *self,
    const QSizeF *size) {
  self->setTextArea(*size);
}

//  void QSvgText::drawCommand(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgText11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgText *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->drawCommand(p, *states);
}

//  bool QSvgText::shouldDrawNode(QPainter *p, QSvgExtraStates &states) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgText14shouldDrawNodeEP8QPainterR15QSvgExtraStates(
    const QSvgText *self,
    QPainter *p,
    QSvgExtraStates *states) {
  return self->shouldDrawNode(p, *states);
}

//  Type QSvgText::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgText4typeEv(const QSvgText *self) {
  return self->type();
}

//  bool QSvgText::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgText18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgText *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->separateFillStroke(a0, *a1);
}

//  void QSvgText::addTspan(QSvgTspan *tspan)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgText8addTspanEP9QSvgTspan(
    QSvgText *self,
    QSvgTspan *tspan) {
  self->addTspan(tspan);
}

//  const QList<QSvgTspan *> QSvgText::tspans() const
extern "C" Q_DECL_EXPORT
QList<QSvgTspan *> *ritual_ZNK8QSvgText6tspansEv(const QSvgText *self) {
  return new QList<QSvgTspan *>(self->tspans());
}

//  void QSvgText::addText(QStringView text)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgText7addTextE11QStringView(
    QSvgText *self,
    const QString *text) {
  self->addText(QStringView(*text));
}

//  void QSvgText::addLineBreak()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgText12addLineBreakEv(QSvgText *self) {
  self->addLineBreak();
}

//  void QSvgText::setWhitespaceMode(WhitespaceMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgText17setWhitespaceModeENS_14WhitespaceModeE(
    QSvgText *self,
    QSvgText::WhitespaceMode mode) {
  self->setWhitespaceMode(mode);
}

//  QRectF QSvgText::internalFastBounds(QPainter *p, QSvgExtraStates &states)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QSvgText18internalFastBoundsEP8QPainterR15QSvgExtraStates(
    const QSvgText *self,
    QPainter *p,
    QSvgExtraStates *states) {
  return new QRectF(self->internalFastBounds(p, *states));
}

//  QRectF QSvgText::internalBounds(QPainter *p, QSvgExtraStates &states)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QSvgText14internalBoundsEP8QPainterR15QSvgExtraStates(
    const QSvgText *self,
    QPainter *p,
    QSvgExtraStates *states) {
  return new QRectF(self->internalBounds(p, *states));
}

//  QPointF QSvgText::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QSvgText8positionEv(const QSvgText *self) {
  return new QPointF(self->position());
}

//  QSizeF QSvgText::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK8QSvgText4sizeEv(const QSvgText *self) {
  return new QSizeF(self->size());
}

//  WhitespaceMode QSvgText::whitespaceMode() const
extern "C" Q_DECL_EXPORT
QSvgText::WhitespaceMode ritual_ZNK8QSvgText14whitespaceModeEv(
    const QSvgText *self) {
  return self->whitespaceMode();
}

//  void QSvgText::draw_helper(QPainter *p, QSvgExtraStates &states, QRectF
//      *boundingRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QSvgText11draw_helperEP8QPainterR15QSvgExtraStatesP6QRectF(
    const QSvgText *self,
    QPainter *p,
    QSvgExtraStates *states,
    QRectF *boundingRect) {
  self->draw_helper(p, *states, boundingRect);
}

//  a Python function taken by a CuteQSvgText, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgText(QSvgText *self, const char *key, void *call) {
  return static_cast<CuteQSvgText *>(self)->take(key, call);
}

//  Type QSvgText::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK8QSvgText4typeEv(const QSvgText *self) {
  return self->QSvgText::type();
}

//  bool QSvgText::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QSvgText18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgText *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->QSvgText::separateFillStroke(a0, *a1);
}
