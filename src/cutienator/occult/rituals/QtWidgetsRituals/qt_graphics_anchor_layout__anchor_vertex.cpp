//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QtGraphicsAnchorLayout::AnchorVertex that Python can take functions over in. Every QtGraphicsAnchorLayout::AnchorVertex
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
#if defined(QT_DEBUG)
typedef QString * (*CuteQtGraphicsAnchorLayout_AnchorVertexCall0)(const void *, int *);
#endif  // defined(QT_DEBUG)
#endif  // QT_CONFIG(graphicsview)
class CuteQtGraphicsAnchorLayout_AnchorVertex : public QtGraphicsAnchorLayout::AnchorVertex {
public:
  using QtGraphicsAnchorLayout::AnchorVertex::AnchorVertex;
  CuteQtGraphicsAnchorLayout_AnchorVertex(const QtGraphicsAnchorLayout::AnchorVertex &other) : QtGraphicsAnchorLayout::AnchorVertex(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
#if defined(QT_DEBUG)
    if (!std::strcmp(key, "_ZNK22QtGraphicsAnchorLayout12AnchorVertex8toStringEv")) {
      taken[0] = call;
      return true;
    }
#endif  // defined(QT_DEBUG)
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
#if defined(QT_DEBUG)
  //  QString QtGraphicsAnchorLayout::AnchorVertex::toString() const
  QString toString() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQtGraphicsAnchorLayout_AnchorVertexCall0 call = reinterpret_cast<CuteQtGraphicsAnchorLayout_AnchorVertexCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QtGraphicsAnchorLayout::AnchorVertex::toString();
  }
#endif  // defined(QT_DEBUG)
#endif  // QT_CONFIG(graphicsview)
};

//  QtGraphicsAnchorLayout::AnchorVertex::AnchorVertex(QGraphicsLayoutItem
//      *item, Qt::AnchorPoint edge)
extern "C" Q_DECL_EXPORT
QtGraphicsAnchorLayout::AnchorVertex *ritual_ZN22QtGraphicsAnchorLayout12AnchorVertexC1EP19QGraphicsLayoutItemN2Qt11AnchorPointE(
    QGraphicsLayoutItem *item,
    Qt::AnchorPoint edge) {
  return new CuteQtGraphicsAnchorLayout_AnchorVertex(item, edge);
}

//  QtGraphicsAnchorLayout::AnchorVertex::AnchorVertex()
extern "C" Q_DECL_EXPORT
QtGraphicsAnchorLayout::AnchorVertex *ritual_ZN22QtGraphicsAnchorLayout12AnchorVertexC1Ev() {
  return new CuteQtGraphicsAnchorLayout_AnchorVertex();
}

//  QtGraphicsAnchorLayout::AnchorVertex::~AnchorVertex()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtGraphicsAnchorLayout12AnchorVertexD1Ev(
    QtGraphicsAnchorLayout::AnchorVertex *self) {
  delete self;
}

#if defined(QT_DEBUG)
//  QString QtGraphicsAnchorLayout::AnchorVertex::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QtGraphicsAnchorLayout12AnchorVertex8toStringEv(
    const QtGraphicsAnchorLayout::AnchorVertex *self) {
  return new QString(self->toString());
}
#endif  // defined(QT_DEBUG)

//  a Python function taken by a CuteQtGraphicsAnchorLayout_AnchorVertex, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtGraphicsAnchorLayout_AnchorVertex(
    QtGraphicsAnchorLayout::AnchorVertex *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtGraphicsAnchorLayout_AnchorVertex *>(self)->take(key, call);
}

#if defined(QT_DEBUG)
//  QString QtGraphicsAnchorLayout::AnchorVertex::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QtGraphicsAnchorLayout12AnchorVertex8toStringEv(
    const QtGraphicsAnchorLayout::AnchorVertex *self) {
  return new QString(self->QtGraphicsAnchorLayout::AnchorVertex::toString());
}
#endif  // defined(QT_DEBUG)

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
