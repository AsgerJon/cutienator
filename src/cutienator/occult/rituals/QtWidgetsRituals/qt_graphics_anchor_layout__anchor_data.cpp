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

//  A QtGraphicsAnchorLayout::AnchorData that Python can take functions over in. Every QtGraphicsAnchorLayout::AnchorData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQtGraphicsAnchorLayout_AnchorDataCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQtGraphicsAnchorLayout_AnchorData : public QtGraphicsAnchorLayout::AnchorData {
public:
  using QtGraphicsAnchorLayout::AnchorData::AnchorData;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN22QtGraphicsAnchorLayout10AnchorData19updateChildrenSizesEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void QtGraphicsAnchorLayout::AnchorData::updateChildrenSizes()
  void updateChildrenSizes() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtGraphicsAnchorLayout_AnchorDataCall0 call = reinterpret_cast<CuteQtGraphicsAnchorLayout_AnchorDataCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QtGraphicsAnchorLayout::AnchorData::updateChildrenSizes();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QtGraphicsAnchorLayout::AnchorData::~AnchorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtGraphicsAnchorLayout10AnchorDataD1Ev(
    QtGraphicsAnchorLayout::AnchorData *self) {
  delete self;
}

//  void QtGraphicsAnchorLayout::AnchorData::updateChildrenSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtGraphicsAnchorLayout10AnchorData19updateChildrenSizesEv(
    QtGraphicsAnchorLayout::AnchorData *self) {
  self->updateChildrenSizes();
}

#if defined(QT_DEBUG)
//  QString QtGraphicsAnchorLayout::AnchorData::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QtGraphicsAnchorLayout10AnchorData8toStringEv(
    const QtGraphicsAnchorLayout::AnchorData *self) {
  return new QString(self->toString());
}
#endif  // defined(QT_DEBUG)

//  a Python function taken by a CuteQtGraphicsAnchorLayout_AnchorData, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtGraphicsAnchorLayout_AnchorData(
    QtGraphicsAnchorLayout::AnchorData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtGraphicsAnchorLayout_AnchorData *>(self)->take(key, call);
}

//  void QtGraphicsAnchorLayout::AnchorData::updateChildrenSizes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QtGraphicsAnchorLayout10AnchorData19updateChildrenSizesEv(
    QtGraphicsAnchorLayout::AnchorData *self) {
  self->QtGraphicsAnchorLayout::AnchorData::updateChildrenSizes();
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
