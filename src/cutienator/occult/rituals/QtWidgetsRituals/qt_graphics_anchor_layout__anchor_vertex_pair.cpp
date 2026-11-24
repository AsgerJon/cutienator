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

//  A QtGraphicsAnchorLayout::AnchorVertexPair that Python can take functions over in. Every QtGraphicsAnchorLayout::AnchorVertexPair
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
#if defined(QT_DEBUG)
typedef QString * (*CuteQtGraphicsAnchorLayout_AnchorVertexPairCall0)(const void *, int *);
#endif  // defined(QT_DEBUG)
#endif  // QT_CONFIG(graphicsview)
class CuteQtGraphicsAnchorLayout_AnchorVertexPair : public QtGraphicsAnchorLayout::AnchorVertexPair {
public:
  using QtGraphicsAnchorLayout::AnchorVertexPair::AnchorVertexPair;
  CuteQtGraphicsAnchorLayout_AnchorVertexPair(const QtGraphicsAnchorLayout::AnchorVertexPair &other) : QtGraphicsAnchorLayout::AnchorVertexPair(other) {}
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
  //  QString QtGraphicsAnchorLayout::AnchorVertexPair::toString() const
  QString toString() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQtGraphicsAnchorLayout_AnchorVertexPairCall0 call = reinterpret_cast<CuteQtGraphicsAnchorLayout_AnchorVertexPairCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QtGraphicsAnchorLayout::AnchorVertexPair::toString();
  }
#endif  // defined(QT_DEBUG)
#endif  // QT_CONFIG(graphicsview)
};

//  QtGraphicsAnchorLayout::AnchorVertexPair::AnchorVertexPair(AnchorVertex
//      *v1, AnchorVertex *v2, AnchorData *data)
extern "C" Q_DECL_EXPORT
QtGraphicsAnchorLayout::AnchorVertexPair *ritual_ZN22QtGraphicsAnchorLayout16AnchorVertexPairC1EPNS_12AnchorVertexES2_PNS_10AnchorDataE(
    QtGraphicsAnchorLayout::AnchorVertex *v1,
    QtGraphicsAnchorLayout::AnchorVertex *v2,
    QtGraphicsAnchorLayout::AnchorData *data) {
  return new CuteQtGraphicsAnchorLayout_AnchorVertexPair(v1, v2, data);
}

#if defined(QT_DEBUG)
//  QString QtGraphicsAnchorLayout::AnchorVertexPair::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QtGraphicsAnchorLayout16AnchorVertexPair8toStringEv(
    const QtGraphicsAnchorLayout::AnchorVertexPair *self) {
  return new QString(self->toString());
}
#endif  // defined(QT_DEBUG)

//  QtGraphicsAnchorLayout::AnchorVertexPair::~AnchorVertexPair()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtGraphicsAnchorLayout16AnchorVertexPairD1Ev(
    QtGraphicsAnchorLayout::AnchorVertexPair *self) {
  delete self;
}

//  a Python function taken by a CuteQtGraphicsAnchorLayout_AnchorVertexPair,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtGraphicsAnchorLayout_AnchorVertexPair(
    QtGraphicsAnchorLayout::AnchorVertexPair *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtGraphicsAnchorLayout_AnchorVertexPair *>(self)->take(key, call);
}

#if defined(QT_DEBUG)
//  QString QtGraphicsAnchorLayout::AnchorVertexPair::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QtGraphicsAnchorLayout16AnchorVertexPair8toStringEv(
    const QtGraphicsAnchorLayout::AnchorVertexPair *self) {
  return new QString(
      self->QtGraphicsAnchorLayout::AnchorVertexPair::toString());
}
#endif  // defined(QT_DEBUG)

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
